# Writing rules for this project

These apply to everything written for a client or a lead: messages, cover letters,
proposals, RFP drafts, decks and Notion pages. They take precedence over the voice rules
inside individual skills where the two disagree.

## 1. People do things

Write with "I" or "we" as the subject. No passive voice, and no inanimate subject acting
on its own ("Payments stay in test mode", "The database lands on staging", "Webhook
endpoints use test secrets"). No contrast endings like "…, not a copy of production" or
"…and not Y".

| Instead of | Write |
|---|---|
| "Payments stay in Stripe test mode on staging." | "I keep payments in Stripe's test mode on staging because no real card should be charged while we test." |
| "The database that lands on staging is anonymised, not a copy of production." | "I anonymise the database before it goes on staging because it holds your customers' details." |
| "Webhook endpoints use separate test secrets, so staging can't act on real Stripe events." | "I give staging its own Stripe test keys because a test should never touch a real payment." |

## 2. No comma before "and" or "or"

Not in lists ("design, build and launch") and not between two clauses ("It's fixed now
and I've tested it").

## 3. "I do this because…" in one flowing thought

- Say what you do and why in the same sentence: "I do X because Y." Skip the "because"
  when the client's own question already makes the reason obvious.
- Keep one thought in one sentence. Don't chop it into several short sentences that
  each restate part of it.
- Keep paragraphs to one to three sentences. Break by thought and use a numbered list
  for steps or asks because readers skip long blocks of text.
- "Because" is the only way to add a reason. Still no tails like ", so…", "so that…",
  "which means…" or "…instead of…".
