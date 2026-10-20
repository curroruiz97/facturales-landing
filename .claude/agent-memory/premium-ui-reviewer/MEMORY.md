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
