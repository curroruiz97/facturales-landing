# Premium UI Reviewer — Agent Memory

## Project: Facturales Landing (facturales.es)

### Design System Tokens
- `--theme: #F94D00` (orange, primary CTA)
- `--header: #0B0D17` (dark headings)
- `--text: #534F5A` (body)
- `--bg: #EFEDE5` (page background, warm off-white)
- `--bg2: #0F172A` (dark sections)
- Fonts: Inter (body, 16px/28px), Plus Jakarta Sans (headings)
- `--box-shadow: 0px 1px 14px 0px rgba(0,0,0,0.13)`
- Border radius on `.theme-btn`: 100px (pill)
- `.theme-btn` hover: circle clip-path reveal, fills to `--header`

### Component Conventions
- `.sub-title` MUST be inside `.section-title` wrapper to get correct pill styles (white bg, uppercase, 14px, Plus Jakarta Sans)
- `.sub-title` always includes a small icon img (`assets/img/home-1/hero/setting.png`) — this is the site's visual language for section eyebrows
- FAQ uses `.faq-items .accordion` pattern with orange active button; bare Bootstrap accordion does not match site style
- Footer is template-inherited; still contains Neotix placeholder content (hello@neotix.com, Riverside Park) across 26 HTML files — global find-replace needed

### Pricing Page Review (2026-03-05)
- Reviewed `pricing.html` — complete rewrite with toggle, 3 cards, included section, comparison table, FAQ, CTA
- Critical: header-top still has Neotix placeholder content (address, email) — not pricing-specific but present
- Critical: `.sub-title` used without `.section-title` wrapper — will not render correctly
- Critical: CTA gradient goes orange → amber → yellow (#f59e0b) — color creep, off-brand
- Critical: Pro card blue (#3b82f6) is a strong brand deviation; Pro CTA uses blue gradient, not --theme
- Issue: Accordion is bare Bootstrap with no styling override — will render Bootstrap default (blue focus ring, grey bg)
- Issue: Comparison table shows "250/año" for Starter but pricing card says "10 facturas/mes" (120/year) — data inconsistency
- Issue: `--pr-*` duplicate root vars are redundant; should use existing `--theme`, `--header`, `--text`, `--bg` tokens
- Issue: Plan descriptions are italic (`font-style:italic`) — unusual and weak for a SaaS product
- Issue: `.pricing-cta` is left-aligned with only col-lg-8 filled — right side is empty
- Good: Toggle animation and annual badge are clean; included-section dark cards are well-structured
- Good: Comparison table pattern (expandable) is functional and appropriately scoped

### Recurring Site Issues
- Template placeholder content (Neotix branding) still present in header-top across all pages
- `sub-title` must be in `.section-title` container
