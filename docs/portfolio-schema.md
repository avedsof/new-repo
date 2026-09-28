# Portfolio database: proposed fields

Status: **applied 2026-09-28.** All 59 projects re-tagged; Avetex Furniture added (60 rows).

Note: Notion merged "rename old field + add field with the same name" into one field, so the
old Industry and Deliverables values were overwritten. They were restored from
`portfolio-snapshot-2026-09-28.json` (the full pre-change export) into the new fields.
Tags and design are kept as "Tags (old)" and "design (old)".
All 25 "guess" rows were confirmed as built (Design + build).

Goal: the skills can match a job to past work on separate questions (what kind of
engagement, what was delivered, what it runs on, what it does, who it's for, how it
looks, how real it is) instead of one mixed Tags field.

## New fields

| Field | Type | Values | Replaces |
|---|---|---|---|
| Engagement | select | Design + build · Design only · Build only (client's design) · Custom plugin / integration · Concept / test task · UX audit | `design`, part of Deliverables |
| Redesign | checkbox | ticked when an existing site was replaced | "Redesign" tag |
| Deliverables | multi-select (cleaned) | Figma designs · Live website · WordPress plugin · Brand identity · App / dashboard design · Audit report | current Deliverables |
| Pages designed | multi-select | Home page · Landing page · Full site · PDP · Catalog / PLP · Checkout · Dashboard · App screens | page types now in Deliverables |
| Stack | multi-select | ACF · Gutenberg · Custom theme · Elementor · Divi · Kadence · WooCommerce · React · Chart.js · FacetWP · SearchWP · The Events Calendar · Brevo | tech tags (API → Features) |
| Features | multi-select | Booking · Listing / directory · Job board · Membership · Subscriptions · Bidding · E-commerce · Calculator · Blog · LMS · Dashboard · Multilingual · Third-party API sync | feature tags |
| Business model | multi-select | B2B · B2C · DTC · SaaS · Marketplace · Service business | B2B, DTC, SaaS tags |
| Industry | multi-select (cleaned) | see below | current Industry |
| Aesthetic | multi-select | Luxury · Feminine · Clean corporate · Bold / playful · Editorial · Dark / tech · Warm / natural · Minimal | luxury, feminine (moved out of Industry) |
| Proof level | select | Live · Not live · Concept | new |
| Showcase frames | text | Figma links to the 3–6 best frames (hero, key screens) | new |
| Case study | relation → Case studies | links to the in-depth write-up | new |
| Story | text | one line: what the business is → what the work involved → what it achieved | new (cover-letter case format) |

Kept as they are: Project, Link, Figma link, Github, Date, Context, Design, Dev, bid, Placements.
The old **Tags** and **design** fields stay (hidden) until the migration is checked, then get deleted.

## Industry clean-up

- Merge **dentistry** into **dental**.
- Fix the spelling of **entertaiment** → entertainment.
- Move **luxury** and **feminine** to Aesthetic (they describe the look, not the business).
- Keep **lifestyle** only where it's the actual market, otherwise remove.
- Add **recruitment** (MEENZ) and **finance** (for jobs like Miss Money Savvy).
- Rename **saas** → **software / SaaS** and **corporate** → **professional services**.

## Case studies database

Holds the case-study overviews used for Upwork portfolio items. Linked to Portfolio through
the **Case study** relation: MEENZ, Elan, Ana San Sebastian, PlySupply, CSV Product Import
Plugin, SAL ID, Local Links Guide, Avetex Furniture (both versions).
The prompt-titled row ("Could you create me a case study deck…") is to be deleted by hand.

## Re-tagging as proposed (before corrections; guesses were all confirmed as Design + build)

Worked out from the current Deliverables, Tags and Link fields. "guess" means the row is
tagged "full design" but its stack tags and live link suggest it was also built. Please
correct anything wrong; the other new fields migrate mechanically from Tags.

| Project | Engagement | Redesign | Proof level | |
|---|---|---|---|---|
| 8BoxwoodLane | Design + build |  | Live | guess |
| Adalysis Home page Redesign Concepts | Concept / test task |  | Concept |  |
| Ana San Sebastian | Design + build | ✓ | Live |  |
| Apex Motion Studio | Design only |  | Not live |  |
| Application form plugin for persowerk | Custom plugin / integration |  | Live |  |
| Artiseme | Design + build |  | Live | guess |
| Autodex | Design + build |  | Live | guess |
| Autotech | Design only | ✓ | Live |  |
| Barca Camps | Design + build |  | Live | guess |
| Beeline | Custom plugin / integration |  | Live |  |
| Booking Pool&Beach | Design + build |  | Live |  |
| Chaicare | Design only |  | Not live | guess |
| CSV Product Import Plugin | Custom plugin / integration |  | Not live |  |
| Custom calculator - gates | Custom plugin / integration |  | Live |  |
| DIT Plugin | Custom plugin / integration |  | Not live |  |
| Dosetest | Design + build |  | Live | guess |
| Dr Douglas Brown | Design + build | ✓ | Live |  |
| Edumena | Design only |  | Not live |  |
| Elan | Design + build |  | Live | guess |
| Emerem | Design + build |  | Live |  |
| Flexcyble | Design only |  | Live | guess |
| GoodHemp | Design only | ✓ | Live | guess |
| GROSSWOHNBAU | Design + build | ✓ | Live | guess |
| Hajarb48 | Design only |  | Live |  |
| Hammasoskari | Build only |  | Live |  |
| Hot Lake Springs | Design + build |  | Live | guess |
| Huidkliniek Cosmed | Design only |  | Not live |  |
| iDispatch | Design only |  | Not live |  |
| Infinite Equity Capital | Concept / test task | ✓ | Concept |  |
| Inkzu | Design + build | ✓ | Live |  |
| KOLN FC fan shop | Design only |  | Not live |  |
| Koop Skincare Products Shop | Design only | ✓ | Not live | guess |
| Leopoldo Diving | Design + build |  | Live | guess |
| LineSkip - Kiosk App | Design only |  | Not live |  |
| Lineskip Food Delivery App | Design only |  | Live |  |
| Local Links Guide | Design + build |  | Live | guess |
| MEENZ | Design + build | ✓ | Live |  |
| Metaforma | Build only |  | Live |  |
| Museum of Illusions | Custom plugin / integration |  | Live |  |
| Mystea | Design + build |  | Live | guess |
| ORIGINAE | Design only |  | Live | guess |
| PediatricsHealth | Build only |  | Live |  |
| PlySupply | Design + build |  | Not live | guess |
| Promonodes | Design only |  | Not live |  |
| PullsandPars | Design + build |  | Live | guess |
| Rainmaker road | Design + build |  | Live | guess |
| ReelCRM | Build only |  | Live |  |
| SAL ID | Custom plugin / integration |  | Live | guess |
| Sayanchaga WooCommerce | Design + build |  | Live |  |
| Selfologist | Design + build |  | Live | guess |
| Skincare and Moore | Design + build |  | Live | guess |
| Sonrisas Mexicanas | Design only |  | Not live |  |
| Stugor Booking | Custom plugin / integration |  | Live |  |
| Therappy | Design + build |  | Live |  |
| Tulip | Design only |  | Not live | guess |
| Volteam | Design + build | ✓ | Not live | guess |
| Westernacher | Build only |  | Not live |  |
| WooCommerce Inventory plugin > Zoho ERP | Custom plugin / integration |  | Not live |  |
| Zwanzig23 | Design + build |  | Live | guess |
