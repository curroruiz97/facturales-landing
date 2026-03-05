# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Landing site for **Facturales** (facturales.es) — a billing/accounting SaaS for Spanish freelancers and SMEs. The app itself lives at `app.facturales.es`; this repo is the static marketing site only.

## Architecture

- **Static HTML site** — no build system, no bundler, no SSR. Pages are plain `.html` files served directly.
- **Template base**: Adapted from "Neotix" (Gramentheme/ThemeForest). Original template references may still appear in CSS comments and meta tags.
- **Shared header/nav**: Injected at runtime via `assets/js/header-include.js` using `document.write()`. Editing navigation or header requires modifying this file, not individual HTML pages.
- **Preloader**: Each page has its own inline preloader markup spelling "FACTURALES".

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Layout | Bootstrap 5 |
| DOM/Interactions | jQuery 3.7.1 |
| Animations | GSAP (ScrollTrigger, ScrollSmoother, SplitText, TextPlugin) |
| Slider | Swiper |
| Mobile menu | MeanMenu |
| Custom logic | `assets/js/main.js` |
| Styles | `assets/css/main.css` (single custom stylesheet) |

## CSS Design Tokens (from `:root` in main.css)

```
--theme: #F94D00   (orange accent)
--header: #0B0D17  (dark headings)
--text: #534F5A    (body text)
--bg: #EFEDE5      (page background)
--bg2: #0F172A     (dark sections)
```

Fonts: **Inter** (body), **Plus Jakarta Sans** (headings/display).

## Key Pages

- `index.html` — Homepage (hero, features, testimonials, pricing preview)
- `pricing.html` — Pricing plans
- `faq.html` — FAQ
- `contact.html` — Contact form
- Service detail pages: `crea-envia-facturas.html`, `crea-envia-presupuestos.html`, `gestiona-tu-stock.html`, `escanea-gastos.html`, `gestiona-clientes.html`, `factura-personalizada.html`, `tu-negocio-bajo-control.html`
- Blog: `news.html`, `news-grid.html`, `news-details.html`
- SEO/content articles: `verifactu-2027-guia-autonomos-pymes.html`, `factura-electronica-vs-verifactu.html`, `contabilidad-negocio-7-pasos.html`

## Development

No build step. Open any `.html` file directly in a browser or use a local server:

```bash
npx serve .
```

## Conventions

- All user-facing text is in **Spanish**.
- CTA links for login/signup point to `https://app.facturales.es/signin.html` and `https://app.facturales.es/signup.html`.
- Images and assets live under `assets/img/`. Logos at `assets/img/logo/`.
- The `premium-ui-reviewer` custom agent (`.claude/agents/premium-ui-reviewer.md`) should be used to review any significant UI changes.
