---
name: ux-audit
description: Produce a UX audit presentation in Figma for a redesign project — findings grouped by area, each shown on an annotated screenshot with the problem and the proposed change, plus a sitemap tree, a page inventory by purpose and guest action, next steps and questions to confirm. Always also produces a separate internal scope-and-estimate deck that is never shown to the client. Use only when the project is a redesign (or the client bought the Phase 0 audit); not for plugin, dev-only or concept tasks.
---

# UX audit deck

Mirrored as a Notion Skill: https://app.notion.com/p/3f0bd8b60a638188b6c6ecaa99ce61f6
(self-contained copy with the deck style rules inlined; keep the two in sync).

Two references for what good looks like:
- **Grande Hot Springs audit**, slides 13–27 (facts that disagree, navigation today vs.
  proposed, sitemap tree, page inventory by purpose, booking paths, next steps,
  questions): https://www.figma.com/design/h65PEq9q85PqSbC8rm0zap
- **Miss Money Savvy audit**, slides 27 onwards:
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
5. **Findings stay tight.** 8–12 finding slides. The whole deck, with structure, next
   steps and questions, usually lands at 20–28 slides.
6. **Only verified facts are stated as facts** (see "Fact check" below). Anything the
   client has to confirm becomes a question at the end, not a claim in a slide or a visual.

## Deck structure (in order)

1. **Cover:** client, "UX audit", date.
2. **Scope and verdict:** what was reviewed (pages, devices, journeys), and the overall
   call in two or three sentences (refresh vs. restructure).
3. **Top changes:** the 3–5 highest-impact changes, ranked by cost to the client.
4. **Audience and competitors** when the proposal calls for it.
5. **Findings by area**, in this order, skipping areas with nothing that passes the filter:
   Home page → Key journeys & booking/conversion → Trust & proof → Forms & tools →
   Visual system. When the same fact reads differently on different pages (prices,
   sizes, names, emails, seasons), add a **"facts that disagree"** table:
   `Topic | What the site says today`, each row naming both versions.
6. **Navigation: today vs. proposed.** Two cards side by side: today's menu items as the
   site shows them, and the proposed menu grouped by what people came to do.
7. **Sitemap tree** (always). See "Sitemap tree slide".
8. **Page inventory by purpose** (always). See "Page inventory slides".
9. **Key journey paths**, when a journey splits across systems (booking, checkout,
   enquiry): `Stay/product | The button leads to | Depends on`, where "Depends on"
   names the question number that decides it.
10. **Proposed page structure** for the key page: logic line plus sections, as in the
    proposal skill.
11. **URLs and assumptions:** what happens to current URLs (kept, relabelled, redirected,
    removed after checks) and the 3–5 assumptions the structure rests on, each tied to a
    question.
12. **Polish list** (optional, one slide): small visual fixes, bulleted.
13. **Next steps:** 4 cards: anything urgent, the questions that unblock the structure,
    what gets designed first, access and materials. Follow with one slide for access
    (`Access | Why we need it | Role`, never passwords) and one for missing materials
    (`Material | What it's for`) when there are any.
    When the next phase is homepage concepts, add a short **What happens next** block so
    the client knows what the concept review will look like: what they'll receive (2–3
    concepts in desktop and mobile, key element states), how to give feedback (pick the
    one that feels most like them, mix freely, comment in Figma or reply) and that they
    approve the direction before the design system. Use the "How the concept review works
    for you" module in the `proposal-writer` skill as the source; keep it consistent with
    what the proposal promised.
14. **Questions to confirm** (always last). First a slide with the questions that shape
    the structure and the estimate (cards: question + "Shapes …"), then content
    questions as `# | Topic | Question`, six per slide. Every question changes scope,
    price or content; each is answerable in one sentence.

## Sitemap tree slide

- Title states the count and the promise: "15 pages in 5 menu sections. Every current
  URL stays".
- A root box for the home page, a connector bus, and one column per menu section.
- Each page is a chip with **the URL on the first line** and **the menu label under
  it** (smaller, body colour), so the client sees both what changes in the menu and
  what stays in the address bar.
- **New pages are highlighted** with a fill colour (mint on the Grande deck); current
  pages keep the canvas colour. A legend top right: "New page" and
  "Current URL · menu label below".
- No arrows or icons; the tree has to fit one slide at the minimum type sizes.

## Page inventory slides

Led by what each page is for and what the visitor should do there, not by audit depth.

- Columns: `Page | What it's for | Guest action | Verdict` (call the third column after
  the site's user: guest, customer, member).
- Page = the URL, with the new menu label under it when it changes
  (`/healing-waters/` · "menu: Hot Springs").
- Verdict is a coloured pill from a fixed set: **New** · **Redesign** ·
  **Keep + restyle** · **Keep + unify** · **Rewrite** · **Merge** · **Remove**.
- Split across two slides when there are more than 8 pages: first the home page, the
  key conversion page and all new pages; then the current pages that keep their URLs.
- End each slide with a one-line takeaway card (why the split, what stays).

## Finding slide anatomy

- Area name in the slide header (same position on every slide).
- A plain, descriptive headline stating the issue ("Hero has five equal-weight buttons").
- The screenshot, whole or cropped to exactly the problem region, with numbered markers.
- For each marker: **Problem** (what happens and what it costs) → **Change** (what we do
  instead). Add **Why** only when the reason isn't obvious.
- Up to three markers per slide; more means split the screen into two slides.
- **End each Problem and Change line on the fact or the action.** No tail that explains
  why or argues against something nobody suggested: ", so…", "so that…",
  "before anything…", "…and not Y", "instead of…", "which means…".
  Test: cover the tail. If the line still says everything, cut it. If the reason
  matters, it goes in **Why**.
  "Merge the two menus so visitors find the booking page faster" → "Merge the two
  menus." with Why: "Visitors look for booking in two places."
  The same rule applies to slide headlines, the verdict and next-step cards.

## Fact check (before building, and again before sending)

Lessons from the Grande Hot Springs partner review:
- **Count from the live site, not from memory.** Carousel cards are not all products
  (an info card is not a stay). Counted items ("8 stays", "13 fields", "three places")
  must match the list the slide gives.
- **"The only place that says X"** needs a search of every relevant page first.
- **Form field counts** come from a real test of the form: count required fields.
- **Relationships with third parties** ("sister resort", partners, owners) are never
  stated unless the site states them publicly. Ask instead.
- **History, dates and superlatives** ("since the 1860s") need a source on the client's
  own site; otherwise cut them.
- **Conflicting numbers** (90 ft vs. 80 ft) stay out of headlines and visuals until
  confirmed; they live only in the "facts that disagree" table and the questions.
- **Names** in visuals follow the proposed structure (e.g. "Tiny Home"), not whichever
  variant the site happens to use.
- Don't advertise another business's product as the client's (a neighbour's day soak
  in the client's "Ways to stay" grid).

## Internal scope deck (always, never shown to the client)

Every audit also produces an internal deck for the partners' review: what we would sell
on the basis of the findings, and for how much.

- **A separate Figma file** named `INTERNAL · <Client> · Scope and estimate`, in the same
  team as the audit. Never a page in the client's audit file: anyone with the audit link
  can open every page of that file.
- Every slide carries "INTERNAL · not for the client" in pink in the header.
- Rates and rules come from the `proposal-writer` skill: design $30/h, development
  $25/h, hours as ranges, design and development always separate.
- Six slides:
  1. Cover: sources (audit link, date, revision), rates.
  2. Options: any urgent paid quick fix, **A** fix the current site, **B** restructure +
     redesign + build; hours, price, timeline, and which one we recommend and why.
  3. Design scope: `Workstream | What it includes (audit slide) | Hours`, total row.
  4. Development scope, same table.
  5. What moves the estimate: `Question | If the answer is… | Change | Extra hours`,
     plus the worst case with every add-on.
  6. Assumptions, exclusions and risks.
- Tie each workstream to the audit slide it comes from, so the proposal can cite it.

## Getting screenshots

Capture the live site with Playwright (desktop 1440 wide, mobile 390 wide), full page,
then crop regions per finding. Scroll the whole page before capturing so lazy and
animated content appears. Keep the full-page captures for the sitemap and inventory
slides. Never squash a screenshot to fit a frame.

## Visual rules

Follow `references/deck-style.md`. Load the `figma:figma-use` skill before building slides.
