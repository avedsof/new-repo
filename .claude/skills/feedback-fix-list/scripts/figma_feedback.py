#!/usr/bin/env python3
"""Collect Figma comments with pinned screenshots for the feedback-fix-list skill.

  collect FILE_KEY --out DIR [--skip-ids ID,ID] [--since ISO] [--overview ID,ID]
      Fetch comments, render each anchored frame once, crop around every comment and
      draw a numbered pin. Writes DIR/manifest.json and DIR/comment-<n>.png.
      --skip-ids  comment IDs already captured in Notion (Tasks."Figma comment ID")
      --since     only comments created after this ISO timestamp
      --overview  comment IDs about the whole page: saved as a downscaled full-frame
                  thumbnail with every pin on that frame, instead of a crop

  status FILE_KEY
      Print {comment_id: resolved_at or null} as JSON, to sync "Resolved in Figma".

Needs network access to api.figma.com with auth (the agent proxy injects it, or set
FIGMA_TOKEN) and Pillow.
"""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = None
API = "https://api.figma.com/v1"
PIN = (245, 6, 184)
MAX_PIXELS = 30_000_000  # stay under Figma's render limit


def get(path):
    req = urllib.request.Request(API + path)
    if os.environ.get("FIGMA_TOKEN"):
        req.add_header("X-Figma-Token", os.environ["FIGMA_TOKEN"])
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def font(size):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/Library/Fonts/Arial Bold.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def pin(draw, x, y, label, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill=PIN, outline="white", width=max(2, r // 6))
    draw.text((x, y), label, fill="white", font=font(int(r * 1.25)), anchor="mm")


def collect(a):
    os.makedirs(a.out, exist_ok=True)
    skip = set(filter(None, (a.skip_ids or "").split(",")))
    overview = set(filter(None, (a.overview or "").split(",")))
    raw = get(f"/files/{a.file_key}/comments")["comments"]
    raw.sort(key=lambda c: c["created_at"])
    replies = {}
    for c in raw:
        if c["parent_id"]:
            replies.setdefault(c["parent_id"], []).append(
                {"user": c["user"]["handle"], "message": c["message"], "created_at": c["created_at"]})
    top = [c for c in raw if not c["parent_id"]
           and c["id"] not in skip and (not a.since or c["created_at"] > a.since)]
    for i, c in enumerate(top, 1):
        c["n"] = i  # pin number = order posted within this run

    node_ids = sorted({c["client_meta"]["node_id"] for c in top if c.get("client_meta", {}).get("node_id")})
    nodes = {}
    if node_ids:
        q = urllib.parse.quote(",".join(node_ids))
        for nid, v in get(f"/files/{a.file_key}/nodes?ids={q}")["nodes"].items():
            if v:
                d = v["document"]
                b = d.get("absoluteBoundingBox") or {}
                nodes[nid] = {"name": d["name"], "type": d["type"],
                              "w": b.get("width", 0), "h": b.get("height", 0)}

    # One render per frame; scale down huge frames and scale offsets to match.
    scales, renders = {}, {}
    for nid, n in nodes.items():
        px = n["w"] * n["h"]
        scales[nid] = 1 if px <= MAX_PIXELS else round((MAX_PIXELS / px) ** 0.5, 2)
    for s in sorted(set(scales.values())):
        ids = [k for k, v in scales.items() if v == s]
        q = urllib.parse.quote(",".join(ids))
        urls = get(f"/images/{a.file_key}?ids={q}&format=png&scale={s}")["images"]
        for nid, url in urls.items():
            if not url:
                continue
            path = os.path.join(a.out, f"frame-{nid.replace(':', '-')}.png")
            urllib.request.urlretrieve(url, path)
            renders[nid] = path

    by_frame = {}
    for c in top:
        by_frame.setdefault(c["client_meta"].get("node_id"), []).append(c)

    out = []
    for c in top:
        meta = c.get("client_meta") or {}
        nid = meta.get("node_id")
        off = meta.get("node_offset") or {}
        entry = {
            "n": c["n"], "id": c["id"], "user": c["user"]["handle"],
            "created_at": c["created_at"], "resolved_at": c["resolved_at"],
            "message": c["message"], "replies": replies.get(c["id"], []),
            "node_id": nid, "node_name": nodes.get(nid, {}).get("name"),
            "link": f"https://www.figma.com/design/{a.file_key}?node-id={(nid or '').replace(':', '-')}#{c['id']}",
            "screenshot": None,
        }
        if nid in renders and off:
            s = scales[nid]
            im = Image.open(renders[nid]).convert("RGB")
            W, H = im.size
            x, y = off["x"] * s, off["y"] * s
            path = os.path.join(a.out, f"comment-{c['n']}.png")
            if c["id"] in overview:
                k = max(1, round(W / 360))
                img = im.resize((W // k, H // k), Image.LANCZOS)
                d = ImageDraw.Draw(img)
                for o in by_frame[nid]:
                    oo = o["client_meta"]["node_offset"]
                    pin(d, oo["x"] * s / k, oo["y"] * s / k, str(o["n"]), 16)
            else:
                ch = 1000 if W > 1000 else 820
                t = max(0, min(H - ch, int(y - ch / 2)))
                img = im.crop((0, t, W, min(H, t + ch)))
                pin(ImageDraw.Draw(img), x, y - t, str(c["n"]), 24)
            img.save(path, optimize=True)
            entry["screenshot"] = path
        out.append(entry)

    with open(os.path.join(a.out, "manifest.json"), "w") as f:
        json.dump({"file_key": a.file_key, "comments": out}, f, indent=2, ensure_ascii=False)
    print(json.dumps([{k: e[k] for k in ("n", "id", "node_name", "message", "screenshot")} for e in out],
                     indent=2, ensure_ascii=False))


def status(a):
    raw = get(f"/files/{a.file_key}/comments")["comments"]
    print(json.dumps({c["id"]: c["resolved_at"] for c in raw if not c["parent_id"]}, indent=2))


def main():
    p = argparse.ArgumentParser()
    sp = p.add_subparsers(dest="cmd", required=True)
    c = sp.add_parser("collect")
    c.add_argument("file_key")
    c.add_argument("--out", required=True)
    c.add_argument("--skip-ids")
    c.add_argument("--since")
    c.add_argument("--overview")
    s = sp.add_parser("status")
    s.add_argument("file_key")
    a = p.parse_args()
    {"collect": collect, "status": status}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
