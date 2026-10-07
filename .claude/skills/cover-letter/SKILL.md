---
name: cover-letter
description: Write an Upwork cover letter in the user's casual chat voice, with portfolio cases picked from the Notion Portfolio database. Use when asked to write, draft or reply to an Upwork job post, bid, or application message. For a full scoping document, use proposal-writer instead (the letter can link to it).
---

# Cover letter

Consolidated from the Notion pages "Upwork Cover Letter Guide", "CoverLetter_Guide" and
"CoverLetter_Styleguide". The same rules are mirrored in the Notion page
"Cover Letter Guide (Consolidated)" for use outside Claude
(https://app.notion.com/p/3e9bd8b60a63815bbfd6dd0effc0b39c); keep them in sync. Where they disagreed, the newer Upwork Cover Letter Guide wins.
Tone examples live in CoverLetter_Styleguide:
`https://app.notion.com/p/3cdbd8b60a6380afb541fec53d9cb592`. Read them for rhythm only;
never reuse their portfolio picks.

## Before writing

1. **Ask which name signs the letter.** Every time. The name decides which GitHub
   account code cases link to (see `.claude/shared/portfolio-matching.md`).
2. Read the job post. If a company or site is named, look it up and use one concrete
   observation from it.
3. Classify the job (same types as `proposal-writer`) and run the portfolio selection
   pass in `.claude/shared/portfolio-matching.md`.
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
- **End the sentence on what you do.** No tail that explains why or argues against
  something nobody suggested: ", so…", "so that…", "before anything…", "…and not Y",
  "instead of…", "which means…", including "X, not shrunken Y" contrasts.
  Test: cover the tail. If the client still gets everything they need, cut it. If the
  reason matters, give it its own short sentence or lead with it.
  "I'll design tablet and mobile too, so they get real layouts and not shrunken desktop
  ones" → "I'll design tablet and mobile layouts too."
  "Custom design in Figma before anything gets built" → "It starts with a custom design
  in Figma."
- 1–2 light typos in the casual narrative only (letter swap, lowercase "i", small
  run-on). Never in names, links, the signature or technical terms.

## Banned

- Em dashes. Colons used as structure.
- "rather than…", "not just X, but Y".
- Explanation tails at the end of a sentence (", so they get real layouts and not
  shrunken desktop ones", "before anything gets built"). See the voice rules.
- Generic expertise observations: "the tricky part is usually…", "where most
  integrations break", "the part most people get wrong". Tie it to a real project or cut it.
- Restating the job requirements back to the client.
- Formal intros ("Dear Client", "I'm excited to apply"), "I have X years of experience",
  "I'm confident my skills…", "Furthermore/Moreover/Additionally",
  "I look forward to hearing from you", "Please find attached".
- "Before I shape a proposal, can I ask…", "Quick question before I dive deeper".
- Bold headers or bullet-heavy formatting inside the letter.
- Questions answered by the post, and logistics questions ("which communication tool?").
- Imaginary cases drafted without asking first (see the shared matching file).
