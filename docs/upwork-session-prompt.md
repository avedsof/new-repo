# Upwork + Notion client messages: session prompt

Paste the block below as the first message of a new session.

---

Set up my Upwork → Notion → client-message workflow for this session.

**Ground rules**
- Upwork is read-only for you. Never call send_message, confirm_preview, respond_to_offer,
  manage_proposals, manage_milestones, update_contract, end_contract or any other write
  tool. I paste every message into Upwork myself.
- Ask me before every Notion write. Show what you'll change first.
- Write every client draft with the client-message skill and the rules in CLAUDE.md.

**1. Check the account**
Call list_accounts and tell me which Upwork account is connected. Our bids in Notion
(Upwork Bids → "Upwork Profile") come from Yulia, Andrew, Polina, Shevk and Nastya.
If the connected account isn't the profile the client talks to, stop and tell me. Don't
read another account's rooms instead.

**2. Link clients to their chat rooms**
For each record in Clients (collection://3ebbd8b6-0a63-8052-8f6a-000bb28c7a6f) with an
empty "Upwork room":
- search_rooms by the client's name, then by the job title from the related bid.
- One clear match: propose https://www.upwork.com/ab/messages/rooms/<room_id> as the
  "Upwork room" value.
- Several matches or none: list them and let me pick. Don't guess.
Show me the full list of matches. After I confirm, write them in one go.

**3. Follow-up sweep**
Collect:
- rooms where awaiting_reply_from is "you" (the client wrote last), and
- Interviews (collection://fd213f62-e364-4257-9ebd-67edd75e1e21) with Follow-up Date
  today or earlier and Interview Stage not Won or Disqualified.
For each client, read:
- the thread (list_messages, newest first; page back with the cursor until the context
  is clear),
- the Clients page (Job post and Client message tabs) and any proposal or RFP page
  linked from it,
- call notes from Granola and Upwork meeting recaps (manage_meetings list_recaps).

**4. Output per client**
- Name and one line on where things stand.
- The draft between two `---` lines, signed with the name on that Upwork profile.
- "Check before sending": placeholders, facts I need to confirm, anything you left out.
Start with the clients who've waited longest.

**5. After I approve**
Propose updates to Interviews (Interview Stage, Follow-up Date, Lost reason, Estimated)
and to the Clients page. Write them only after I say yes. If I paste back the version I
actually sent, compare it with your draft and suggest one or two changes to the
client-message skill.
