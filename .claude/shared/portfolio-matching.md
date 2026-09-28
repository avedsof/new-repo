# Portfolio matching

Shared by the `cover-letter` and `proposal-writer` skills. Read past work directly from
Notion (the old Portfolio.html export is no longer used).

- Portfolio database (every project): `collection://2bdbd8b6-0a63-817a-86bf-000b152c4a85`
- Case studies database (in-depth write-ups for the best projects):
  `collection://850bd8b6-0a63-830c-adb5-87c54d079654`

## Fields to query (see docs/portfolio-schema.md)

Engagement · Redesign · Deliverables · Pages designed · Stack · Features · Business model ·
Industry · Aesthetic · Proof level · Showcase frames · Story · Case study.
Ignore "Tags (old)" and "design (old)". Filter in SQL on these fields first, then read the
shortlisted pages. Use **Story** as the starting point for the cover-letter case text and
**Showcase frames** for images; if Story is empty, write one from the case study or page
and offer to save it back.

## Selection pass (do it every time, silently)

1. From the job post, identify: functionality, industry, visual/aesthetic world,
   tech stack, conversion goal, client type.
2. Shortlist at least 6 candidate projects from the Portfolio database.
3. Pick the final 2–4 (cover letter) or 1–3 (proposal) by this priority:
   1. Same functionality beats same industry.
   2. Exact niche beats broad category.
   3. Aesthetic fit matters for design jobs.
   4. Tech stack matters for development-only jobs.
   5. Shipped work beats concepts when the client needs a build.
   6. Familiar examples are allowed only if they still win on the points above.
4. Test each pick: "Why would this client feel this project is about them?"
   A weak or generic answer means drop it.
5. Pull the summary from the Case studies database when the project has one.

## When nothing fits: imaginary case (ask first)

If no real project passes the selection test, **stop and ask the user** whether to draft
an imaginary case. Don't draft one unasked.

If they say yes:
1. Build it from real projects: take the closest real case(s) and adapt them to the job's
   criteria (functionality, industry, aesthetic, stack, goal).
2. Show it to the user as a draft, written exactly as it would appear in the cover letter
   (`⚡️ [Project]. [story]`) or proposal (relevant-work tab), headed
   **IMAGINARY CASE: review before sending**, followed by a note listing which real
   projects it was adapted from and what was changed.
3. No made-up live links, GitHub repos or metrics. Link only real Figma/live URLs from the
   source projects, and only where they genuinely illustrate the point.
4. The user decides whether and how it goes into the final text.

## GitHub links by signature

Ask which name signs the letter or proposal, then use that person's GitHub for code cases:

| Signature | GitHub |
|---|---|
| Andrew | https://github.com/andrewpuzyrevichG |
| Yulia | https://github.com/yuliakolyada624 |
| Any other name | Ask which of the two to use |

Known repos on both accounts: Beds24 booking engine
(`andrewpuzyrevichG/beds24-booking`, `yuliakolyada624/beds24_booking_engine`) and the
Zoho/WooCommerce plugin (`andrewpuzyrevichG/zoho_plugin`, `yuliakolyada624/zoho_int-main`).
SAL plugins: only `andrewpuzyrevichG/sal_id` is known; for a Yulia letter, ask for the
repo or show the live site https://sal.org.sg/ instead.

## Links

Full plain URLs (live site, Figma, GitHub). No Markdown link syntax in cover letters.
