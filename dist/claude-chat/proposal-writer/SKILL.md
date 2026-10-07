---
name: proposal-writer
description: Write a client proposal (Upwork bid or direct scoping doc) for website work as a Notion page, using a fixed skeleton plus modules chosen by project type, with past work matched from the Notion Portfolio and Case studies databases, plus a short supporting message to send with it. Use when asked to write, draft or structure a proposal, bid, estimate or scoping document for a website, redesign, WordPress or WooCommerce build, plugin, UX audit or concept task. For a short Upwork cover letter, use the cover-letter skill instead.
---

# Proposal writer

Claude chat version of the proposal-writer skill from the avedsof/new-repo repository.
It is self-contained: the portfolio-matching rules and the voice rules from the
cover-letter skill are included below.
Needs the Notion connector to read the Portfolio and Case studies databases and to
create the proposal page. Without it, write the proposal in the chat as one document
and ask the user for the client brief and the past projects to cite.

The skeleton never changes; the modules change with the project type. That is how
proposals stay consistent while projects stay different.

## Inputs

1. The job post or client brief, the client's messages and any call notes. In Notion
   these usually sit on the client's page in the Clients database (under Lab), in the
   "Job post" and "Client message" tabs.
2. The client's current website, if there is one: look at it before writing. If it
   doesn't load, say so and don't describe it.
3. Every reference site the client sent: look at each one before writing about it.
4. Past work from Notion, picked with the portfolio-matching rules below.
5. **Ask which name signs the proposal**, unless the client's messages already address
   one of us by name. The name decides which GitHub account code cases link to.
6. The price, if the user has already set one. The user's price wins over the rates
   below; break it down so it adds up exactly.
7. Output: a new Notion page under the Lab page
   https://app.notion.com/p/494bd8b60a6382b1b25601bf122dd7f1
   titled `<Name> for <Client>`. If Lab can't be reached, ask where to save it.

## Who we are (context, don't recite)

A small full-cycle studio: UX/UI design in Figma, custom WordPress builds (ACF Pro +
Gutenberg), WooCommerce, custom plugins, API integrations (Zoho, Beds24, Amelia,
Stripe, OpenAI, Zapier, Make, REST, cron) and AI automation. Andrew leads development,
Yulia leads design. Confirm with the user how to describe roles if the client asks.

## Step 1: classify the project

Pick one engagement type from the job post. If it is genuinely unclear, ask before writing.

| Type | Signals in the brief |
|---|---|
| Redesign + build | new site or rebuild, CMS, migration, integrations |
| Redesign (design only) | Figma deliverable, developer already in place |
| Custom plugin / dev | functionality, API, WooCommerce logic, no design ask |
| UX audit only | review, audit, "what's wrong with our site" |
| Concept / test task | one page, home page concept, trial assignment |

## Step 2: the skeleton (always, in this order)

0. **Their questions and requirements, answered first.** When the client asked for
   specific things (a price per site and combined, a timeline, what's included,
   ongoing costs, milestones, links, who does the work), answer them at the very top,
   one tab per question. A client who sets hard requirements ("no links, no
   consideration") must see them met before anything else.
1. **My read.** Open with a specific real strength and say what should not be touched
   (a founder, existing proof, a strong technical asset, assets already in place).
   Never generic praise. Then the **highest-impact decisions** as a table:
   `Decision | What I see now | What I propose`.
2. **Core problems or reasons**, ranked by cost to the client. 3–6 items. Each: a bold
   diagnosis phrase, then the business consequence. An observation without a
   consequence is cut. **Tie each point to something the client showed you** (their
   site, their references, their brief). A point that reads as a general warning
   sounds harsh out of context; "your references range from a one-page site to a whole
   portal, and where yours sits decides the work" lands better than "scope grows quietly".
3. **Audience and category.** Always included, and it is research, not a persona:
   - **Who actually buys**, concretely: who they are, what they are really evaluating,
     what makes them hesitate. Never "a decision maker".
   - **How 3–4 references or competitors design for their audience.** Table:
     `Reference | Who they design for | What works | What we'd avoid copying`.
     Prefer the client's own references when they sent some.
   - **What applies here.** 2–3 sentences: which patterns fit this client's buyer,
     which don't and why, and the position that follows.
4. **The structural call.** State the fork (refresh vs. restructure, template vs.
   custom, Shopify vs. WooCommerce, plugin vs. custom code) and the decision, with the
   reason. Don't hedge. Quantify only from something observed; never invent a percentage.
5. **Module sections** for the project type (step 3).
6. **Relevant work** (step 4), placed before the price so value lands before cost.
7. **Estimate, timeline, assumptions** (rules below).
8. **Questions**, grouped by category (rules below). Never skipped.
9. **Next steps**, 2–4 checkboxes, ending with the start of the first phase. Each one
   is a decision on the approach or a clarification that changes scope. Never
   logistics or anything the client has already answered.

## Step 3: modules by project type

| Module | Redesign + build | Design only | Plugin / dev | Audit only | Concept |
|---|---|---|---|---|---|
| Phase 0: optional UX audit (lean 5 h / full 10 h) | ✓ | ✓ | – | – | – |
| What the redesign looks like in practice | ✓ | ✓ | – | – | short |
| Proposed page structure table | ✓ | ✓ | – | ✓ | ✓ |
| Competitor / category direction | optional | optional | – | ✓ | – |
| Phases: concepts → design system → templates | ✓ | ✓ | – | – | – |
| How the concept review works for you | ✓ | ✓ | – | – | ✓ |
| What the concepts look like in practice | ✓ | ✓ | – | – | ✓ |
| WordPress approach (ACF Pro + Gutenberg) | ✓ | – | if WP | – | – |
| Integrations list | ✓ | – | ✓ | – | – |
| Technical scope, data flow, edge cases | – | – | ✓ | – | – |
| Audit scope and sample findings | – | – | – | ✓ | – |
| Page/template list with open questions | ✓ | ✓ | – | – | – |
| Working setup (large projects only, 60+ h) | ✓ | ✓ | ✓ | – | – |

**What the redesign looks like in practice:** 3–5 principles, chosen for this client,
only those that answer a problem named in section 2:
- a system that produces pages, not one-off designs;
- one primary and one secondary action per screen;
- adjectives replaced by numbers, names, photos and dates;
- modular, reorderable and A/B-ready sections (only if the client tests).

**Proposed page structure table** is the signature artifact:
- one **Logic** line as an arrow chain (hook → proof → mechanics → offer → close),
  naming the 1–2 structural changes versus the current page;
- sections grouped under sub-headers (Above the fold, Proof, The offer, Close);
- columns `# | Section | Intent and content`; every row says why the section exists;
- new sections that don't exist today are flagged explicitly.

**How the concept review works for you:** written for the client, placed right under
the concepts phase. Cover:
- **What they receive:** one Figma link with 2–3 homepage concepts, each in desktop
  and mobile (say "mobile first" when their audience is mostly on phones); a mini UI
  kit with the key element states (buttons, form fields) beside each concept; a
  reusable icon set only if it is in the estimate.
- **How to give feedback:** tell us which concept feels most like them, and mix freely
  ("the hero from 2 with the colours from 1"); comment directly in Figma or reply by
  message, whichever is easier.
- **What happens next:** consolidated revision rounds (the number from the
  assumptions), then an explicit "approved" before the design system starts.

Keep it to one short block in their own words, not a process diagram. Never promise a
deliverable the estimate doesn't cover. Example:

> You'll get one Figma link with three homepage concepts, each in desktop and mobile,
> with the key buttons and form states laid out beside them. When you review, tell us
> which one feels most like you, and feel free to mix ("the hero from 2 with the
> colours from 1"). Comment in Figma or reply by message, whichever is easier. Two
> consolidated revision rounds follow, then you approve the direction before we build
> the design system.

**What the concepts look like in practice:** 1–3 real concept files from the Portfolio
(Engagement "Concept / test task" or Pages designed "Home page"), each with one line on
what the client compared and what it decided. Pick the one closest to this client's
audience (a mobile-first fashion page for a streetwear store, for example).

**WordPress approach:** default recommendation is a custom theme with ACF Pro and
Gutenberg, not a page builder or a bought template. Short
`Decision | Why it matters for this client` table. The team can add pages without a
developer: blocks mirror the Figma components 1:1. Handoff: video walkthroughs plus a
short written guide. The ACF Pro licence is covered on our side.

**Client templates:** when a client offers an older theme or template, recommend a
clean build and say why (outdated code, bundled page builders and plugins with their
own licences and updates, harder to make look like their brand than a clean build),
and still offer to look at it for layouts or styles they like.

**Working setup** (large projects only): one shared source-of-truth folder; a
content-status tracker (`Page/Section | Content | Assets | Design | Dev`); weekly or
bi-weekly async check-in; approval checkpoints at named milestones, each needing an
explicit "approved" or "changes requested".

## Step 4: relevant work

- Run the selection pass below.
- Cite 2–4 projects. For each, say specifically why it is comparable (same stack, same
  audience, same structural problem). No bare links.
- Name the single most comparable project in a callout when one stands out.
- Pull the case-study summary from Case studies when the project has one.
- Describe each project only as the Portfolio supports it: a Figma-only project is
  design work, not a live site; check the Stack field before calling something
  WooCommerce; flag staging links (wp4u.link) to the user before sending.

## Estimate, timeline and assumptions

- Table: `Workstream | What it includes | Hours | Price`. Design, development and
  technical/SEO/QA/handover are always separate rows; never one bundled number.
- Rates: **design $30/h** (UX audit, concepts, design system, templates, design
  handoff); **development $25/h** (build, integrations, migration, SEO, analytics, QA,
  training). Show hours as ranges and price the range, **unless** the client asked for
  a fixed price or the user set one: then give fixed hours that add up exactly.
- Several deliverables (two sites, three layers): price each, then the combined total.
- Milestones: tie each payment to a deliverable the client can check ("Figma design
  approved", "site live, handover delivered"). Follow the client's preferred split.
- Say why the sequence is what it is ("we don't build the system before you like the
  direction").
- If scope is uncertain, offer two named options (Option A / Option B), each with
  hours, price and timeline.
- Timeline in phases or weeks tied to the estimate. When there's a deadline, work
  backward from it and say when the work must start and what can start now.
- **Ongoing costs**, when the client asks or the platform choice depends on them:
  list only what they'd pay anyway (hosting, domains, email provider, payment fees)
  and anything paid that might be added, and say you'll flag it before adding it.
- Assumptions, always explicit: revision rounds; client supplies copy, photography,
  product data and content; illustration, 3D, motion, copywriting, multilingual and
  CRM work excluded unless scoped. Include an `Included / Outside scope` pair of tabs
  for build projects.

## Questions

- Grouped by category (Business and data / Structure and content / Assets and
  technical, or one group per site when there are several).
- Each answerable in one sentence, and each visibly changes scope, price or timeline.
  Say why when it isn't obvious, in its own sentence ("Do you have copy outlines for
  the pages? The number of sections per page decides the design and build time.").
- When something can't be judged without client data, ask for it here instead of guessing.

## Facts before claims

- Never state how a site is built, what it contains or how it performs without having
  checked it in this conversation. If a page can't be opened, say so.
- When the user gives you a claim about a reference ("it's headless", "it's a
  template"), check it before writing it in. If it doesn't hold, write what you found
  and tell the user what changed.
- No invented numbers, metrics, client names or dates.

## Voice (shared with the cover-letter skill, adapted for a proposal)

The proposal page can use headings, tables, tabs and callouts. The prose inside them
follows these rules:
- A confident specialist explaining a plan to a peer. Direct, specific, numbers over
  adjectives, confident but not salesy. If a sentence could sit in a corporate
  brochure, rewrite it.
- Short declarative verdicts ("I'd rebuild." "This is where most of the gain sits.").
- Mirror concrete details from the brief (a tool, a reference, "the templates you
  mentioned").
- Method statements put the outcome first: "To keep the values editable later I'm
  connecting them to ACF fields", not "I'd connect the values to ACF fields so they
  stay editable".
- Asks are direct: "Could you share the page list…", "Can I see your current setup first?"
- Ground every expertise claim in a real project or in something observed on the
  client's site or references.
- Bold the diagnosis phrase, not the whole sentence.
- **End the sentence on what we do.** No tail that explains why or argues against
  something nobody suggested: ", so…", "so that…", "before anything…", "…and not Y",
  "instead of…", "which means…", including "X, not shrunken Y" contrasts.
  Test: cover the tail. If the client still gets everything they need, cut it. If the
  reason matters, give it its own short sentence or lead with it.
  "I'll design tablet and mobile too, so they get real layouts and not shrunken desktop
  ones" → "I'll design tablet and mobile layouts too."
  "Custom design in Figma before anything gets built" → "It starts with a custom design
  in Figma."
- Callouts sparingly: recommendation (🔑), decision needed (⚠️), most comparable
  project (⭐), "already works, don't touch".
- Write "we" for the studio and "I" for the person signing; keep it consistent.
- No typos in the proposal page itself.

## The supporting message

Always finish with a short message to send with the proposal (Upwork chat or email),
in the cover-letter voice:
- Greeting with their name, one line of thanks tied to something specific they sent.
- The link to the proposal page.
- The short answers to what they asked (price per item and combined, timeline,
  milestones), then the one or two decisions that matter most (the platform call, the
  verification approach), each in a sentence or two with the reason.
- What you need from them to keep the price fixed (page list, copy outlines, files).
- If they offered a call, accept it warmly; if they said no calls, don't offer one.
- Close: "Hope to talk more soon, [Name]".
- For a follow-up after silence: no guilt, no "just checking in". Restate the value in
  two or three lines, link the page, name the date the work must start to hit their
  deadline, and ask for the one answer that unblocks it.
- Casual chat voice, 1–2 light typos in the narrative only (letter swap, lowercase
  "i"), never in names, links, prices or the signature.

## Banned (proposal and message)

- Em dashes. In the message, also colons used as structure, bold headers and
  bullet-heavy formatting.
- "rather than…", "not just X, but Y".
- Generic expertise observations: "the tricky part is usually…", "where most
  integrations break", "the part most people get wrong".
- Restating the job requirements back to the client.
- Formal intros ("Dear Client", "I'm excited to apply"), "I have X years of
  experience", "I'm confident my skills…", "Furthermore/Moreover/Additionally",
  "I look forward to hearing from you", "Please find attached".
- Explanation tails at the end of a sentence (", so they get real layouts and not
  shrunken desktop ones", "before anything gets built"). See the voice rules.
- Opening with generic praise.
- A problem without its business consequence.
- A single bundled hours/price number.
- Principles or setup blocks that don't answer this client's problems.
- Skipping the questions section.
- Questions answered by the brief, and logistics questions ("which communication tool?").

## After writing

- Fetch the page back and check that tabs, tables and callouts rendered (no literal
  markup, no broken rows; avoid merged table cells).
- Tell the user: the page is private until they turn on view sharing; which links are
  staging or Figma-only; any claim from their notes you corrected; anything you
  couldn't open.
- If the user edits the page, fetch it again before changing anything, edit only what
  they asked for, and point out inconsistencies their edits introduced (a timeline in
  one tab that no longer matches another) without fixing them unasked.

## Lightweight version (chat reply, no full proposal)

**What currently works** (with specifics) → **What needs restructuring** (numbered,
each tied to the client's stated goal) → **Bottom line** in one paragraph.

# Portfolio matching

Read past work directly from Notion:
- Portfolio database (every project): https://app.notion.com/p/2bdbd8b60a6381a68822f4adeed37b4f
- Case studies database (in-depth write-ups): https://app.notion.com/p/bbcbd8b60a6383469bee01bfee967f79

## Fields to query

Engagement · Redesign · Deliverables · Pages designed · Stack · Features · Business
model · Industry · Aesthetic · Proof level · Showcase frames · Story · Case study.
Ignore "Tags (old)" and "design (old)". Filter on these fields first, then read the
shortlisted pages. The title field is "Project". If a project the user names isn't in
the Portfolio, ask for its links instead of guessing.

## Selection pass (do it every time, silently)

1. From the brief, identify: functionality, industry, visual/aesthetic world, tech
   stack, conversion goal, client type.
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
6. When the user names the projects to show, use those, and still check each one
   against the brief's hard requirements (for example "two live sites with member
   login"). If they don't meet them, tell the user before writing.

## When nothing fits: imaginary case (ask first)

If no real project passes the selection test, **stop and ask the user** whether to
draft an imaginary case. Don't draft one unasked. If they say yes, adapt the closest
real case(s), show it headed **IMAGINARY CASE: review before sending** with a note on
what it was adapted from, and use no made-up links, repos or metrics.

## GitHub links by signature

| Signature | GitHub |
|---|---|
| Andrew | https://github.com/andrewpuzyrevichG |
| Yulia | https://github.com/yuliakolyada624 |
| Any other name | Ask which of the two to use |

Known repos on both accounts: Beds24 booking engine
(`andrewpuzyrevichG/beds24-booking`, `yuliakolyada624/beds24_booking_engine`) and the
Zoho/WooCommerce plugin (`andrewpuzyrevichG/zoho_plugin`, `yuliakolyada624/zoho_int-main`).
SAL plugins: only `andrewpuzyrevichG/sal_id` is known; for a Yulia proposal, ask for
the repo or show the live site https://sal.org.sg/ instead.

## Links

Full plain URLs for live sites, Figma files and GitHub repos. Markdown links are fine
inside the Notion page; in the supporting message, use plain URLs.
