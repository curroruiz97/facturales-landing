# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Landing site for **Facturales** (facturales.es) — a financial suite (facturación, bancos, cobros, gastos, impuestos) for Spanish freelancers and SMEs. The app itself lives at `app.facturales.es`; this repo is the static marketing site only.

## Architecture

- **Static HTML site** — no build system, no bundler, no SSR. Pages are plain `.html` files served directly.
- **Design system**: `assets/css/facturales-ds.css` (loaded AFTER `main.css` on every page). All new markup lives under `body.fx` and uses `fx-*` classes (buttons, cards, badges, sections, mockups, FAQ accordion with `<details>`, pricing, forms, article prose, header, footer). `main.css` is the legacy template sheet (Neotix); keep it loaded but do not build new components with it.
- **Shared header/nav**: injected via `assets/js/header-include.js` (`document.write`). **Shared footer**: `assets/js/footer-include.js`. Edit navigation/footer there, not in pages. Behaviour (menu Producto, mobile menu with focus trap/Esc, pricing toggle, contact form → mailto) lives in `assets/js/facturales.js` (vanilla, no dependencies).
- jQuery/GSAP/Swiper/MeanMenu and the preloader are no longer used by the real pages (only by legacy template demo pages).
- Template demo pages (`index-2/3/4`, `team*`, `project*`, `service*.html`, `service copy.html`, `service-details copy.html`) carry `noindex, nofollow` and are not linked; `news.html`/`news-details.html` are noindex copies of the blog index.

## Brand / Design tokens (`:root` in facturales-ds.css; mirrored in main.css)

```
--fx-acento: #EC8228        corporate orange (exact). Hover #d47524
--fx-acento-claro: #c2410c  orange text on light backgrounds (AA)
--fx-sobre-acento: #1a0d02  text on orange fills (never white)
--fx-ground: #020100        near-black page background
--fx-glow: #c66121 → #673011 → black   radial glow, top right
--fx-surface: rgba(255,255,255,.07)  --fx-line: rgba(255,255,255,.14)
radii 8 / 12 / 22 px, pill buttons; green only for semantic «ok/cobrado/ingreso»
```

Font: **Onest** (Google Fonts, 400/500/600/700) everywhere. Icons: inline SVG, 2 px stroke, one family (Lucide-style; copy them from existing pages or `header-include.js`). Light sections (`.fx-claro`) only for long reading (articles). Logo: rombo `assets/img/logo/facturales-rombo.svg` (+ `-oscuro` for light backgrounds) with the word «Facturales» in Onest 700; favicon `assets/img/favicon.svg`.

## Key Pages

- `index.html` — Home (suite financiera: hero, módulos, Bancos, Cobros, Gastos, Impuestos+VERI*FACTU, Equipo, Seguridad, Apps, precios, FAQ, CTA)
- `funciones.html` — all modules; `pricing.html`; `faq.html`; `contact.html`; `about.html`; `404.html`
- Module pages: `crea-envia-facturas.html`, `crea-envia-presupuestos.html`, `bancos-conciliacion.html`, `cobros.html`, `escanea-gastos.html` (Gastos y justificantes), `impuestos.html`, `tu-negocio-bajo-control.html` (Panel y gráficas), `gestiona-clientes.html`, `gestiona-tu-stock.html` (catálogo de productos y servicios — the app has NO stock/warehouse control), `factura-personalizada.html`
- Blog: `news-grid.html` (index) + articles `verifactu-2027-guia-autonomos-pymes.html`, `factura-electronica-vs-verifactu.html`, `contabilidad-negocio-7-pasos.html`
- `sitemap.xml` (only real, indexable pages) and `robots.txt`; OG image `assets/img/og-facturales.png`

## Development

No build step. Use a local server (external SVG/logo and fonts):

```bash
npx serve .   # or: python3 -m http.server 5190
```

## Conventions

- All user-facing text is in **Spanish**. No invented claims: no testimonials, customer counts, ratings, «sin tarjeta», direct bank connection (PSD2 is disabled), recurring invoices, automatic reminders, stock control or automatic AEAT submission. Bancos/Cobros/Gastos/Gráficas are «Nuevo» (gradual rollout) — no dates.
- Prices must match the app defaults (`src/services/plans/plans-config.service.ts`): Starter 6,45/4,95, Pro 11,95/8,95, Ilimitado 23,95/17,95 €/mes + IVA (monthly/annual); 14-day trial.
- App links use clean routes: `https://app.facturales.es/signin`, `/signup`, `/aviso-legal`, `/condiciones-legales`, `/politica-de-privacidad`, `/politica-de-cookies`, `/eliminar-cuenta`.
- Accessibility: one `h1` per page, visible focus (`:focus-visible`), touch targets ≥44 px, AA contrast, `lang="es"`, `prefers-reduced-motion` respected.
- The `premium-ui-reviewer` custom agent (`.claude/agents/premium-ui-reviewer.md`) should be used to review any significant UI changes.
