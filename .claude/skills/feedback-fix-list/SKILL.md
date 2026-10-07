---
name: feedback-fix-list
description: Turn client feedback (Figma comments plus client messages) into one Feedback record and a linked fix list in the project's Notion page, with pinned screenshots grouped by concept or screen, and a draft reply to the client. Also re-syncs a round later, adding new comments and marking tasks whose Figma comments were resolved. Use when asked to gather, collect, log or sort client feedback or Figma comments, make a fix list or task list from feedback, or update/sync an existing feedback round. Not for writing proposals or RFPs.
---

# Feedback → fix list

Mirrored as a Notion Skill: https://app.notion.com/p/3f2bd8b60a638198ada3ee85ff9dced0
(keep the two in sync).

One **Feedback record** = one round of client feedback (one review of one deliverable).
Each action from it becomes a row in **Tasks**, linked back to the record.
Reference round: https://app.notion.com/p/3f2bd8b60a63815eb6c8f1a6e21fdd9d
(Miss Money Savvy, Phase 2 concepts, round 1).

## Inputs

1. **Project page** in Notion, under Prjcts (`https://app.notion.com/p/db2bd8b60a638250956c81112ca8257c`).
   It holds the Figma link (usually a "Figma" tab), the brief, and the two inline
   databases below. Ask for the page if the user didn't name the project.
2. **Figma file key**, from the Figma link on the project page or the user's message
   (`figma.com/design/<fileKey>/...`; for a branch URL use the branch key).
3. **Client messages**, if any: pasted by the user, or in the client's page/tab. Treat
   them as comments without a screenshot (Source = the channel).
4. **Phase and round**: from the RFP phases on the project page and the existing
   Feedback records (next round = highest existing + 1 for the same phase).

## Databases (per project, inline on the project page)

Fetch both schemas before writing. If they're missing, create them with exactly this
schema, then add the relation from Tasks.

**Feedback**: `Name` title · `Status` status (Not started / In progress / Done) ·
`date` date · `Actions needed` text · `Phase` select (Phase 1 · UX audit, Phase 2 ·
Homepage concepts, Phase 3 · Design system & templates) · `Verdict` select (Approved /
Changes requested / Undecided) · `Waiting on` select (Client / Us) · `Comment count`
number · `Resolved in Figma` checkbox · `Tasks` (relation, synced from Tasks).

**Tasks**:
```sql
CREATE TABLE ("Task" TITLE, "Status" STATUS,
  "Feedback" RELATION('<feedback data source id>', DUAL 'Tasks'),
  "Concept" SELECT(<one option per concept/screen>, 'All concepts':gray),
  "Device" SELECT('Desktop', 'Mobile', 'Both':gray),
  "Type" SELECT('Fix':orange, 'Keep':green, 'Explore':blue, 'Decision':red),
  "Scope" SELECT('In scope':green, 'Needs estimate':yellow, 'Out of scope':red),
  "Owner" PEOPLE, "Client quote" RICH_TEXT, "Figma comment ID" RICH_TEXT,
  "Figma link" URL, "Resolved in Figma" CHECKBOX, "Created" CREATED_TIME)
```
Add new Concept options with `ALTER COLUMN` when a project has other concepts or screens.

## Steps: new round

1. **Find what's already captured.** Query Tasks for every `Figma comment ID`. These are
   skipped so nothing is logged twice.
2. **Collect comments and screenshots** with the script (needs Figma API access and Pillow):
   ```bash
   python3 .claude/skills/feedback-fix-list/scripts/figma_feedback.py collect <fileKey> \
     --out <scratchpad>/feedback --skip-ids <ids,from,step 1>
   ```
   It writes `manifest.json` (number, ID, author, date, message, replies, frame name,
   deep link, screenshot path) and one PNG per comment, cropped around the comment with
   a pink numbered pin. Look at every screenshot: check that the pin sits on what the
   comment talks about, and note what it's actually pinned on (e.g. a graphic, not the
   header logo). For a comment about the whole page, re-run with `--overview <id>` to
   get a full-frame thumbnail with all pins.
   If the API is unavailable, use the Figma MCP (`get_screenshot` on the frame) and say
   the pins are missing.
3. **Group by concept or screen** using the frame names (`Concept 1 · Desktop`, …).
   Flag comments that are pinned on one concept but talk about others or the whole page.
   Only include comments from the client; skip our own and replies that only say thanks.
4. **Upload screenshots**: `notion-create-file-upload` per PNG, then one multipart POST
   per file to the returned URL with its headers. Use the `file-upload://` source in the page.
5. **Create the Feedback record** in that project's Feedback database:
   - Name `<Phase short> · <deliverable> — round <n> feedback`, icon 💬.
   - Properties: Status Not started, date = date of the comments, Phase, Verdict
     (Approved only if they said so; Undecided when they didn't pick a direction;
     otherwise Changes requested), Waiting on (Client if we need an answer before
     working, else Us), Comment count, Resolved in Figma unticked, Actions needed = one
     line, blocker first.
   - Body, in order:
     1. Red ⚠️ callout for any **blocker** (no pick, contradicting comments, missing info).
     2. Source line: count, author, time range, Figma page link.
     3. Green ✅ callout linking the Tasks database: "fix list lives there".
     4. **Signal at a glance** table: Concept · 👍 Liked · 👎 Concerns · Read.
     5. Blue 💡 callout with **our read**, labelled as not confirmed by the client.
     6. One `##` section per concept (frame links under the heading), one `###` per
        comment: `<circled n> <topic> — <device>`, the client's exact words as a quote,
        the screenshot, then plain bullets of the actions (no checkboxes: Tasks is the
        tracker).
     7. **Open questions for the client**.
     8. **Draft message to the client** (gray ✉️ callout).
6. **Create one Task per action**, linked to the record: Type (Fix / Keep for things they
   liked / Explore / Decision), Concept, Device, Scope (`Needs estimate` for anything
   that may exceed the agreed hours, e.g. motion, new pages), Client quote (only the
   relevant sentence), Figma comment ID, Figma link (`manifest.link`). Several tasks can
   share one comment ID. Add a `Decision` task for each blocker.
7. **Verify**: fetch the record back; check that images rendered and the task count
   matches the Tasks relation.

## Steps: sync an existing round

1. Run `figma_feedback.py status <fileKey>`.
2. For each task whose comment now has `resolved_at`, tick `Resolved in Figma`.
   Don't change the task's Status: resolving a comment in Figma isn't the same as the fix
   being done. Say which ones changed.
3. When every task of a round is ticked, tick the record's `Resolved in Figma`.
4. New comments (not in Tasks) go into a **new round** record, unless the user says they
   belong to the open one; then append sections and tasks there.

## Draft message to the client

Short, friendly, in the user's casual voice. Thank them, ask the one thing that blocks
the work first (e.g. which concept is the base), give our recommendation with the
reason, list in one sentence what we'll change once they answer, and ask about anything
that may change scope. Never say a scope item is included or quote hours. The message
is a draft for the user; never send it.

## Missing or conflicting input

- No Figma access → ask for the file link or comments pasted; still build the record.
- A comment's frame doesn't map to a concept → put it under "General" and say so.
- Comments contradict each other → quote both under the blocker callout.
- Don't copy credentials from the project page into any record.
