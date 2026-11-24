# Cover letter V2 for ChatGPT

The Claude "v2" cover-letter skill, packaged for ChatGPT, with the whole portfolio bundled
so it works without a Notion connector. Portfolio snapshot: 24 Nov 2026 (71 projects, 9 case studies).

## Files
- `SKILL.md`: the instructions (Agent Skills format).
- `references/portfolio.md`: every portfolio project, readable.
- `references/portfolio.json`: the same data, structured.
- `references/case-studies.md`: case study overviews.
- `gpt-instructions.txt`: short instructions for the Custom GPT route.

## Install as a ChatGPT skill
If your ChatGPT plan offers Skills, upload the zip there as a skill.
The skill reads its own `references/` files.

## Install as a Custom GPT
1. Explore GPTs → Create → Configure.
2. Paste `gpt-instructions.txt` into Instructions.
3. Upload `SKILL.md`, `references/portfolio.md` and `references/case-studies.md` as Knowledge.
4. Turn on Web Search so it can look up the client's site.

## Updating the portfolio
The files are a snapshot. When the Notion Portfolio changes, ask Claude to rebuild this package.
