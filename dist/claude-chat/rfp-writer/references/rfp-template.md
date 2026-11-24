# RFP page template (Notion-flavored Markdown)

Copy, fill the `<…>` parts, delete sections that don't apply (Options, Draft answers).
Children inside callouts, tabs and toggles must be indented with tabs.

```markdown
<callout icon="🎨" color="gray_bg">
	**Color key:** ⬜ gray = context · 🟥 red = already sent to the client, keep consistent · 🟦 blue = Option 1 · 🟪 purple = Option 2 · 🟨 yellow = needs your judgment · 🟩 green = estimate. Tools, features and hour ranges are marked as `code`.
</callout>
<callout icon="🇺🇦" color="gray_bg">
	## Коротко про проєкт
	<2–3 речення українською: хто клієнт, що треба зробити, що потрібно від тебе зараз.>
</callout>
<callout icon="👤" color="gray_bg">
	## The client
	**<Name>**, <role> of **<Company>**: <what the business is>. <Hard requirements from the brief>.
	Selection process / deadline: <…>.
</callout>
<callout icon="🔑" color="red_bg">
	## What we've sent already
	- Proposal: [<Figma/Notion>](<url>)
	- Price quoted: `<$range>` · timeline `<weeks>`
	- <Promises, recommendations the client is reacting to>
	<span color="red">**Note:** <discrepancy, if any></span>
</callout>
<callout icon="📩" color="gray_bg">
	## What the client is asking now
	<tabs>
		<tab icon="❓">
			Their questions
			1. <…>
		</tab>
		<tab icon="🎯">
			What they really want
			- <…>
		</tab>
		<tab icon="✉️">
			Source
			> <quoted job post / message / meeting recap excerpt>
		</tab>
	</tabs>
</callout>
<callout icon="🧱" color="gray_bg">
	## Scope
	<tabs>
		<tab icon="🗺️">
			Pages
			<…>
		</tab>
		<tab icon="👪">
			Flows
			<…>
		</tab>
		<tab icon="💳">
			Payments / integrations
			<…>
		</tab>
		<tab icon="🧰">
			Stack
			<…>
		</tab>
	</tabs>
</callout>
## <Options heading>
<tabs>
	<tab icon="🟦">
		Option 1 · <name>
		<callout icon="🧭" color="blue_bg">
			**<One-line summary>**
			**How it works**
			- <…>
			**Limits**
			- <…>
			**Still manual:** <…>
		</callout>
		<callout icon="💸" color="green_bg">
			**My estimate:** design `+<h>` (\$<…>) · dev `+<h>` (\$<…>) → total about **\$<range>**.
		</callout>
	</tab>
	<tab icon="🟪">
		Option 2 · <name>
		<callout icon="🧩" color="purple_bg">
			<same structure>
		</callout>
		<callout icon="💸" color="green_bg">
			**My estimate:** <…>
		</callout>
	</tab>
	<tab icon="⚖️">
		Compare
		<table header-row="true" header-column="true">
			<tr>
				<td></td>
				<td color="blue_bg">Option 1</td>
				<td color="purple_bg">Option 2</td>
			</tr>
			<tr>
				<td><criterion></td>
				<td><…></td>
				<td><…></td>
			</tr>
		</table>
		<callout icon="💡" color="gray_bg">
			**My recommendation:** <…>. <Condition that would change it>.
		</callout>
	</tab>
</tabs>
## Your review
<callout icon="⚠️" color="yellow_bg">
	## Needs your judgment
	- [ ] **<Question>:** <detail with `tool` names>
</callout>
<callout icon="💸" color="green_bg">
	## Request for estimation
	Please confirm or adjust the hours below. Rates: design `$30/h`, dev `$25/h`.
	<table header-row="true" fit-page-width="true">
		<tr>
			<td>Workstream</td>
			<td>My estimate</td>
			<td>Your estimate</td>
			<td>Notes</td>
		</tr>
		<tr color="gray_bg">
			<td>**Base:** <workstream></td>
			<td>`<h>`</td>
			<td></td>
			<td></td>
		</tr>
		<tr color="blue_bg">
			<td>**Opt 1:** <workstream></td>
			<td>`<h>`</td>
			<td></td>
			<td></td>
		</tr>
	</table>
	**Deliverable from you:** <what the developer returns>.
</callout>
<details>
<summary>📝 Draft answers to the client (pending your review)</summary>
	1. <…>
</details>
<details>
<summary>📎 Sources</summary>
	- Job post: <link or "client page, Job post tab">
	- Client messages: <…>
	- My notes: <…>
	- Meeting recap: <mention or "none">
</details>
```
