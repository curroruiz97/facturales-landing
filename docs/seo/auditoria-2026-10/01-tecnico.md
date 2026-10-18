# Auditoría SEO técnica de facturales.es

Fecha: 18/10/2026. Alcance: web de marketing (repo `/home/user/facturales-landing`, commit `be45213`) y la web en vivo `https://facturales.es`, más la app `app.facturales.es` (repo `/home/user/facturales`). No se ha modificado ningún archivo de los repositorios.

> **Importante (desfase de despliegue).** La web en vivo es la versión subida el **16/10/2026 21:46** (`last-modified` de `/`). **Los 23 HTML comparados, los JS, los CSS y `sitemap.xml` difieren del repo** (por ejemplo, `index.html` pesa 43 524 B en vivo y 62 098 B en el repo; `assets/img/logo/logo-white.webp` da 404 en vivo). Solo `robots.txt` coincide. Salvo que se indique lo contrario, los hallazgos on-page se refieren al **repo** (lo que se va a desplegar) y los de servidor/cabeceras a la **web en vivo**.

---

## 0. Resumen ejecutivo

| # | Problema | Prioridad | Evidencia (resumen) |
|---|---|---|---|
| 1 | Host duplicado `www` sin redirección 301 | **P0** | `https://www.facturales.es/` → 200 (43 524 B, idéntico) |
| 2 | `/index.html` devuelve 200 y **todas las páginas enlazan a `index.html`** (logo, migas, nav) | **P0** | 19 páginas enlazan a `index.html` en HTML estático |
| 3 | Archivos internos públicos (CLAUDE.md, *.py, partials, scss, .map, package-lock) | **P0** | `/CLAUDE.md` 200, `/update_articles.py` 200, `/partials/header.njk` 200 |
| 4 | Nav y footer solo existen vía `document.write` (JS): sin JS la home pasa de 86 a 26 enlaces, sin enlaces legales; `about.html` queda inalcanzable | **P1** | Medido con Playwright (JS on/off) |
| 5 | Sin analítica, sin Search Console verificable, sin Bing WMT | **P0 (operativo)** | grep sin resultados en ambos repos; TXT DNS solo Stripe y SPF |
| 6 | 404 servido por la página genérica de Plesk (en inglés), no por `404.html` | P1 | Cuerpo de `/no-existe-xyz` = «404 Not Found … Server Error» |
| 7 | Sin HSTS ni `Cache-Control` en la landing | P1 | Cabeceras de `/` y `/assets/css/main.css` |
| 8 | Plantillas demo accesibles (200) aunque con noindex, incluido `service copy.html` con espacio | P2 | `index-2/3/4`, `team*`, `project*`, `service*` → 200 |
| 9 | Móvil: la captura de escritorio del hero (oculta) se descarga con `fetchpriority=high` y la captura móvil visible va con `loading=lazy` | P1 | Lighthouse: LCP 2,8 s en `crea-envia-facturas` (repo), 131 KiB desperdiciados |
| 10 | CSS bloqueante: Google Fonts + `main.css` (205 KB, ~90 % sin usar) + `facturales-ds.css` + `header-include.js` síncrono | P1 | Lighthouse: render-blocking ~0,85 s + 0,6 s + 0,46 s + 0,31 s |
| 11 | Datos estructurados incompletos: sin `WebSite`, sin `BreadcrumbList`, ofertas sin IVA ni periodo, sin `Product/Offer` en precios, `Article` sin `dateModified` ni autor persona | P1 | Inventario §4 |
| 12 | Títulos sin la keyword principal («programa/software de facturación») y 6 descripciones de más de 170 caracteres | P1 | Tabla §3 |
| 13 | URLs `.html` con nombres poco alineados con las keywords (`news-grid`, `escanea-gastos`, `tu-negocio-bajo-control`…) | P2 (planificar) | §7 |
| 14 | Rutas `facturales.es/confirm-email` y `/reset-password` (listadas en la doc de la app como redirect URLs de Supabase) dan 404 | P1 (si se usan) | `docs/APIS_Y_DEPENDENCIAS.md:32` |
| 15 | Sin `/llms.txt`, sin `apple-touch-icon`, sin `manifest` | P3 | 404 |

Rendimiento medido (Lighthouse 12.8.2, móvil simulado): **94-96/100 en vivo y 92-93/100 con la versión del repo**. Es bueno, pero el LCP (2,3-2,8 s) depende casi por completo del *render delay* causado por los recursos bloqueantes. SEO/Accesibilidad/Buenas prácticas de Lighthouse: 100 en las 8 mediciones.

---

## (a) HALLAZGOS COMPROBADOS

### 1. Indexación y rastreo

#### 1.1 robots.txt (en vivo = repo)
```
User-agent: *
Allow: /
Disallow: /partials/
Sitemap: https://facturales.es/sitemap.xml
```
- Correcto y permisivo. No bloquea a GPTBot, ClaudeBot ni PerplexityBot (las cinco UAs probadas reciben 200 y 43 524 B en `/`).
- `Disallow: /partials/` **no protege**: `https://facturales.es/partials/header.njk` → **200 (14 040 B)**. robots.txt no es un control de acceso, y además anuncia la ruta.
- `https://www.facturales.es/robots.txt` sirve el mismo archivo, así que el host www es rastreable por sí mismo.

#### 1.2 sitemap.xml
- Repo: 20 URLs. **Coincide exactamente con las 20 páginas indexables** (todas las páginas con canonical autorreferente y sin noindex). No incluye noindex, demo ni duplicadas: correcto.
- Vivo: las mismas 20 URLs, todas con `lastmod` 2026-10-16. En el repo, 2026-10-16/17. Son fechas puestas en bloque, no la última modificación real de cada página, así que Google acabará ignorándolas. `priority` lo ignora Google (inocuo).
- No hay `<image:image>` (las capturas reales podrían posicionar en Google Imágenes) ni índice de sitemaps (no hace falta con este tamaño).

#### 1.3 Meta robots y canonical por página (repo; en vivo coincide en canonical/robots)
- Las 20 indexables tienen canonical **absoluto, https, sin www y autorreferente**. `index.html` → `https://facturales.es/`.
- `news.html` y `news-details.html`: `noindex, follow` **y** canonical a `news-grid.html`. Son señales contradictorias (noindex + canonical a otra URL); lo recomendable es un 301.
- `404.html`: `noindex` y canonical a sí misma (correcto como página, pero el servidor no la usa: ver 1.6).
- Plantillas demo (`index-2/3/4`, `team*`, `project*`, `service*`, `service copy.html`, `service-details copy.html`): `noindex, nofollow`, sin canonical, `lang="en"` y meta description «Brevon - Multipurpose Business HTML Template». **Todas responden 200 en vivo.**
- `service-details.html`: noindex, en español, con title «Facturales - Servicios | Software de facturación…». Es una página antigua que sigue en vivo (75 731 B).

#### 1.4 Hosts, protocolo, slash, mayúsculas
Comprobado con `curl -s -o /dev/null -w "%{http_code} %{redirect_url}"`:

| URL | Resultado | Valoración |
|---|---|---|
| `http://facturales.es/` | 301 → `https://facturales.es/` | OK |
| `http://www.facturales.es/` | 301 → `https://www.facturales.es/` | **Mal**: debería ir directo a `https://facturales.es/` (un salto) |
| `https://www.facturales.es/` | **200**, mismo contenido | **Duplicado de host** (lo mitiga el canonical, pero se reparte el rastreo y la señal de enlaces) |
| `https://facturales.es/index.html` | **200** | Duplicado de `/` y enlazado internamente |
| `https://facturales.es/pricing` | 404 | Aceptable (no existen URLs limpias) |
| `https://facturales.es/pricing.html/` | 404 | OK |
| `https://facturales.es/PRICING.html`, `/Pricing.html` | 404 | OK (sensible a mayúsculas, sin duplicados) |
| `https://facturales.es/service%20copy.html` | 200 (noindex) | Basura indexable por error humano; borrar |
| `https://facturales.es/conectado-a-gestor.html` | 404 | Página borrada en el commit `187a7dc` (05/03/2026) sin redirección |

DNS (`dns.google`): `www.facturales.es` es CNAME de `facturales.es` → A `212.227.90.205` (rango IONOS). El certificado TLS cubre www (curl a https://www… sin error).

#### 1.5 Cabeceras HTTP (en vivo)
`curl -sI https://facturales.es/`:
```
server: nginx / x-powered-by: PleskLin / x-accel-version: 0.01
content-type: text/html            ← sin charset (el HTML lo declara con <meta charset>)
last-modified / etag / vary: Accept-Encoding
```
- **Compresión**: gzip (CSS: 213 055 B → 26 441 B) y **brotli** (`content-encoding: br` con `Accept-Encoding: br`). OK.
- **Sin `Cache-Control` ni `Expires`** en HTML, CSS, JS ni imágenes. Lighthouse marca `uses-long-cache-ttl` (6-10 recursos por página).
- **Sin HSTS** (`Strict-Transport-Security`) en el dominio raíz. La app sí lo envía (`max-age=31536000; includeSubDomains; preload`), pero eso solo cubre `app.facturales.es` y sus subdominios, no el apex.
- Sin `X-Robots-Tag` (correcto para la landing). Sin `X-Content-Type-Options`, `Referrer-Policy` ni CSP.

#### 1.6 Página 404
- `https://facturales.es/no-existe-xyz` → **404 real** (no hay soft 404), pero el cuerpo es la página genérica de Plesk (`/error_docs/`, `lang="en"`, «Server Error 404 Page Not Found», 808 B). **No usa `404.html`**, que existe y está bien hecha.
- `404.html` usa rutas **relativas** (`assets/css/...`, `index.html`). Si se configura como ErrorDocument, se romperá en URLs anidadas (`/blog/x`). Habría que pasarlas a absolutas desde la raíz (`/assets/...`).

#### 1.7 Archivos expuestos que no deberían ser públicos (en vivo)

| URL | Estado | Riesgo |
|---|---|---|
| `/CLAUDE.md` | 200 (versión antigua, 2 661 B) | Indexable; expone el stack |
| `/fix_title_case.py`, `/update_articles.py` (23 KB), `/remove_comments.py` | 200 `text/x-python` | Indexables como texto; contenido interno |
| `/partials/header.njk` | 200 | Plantilla interna |
| `/assets/css/main.css.map`, `/assets/scss/main.scss` | 200 | Inocuo, pero innecesario |
| `/package-lock.json` | 200 | Innecesario |
| `/.git/HEAD` | 403 | OK (protegido) |
| `/assets/`, `/assets/img/` | 403 | OK (sin listado de directorio) |

#### 1.8 Historial: URLs antiguas que pudieran estar indexadas
- `git log --all --name-only` → todos los `.html` que han existido: los actuales más **`conectado-a-gestor.html`** (creado el 03/02/2026, borrado el 05/03/2026, title «Facturales - Sistema de contabilidad», h1 «Conectado a Gestor»). Hoy da 404.
- Renombrados: solo `assets/img/logo-short.svg → assets/img/favicon.svg`. No hay HTML renombrados. **Las URLs actuales existen desde febrero de 2026** (8 meses de historial con el mismo nombre), así que una migración de URLs moverá señales ya acumuladas, aunque probablemente modestas.
- Probadas en vivo y todas 404: `home.html`, `coming-soon.html`, `signin.html`, `signup.html`, `blog`, `precios.html`, `servicios.html`, `contacto.html`, `about-us.html`, `aviso-legal.html`, `politica-de-*.html`, `terminos.html`, `privacy.html`, `legal.html`, `reset-password`, `confirm-email`.
- `/home/user/facturales/vercel.json` redirige rutas antiguas `.html` de la **app** (`/index-2.html`, `/home.html`, `/coming-soon.html`, `/signin.html`…) a rutas limpias. Esto indica que la app tuvo una fase HTML estática, pero esas rutas vivían en `app.`, no en el apex.
- **`/home/user/facturales/docs/APIS_Y_DEPENDENCIAS.md:32`**: «Redirect URLs: `https://facturales.es/confirm-email`, `https://facturales.es/reset-password`». Ambas dan **404 en la landing**. Si algún correo de Supabase o enlace antiguo apunta ahí, el usuario aterriza en un 404.
- No se pudo consultar Wayback Machine: la API CDX no respondió desde este entorno (HTTP 000).

### 2. Enlazado interno

#### 2.1 Nav y footer por `document.write`
- `assets/js/header-include.js` (12 806 B) y `assets/js/footer-include.js` (3 065 B) son `<script>` **síncronos sin defer** en el `<body>` (por ejemplo, `index.html` línea 33) que hacen `document.write(html)`. La app no tiene versión sin JS (`<noscript>`).
- Prueba con Playwright (Chromium 1194, viewport 390×844, repo servido en local):

| Página | JS activado: enlaces / URL internas únicas | JS desactivado: enlaces / URL internas | Header | Footer | Enlaces legales |
|---|---|---|---|---|---|
| index.html | 86 / 20 | **26 / 13** | sí → **no** | sí → **no** | 4 → **0** |
| about.html | 66 / 17 | **6 / 3** | sí → no | sí → no | 4 → 0 |
| verifactu-2027… | 69 / 19 | **9 / 5** | sí → (header del artículo) | sí → no | 4 → 0 |

- Googlebot renderiza JS y verá el nav. GPTBot, ClaudeBot, PerplexityBot y otros crawlers de LLM, la mayoría de herramientas SEO y Bing en parte **no ejecutan JS**: para ellos el sitio no tiene nav, ni footer, ni logo enlazado, ni enlaces a aviso legal o privacidad.
- `document.write` en script síncrono del mismo origen funciona (Chrome solo lo interviene en scripts de otro origen con 2G), pero bloquea el parser: Lighthouse lo cuenta como render-blocking (~310 ms en cada página del repo).

#### 2.2 Grafo de enlaces (HTML estático del repo, BFS desde la home)

| Página | Enlaces internos salientes (estático) | Profundidad sin JS | Profundidad con JS | Enlaces entrantes estáticos |
|---|---|---|---|---|
| index.html | 11 | 0 | 0 | 19 (todos a `index.html`, ninguno a `/`) |
| pricing.html | 2 | 1 | 1 | 15 |
| funciones.html | 12 | 1 | 1 | 14 |
| faq.html | 3 | 1 | 1 | **1** |
| contact.html | 1 | 2 | 1 | 2 |
| **about.html** | 3 | **NO ALCANZABLE** | 1 | **0** |
| crea-envia-facturas.html | 6 | 1 | 1 | 8 |
| crea-envia-presupuestos.html | 6 | 2 | 1 | 3 |
| bancos-conciliacion.html | 6 | 1 | 1 | 6 |
| cobros.html | 6 | 1 | 1 | 7 |
| escanea-gastos.html | 6 | 1 | 1 | 5 |
| impuestos.html | 6 | 1 | 1 | 5 |
| tu-negocio-bajo-control.html | 6 | 1 | 1 | 2 |
| gestiona-clientes.html | 6 | 2 | 1 | 5 |
| gestiona-tu-stock.html | 6 | 1 | 1 | 4 |
| factura-personalizada.html | 6 | 2 | 1 | 2 |
| news-grid.html | 5 | 2 | 1 | 3 |
| verifactu-2027-guia-autonomos-pymes.html | 5 | 1 | 1 | 5 |
| factura-electronica-vs-verifactu.html | 5 | 2 | 2 | 3 |
| contabilidad-negocio-7-pasos.html | 5 | 2 | 2 | 3 |

Observaciones:
- Sin JS, `about.html` es **huérfana**: solo la encuentra quien lea el sitemap.
- **Los artículos del blog no enlazan a ninguna página de módulo** (solo a `funciones.html`, `news-grid.html`, a los otros artículos y al registro). Por ejemplo, la guía VERI*FACTU no enlaza a `crea-envia-facturas.html`, y «contabilidad en 7 pasos» no enlaza a `bancos-conciliacion.html` ni a `escanea-gastos.html` pese a tener secciones «Conciliación bancaria» y «Digitaliza».
- `pricing.html` solo tiene 2 enlaces internos estáticos (`index.html`, `contact.html`).
- Los anchors de las migas son genéricos («Inicio», «Funciones», «Recursos»). Las tarjetas «Funciona mejor junto a» usan anchors descriptivos (h3 «Cobros», «Bancos y conciliación»): correcto.

### 3. Metadatos on-page (repo)

`lang="es"` en todas las indexables; `viewport` correcto; `theme-color` `#020100`; OG completo (`og:title`, `og:description`, `og:url` = canonical, `og:image` 1200×630 PNG de 203 KB con width, height y alt, `og:locale es_ES`); `twitter:card=summary_large_image`. Los artículos usan `og:type=article` y `article:published_time`. **Ninguna página indexable tiene imágenes sin atributo `alt`**. Los `alt=""` se usan solo en decorativas (rombo 34 px en tarjetas del blog, miniaturas de `funciones.html` y una captura móvil duplicada en la home). Cada página tiene **un único h1**.

| Página | Title (car.) | Description (car.) | H1 | H2/H3 | Palabras* |
|---|---|---|---|---|---|
| index.html | Facturales · Suite financiera para autónomos y pymes (52) | 193 ⚠ | Facturas, bancos e impuestos de tu negocio, en un solo lugar. | 9 h2 / 20 h3 | 1 801 |
| pricing.html | Precios · Facturales \| Planes desde 4,95 €/mes (46) | 144 | Un precio claro para cada etapa de tu negocio. | 7 h2 (Starter/Pro/Ilimitado como h2) / 9 h3 | 616 |
| funciones.html | Funciones · Facturales \| Facturación, bancos, cobros, gastos e impuestos (72 ⚠) | 198 ⚠ | Una suite financiera completa, sin piezas sueltas. | 16 h2 / 0 h3 | 269 ⚠ |
| faq.html | Preguntas frecuentes · Facturales (33) | 187 ⚠ | Preguntas frecuentes | 7 h2 | 900 |
| contact.html | Contacto · Facturales (21) | 113 | Hablemos. | 3 h2 | 85 |
| about.html | Sobre Facturales · Suite financiera para autónomos y pymes (58) | 153 | Hacemos que las finanzas… | 3 h2 / 3 h3 | 146 ⚠ |
| crea-envia-facturas.html | Facturación con VERI*FACTU · Facturales (39) | 174 ⚠ | Facturas correctas a la primera, listas para VERI*FACTU. | 7 h2 / 19 h3 | 732 |
| crea-envia-presupuestos.html | Presupuestos y conversión a factura · Facturales (48) | 170 ⚠ | Del presupuesto a la factura sin volver a escribir nada. | 5 h2 / 12 h3 | 316 |
| bancos-conciliacion.html | Bancos y conciliación bancaria · Facturales (43) | 152 | Concilia tu banco con tus facturas y gastos en minutos. | 6 h2 / 14 h3 | 430 |
| cobros.html | Cobros, previsión y antigüedad de deuda · Facturales (52) | 167 ⚠ | Cobra a tiempo sin perseguir a nadie. | 7 h2 / 14 h3 | 505 |
| escanea-gastos.html | Gastos, OCR y justificantes · Facturales (40) | 161 | Cada gasto con su justificante, sin perseguir tickets. | 6 h2 / 14 h3 | 384 |
| impuestos.html | Impuestos: modelos 303 y 130 y cierres · Facturales (51) | 177 ⚠ | El trimestre, con los números ya hechos. | 5 h2 / 12 h3 | 324 |
| tu-negocio-bajo-control.html | Panel y gráficas de tu negocio · Facturales (43) | 175 ⚠ | Cómo va tu negocio, sin abrir una hoja de cálculo. | 6 h2 / 13 h3 | 330 |
| gestiona-clientes.html | Clientes y contactos · Facturales (33) | 161 | Tus clientes, con todo lo que les has facturado. | 5 h2 / 12 h3 | 269 ⚠ |
| gestiona-tu-stock.html | Inventario: catálogo y control de stock · Facturales (52) | 170 ⚠ | Tu catálogo y tu stock, siempre al día. | 6 h2 / 18 h3 | 515 |
| factura-personalizada.html | Diseño de factura con tu marca · Facturales (43) | 134 | Facturas con tu marca, sin pelearte con plantillas. | 5 h2 / 12 h3 | 264 ⚠ |
| news-grid.html | Recursos y blog · Facturales (28) | 103 | Guías claras sobre facturación, impuestos y gestión. | 4 h2 | 208 |
| verifactu-2027-guia-autonomos-pymes.html | VERI*FACTU en 2027: Guía para Autónomos y Pymes \| Facturales (60) | 131 | VERI*FACTU en 2027: qué es… (108 car.) | 8 h2 / 2 h3 | 578 ⚠ |
| factura-electronica-vs-verifactu.html | Factura Electrónica vs VERI*FACTU: Diferencias y Plazos \| Facturales (68 ⚠) | 143 | Factura electrónica obligatoria vs VERI*FACTU… | 6 h2 / 2 h3 | 360 ⚠ |
| contabilidad-negocio-7-pasos.html | Cómo Llevar la Contabilidad de tu Negocio: 7 Pasos \| Facturales (63 ⚠) | 136 | Cómo llevar la contabilidad de tu negocio (sin ser contable)… | 10 h2 / 2 h3 | 391 ⚠ |

\* Palabras visibles del `<body>` sin script/style/svg y **sin** nav/footer (que se inyectan por JS). Script de cálculo: `[scratchpad de la auditoría]/scripts/onpage.py` más un recuento ad hoc.

Problemas detectados:
- **Ningún title contiene «programa de facturación» ni «software de facturación»**, previsiblemente las keywords transaccionales de más volumen del nicho (sin verificar con datos de volumen, ver Hipótesis). La home se posiciona como «Suite financiera», un término de baja demanda en España (hipótesis).
- Las descripciones de más de 160 caracteres se truncan en el SERP: index (193), funciones (198), faq (187), impuestos (177), tu-negocio (175), crea-envia-facturas (174), presupuestos/stock (170), cobros (167).
- Estilo inconsistente: los módulos usan «X · Facturales» y los artículos «Title Case | Facturales» (en español se escribe en minúscula tras la primera palabra).
- **Contenido escaso (thin)**: `funciones.html` (269 palabras, solo h2 sin cuerpo), `about.html` (146), `contact.html` (85), `gestiona-clientes` (269), `factura-personalizada` (264) y los artículos (360-578 palabras para queries informacionales competidas como «verifactu» o «factura electrónica obligatoria»).
- **Canibalizaciones posibles**:
  - VERI*FACTU: `index` (h3 «Facturas preparadas para VERI*FACTU»), `crea-envia-facturas` (title «Facturación con VERI*FACTU»), `verifactu-2027-guia…` y `factura-electronica-vs-verifactu` (los dos artículos tienen h2 «Qué es VERI*FACTU»).
  - FAQ: «¿Hay permanencia?» se repite en `index` y `pricing`, y `faq.html` agrega preguntas de los módulos. Es aceptable mientras las respuestas no sean idénticas.
  - `news.html` y `news-details.html` son **copias exactas** de `news-grid.html` (mismo title, description y h1) con noindex.
  - `service-details.html` (noindex, en vivo) compite semánticamente con «Software de facturación para autónomos y pymes».
- `pricing.html`: los nombres de plan (Starter/Pro/Ilimitado) son **h2**, al mismo nivel que «Compara los planes». La jerarquía es mejorable (h2 «Planes» + h3 por plan).
- En los h3 de galería falta un espacio entre el título y el `<small>` («La ficha de cada facturaEstado, líneas…» en el texto extraído). Es menor, pero así lo leen los crawlers y los lectores de pantalla.

### 4. Datos estructurados (repo)

| Página | JSON-LD presentes | Comentario |
|---|---|---|
| index.html | `Organization`, `SoftwareApplication`, `FAQPage` (9 Q) | Tres bloques sueltos sin `@id` ni relación entre ellos |
| pricing.html | `FAQPage` (6 Q) | **Sin `Product`/`SoftwareApplication`/`Offer`**: la página de precios no declara los precios |
| faq.html | `FAQPage` (25 Q) | OK |
| 9 páginas de módulo | `FAQPage` (2-5 Q) | OK. Ninguna tiene `BreadcrumbList` pese a las migas visibles |
| funciones.html, about.html, contact.html, news-grid.html | ninguno | Faltan `CollectionPage`/`AboutPage`/`ContactPage`/`Blog` |
| 3 artículos | `Article` | Sin `dateModified`; autor `Organization`; `publisher.logo` = SVG del rombo; `image` = OG genérica |

Validación lógica:
- **JSON válido en todos los bloques** (parseados con `json.loads`). **Todas las preguntas y respuestas de los `FAQPage` aparecen literalmente en el texto visible** (comprobado por script: 0 discrepancias).
- `Organization.logo` = `https://facturales.es/assets/img/logo/facturales-rombo.svg`. Google Imágenes admite SVG, pero las pautas de logo piden una imagen de al menos 112×112 rastreable. Una PNG cuadrada de 512×512 es la opción más robusta para el panel de conocimiento y otros consumidores (Bing, LLMs). Además falta `sameAs`: no hay perfiles sociales ni enlaces a App Store/Google Play en ningún sitio del repo (grep sin resultados).
- `SoftwareApplication.offers`: `price` 6.45/11.95/23.95 (mensual) **sin `priceSpecification`** (sin `UnitPriceSpecification`, `billingDuration`/`unitCode` mensual, `valueAddedTaxIncluded: false`) y sin la variante anual (4,95/8,95/17,95). Sin `aggregateRating`/`review` Google no muestra rich result de software (correcto no inventarlos), pero el marcado sigue siendo útil semánticamente.
- `FAQPage`: desde 2023 Google solo muestra el rich result FAQ en sitios gubernamentales o de salud. Mantenerlo es inocuo y útil para LLMs/Bing.
- `Article.headline` tiene 108 caracteres (Google recomendaba ≤110: en el límite). Las fechas `datePublished` (2026-02-03/10/17) **coinciden** con `<time datetime>` visibles.
- No hay `WebSite` (necesario para que Google entienda el nombre del sitio, `alternateName`) ni `WebPage` por página.

### 5. Rendimiento / Core Web Vitals

Lighthouse 12.8.2 (instalado en `[scratchpad de la auditoría]/lh`), Chromium 1194, `--form-factor=mobile`, throttling simulado. «Vivo» = https://facturales.es (versión del 16/10). «Repo» = el repo servido con `serve` y compresión (versión a desplegar). JSON en `[scratchpad de la auditoría]/lh/*.json`.

| Página | Versión | Perf | FCP | LCP | TBT | CLS | Speed Index | Peso | Requests | Elemento LCP |
|---|---|---|---|---|---|---|---|---|---|---|
| Home | vivo | 96 | 2,3 s | 2,3 s | 0 ms | 0,013 | 2,6 s | 85 KiB | 12 | `p.fx-lead` |
| Home | repo | 92 | 2,4 s | 2,6 s | 0 ms | 0 | **4,2 s** | 199 KiB | 14 | `p.fx-lead` |
| Pricing | vivo | 95 | 2,3 s | 2,3 s | 0 | 0,001 | 2,5 s | 81 KiB | 12 | `h1` |
| Pricing | repo | 93 | 2,4 s | 2,4 s | 0 | 0 | 4,2 s | 100 KiB | 12 | `h1` |
| crea-envia-facturas | vivo | 96 | 2,3 s | 2,3 s | 0 | 0 | 2,3 s | 81 KiB | 11 | `p.fx-lead` |
| crea-envia-facturas | repo | 92 | 2,5 s | **2,8 s** | 0 | 0 | 2,8 s | **338 KiB** | 16 | `img` móvil 780 px |
| Artículo VERI*FACTU | vivo | 95 | 2,4 s | 2,4 s | 0 | 0 | 2,4 s | 80 KiB | 10 | `h1` |
| Artículo VERI*FACTU | repo | 92 | 2,4 s | 2,4 s | 0 | 0 | 4,2 s | 100 KiB | 11 | `h1` |

Diagnóstico:
- **El LCP es casi todo *render delay*** (1,6-2,1 s de ~2,4 s; TTFB ~0,45-0,65 s). La causa son los recursos bloqueantes. Lighthouse estima por recurso (repo, home): Google Fonts CSS ~851 ms, `main.css` ~617 ms, `facturales-ds.css` ~467 ms y `header-include.js` ~316 ms. En pricing también `footer-include.js` (~311 ms).
- **`main.css`**: 205 197 B sin comprimir (8 932 líneas, plantilla Neotix), ~28 KB transferidos. Lighthouse estima **25-37 KiB sin usar de ~28 KiB**, es decir, casi todo. Según CLAUDE.md, en las páginas reales solo se necesita para el cubo del hero (`cube-spin`, `cube-float`, `.cubes-wrapper`, ~99 coincidencias de «cube»), que solo aparece en `index.html`. Además `main.css` línea 18 hace **`@import` de Google Fonts otra vez** (petición encadenada redundante).
- **Fuentes**: Onest por Google Fonts, `display=swap`, un solo woff2 variable (34 KB) desde `fonts.gstatic.com`. Hay preconnect, pero el CSS de Google sigue siendo bloqueante y de otro origen.
- **Imágenes (repo)**: WebP con `srcset`, `width`/`height` (CLS 0) y `loading=lazy` fuera del hero. Buen trabajo. **Fallo de dirección de arte en móvil** (`.fx-adaptable`, `facturales-ds.css:745-749`): la captura de escritorio va en un `<img>` con `loading="eager" fetchpriority="high"` y se oculta con `display:none` por debajo de 700 px, **pero se descarga igual** (en el registro de red del móvil: `facturas-emitidas-1280.webp` 55,7 KB con prioridad High; `panel-1280.webp` 49 KB en la home). La captura móvil visible (`movil/*-780.webp`) lleva `loading="lazy"` y prioridad Low. En `crea-envia-facturas` es el elemento LCP: *load delay* 204 ms y `uses-responsive-images` 131 KiB desperdiciados. Ocurre en todas las páginas de módulo con `fx-adaptable`.
- `assets/img/app` pesa 4,6 MB en disco, pero cada página descarga solo lo que usa. OK.
- **JS**: 3 archivos propios (≈ 3 + 1,5 + 4 KB transferidos), sin jQuery/GSAP en las páginas reales. TBT 0 ms.
- **Caché**: sin `Cache-Control`. Los recursos ya llevan `?v=20261018` en el repo, así que se puede usar `max-age=31536000, immutable` sin riesgo.
- El Speed Index de 4,2 s en el repo (frente a 2,3-2,6 s en vivo) coincide con las animaciones de entrada (`data-fx-revela`, `fx-aparece`) y el cubo animado de la home. Es probable que Lighthouse cuente la aparición progresiva como contenido tardío (hipótesis razonable: no afecta a LCP/CLS).

### 6. Móvil, accesibilidad básica, HTTPS, iconos
- Viewport correcto; sin scroll horizontal a 390 px (Playwright: `scrollWidth <= innerWidth` en home, about y artículo).
- Lighthouse: Accesibilidad 100 y Buenas prácticas 100 en las 8 mediciones.
- HTTPS en todo; sin contenido mixto (no hay `http://` salvo los namespaces `w3.org` de SVG).
- Favicon: solo `assets/img/favicon.svg` (`rel=icon`, SVG). **`/favicon.ico` → 404, `/apple-touch-icon.png` → 404, sin `<link rel="apple-touch-icon">`, sin `manifest`.** Google admite favicon SVG, pero algunos navegadores, iOS y lectores RSS piden `/favicon.ico` y `apple-touch-icon`.
- `color-scheme: dark` y `theme-color` presentes.
- Las animaciones `data-fx-revela` solo ocultan contenido bajo `.fx-anim` (lo añade el JS) y respetan `prefers-reduced-motion` (`facturales-ds.css:860-863`). **Sin JS el contenido es visible**: correcto para el SEO.

### 7. Arquitectura de URLs (estado actual)

| URL actual | Contenido | Keyword objetivo probable (hipótesis) | Alineación |
|---|---|---|---|
| `/` | Home | programa de facturación para autónomos / software de facturación | — |
| `/pricing.html` | Precios | precios programa facturación | En inglés |
| `/funciones.html` | Hub de funciones | funcionalidades | Aceptable |
| `/crea-envia-facturas.html` | Facturación + VERI*FACTU | programa de facturación / software facturación verifactu | Débil (verbo, no keyword) |
| `/crea-envia-presupuestos.html` | Presupuestos | programa de presupuestos | Débil |
| `/bancos-conciliacion.html` | Conciliación | conciliación bancaria | Aceptable |
| `/cobros.html` | Cobros/recordatorios | control de cobros, recordatorio de pago | Aceptable |
| `/escanea-gastos.html` | Gastos y justificantes | gestión de gastos, escanear tickets | Débil |
| `/impuestos.html` | 303/130 | modelo 303, modelo 130 autónomos | Débil |
| `/tu-negocio-bajo-control.html` | Panel y gráficas | cuadro de mando / panel financiero | **Muy débil** |
| `/gestiona-clientes.html` | Clientes | gestión de clientes / CRM facturación | Débil |
| `/gestiona-tu-stock.html` | Inventario | programa de inventario / control de stock | Débil |
| `/factura-personalizada.html` | Diseño de factura | plantilla de factura personalizada | Aceptable |
| `/faq.html`, `/contact.html`, `/about.html` | Soporte | — | En inglés |
| `/news-grid.html` | Índice del blog | blog | **Nombre de plantilla** |
| `/verifactu-2027-guia-autonomos-pymes.html` etc. | Artículos | verifactu, factura electrónica obligatoria | Correcta, pero sin carpeta `/blog/` |

Restricción técnica descubierta: **todas las páginas usan rutas relativas** (`assets/...`, `index.html`, `pricing.html`). `header-include.js:6` y `footer-include.js:6` calculan la página activa con `location.pathname.split("/").pop() || "index.html"`. Ambas cosas **se rompen** con URLs de directorio (`/precios/`): los recursos se resolverían como `/precios/assets/...` (404) y la página activa del nav quedaría vacía.

### 8. app.facturales.es

| URL | Estado | Notas |
|---|---|---|
| `/` | 308 → `/dashboard` | |
| `/robots.txt` | 200 | `User-agent: * Allow: /` con comentario explicativo (correcto: deja rastrear para que se vea el noindex) |
| `/sitemap.xml` | 404 | Correcto |
| `/signin`, `/signup`, `/aviso-legal`, `/politica-de-privacidad` | 200 (SPA, 6 058 B, `<title>Facturales</title>`) | **`X-Robots-Tag: noindex, nofollow, noarchive`** en todas las respuestas (`vercel.json`, header `"/(.*)"`) |
| `/no-existe-xyz` | **200** (soft 404 de SPA) | Neutralizado por el noindex |

- **No hay riesgo de duplicado ni de thin content indexado en la app**: todo es noindex por cabecera. Tampoco hay meta description ni canonical, que no hacen falta con noindex.
- Efecto colateral: **las páginas legales** (aviso legal, condiciones, privacidad, cookies) viven solo en la app y son **noindex**, y la landing enlaza a ellas solo desde el footer inyectado por JS. Para una marca financiera es una señal de confianza (E-E-A-T) débil: un buscador no puede ver ni asociar al dominio principal quién está detrás del servicio (titular, NIF, domicilio).
- `vercel.json` aplica HSTS `includeSubDomains; preload` solo a `app.`. El apex no tiene HSTS.

### 9. Analítica y verificación
- `grep -rniE 'gtag|googletagmanager|google-site-verification|plausible|clarity|hotjar|posthog|umami|matomo|fbq|cookiebot|msvalidate'` en `*.html`/`*.js` de la landing: solo una coincidencia falsa en `bootstrap.bundle.min.js`. En la app (`*.html,*.ts,*.tsx,*.json`, incluidos `@vercel/analytics` y `speed-insights`): **0 resultados**.
- HTML en vivo: 0 coincidencias de `gtag|googletagmanager|verification`.
- DNS TXT de `facturales.es`: solo `stripe-verification=…` y `v=spf1 include:_spf-eu.ionos.com ~all`. **No hay `google-site-verification`.** Search Console podría estar verificado por archivo HTML (no se puede enumerar) o no estarlo; ver Hipótesis.
- No hay banner de consentimiento (coherente con no tener analítica ni cookies de terceros, aunque Google Fonts por CDN transfiere la IP a Google: debate RGPD conocido en la UE).
- **No hay forma de medir conversiones** landing → `app.facturales.es/signup`.

---

## (b) HIPÓTESIS (sin verificar)

1. **Plesk con Apache detrás de nginx** (`x-accel-version`, `x-powered-by: PleskLin`): es probable que `.htaccess` funcione en el docroot (modo proxy de Plesk activado). Para verificarlo, sube un `.htaccess` con `Header set X-Htaccess-Test "1"` y comprueba con `curl -sI https://facturales.es/ | grep -i x-htaccess`. Si no aparece, usa «Directivas adicionales de nginx» en Plesk (Sitios web y dominios → Configuración de Apache y nginx).
2. **Volúmenes de búsqueda**: no se han consultado herramientas de keywords en esta auditoría. Las keywords «programa de facturación», «software de facturación autónomos», «control de stock», «conciliación bancaria», «modelo 303» y «verifactu» se proponen por conocimiento del nicho. Hay que validarlas con datos (Search Console, Ahrefs/SE Ranking) antes de renombrar URLs.
3. **Indexación actual**: no se ha podido consultar Search Console ni `site:`. Es posible que Google tenga indexadas `www.facturales.es/...`, `/index.html`, `conectado-a-gestor.html` o plantillas antiguas en inglés de la etapa anterior (el title «Facturales - Sistema de contabilidad» estuvo en todas las páginas hasta octubre). También archivos `.py` y `CLAUDE.md` si alguien los enlazó.
4. **Search Console**: puede estar verificado por archivo HTML o por etiqueta en una versión antigua. No hay evidencia de verificación por DNS.
5. **`/confirm-email` y `/reset-password` en el apex**: si los correos de Supabase usan `SITE_URL=https://facturales.es` en alguna plantilla, hay usuarios aterrizando en un 404 de Plesk. Revisa la configuración de Supabase Auth (Site URL y Redirect URLs) y las plantillas de correo.
6. El Speed Index alto del repo (4,2 s) se debe a las animaciones de entrada y al cubo, no a la descarga de recursos (sin verificar con trazas).
7. Bing y crawlers de LLM indexan hoy una versión «sin nav» del sitio. El impacto en citaciones de ChatGPT/Perplexity no está cuantificado.

---

## (c) RECOMENDACIONES PRIORIZADAS

Leyenda: Impacto (A/M/B), Esfuerzo (A/M/B), Riesgo (A/M/B).

### P0 — Hacer ya (antes o junto al próximo despliegue)

**P0-1. Un único host: 301 de www (y http) a `https://facturales.es` en un salto.** Impacto A · Esfuerzo B · Riesgo B
- Tarea: en Plesk, Sitios web y dominios → Hosting y DNS → «Redirección SEO preferente 301» → **non-www** (opción nativa de Plesk). Alternativa: `.htaccess` en el docroot:
  ```apache
  RewriteEngine On
  RewriteCond %{HTTPS} off [OR]
  RewriteCond %{HTTP_HOST} ^www\. [NC]
  RewriteRule ^ https://facturales.es%{REQUEST_URI} [R=301,L]
  ```
- Aceptación: `http://www.`, `https://www.` y `http://` redirigen con **un solo** 301 a `https://facturales.es/…`, conservando ruta y query.
- Validación:
  ```bash
  for u in http://www.facturales.es/pricing.html https://www.facturales.es/pricing.html http://facturales.es/pricing.html; do curl -s -o /dev/null -w "$u %{http_code} %{redirect_url}\n" "$u"; done
  # esperado: 301 https://facturales.es/pricing.html (los tres)
  ```

**P0-2. `/index.html` → `/` y enlaces internos a `/`.** Impacto M · Esfuerzo B · Riesgo B
- `.htaccess`:
  ```apache
  RewriteCond %{THE_REQUEST} \s/index\.html[\s?] [NC]
  RewriteRule ^index\.html$ https://facturales.es/ [R=301,L]
  ```
- Repo: sustituir `href="index.html"` por `href="/"` en las 20 páginas (migas), `assets/js/header-include.js` (logo y nav) y `assets/js/footer-include.js`. Ajustar la lógica `ruta` (`|| "index.html"`) para que marque la home cuando `pathname === "/"`.
- Aceptación: `grep -c 'href="index.html"' *.html assets/js/*-include.js` = 0 en las páginas reales; `curl -sI https://facturales.es/index.html` → 301 a `/`.

**P0-3. Retirar del servidor los archivos internos.** Impacto M (higiene e indexación) · Esfuerzo B · Riesgo B
- Borrar del docroot de producción: `CLAUDE.md`, `*.py`, `package-lock.json`, `partials/`, `assets/scss/`, `assets/css/main.css.map`, `service copy.html`, `service-details copy.html`. Y además en `.htaccess`:
  ```apache
  <FilesMatch "\.(py|md|njk|map|scss|lock)$|^package(-lock)?\.json$">
    Require all denied
  </FilesMatch>
  RedirectMatch 404 ^/partials/
  ```
- Mejor aún: desplegar desde una lista blanca (`rsync --include` de `*.html`, `assets/{css,js,img}`, `robots.txt`, `sitemap.xml`, favicon) en lugar de copiar el repo entero.
- Validación:
  ```bash
  for p in CLAUDE.md fix_title_case.py update_articles.py partials/header.njk package-lock.json assets/css/main.css.map "service%20copy.html"; do curl -s -o /dev/null -w "$p %{http_code}\n" https://facturales.es/$p; done  # esperado: 403/404/410
  ```

**P0-4. Medición: Search Console + Bing Webmaster + analítica respetuosa.** Impacto A · Esfuerzo B · Riesgo B
- Search Console como **propiedad de dominio** (TXT `google-site-verification` en el DNS de IONOS): cubre www, apex y app. Enviar `sitemap.xml`. Hacer lo mismo en Bing Webmaster Tools (importable desde GSC). Bing alimenta a ChatGPT Search y Copilot.
- Analítica: opción A, Plausible/Umami/Matomo sin cookies (sin banner). Opción B, GA4 con Consent Mode v2 y banner. Medir el evento `click_signup` en todos los `a[href^="https://app.facturales.es/signup"]` (delegación de eventos en `assets/js/facturales.js`) y, si se puede, la conversión `signup_completed` en la app.
- Aceptación: GSC muestra «Propiedad verificada» y el sitemap «Correcto» con 20 URLs descubiertas; la herramienta de analítica recibe pageviews y clics de signup.

**P0-5. Desplegar la versión del repo y automatizar el despliegue.** Impacto M · Esfuerzo M · Riesgo B
- La web en vivo va por detrás (todos los HTML difieren). Proponer un despliegue reproducible (por ejemplo, GitHub Action con `rsync`/SFTP a Plesk o Git de Plesk) con lista blanca de archivos (ver P0-3).
- Validación: `for f in index.html pricing.html sitemap.xml; do curl -s https://facturales.es/$f | cmp - /home/user/facturales-landing/$f && echo "OK $f"; done`.

### P1 — Próximas 2-4 semanas

**P1-1. Nav y footer en el HTML estático (eliminar `document.write`).** Impacto A (LLM/Bing, enlazado, rendimiento) · Esfuerzo M · Riesgo M
- Opción recomendada sin build en servidor: un script de generación (Node o Python) que inserte el contenido de `partials/header.html`/`footer.html` entre marcadores `<!-- fx:header -->…<!-- /fx:header -->` en cada `.html` y se ejecute antes de cada despliegue (o en CI). Se mantiene «una sola fuente». Alternativas: SSI de Apache (`Options +Includes`, `<!--#include virtual="/partials/header.html" -->`) o 11ty (ya hay un `partials/header.njk`).
- Mover a `facturales.js` (defer) el comportamiento que hoy está en los include (marcar la página activa).
- Aceptación: con JS desactivado, cada página tiene `<header>` con nav y `<footer>` con enlaces legales, y `about.html` es alcanzable desde la home.
- Validación: `curl -s https://facturales.es/ | grep -o 'href="[^"]*about[^"]*"'` devuelve al menos un resultado. Repetir el script de Playwright `[scratchpad de la auditoría]/scripts/nojs.js` y comprobar que los enlaces con JS off ≈ JS on.

**P1-2. 404 personalizada y redirecciones de rutas huérfanas.** Impacto M · Esfuerzo B · Riesgo B
- Cambiar en `404.html` todas las rutas a absolutas (`/assets/...`, `/`, `/funciones.html`), quitar el canonical (una 404 no lo necesita) y mantener `noindex`.
- `.htaccess`:
  ```apache
  ErrorDocument 404 /404.html
  Redirect 301 /conectado-a-gestor.html https://facturales.es/funciones.html
  Redirect 301 /news.html https://facturales.es/news-grid.html
  Redirect 301 /news-details.html https://facturales.es/news-grid.html
  Redirect 301 /confirm-email https://app.facturales.es/confirm-email
  Redirect 301 /reset-password https://app.facturales.es/reset-password
  ```
  (Los 301 de mod_alias conservan la query string. Comprobar también los tokens en `#hash`, que el navegador conserva solo).
- Plantillas demo: borrarlas del servidor y devolver **410**: `RedirectMatch gone ^/(index-[234]|team(-details)?|project(-details)?|service(-details)?)\.html$` y `^/service(-details)?%20copy\.html$`. Antes, confirmar en GSC que no reciben tráfico.
- Validación: `curl -s https://facturales.es/no-existe | grep -c 'No encontramos esta página'` = 1 con código 404; `curl -s -o /dev/null -w "%{http_code}" https://facturales.es/index-2.html` = 410.

**P1-3. Cabeceras: HSTS, caché y seguridad básica.** Impacto M · Esfuerzo B · Riesgo B (HSTS: M si se añade `preload`)
```apache
<IfModule mod_headers.c>
  Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  <FilesMatch "\.(css|js|webp|png|svg|woff2|ico)$">
    Header set Cache-Control "public, max-age=31536000, immutable"
  </FilesMatch>
  <FilesMatch "\.(html|xml|txt)$">
    Header set Cache-Control "no-cache"
  </FilesMatch>
</IfModule>
AddDefaultCharset UTF-8
```
- Requisito: cada cambio de CSS/JS/imagen **debe** cambiar `?v=` o el nombre de archivo. Las imágenes no llevan versión hoy. Si se reemplaza una captura con el mismo nombre, usar `max-age=604800` para las imágenes en lugar de `immutable`.
- Validación: `curl -sI https://facturales.es/ | grep -i strict-transport` y `curl -sI "https://facturales.es/assets/css/facturales-ds.css?v=20261018" | grep -i cache-control`.

**P1-4. Rendimiento: CSS y fuentes no bloqueantes y LCP móvil.** Impacto M-A (LCP 2,4-2,8 → ~1,5-1,8 s estimado) · Esfuerzo M · Riesgo M
1. **Retirar `main.css` de todas las páginas**: extraer las reglas del cubo (`.cubes-wrapper`, `@keyframes cube-spin/cube-float` y dependencias, `main.css` desde la línea ~4519 y ~8394) a `facturales-ds.css` (o a un `fx-rombo.css` solo para la home). Comprobar visualmente con `premium-ui-reviewer`. Si no se retira, al menos eliminar el `@import` de Google Fonts de `main.css:18`.
2. **Auto-alojar Onest** (woff2 variable, `assets/fonts/onest-var.woff2`), `@font-face` con `font-display: swap` dentro de `facturales-ds.css` y `<link rel="preload" as="font" type="font/woff2" crossorigin href="/assets/fonts/onest-var.woff2">`. Eliminar los preconnect y el `<link>` a fonts.googleapis.com. De paso se elimina la transferencia de IP a Google (RGPD).
3. **Hero adaptable**: sustituir los dos `<img>` (`.fx-solo-ancho` + `.fx-solo-estrecho`) por un `<picture>` con `<source media="(max-width: 699px)" srcset="…movil-400.webp 400w, …movil-780.webp 780w" sizes="272px">` y el `<img>` de escritorio como fallback, con `fetchpriority="high"` y sin `lazy`. Si se mantiene el marco de teléfono distinto, al menos: escritorio `loading="lazy"` sin `fetchpriority` en móvil, y la captura móvil `loading="eager" fetchpriority="high"`. O un `<link rel="preload" as="image" imagesrcset=… media="(max-width: 699px)">`.
4. Tras P1-1, el header ya no necesitará JS síncrono.
- Aceptación (Lighthouse móvil, repo): Performance ≥ 97 y LCP ≤ 1,8 s en home, pricing, crea-envia-facturas y artículo; `render-blocking-resources` = solo `facturales-ds.css` (o vacío con CSS crítico inline); en `crea-envia-facturas` móvil no se descarga `facturas-emitidas-1280.webp`.
- Validación: `CHROME_PATH=/opt/pw-browsers/chromium-1194/chrome-linux/chrome npx lighthouse https://facturales.es/crea-envia-facturas.html --form-factor=mobile --only-categories=performance --output=json` y revisar `network-requests`.

**P1-5. Datos estructurados: grafo con `@id`.** Impacto M · Esfuerzo B-M · Riesgo B
Grafo recomendado (un `<script type="application/ld+json">` con `@graph` por página; las entidades comunes con el mismo `@id` en todas):
```json
{"@context":"https://schema.org","@graph":[
 {"@type":"Organization","@id":"https://facturales.es/#organization","name":"Facturales","url":"https://facturales.es/",
  "logo":{"@type":"ImageObject","@id":"https://facturales.es/#logo","url":"https://facturales.es/assets/img/logo/facturales-logo-512.png","width":512,"height":512},
  "email":"info@facturales.es","contactPoint":[{"@type":"ContactPoint","contactType":"customer support","email":"soporte@facturales.es","availableLanguage":"es"}],
  "sameAs":[/* solo perfiles reales: LinkedIn, App Store, Google Play… */]},
 {"@type":"WebSite","@id":"https://facturales.es/#website","url":"https://facturales.es/","name":"Facturales","inLanguage":"es-ES","publisher":{"@id":"https://facturales.es/#organization"}},
 {"@type":"SoftwareApplication","@id":"https://facturales.es/#software","name":"Facturales","applicationCategory":"BusinessApplication","applicationSubCategory":"Software de facturación","operatingSystem":"Web, iOS, Android","url":"https://facturales.es/","publisher":{"@id":"https://facturales.es/#organization"},
  "offers":[{"@type":"Offer","name":"Starter (mensual)","price":"6.45","priceCurrency":"EUR",
    "priceSpecification":{"@type":"UnitPriceSpecification","price":"6.45","priceCurrency":"EUR","unitCode":"MON","referenceQuantity":{"@type":"QuantitativeValue","value":1,"unitCode":"MON"},"valueAddedTaxIncluded":false},
    "url":"https://facturales.es/pricing.html","availability":"https://schema.org/InStock"}
    /* … Starter anual 4.95, Pro 11.95/8.95, Ilimitado 23.95/17.95, con los mismos campos */]},
 {"@type":"WebPage","@id":"https://facturales.es/crea-envia-facturas.html#webpage","url":"https://facturales.es/crea-envia-facturas.html","name":"Facturación con VERI*FACTU","isPartOf":{"@id":"https://facturales.es/#website"},"about":{"@id":"https://facturales.es/#software"},"breadcrumb":{"@id":"https://facturales.es/crea-envia-facturas.html#breadcrumb"},"inLanguage":"es-ES"},
 {"@type":"BreadcrumbList","@id":"https://facturales.es/crea-envia-facturas.html#breadcrumb","itemListElement":[
   {"@type":"ListItem","position":1,"name":"Inicio","item":"https://facturales.es/"},
   {"@type":"ListItem","position":2,"name":"Funciones","item":"https://facturales.es/funciones.html"},
   {"@type":"ListItem","position":3,"name":"Facturación"}]}
]}
```
- Artículos: `BlogPosting` con `@id …#article`, `isPartOf` → `#website`, `publisher` → `#organization`, `datePublished` y **`dateModified`** (reflejados también en visible: «Actualizado el …»), `author` como **`Person`** real con `url` a una página de autor y credenciales (asesor fiscal colaborador, si existe; si no, mantener `Organization`). `image` específica del artículo (1200×675 o más), `inLanguage`, `mainEntityOfPage` → `#webpage`.
- `pricing.html`: añadir el `SoftwareApplication` con todas las ofertas (o referenciar `#software`) más `BreadcrumbList`.
- `news-grid.html`: `Blog` o `CollectionPage` con `ItemList` de artículos. `about.html`: `AboutPage`. `contact.html`: `ContactPage`. `funciones.html`: `CollectionPage`/`ItemList` de módulos.
- Logo: crear una PNG cuadrada de 512×512 del rombo (o del logotipo completo sobre fondo sólido) para `Organization.logo` y `publisher.logo`.
- Aceptación: Rich Results Test sin errores en home, pricing, un módulo y un artículo; validator.schema.org sin advertencias de `@id` huérfanos.
- Validación local: `python3 -I -c "import json,re,sys;s=open(sys.argv[1]).read();[json.loads(x) for x in re.findall(r'<script type=\"application/ld\+json\">(.*?)</script>',s,re.S)];print('ok')" pricing.html`.

**P1-6. Titles y descripciones orientados a keywords.** Impacto A · Esfuerzo B · Riesgo B (validar las keywords antes, ver Hipótesis 2)
- Propuestas (ajustar con datos):
  - Home: «Programa de facturación para autónomos y pymes con VERI*FACTU · Facturales» (≤ 60-65 car.).
  - crea-envia-facturas: «Software de facturación con VERI*FACTU y facturas recurrentes · Facturales».
  - gestiona-tu-stock: «Programa de inventario y control de stock · Facturales».
  - impuestos: «Modelo 303 y 130 calculados desde tus facturas · Facturales».
  - tu-negocio-bajo-control: «Cuadro de mando financiero para pymes · Facturales».
  - escanea-gastos: «Gestión de gastos y escáner de tickets con OCR · Facturales».
  - gestiona-clientes: «Gestión de clientes y facturación por cliente · Facturales».
  - funciones: acortar a ≤ 60 caracteres.
  - Artículos: pasar a minúsculas según la norma española y ≤ 60 caracteres.
- Descripciones: todas entre 120 y 158 caracteres (hoy 9 superan 160).
- Validación: `python3 -I` con el script `[scratchpad de la auditoría]/scripts/onpage.py` y comprobar `len(title)<=65` y `120<=len(desc)<=158`.

**P1-7. Enlazado contextual desde el blog y a pricing/faq.** Impacto M · Esfuerzo B · Riesgo B
- Guía VERI*FACTU → `crea-envia-facturas.html` (anchor «software de facturación con VERI*FACTU»). Factura electrónica vs VERI*FACTU → `crea-envia-facturas.html#facturae`. Contabilidad en 7 pasos → `bancos-conciliacion.html` («conciliación bancaria»), `escanea-gastos.html` («digitalizar tickets»), `impuestos.html` («modelo 303 y 130»), `tu-negocio-bajo-control.html` («cuadro de mando»).
- `pricing.html` → `funciones.html` y `faq.html`. Desde los módulos, un enlace «Ver precios» con anchor descriptivo.
- Aceptación: cada artículo enlaza al menos a 2 páginas de módulo en el cuerpo; `faq.html` y `about.html` reciben al menos 3 enlaces estáticos.

**P1-8. Páginas legales visibles e indexables en el dominio principal (E-E-A-T).** Impacto M · Esfuerzo M · Riesgo B
- Publicar `/aviso-legal.html` (titular, NIF, domicilio, registro), `/privacidad.html`, `/cookies.html` y `/condiciones.html` en la landing (pueden ser la fuente canónica y la app enlazarlas), con enlaces estáticos en el footer (P1-1). Alternativa mínima: quitar el `noindex` solo de esas rutas en `vercel.json`, aunque la app SPA sirve 6 KB sin contenido sin JS, así que es peor opción.

### P2 — Planificar (1-2 meses)

**P2-1. Migración a URLs limpias.** Impacto M-A a medio plazo · Esfuerzo A · Riesgo **A** (se pierden señales si se hace mal)

Propuesta (keywords pendientes de validar):

| Actual | Propuesta |
|---|---|
| `/` | `/` |
| `/pricing.html` | `/precios/` |
| `/funciones.html` | `/funciones/` |
| `/crea-envia-facturas.html` | `/programa-facturacion/` (o `/software-facturacion/`) |
| `/crea-envia-presupuestos.html` | `/presupuestos/` |
| `/bancos-conciliacion.html` | `/conciliacion-bancaria/` |
| `/cobros.html` | `/control-cobros/` |
| `/escanea-gastos.html` | `/gestion-gastos/` |
| `/impuestos.html` | `/modelo-303-130/` (o `/impuestos/`) |
| `/tu-negocio-bajo-control.html` | `/cuadro-de-mando/` |
| `/gestiona-clientes.html` | `/gestion-clientes/` |
| `/gestiona-tu-stock.html` | `/control-stock-inventario/` |
| `/factura-personalizada.html` | `/plantilla-factura-personalizada/` |
| `/faq.html` | `/preguntas-frecuentes/` |
| `/contact.html` | `/contacto/` |
| `/about.html` | `/sobre-nosotros/` |
| `/news-grid.html` (+ news.html, news-details.html) | `/blog/` |
| `/verifactu-2027-guia-autonomos-pymes.html` | `/blog/verifactu-guia-autonomos-pymes/` (sin año en el slug, para poder actualizarlo) |
| `/factura-electronica-vs-verifactu.html` | `/blog/factura-electronica-vs-verifactu/` |
| `/contabilidad-negocio-7-pasos.html` | `/blog/como-llevar-contabilidad-negocio/` |

Implementación en hosting estático sin build: **un directorio por página con `index.html`** (`/precios/index.html`). Apache sirve `/precios/` y redirige `/precios` → `/precios/` (DirectorySlash). No hacen falta rewrites internos.

Pasos y requisitos previos:
1. Convertir **todas** las rutas relativas a absolutas desde la raíz (`/assets/...`, `/precios/`) en HTML, JS de nav/footer, `404.html` y CSS (`url(...)`). Corregir la lógica `ruta` de los include (o eliminarla con P1-1) para comparar `location.pathname`.
2. Actualizar canonical, `og:url`, JSON-LD (`@id`, `mainEntityOfPage`, migas), `sitemap.xml` (solo URLs nuevas, `lastmod` real), enlaces internos y, en la app, cualquier enlace a la landing.
3. `.htaccess` con mapa 1:1 (**sin cadenas**: cada URL antigua va directa a la final, y P0-1 se fusiona en la misma regla):
   ```apache
   RewriteEngine On
   RewriteCond %{HTTPS} off [OR]
   RewriteCond %{HTTP_HOST} ^www\. [NC]
   RewriteRule ^(.*)$ https://facturales.es/$1 [R=301,L,NE]
   RewriteRule ^index\.html$ / [R=301,L]
   RewriteRule ^pricing\.html$ /precios/ [R=301,L]
   RewriteRule ^funciones\.html$ /funciones/ [R=301,L]
   RewriteRule ^crea-envia-facturas\.html$ /programa-facturacion/ [R=301,L]
   RewriteRule ^crea-envia-presupuestos\.html$ /presupuestos/ [R=301,L]
   RewriteRule ^bancos-conciliacion\.html$ /conciliacion-bancaria/ [R=301,L]
   RewriteRule ^cobros\.html$ /control-cobros/ [R=301,L]
   RewriteRule ^escanea-gastos\.html$ /gestion-gastos/ [R=301,L]
   RewriteRule ^impuestos\.html$ /modelo-303-130/ [R=301,L]
   RewriteRule ^tu-negocio-bajo-control\.html$ /cuadro-de-mando/ [R=301,L]
   RewriteRule ^gestiona-clientes\.html$ /gestion-clientes/ [R=301,L]
   RewriteRule ^gestiona-tu-stock\.html$ /control-stock-inventario/ [R=301,L]
   RewriteRule ^factura-personalizada\.html$ /plantilla-factura-personalizada/ [R=301,L]
   RewriteRule ^faq\.html$ /preguntas-frecuentes/ [R=301,L]
   RewriteRule ^contact\.html$ /contacto/ [R=301,L]
   RewriteRule ^about\.html$ /sobre-nosotros/ [R=301,L]
   RewriteRule ^(news-grid|news|news-details)\.html$ /blog/ [R=301,L]
   RewriteRule ^verifactu-2027-guia-autonomos-pymes\.html$ /blog/verifactu-guia-autonomos-pymes/ [R=301,L]
   RewriteRule ^factura-electronica-vs-verifactu\.html$ /blog/factura-electronica-vs-verifactu/ [R=301,L]
   RewriteRule ^contabilidad-negocio-7-pasos\.html$ /blog/como-llevar-contabilidad-negocio/ [R=301,L]
   RewriteRule ^conectado-a-gestor\.html$ /funciones/ [R=301,L]
   ```
   Nota: la primera regla manda `http://www.…/pricing.html` a `https://facturales.es/pricing.html` y luego a `/precios/` (2 saltos). Para un único salto, anteponer la regla de www/http a cada regla del mapa o, en nginx, usar un `map`. Dos saltos siguen siendo aceptables para Google (sigue hasta 10).
   En **nginx (Plesk → Configuración de Apache y nginx → Directivas adicionales de nginx)**, si Apache no procesa `.htaccess`:
   ```nginx
   if ($host = www.facturales.es) { return 301 https://facturales.es$request_uri; }
   location = /pricing.html { return 301 /precios/; }
   location = /index.html  { return 301 /; }
   # … una línea por URL
   ```
4. Plan de corte: crawl previo (lista de URLs y estado), despliegue en un horario de poco tráfico, validación con script, envío del sitemap nuevo a GSC y Bing, inspección de URL de las 5 principales, mantener el sitemap viejo 2-4 semanas para acelerar el descubrimiento de los 301, y monitorizar Cobertura y Rendimiento semanalmente durante 8 semanas. **Mantener los 301 de por vida.**
5. Riesgos: caída temporal de posiciones (2-6 semanas habituales); recursos rotos por rutas relativas (el riesgo principal en este repo); cadenas de redirección; enlaces externos que no se pueden actualizar; caché del navegador de los 301 (es permanente, así que conviene probar antes con 302 en un subdominio de staging); el `ruta` del header-include.
- Validación:
  ```bash
  while read old new; do r=$(curl -s -o /dev/null -w "%{http_code} %{redirect_url}" "https://facturales.es/$old"); echo "$old -> $r (esperado 301 https://facturales.es$new)"; done < redirects.tsv
  curl -s https://facturales.es/sitemap.xml | grep -o '<loc>[^<]*' | sed 's/<loc>//' | xargs -n1 curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" | grep -v '^200'   # debe salir vacío
  ```
- Recomendación de calendario: hacer P0/P1 primero (www, index.html, nav estático, títulos), medir 4-6 semanas en GSC y migrar después. Si la migración se hace, hacerla **una sola vez** y junto con el paso a nav estático (los dos tocan todos los archivos).

**P2-2. Contenido escaso.** Impacto M · Esfuerzo M-A · Riesgo B
- `funciones.html`: añadir 1-2 frases por módulo bajo cada h2 (hoy solo hay títulos y miniaturas). `about.html`: equipo, empresa, historia, ubicación y datos legales. Artículos: ampliar a 1 200-2 000 palabras con fuentes oficiales (BOE, AEAT), FAQs, «Actualizado el …» y tablas de plazos.
- Resolver el solapamiento VERI*FACTU: la guía como pilar «qué es VERI*FACTU», el comparativo centrado en «factura electrónica obligatoria B2B» y el módulo en «software», con enlaces cruzados.

**P2-3. Sitemap útil.** Impacto B · Esfuerzo B · Riesgo B
- `lastmod` real por página (generado desde `git log -1 --format=%cs -- archivo` en el script de despliegue), eliminar `priority`, añadir `<image:image>` con las capturas principales de cada módulo.

### P3 — Mejoras menores

- **P3-1.** `/favicon.ico` (32×32), `<link rel="apple-touch-icon" href="/apple-touch-icon.png">` (180×180) y `site.webmanifest` con `name`, `icons` y `theme_color`. Validación: `curl -s -o /dev/null -w "%{http_code}" https://facturales.es/favicon.ico` = 200.
- **P3-2.** `/llms.txt` con una descripción breve de Facturales, enlaces a los módulos, precios (con «+ IVA»), FAQ y guías. Sin claims inventados (respetar CLAUDE.md: banco «Próximamente», sin envío automático a la AEAT). Validación: 200 con `text/plain` o `text/markdown`.
- **P3-3.** `pricing.html`: h2 «Planes» y h3 por plan. Añadir un espacio o separador entre `<h3>` y `<small>` en las galerías.
- **P3-4.** Corregir las plantillas demo que sigan en el repo (`lang="en"`, «Brevon…») o eliminarlas del repo para que no vuelvan a desplegarse.
- **P3-5.** `content-type: text/html; charset=utf-8` (`AddDefaultCharset UTF-8`).
- **P3-6.** Alt de las miniaturas de `funciones.html`: hoy `alt=""`. Como acompañan a un h2 descriptivo es aceptable, pero un alt corto («Captura de facturas emitidas») aporta señal en Google Imágenes.

---

## Anexo A — Comandos y artefactos usados
- Estado HTTP y cabeceras: `curl -s -o /dev/null -w "%{http_code} %{redirect_url} %{size_download}"` y `curl -sI` (con `-H 'Accept-Encoding: br'`).
- Diferencias vivo/repo: descarga en `[scratchpad de la auditoría]/live/` y `cmp`.
- Extracción on-page: `[scratchpad de la auditoría, no versionado]/scripts/onpage.py` → `[scratchpad de la auditoría, no versionado]/onpage.json`.
- Prueba JS on/off: `[scratchpad de la auditoría, no versionado]/scripts/nojs.js` (Playwright 1.56.1 global, Chromium 1194).
- Lighthouse: `[scratchpad de la auditoría, no versionado]/lh/` (`live-*.json`, `repo-*.json`, `sum.py`).
- Historial: `git log --all --name-status --diff-filter=DR` y `git log --all --name-only | grep .html`.
- DNS: `https://dns.google/resolve?name=facturales.es&type=TXT`.
- No disponibles: Wayback CDX (sin respuesta), Search Console y herramientas de keywords.
