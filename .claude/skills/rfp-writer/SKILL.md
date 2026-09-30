---
name: rfp-writer
description: Write an internal RFP page in Notion for the developer (or designer) to review before we price or answer a client. Built from the original job post, the client's messages, the user's own notes and, when there is one, the Notion meeting recap. Use when asked to create, draft or prepare an RFP, a request for estimation, a dev review page or a scope page for a client. Not client-facing; for the client's proposal use proposal-writer.
---

# RFP writer

An RFP here is an **internal** Notion page that hands a client request to our developer:
what the client wants, what we've already promised, the options, what needs their
judgment and a table for their estimate. Reference page:
https://app.notion.com/p/3ebbd8b60a6381ac8e2feacb7cf2e9fb (Nicea Murray - RFP).
The page skeleton and the Notion markup live in `references/rfp-template.md`.

## Inputs

Collect all of these before writing. Ask only for what's missing and matters.

1. **Original job post.** Usually on the client's page in the Clients database
   (`collection://3ebbd8b6-0a63-8052-8f6a-000bb28c7a6f`, under Lab), in the "Job post" tab.
2. **Client's messages**, newest last. Usually the "Client message" tab on the same page,
   or pasted by the user.
3. **The user's own notes.** Often in Ukrainian and informal. Keep the facts, translate
   them into the English body, and keep a note in the original words only when the
   nuance matters (as a gray 💡 callout, like the Arnav Sawant RFP).
4. **Meeting recap, if any.** Search Notion for it before writing:
   - `notion-query-meeting-notes` (or `notion-search`) with the client's name, company
     name and the project title;
   - read the summary and the user's notes; don't pull the full transcript unless the
     summary is missing something specific;
   - use what was agreed on the call (scope, timeline, budget, decisions, next steps) and
     name the meeting as the source.
5. **What we've already sent:** proposal (Figma or Notion link), prices, timeline,
   questionnaire. Check the client's page and the Lab page for them.
6. **Rates** come from `proposal-writer`: design `$30/h`, development `$25/h`.

If the client page doesn't exist in Clients, ask where the RFP should go.

## Output

- A new page **under the client's page**, titled `<Client name> - RFP`, icon 📐.
- If an RFP page already exists for this client, update it instead of creating a second
  one, and say what changed.
- After creating it, fetch the page back and check that the tabs, tables and toggles
  rendered (no `<unknown>` blocks, no literal markup).
- Tell the user to give the developer edit access so they can fill in the table.

## Page structure (in this order)

Full markup in `references/rfp-template.md`.

1. **Color key** (gray callout, one line). Keep the colors identical on every RFP.
2. **🇺🇦 Коротко про проєкт** (gray callout): **2–3 sentences in Ukrainian**: who the
   client is, what they need built, and what we need from the developer right now.
   Plain language, no English jargon beyond tool names (`WordPress`, `Stripe`).
3. **👤 The client** (gray): who they are, the business, the brief's hard requirements,
   the selection process or deadline.
4. **🔑 What we've sent already** (red): links, the price and timeline we quoted,
   promises made. Put any **discrepancy** (a client misquoting our price, conflicting
   facts between sources) in red text.
5. **📩 What the client is asking now** (gray) with tabs:
   `Their questions` · `What they really want` · `Source` (job post excerpt, message
   or meeting recap, quoted).
6. **🧱 Scope** (gray) with tabs that fit the project, e.g. `Pages` · `Flows` ·
   `Payments / integrations` · `Stack`. Mark what we proposed vs. what the client added.
7. **Options**, when the request has real alternatives (a lean and a fuller version,
   or two technical approaches). Tabs, one per option, plus a `Compare` tab:
   - each option: how it works, limits, what stays manual, how to build it,
     then a green 💸 estimate callout;
   - `Compare`: a table with the option columns colored, then a gray 💡 callout with
     our recommendation and the condition that would change it.
   Skip this section when there's a single path; put the scope straight into the estimate.
8. **⚠️ Needs your judgment** (yellow): a to-do checklist of concrete technical
   questions only the developer can answer (plugin choice, API limits, feasibility,
   hidden costs, risks). Each item names the tool or feature in `code`.
9. **💸 Request for estimation** (green): a table
   `Workstream | My estimate | Your estimate | Notes`, one row per workstream, rows
   colored by option (gray base, blue option 1, purple option 2). Rates underneath, then
   **Deliverable from you:** what the developer returns.
10. **📝 Draft answers / next message to the client** (toggle, collapsed), marked
    "pending your review", when the client asked questions.
11. **📎 Sources** (toggle): every input used, with links (job post, messages, notes,
    meeting recap).

## Color and highlighting rules

| Color | Meaning |
|---|---|
| `gray_bg` | context: client, request, scope, recommendation |
| `red_bg` | already sent or promised to the client; red text for discrepancies |
| `blue_bg` | option 1 |
| `purple_bg` | option 2 (`orange_bg` for a third, if ever needed) |
| `yellow_bg` | needs the developer's judgment |
| `green_bg` | estimates and the request for estimation |

- The same color always means the same thing, including table row colors.
- Mark as `code`: tool and plugin names, features and settings, hour ranges and rates.
  Don't mark whole sentences.
- Use tabs where the reader switches between parallel things (options, sources, scope
  areas). Don't tab a single block of text.
- Escape `$` as `\$` outside code spans, or the Notion markup breaks.

## Writing rules

- **English body, Ukrainian summary.** The developer reads both.
- Facts only from the inputs. Estimates are labeled "my estimate" and always given as
  ranges; say which parts are guesses the developer should check.
- Keep the client's own words for requirements when they're precise; quote, don't
  paraphrase, in the `Source` tab.
- Say what's still unknown instead of filling gaps.
- Short sentences, bold the key phrase, no filler. The tone will be tuned in later
  iterations; for now follow the reference page.

## Do not

- Send anything to the client from this skill; the RFP is internal.
- Invent prices, hours or dates that aren't in the inputs or marked as our estimate.
- Leave the Ukrainian summary out.
- Create a second RFP page for the same client.
