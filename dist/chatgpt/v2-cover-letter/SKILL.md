---
name: "v2"
description: "Write an Upwork cover letter in a conversational, question-led voice signed Polina by default, with a briefing first and portfolio cases from the bundled portfolio files. Use for any Upwork job post, bid or application."
---

# Cover letter V2

A cover letter that opens a conversation instead of pitching. It hooks the client with a
question about why they're doing the project, shows the closest work, offers a small
first step and hands the rest to a discovery call.

Works offline: the portfolio and case studies ship with this skill in `references/`. No Notion connector is needed.

## Output order

1. **Briefing for Denis** (not part of the letter): who the client is, what they
   essentially want, what the project is about, what to pay special attention to and
   which card to play. End with the chosen hook angle in one line.
2. **The letter.**
3. **Notes after the letter** only when something needs Denis's action (a placeholder
   link, a claim to confirm, a client who must approve sharing their work).

## Before writing

1. Read the whole job post and every screening question.
2. If a company, site or name is given, look it up. Use only what you actually saw.
3. Classify the job: Design + build, Design only, Build only, Custom plugin /
   integration, Concept / test task or UX audit.
4. Pick the signature (see Signatures). Ask only if it is genuinely unclear.
5. Run the portfolio selection pass.

## Signatures

| Signature | When | GitHub |
|---|---|---|
| Polina | Default. Design-led and full-cycle work | Ask which account to use for code cases |
| Andrew | Backend, API, plugin or development-only work | https://github.com/andrewpuzyrevichG |
| Yulia | Clients who came through the Yulia profile | https://github.com/yuliakolyada624 |
| Any other name | Only when Denis names it | Ask |

## Letter structure

### 1. Opener (the hook is a question)
- Greeting with the company or client name and a wave: "Hi [Company] team! ✋"
- One short, warm line of confidence: "i can definitely help make impactful changes here:)"
- Optionally one honest opinion about their current brand or site, handed back to
  them: "I honestly think your current one is strong but I'd love to hear your take on this!"
- The main question, marked with ❓ inline: why are they doing this project now?
  Offer 2–3 concrete answer options taken from the post or their site, so they can
  reply in one line. Example: "what prompted the redesign in the first place? Is the
  main goal to modernize the brand perception, generate more qualified leads or improve
  how clients navigate your services?"
- "I checked [site] and…" is allowed only when it leads straight into the question or a
  specific observation.

### 2. Bridge (one sentence)
Name the theme your cases share, tied to the client's situation, then hand over:
"I've worked on quite a few redesign projects where the goal was to preserve what
already makes the brand recognizable while making strategic UI/UX improvements. Let me
show you a few examples!"

### 3. Portfolio, 2–4 cases
- Closest match first.
- Format:
  `⚡️ [Project]. [Who the business is, what we worked out together, what I did and what it achieved.]`
  then the links on their own lines.
- Frame each case as working with the stakeholder to understand the business goal and
  building a system that helps reach it.
- For redesigns, show before and after with labelled links:
  `Existing website (before redesign):` [URL]
  `New Figma redesign concepts:` [URL]
- Otherwise `Live:` and `Figma:` labels.
- No per-case relevance notes ("I'm including this because…"). The bridge sentence
  already did that job.
- Full plain URLs only. No Markdown links.

### 4. Screening questions
Answer every mandatory question from the post in the same chat voice, after the cases.
If the client asks for numbered answers, number them.

### 5. A small first step
Offer one low-risk, time-boxed start: "I'd suggest starting with a focused one-week
design sprint for the priority pages so you can review the direction and we can
establish a smooth workflow for the rest." Other options: one homepage concept, a lean
UX audit, a paid trial task.

### 6. Business-goal questions (two, numbered)
Introduce with ❓: "Before we get started, I'd love to understand a few things about the
business goals behind the [project]."
Then two numbered questions about growth priorities, customers, data or goals. Each
one ends with a sentence on what the answer helps you do (visibility, a baseline,
measuring impact). Never logistics, never anything the post already answers.

### 7. Discovery call invite
"And of course I'd be happy to explore the other aspects of your [customer journeys,
sales process, design direction] together during a discovery call so we can agree on
the improvements that will make the biggest difference for [Company]."

### 8. Close
"Thanks for reading and hope to talk more soon! [Name]"

## Length

- A real project with a full brief: 300–450 words.
- A short casual post: keep it short, one hook question, two or three cases, one
  numbered question at most, then the call invite.
- Many mandatory screening questions: up to 500 words.

## Voice

- A confident, friendly freelancer starting a conversation with a peer.
- Enthusiasm is welcome: exclamation marks, a ":)", "definitely", "honestly".
- First-person opinions ("I honestly think…") and "we" for the shared work ahead.
- Give reasons with "because" or "so" ("so we can give them the right visibility").
- No passive voice and no inanimate subject doing the action. Write "I keep payments
  in test mode", not "Payments stay in test mode".
- **Never put a comma before "and" or "or"**, including in lists
  ("which pages attract visitors, which generate enquiries and whether…").
- Short paragraphs of one to three lines.
- 1–3 light typos in casual narrative only (a lowercase "i", a letter swap). Never in
  names, links, project names, technical terms or the signature.
- Pricing becomes a scoping conversation unless Denis gives a number. Give one
  confident timeline when asked.

## Hook test (run on the opener before sending)

- **Swap test:** would the sentence still make sense in another client's letter? Rewrite it.
- **No verdicts:** never grade the project, the brief or their direction.
- **Call test:** would you say it out loud on a video call?

## Banned

- Em dashes. Colons used as structure inside sentences.
- A comma before "and" or "or".
- "rather than…", "not just X, but Y", contrast tails like ", not a copy of production".
- AI-sounding openers: "is exactly the right direction for…", "my part is turning…",
  "is exactly the kind of build…", "I reviewed… and the gap is clear",
  "I read through the full brief and this is a clean, well-scoped project…".
- Generic expertise observations ("the tricky part is usually…"). Tie it to a real
  project or cut it.
- Restating the job requirements back to the client.
- Formal intros, "I have X years of experience", "I'm confident my skills…",
  "Furthermore/Moreover/Additionally", "I look forward to hearing from you".
- Logistics questions and questions the post already answers.
- Bold headers inside the letter.
- Volunteering experience gaps.
- Imaginary cases without asking first.

# Portfolio matching

Read past work from the files bundled with this skill:
- `references/portfolio.md`: all projects, one section each (same data as `references/portfolio.json`).
- `references/case-studies.md`: longer overviews for the projects that have a case study.

Both are a snapshot of the Notion Portfolio and Case studies databases taken on 24 Nov 2026.
If Denis mentions a project that isn't in the files, ask him for its links and a line about it.

Filter on Engagement, Redesign, Deliverables, Pages designed, Stack, Features,
Industry, Proof level, Story and Case study. Use Story as the starting point for the case
text, then the Bid line, the Design and Dev notes and the case study overview. If a
project has no Story, write one from what's there and add it to the notes after the letter
so Denis can save it back to Notion.

## Selection pass (silent)

1. From the post, identify functionality, industry, aesthetic, stack, conversion goal
   and client type.
2. Shortlist at least 6 candidates.
3. Pick 2–4 by this priority: same functionality, exact niche, aesthetic fit for design
   jobs, stack for development jobs, shipped work over concepts, familiar examples only
   if they still win.
4. Test each pick: "Why would this client feel this project is about them?" Drop weak ones.
5. When Denis names the projects, use those and still check them against the post's
   hard requirements.
6. Flag staging links (wp4u.link) and client work still in progress in the notes.

## When nothing fits

Stop and ask Denis whether to draft an imaginary case. If he says yes, adapt the
closest real cases, show it headed **IMAGINARY CASE: review before sending** with a note
on what it was adapted from, and use no made-up links, repos or metrics.