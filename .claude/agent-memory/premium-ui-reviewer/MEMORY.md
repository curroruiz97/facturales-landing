# Premium UI Reviewer — Agent Memory

## Project: Facturales Landing (facturales.es) — static HTML, see /CLAUDE.md
NOTE: the first notes of this file (Neotix template tokens #F94D00, Inter, `.sub-title`, bootstrap accordion) are OBSOLETE.
Current system: `assets/css/facturales-ds.css`, `body.fx`, `fx-*` classes, Onest font, orange #EC8228 on near-black, pill buttons.

### CSS organisation (end of facturales-ds.css)
- [A] global/header/footer/mobile menu/home, [B] pricing/funciones/faq/contact/about/404, [C] module pages (`body.fx-pagina-modulo`), [D] blog/articles.
- Tools used for review: Playwright via `createRequire("/home/user/facturales/package.json")`, chromium at /opt/pw-browsers/chromium; checker `.../scratchpad/landing/medir.mjs` (pricing "cortado" = `.fx-sr` false positives).
- Screenshots must scroll the page first (lazy images). Contact sheets via PIL work well for reviewing many chunks.

### Patterns that work (keep)
- Compact mobile cards (icon + title in one row, text below) — used in [C] and now also in [A] for home Seguridad, funciones Además, pricing "Incluido".
- Pricing plan cards use subgrid (`.fx-planes--alineados`) -> price/CTA/list aligned in monthly AND annual mode at 900+; tablet = price+CTA left, list right.
- Orphan last card in 2-col grids: span full row (`:last-child:nth-child(odd)`).
- Subgrid for 4-col icon/title/text cards at >=1200 aligns text when a title wraps.

### Issues found/fixed in the responsive pass (2026-10)
- Home manifiesto h2 (72px) was bigger than h1 (64px) at >=1333px and its box was centered at 1080px (left edge 84px off the grid) -> capped to 56px, aligned.
- Landscape phone (844x390): home h1 had max-width 15ch -> 4 lines, CTA below fold; widened to 24ch.
- Contact privacy link in checkbox label measured 20px tall -> inline-block with 12px block padding / -12px margin.

### Recommendations not applied
- Funciones mobile: 10 module cards of ~415px each (~4000px scroll); consider 2-col mini grid or horizontal screenshot crop smaller.
- Home/pricing: FAQ heading is left-aligned in a narrow centred column while neighbouring section headings are centred.

### Pricing review (2026-10-20, plan change Starter/Pro/Negocio)
- `.fx-lista` is `display:grid`; inside the subgrid row of `.fx-planes--alineados` (>=900px) its auto rows STRETCH, so the shorter list (Negocio, 6 li) gets airier spacing than Pro (8 li). Fix: `.fx-plan .fx-lista{align-content:start}` (verified in-page: gaps uniform, Negocio tail ~48px).
- `.fx-badge--nuevo` inside `.fx-tabla__grupo th` inherits `text-transform:uppercase` + letter-spacing from the group label and makes the row 59px vs 52px; fix `.fx-tabla__grupo .fx-badge--nuevo{margin-block:-4px;margin-inline-start:8px;text-transform:none;letter-spacing:0}` (verified: all group rows 52px / 44px mobile).
- Contrast numbers (all pass): badge #F5A35C on rgba(26,13,2,.72) ≈ 9.3:1; group label #EC8228 on table surface ≈ 6.9:1; ink-3 .60 ≈ 7.2:1.
- Comparison table: 7 of 17 data rows are ✓✓✓ identical and duplicate the «Incluido en todos los planes» cards (~26% desktop / ~31% mobile of table height). Single-row groups (Nóminas, Almacenamiento) cost a 52px header each.
- Pre-existing: table group `<th scope="rowgroup" colspan=4>` sits inside ONE `<tbody>` (misuse; needs one tbody per group); breadcrumb «Inicio» link 34x18px.
- Copy risk: badge «Todo incluido» on Negocio next to «+ IVA» and OCR 400 / nóminas 25 caps is an overclaim (project rule: no invented claims).
- Playwright recipe works: createRequire("/home/user/facturales/package.json") + chromium-1194; hide fixed header with addStyleTag before element screenshots (sticky header otherwise overlays crops).
