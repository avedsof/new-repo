---
name: ux-audit
description: Produce a UX audit presentation in Figma for a redesign project — findings grouped by area, each shown on an annotated screenshot with the problem and the proposed change, plus sitemap, page inventory and proposed page structure. Use only when the project is a redesign (or the client bought the Phase 0 audit); not for plugin, dev-only or concept tasks.
---

# UX audit deck

The reference for what good looks like is the Miss Money Savvy audit, slides 27 onwards
(sitemap today vs. proposed, page inventory with verdicts):
https://www.figma.com/design/EjerlBtazjKKklHVDPVvxJ/Miss-Money-Savvy
Its earlier slides are the reference for what to avoid: one small observation per
slide, section-divider slides, cropped screenshots.

## When to run

Only when the engagement type is **Redesign + build**, **Redesign (design only)** or
**UX audit only**, or when the client accepted the optional Phase 0 audit in a proposal.
Otherwise say so and stop.

## Principles

1. **Decisions, not observations.** Every finding ends in a structural change: to the
   information architecture, page order, a flow, the content model or a component.
2. **The filter.** "If this were fixed, would a user act differently?" If not, cut it or
   put it on the single polish slide.
3. **Group by area, never one issue per slide.** Related issues on the same screen
   share a slide.
4. **Show, then say.** The screenshot carries the finding; text explains it.
5. **12–18 slides.** Longer means findings weren't grouped or filtered.

## Deck structure (in order)

1. **Cover:** client, "UX audit", date.
2. **Scope and verdict:** what was reviewed (pages, devices, journeys), and the overall
   call in two or three sentences (refresh vs. restructure).
3. **Top changes:** the 3–5 highest-impact changes, ranked by cost to the client.
4. **Findings by area**, in this order, skipping areas with nothing that passes the filter:
   Navigation & structure → Home page → Key journeys & conversion → Trust & proof →
   Forms & tools → Visual system.
5. **Sitemap: today vs. proposed.** Grouped by what people came to do.
6. **Page inventory:** `# | Page | Depth | Verdict | Note`, verdicts from a fixed set:
   Redesign / Merge or template / Keep + restyle / Keep + unify / Keep / Remove / Add.
7. **Proposed page structure** for the key page: logic line plus sections, as in the
   proposal skill.
8. **Polish list** (optional, one slide): small visual fixes, bulleted.
9. **Priorities and next steps:** what to do first, and how it maps to the redesign scope.

## Finding slide anatomy

- Area name in the slide header (same position on every slide).
- A plain, descriptive headline stating the issue ("Hero has five equal-weight buttons").
- The screenshot, whole or cropped to exactly the problem region, with numbered markers.
- For each marker: **Problem** (what happens and what it costs) → **Change** (what we do
  instead). Add **Why** only when the reason isn't obvious.
- Up to three markers per slide; more means split the screen into two slides.

## Getting screenshots

Capture the live site with Playwright (desktop 1440 wide, mobile 390 wide), full page,
then crop regions per finding. Keep the full-page captures for the sitemap and inventory
slides. Never squash a screenshot to fit a frame.

## Visual rules

Follow `references/deck-style.md`. Load the `figma:figma-use` skill before building slides.
