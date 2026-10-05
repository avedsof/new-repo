---
name: cover-letter
description: Write an Upwork cover letter in the user's casual chat voice, with portfolio cases picked from the Notion Portfolio database. Use when asked to write, draft or reply to an Upwork job post, bid, or application message.
---

# Cover letter

Claude chat version of the cover-letter skill from the avedsof/new-repo repository
(self-contained: the portfolio-matching rules are included below).
Needs the Notion connector to read the Portfolio and Case studies databases.
Tone examples live in the Notion page CoverLetter_Styleguide:
https://app.notion.com/p/3cdbd8b60a6380afb541fec53d9cb592
Read them for rhythm only; never reuse their portfolio picks.

## Before writing

1. **Ask which name signs the letter.** Every time. The name decides which GitHub
   account code cases link to (see "GitHub links by signature").
2. Read the job post. If a company or site is named, look it up and use one concrete
   observation from it.
3. Classify the job: Design + build, Design only, Build only (client design),
   Custom plugin / integration, Concept / test task, or UX audit. Then run the
   portfolio selection pass below.
4. If a proposal page exists for this job, link it in the letter.

## Who I am (context, don't recite)

Full-cycle freelancer: UX/UI design in Figma, custom WordPress builds (ACF Pro +
Gutenberg), custom plugins, API integrations (Zoho, Beds24, Amelia, Stripe, OpenAI,
Zapier, Make, WooCommerce, REST, cron), and AI automation.

## Structure

1. **Opener: one thought in one breath.** Greeting + name → one grounded observation
   about their site or post → what the letter gives them, phrased as an outcome for
   their business (how partners see the brand, how fast customers get the offer),
   not as a task list. A specific, useful critique beats a safe compliment.
2. **Screening questions** from the post, if any, answered directly right after the
   opener or right after the portfolio, still in chat voice, not Q&A style.
3. **Portfolio, 2–4 cases**, each in this format:
   `⚡️ [Project]. [What the business is, what the work involved, what it achieved
   (perception, usability, conversion, CMS, scalability).]`
   `Figma / Live link: [full plain URL]`
   No relevance-signposting ("I'm including this because", "relevant here because").
   The client should recognise their own situation in the story.
4. **Approach, only if the post asks how.** Short and friendly, outcome first
   (see voice rules). Ground any expertise claim in a real past project.
5. **Next step.** Always propose how the work starts and what's needed to scope it.
   Questions only if they matter for scope and aren't answered by the post. It's fine
   to skip questions when the portfolio and approach already move things forward.
6. **Estimates: don't jump in.** If asked, name what the scope depends on (branding
   refresh or not, page count, content readiness) and give a rough hour range for the
   most likely case.
7. **Close short and warm.** "Hope to talk more soon, [Name]" /
   "Thank you and hope to talk more soon, [Name]". No availability claims unless the
   post asks about timing.

Short, casual post → short, casual letter. Match the post's length and energy.

## Voice rules

- A confident freelancer DM-ing a peer. If a sentence could sit in a corporate
  proposal PDF or a sales pitch, rewrite it.
- Connectors that fit: "and of course…", "and if you like what you're seeing…",
  "Let me show you…", "I'd hope to…", "I'd love to…", "see [link] for this", "quite a few".
- Mirror 1–2 concrete details from the post (a tool, a deliverable, "the sitemap you
  mentioned").
- For design jobs, name the process when it helps ("2–3 homepage concepts in
  different style directions").
- Method statements put the outcome first:
  "To keep the values editable later I'm connecting them to ACF fields", not
  "I'd connect the values to ACF fields so they stay editable".
  When the client needs to act, make it an ask: "Can I see your current setup first?"
- Asks are direct: "Can I ask you to share…", "Could you show me…".
- 1–2 light typos in the casual narrative only (letter swap, lowercase "i", small
  run-on). Never in names, links, the signature or technical terms.

## Banned

- Em dashes. Colons used as structure.
- "rather than…", "not just X, but Y".
- Generic expertise observations: "the tricky part is usually…", "where most
  integrations break", "the part most people get wrong". Tie it to a real project or cut it.
- Restating the job requirements back to the client.
- Formal intros ("Dear Client", "I'm excited to apply"), "I have X years of experience",
  "I'm confident my skills…", "Furthermore/Moreover/Additionally",
  "I look forward to hearing from you", "Please find attached".
- "Before I shape a proposal, can I ask…", "Quick question before I dive deeper".
- Bold headers or bullet-heavy formatting inside the letter.
- Questions answered by the post, and logistics questions ("which communication tool?").
- Imaginary cases drafted without asking first (see "When nothing fits").

# Portfolio matching

Read past work directly from Notion:
- Portfolio database (every project): https://app.notion.com/p/2bdbd8b60a6381a68822f4adeed37b4f
- Case studies database (in-depth write-ups): https://app.notion.com/p/bbcbd8b60a6383469bee01bfee967f79

## Fields to query

Engagement · Redesign · Deliverables · Pages designed · Stack · Features · Business model ·
Industry · Aesthetic · Proof level · Showcase frames · Story · Case study.
Ignore "Tags (old)" and "design (old)". Filter on these fields first, then read the shortlisted pages. Use **Story** as the starting point for the cover-letter case text and
**Showcase frames** for images; if Story is empty, write one from the case study or page
and offer to save it back.

## Selection pass (do it every time, silently)

1. From the job post, identify: functionality, industry, visual/aesthetic world,
   tech stack, conversion goal, client type.
2. Shortlist at least 6 candidate projects from the Portfolio database.
3. Pick the final 2–4 by this priority:
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
   (`⚡️ [Project]. [story]`) headed
   **IMAGINARY CASE: review before sending**, followed by a note listing which real
   projects it was adapted from and what was changed.
3. No made-up live links, GitHub repos or metrics. Link only real Figma/live URLs from the
   source projects, and only where they genuinely illustrate the point.
4. The user decides whether and how it goes into the final text.

## GitHub links by signature

Ask which name signs the letter, then use that person's GitHub for code cases:

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
