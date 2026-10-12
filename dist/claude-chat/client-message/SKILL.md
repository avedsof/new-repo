---
name: client-message
description: Turn a developer's or designer's update (often informal, technical, or in Ukrainian) into a message for the client that reads naturally and casually while keeping the technical facts right. Also for status updates, follow-ups, bad news, asks for access or content, and replies to client questions on an active project. Use when asked to write, rewrite, translate or polish a message, reply or update for a client. For new-job pitches use cover-letter; for scoping documents use proposal-writer.
---

# Client message

Mirrored as a Notion Skill: https://app.notion.com/p/3f6bd8b60a63815ebccaf7c11d847456
(keep the two in sync).

Claude chat version of the client-message skill from the avedsof/new-repo repository.
Works without connectors. With the Notion connector, it can also read the client page
and proposal for context.

Turns what the team says into what the client needs to hear. The client should finish
the message knowing what changed for them, what (if anything) they need to do, and what
happens next. They should never have to decode a technical term to get there.

## Inputs

1. **The source:** the developer's or designer's message, notes, a Loom summary or a
   ticket. It may be in Ukrainian or Russian, informal, half-finished or full of jargon.
2. **The client and the thread:** the client's last message and, when there is one, the
   client page in Notion (Clients database, under Lab) with the proposal and what was
   promised. Read them before writing.
3. **Who signs:** usually the name the client already writes to. If it isn't clear, ask.
4. **The channel:** Upwork chat, email, Slack or WhatsApp. If not given, write for chat.

## Step 1: sort the source

Pull every fact out of the source and put it in one of these buckets. Don't write yet.

| Bucket | What goes in it |
|---|---|
| Done | What now works, is live, or is finished, with links |
| Needs the client | Access, content, files, approvals, answers |
| Decision | A choice the client has to make, with the options |
| Next | What we do next and when |
| Risk or bad news | Delays, bugs, limits, extra cost |
| Internal only | Who on our side did what, internal hours and rates, doubts, tool names the client won't touch, blame, other clients |

**Internal only never goes in the message.** Everything else does, unless it changes
nothing for the client.

## Step 2: check before writing

- **Facts only from the source.** No dates, prices, durations or promises that aren't in
  it. If the client will obviously ask "when?" and the source doesn't say, leave a
  `[date?]` placeholder and list it under "Check before sending".
- **Scope.** Compare anything new with what the proposal included. If it's outside
  scope, say so plainly in the message and give the extra hours and price at the agreed
  rates, or leave a placeholder if the hours aren't known. Never slip extra work in for
  free without the user deciding that.
- **Unclear source.** If a sentence in the source can be read two ways and the meaning
  changes what the client hears, ask the user before writing. Don't guess.

## Step 3: translate the technical part

Lead with what it means for the client, then the term only if they need it to act.

| The team says | The client reads |
|---|---|
| "Deployed to staging" | "I've put it on the test copy of the site for you to review: [link]" |
| "Cleared the cache / CDN" | "If you don't see the change yet, refresh the page or give it a few minutes" |
| "Plugin conflict after the WP update" | "I've fixed the booking form after a WordPress update broke it and tested it end to end" |
| "Need DNS access / an A record" | "Could you give me access to your domain settings at [registrar]? I need to point the domain to the new site" |
| "301s set up" | "I've pointed your old links to the right new pages" |
| "LCP down from 4.3 s to 2.1 s" | "I've got the homepage showing its main content in about 2 seconds on a phone, down from over 4" |
| "API returns 429" | "I've spaced out the requests to the booking system because it only accepts a few at a time" |
| "Hotfix pushed to prod" | "I've fixed it on the live site" |

- Keep numbers, names and links exact. Round only for readability ("about 2 seconds").
- A tool or setting name stays only when the client has to find or click it, written
  the way their screen shows it ("Settings → Users").
- One idea per sentence. If a technical point needs two sentences, the second one is the
  outcome for them.

## Step 4: structure

Short, in this order, skipping what doesn't apply:

1. **Greeting with their name** and one line of context tied to their last message.
2. **What's done**, as outcomes, with links.
3. **What we need from you**, as direct asks. Two or more asks, or steps they must
   follow in order, become a numbered list. One ask stays a sentence.
4. **A decision**, when there is one: the options in a sentence each, your
   recommendation and the reason in one more.
5. **What happens next** and when.
6. **Close:** "Hope to talk more soon, [Name]" or "Thanks and hope to talk more soon,
   [Name]", or simply "Thanks, [Name]" in an ongoing thread.

Bad news goes early, in plain words: what happened, what it means for them, what we're
doing about it, and the new date or cost. One "sorry" if we caused it, then the fix. No
blame on anyone, including the team.

Match the length of the client's own messages. A two-line question gets a short answer,
not a report.

## Voice

- A confident freelancer writing to someone they work with. If a sentence could sit in
  a corporate status report, rewrite it.
- Outcome first: "To keep the form spam-free I've added a hidden check", not "I've added
  a hidden check so the form stays spam-free".
- **People do things.** "I" or "we" is the subject. No passive voice and no inanimate
  subject acting on its own ("Payments stay in test mode" → "I keep payments in test
  mode"). No contrast endings like "…, not a copy of production".
- **"I do this because…" in one thought.** Say what you do and why in one sentence. Skip
  the "because" when the client's question already makes the reason obvious. Don't
  chop one thought into several short sentences. "Because" is the only way to add a
  reason: no ", so…", "so that…", "which means…", "instead of…" or "…and not Y".
- **No comma before "and" or "or"**, in lists or between clauses.
- Asks are direct: "Could you send…", "Can I ask you to…".
- Mirror one concrete detail from their last message.
- "I" for the person signing, "we" for the team when the team did it. Never name the
  developer or designer unless the client already knows them.
- 1 light typo at most, in the casual narrative only (a lowercase "i", a letter swap).
  None in names, links, numbers, prices, dates or instructions. Skip it entirely in bad
  news or anything about money.

## Formatting

- **Chat (Upwork, Slack, WhatsApp):** paragraphs of one to three sentences, no headers,
  no bold, numbered lists only for asks or steps. Plain URLs on their own line.
- **Email:** the same, plus a short subject line that says what it's about ("Booking
  form fixed + one thing I need from you").
- No tables, no emoji unless the client uses them first.

## Never

- Em dashes. Colons used as structure.
- "rather than…", "not just X, but Y".
- A comma before "and" or "or".
- Passive voice or a thing as the subject ("The form now sends…", "Payments stay…").
- "Just checking in", "Just following up", "Hope this finds you well", "Please be
  advised", "Kindly", "As per", "Per my last message", "Furthermore/Moreover/
  Additionally", "I look forward to hearing from you".
- Over-apologising, or apologising for things that weren't our fault.
- Internal details: who on our side did what, internal hours or rates, doubts, other
  clients.
- Dates, prices or promises the source doesn't support.
- Offering a call when the client said they don't want one.

## Output

1. The message, ready to paste, between two `---` lines.
2. **Check before sending:** placeholders to fill, facts you couldn't confirm, anything
   from the source you left out on purpose and why (in one line each).
3. If the source was in another language, a one-line note on any term you weren't sure
   how to translate.

## Example

Source (developer, Ukrainian, informal):
> Оновив WP до 6.6, після цього злетіла форма бронювання через конфлікт з плагіном календаря. Відкотив плагін, все працює, протестив 3 броні. Але треба буде або міняти плагін, або чекати поки вони пофіксять, це десь 2-3 год якщо міняти. Ще потрібен доступ до Cloudflare щоб налаштувати кеш.

Message:

---

Hi Sarah,

Quick update on the site. When I updated WordPress this week the booking form stopped working for a short time but I've fixed it and tested three bookings end to end.

For now I've held the calendar plugin on its older version because the new one clashes with the update. I'd spend about 2 to 3 hours ($50 to $75) swapping it for a better-supported plugin because I don't want the next update to break bookings again. We can also wait for its developers to fix it if you'd rather hold off.

One thing I need from you. Could you add me to your Cloudflare account? I'd like to set up caching there to make your pages load faster.

Thanks and hope to talk more soon,
Yulia

---

Check before sending: confirm the 2 to 3 hours are outside the current scope and the rate is $25/h; add the Cloudflare invite email if she'll ask which one.
