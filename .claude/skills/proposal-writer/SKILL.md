---
name: proposal-writer
description: Write a client proposal (Upwork bid or direct scoping doc) as a Notion page, using a fixed skeleton plus modules chosen by project type, and matching past work from the Portfolio and Case studies databases. Use when asked to write, draft or structure a proposal, bid, estimate or scoping document for a website, redesign, WordPress build, plugin, UX audit or concept task.
---

# Proposal writer

Built from the Whiskey Library, Miss Money Savvy, Venla and Nulixir proposals.
The skeleton never changes; the modules change with the project type. That is how
proposals stay consistent while projects stay different.

## Inputs

1. The job post or client brief (and any call notes).
2. The client's current website, if there is one: look at it before writing.
3. Past work from Notion, picked with `.claude/shared/portfolio-matching.md`.
4. **Ask which name/profile signs the proposal.** Every time.
5. Output: a new Notion page under the proposals parent
   `https://app.notion.com/p/3bbbd8b60a63808491b3c9ff358ed194`,
   titled `<Name> for <Client>`.

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

1. **My read.** Open with a specific real strength and say what should not be touched
   (a founder, existing proof, a strong technical asset). Never generic praise.
   Then the **three highest-impact changes** as a table:
   `Change | What I see now | What I propose`.
2. **Core problems**, ranked by cost to the client, not by page order. 3–6 items.
   Each: a bold diagnosis phrase, then the business consequence
   ("X asks for Y from someone who just arrived, so they leave and you never hear from them").
   An observation without a consequence is cut.
3. **Audience and category.** Always included, and it is research, not a persona:
   - **Who actually buys**, concretely: who they are, what they are really evaluating,
     what makes them hesitate. "An eval lead at a frontier lab about to make a
     capability claim", never "a decision maker".
   - **How 3–4 competitors design for their audience.** Table:
     `Reference | Who they design for | What works | What we'd avoid copying`.
     The middle columns connect each design choice to the audience it serves.
   - **What applies here.** 2–3 sentences: which patterns fit this client's buyer,
     which don't and why, and the position that follows ("the clarity of a tool, the
     proof of an established UK service, the warmth of a real person").
   Keep it to one screen in an Upwork bid; go deeper in paid Phase 0 audits.
4. **The structural call.** State the fork (refresh vs. restructure, template vs. custom,
   plugin vs. custom code) and the decision, with the reason. Don't hedge.
   Quantify only from something observed; never invent a percentage.
5. **Module sections** for the project type (step 3).
6. **Relevant work** (step 4), placed before the price so value lands before cost.
7. **Estimate, timeline, assumptions** (rules below).
8. **Questions**, grouped by category (rules below). Never skipped, even when scope feels clear.
9. **Next steps**, 2–4 checkboxes, ending with the start of the first phase.
   Each one is a decision on the approach or a clarification that changes scope
   ("Choose Option A or B", "Confirm whether past boxes can show brand names").
   Never logistics or anything the client has already answered
   ("Which communication tool do you prefer?").

## Step 3: modules by project type

| Module | Redesign + build | Design only | Plugin / dev | Audit only | Concept |
|---|---|---|---|---|---|
| Phase 0: optional UX audit (lean 5 h / full 10 h) | ✓ | ✓ | – | – | – |
| What the redesign looks like in practice | ✓ | ✓ | – | – | short |
| Proposed page structure table | ✓ | ✓ | – | ✓ | ✓ |
| Competitor / category direction | optional | optional | – | ✓ | – |
| Phases: concepts → design system → templates | ✓ | ✓ | – | – | – |
| WordPress approach (ACF Pro + Gutenberg) | ✓ | – | if WP | – | – |
| Integrations list | ✓ | – | ✓ | – | – |
| Technical scope, data flow, edge cases | – | – | ✓ | – | – |
| Audit scope and sample findings | – | – | – | ✓ | – |
| Page/template list with open questions | ✓ | ✓ | – | – | – |
| Working setup (large projects only, 60+ h) | ✓ | ✓ | ✓ | – | – |

**What the redesign looks like in practice:** 3–5 principles, chosen for this client.
The recurring ones below are a menu, not boilerplate. Use only those that answer a
problem named in section 2:
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

**WordPress approach:** default recommendation is a custom theme with ACF Pro and
Gutenberg, not a page builder. Short `Decision | Why it matters for this client` table.
Blocks mirror the Figma components 1:1 so the team can add pages without a developer.
Handoff: Loom walkthroughs plus written/Figma documentation.

**Working setup** (large projects only): one shared source-of-truth folder with a
naming convention; a content-status tracker
(`Page/Section | Content | Assets | Design | Dev`); weekly or bi-weekly async check-in
(Loom plus written summary); approval checkpoints at named milestones (homepage,
design system, templates), each needing an explicit "approved" or "changes requested".

## Step 4: relevant work

- Run the selection pass in `.claude/shared/portfolio-matching.md`.
- Cite 1–3 projects. For each, say specifically why it is comparable
  (same stack, same audience, same structural problem). No bare links.
- Name the single most comparable project in a callout when one stands out.
- Pull the case-study summary from Case studies when the project has one.

## Estimate, timeline and assumptions

- Table: `Workstream | What it includes | Hours`. Design, development and
  technical/SEO/QA/training are always separate rows; never one bundled number.
- Give total hours **and** a USD price. Rates: **design $30/h** (UX audit, concepts,
  design system, templates, design handoff); **development $25/h** (build,
  integrations, migration, SEO, analytics, QA, training). Show hours as ranges and
  price the range.
- Say why the sequence is what it is ("we don't build the system before you like the direction").
- If scope is uncertain, offer two named options (Option A focused fix / Option B full
  restructure + build), each with hours, price and timeline.
- Timeline in phases/weeks tied to the estimate.
- Assumptions, always explicit: 2 revision rounds included; client supplies copy,
  photography and content; illustration, 3D, motion, copywriting, multilingual and
  CRM work excluded unless scoped. Include an `Included / Outside scope` pair of tabs
  for build projects.

## Questions

- Grouped by category (Business and data / Structure and content / Assets and technical).
- Each answerable in one sentence, and each visibly changes scope, price or timeline.
- When something can't be judged without client data (analytics, revenue split, churn,
  brand assets), ask for it here instead of guessing.
- If the client asked questions in the job post, answer them in their own tab first.

## Tone

- Direct, specific, numbers over adjectives, confident but not salesy.
- Short declarative verdicts ("I'd restructure." "This is where most of the gain sits.").
- Bold the diagnosis phrase, not the whole sentence.
- Callouts sparingly: recommendation (🔑), decision needed (⚠️), phase headers,
  "already works, don't touch".

## Lightweight version (chat reply, no full proposal)

**What currently works** (with specifics) → **What needs restructuring** (numbered,
each tied to the client's stated goal) → **Bottom line** in one paragraph.

## Do not

- Open with generic praise.
- List a problem without its business consequence.
- Give a single bundled hours/price number.
- Paste principles or setup blocks that don't answer this client's problems.
- Skip the questions section.
