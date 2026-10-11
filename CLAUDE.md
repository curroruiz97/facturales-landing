# CLAUDE.md

Guía para Claude Code (claude.ai/code) al trabajar en este repositorio.

## Qué es esto

Landing de **Facturales** (facturales.es), una aplicación de facturación para autónomos y pymes en España. La aplicación vive en `app.facturales.es`; este repositorio es **solo el sitio de marketing estático**. El titular legal es AVENUE DIGITAL GROUP, S.L.

## Arquitectura

- **Sitio estático**: sin build, sin bundler, sin SSR ni dependencias de npm. Cada página es un `.html` de la raíz que se sirve tal cual. Las URL canónicas llevan `.html` (no hay configuración de hosting con URL limpias).
- **Base visual**: plantilla "Neotix" (ThemeForest) muy adaptada. Solo debe quedar su cabecera de licencia en `assets/css/main.css`; los textos, páginas y componentes son de Facturales.
- **Cabecera y menú**: viven en `assets/js/header-include.js`, que con `document.write()` escribe la barra de prueba, la cabecera con el menú de escritorio y el panel de navegación móvil, todo a partir de los mismos datos de servicios. Para cambiar la navegación hay que editar **ese fichero**, no cada página. El script deduce la raíz del sitio de su propia URL, así que también funciona desde rutas anidadas (p. ej. la página 404), y marca la página actual con `aria-current="page"`.
- **Pie y marcado común** están copiados en cada HTML (pie legal, skip link, botón de subir, `<main id="main">`). Si cambias uno, cámbialo en todas las páginas; `scripts/check-site.py` avisa de los desajustes más habituales.
- **JavaScript propio, sin jQuery**: `main.js` (cabecera pegajosa, panel móvil accesible, submenú por teclado, volver arriba, revelado), `home.js` (solo la home: carrusel Swiper sin autoplay y animaciones GSAP), `pricing.js` (conmutador Anual/Mensual y tabla), `orbit-cta.js` (diagrama de las fichas). Todo va con `defer`.
- **Librerías de terceros** (en `assets/js` y `assets/css`): Bootstrap (rejilla, utilidades y acordeón; el JS solo en home, FAQ y precios), GSAP + ScrollTrigger + SplitText y Swiper (solo la home) y WOW (entrada de elementos). No hay ScrollSmoother: el scroll es nativo.
- **Estilos**: `assets/css/main.css` (común, podado con PurgeCSS: solo contiene lo que usan las páginas actuales), `assets/css/pages/<página>.css` (uno por página con maquetas propias), `assets/css/icons.css` (iconos) y `orbit-cta.css`. Los tokens están en `:root` de `main.css`.
- **Tipografías** autoalojadas en `assets/fonts/` (Inter y Plus Jakarta Sans variables, solo latín, licencia OFL). Sin CDN, Google Fonts ni terceros: el sitio no hace peticiones externas.
- **Iconos**: subconjunto de 88 glifos "solid" de Font Awesome Pro 6.0.0 (`assets/fonts/fa-solid-subset.woff2` + `assets/css/icons.css`). Si usas un icono nuevo (`fa-solid fa-xxx`), `check-site.py` falla hasta que lo añadas: regenera la fuente con `pyftsubset` desde `fa-solid-900.ttf` (los originales están en el historial: `git show f8d58a3:assets/webfonts/fa-solid-900.ttf` y `…/assets/css/all.min.css`, que da el código de cada icono) y añade su regla `.fa-xxx::before { content: "\f…" }` a `icons.css`. Las clases `fa-regular`, `fa-light` o `fa-brands` ya no existen.
- **Imágenes** en `assets/img/` (WebP; logos en `assets/img/logo/`, portadas del blog en `assets/img/blog/` con su JPG para Open Graph).
- **Si falta un componente de la plantilla** (equipo, proyectos, formularios…), el CSS podado se recupera del historial de git (commit "Poda el CSS sin uso").

## Páginas reales (15)

| Página | Qué es |
|---|---|
| `index.html` | Home |
| `pricing.html` | Planes y comparativa |
| `faq.html` | Preguntas frecuentes |
| `service-details.html` | Hub de servicios |
| `tu-negocio-bajo-control.html`, `crea-envia-facturas.html`, `crea-envia-presupuestos.html`, `escanea-gastos.html`, `gestiona-clientes.html`, `factura-personalizada.html` | Fichas de servicio |
| `news-grid.html` | Listado del blog |
| `verifactu-2027-guia-autonomos-pymes.html`, `factura-electronica-vs-verifactu.html`, `contabilidad-negocio-7-pasos.html` | Artículos |
| `404.html` | Página de error (rutas absolutas, `noindex`) |

No existe `contact.html` ni ninguna página de contacto con formulario: el contacto es `info@facturales.es`. Las 13 páginas de plantilla originales y la ficha de stock se eliminaron; no las recuperes.

## Verificación obligatoria antes de cada commit

```bash
python3 scripts/check-site.py        # sin dependencias; sale con código 1 si algo falla
python3 -m http.server 5183          # o: npx serve .   (para ver el sitio en local)
```

`.github/workflows/landing-ci.yml` ejecuta `check-site.py` en cada push y pull request. El script revisa, para cada `.html`:

- **Estructura y enlaces**: balance de `<div>` y anidado, `lang="es"`, título y meta description únicos, un único `<h1>`, enlaces y recursos locales existentes, sin `href="#"` ni anclas rotas, sin restos de plantilla (Brevon, Gramentheme, Neotix, lorem ipsum) y sin peticiones a hosts externos.
- **SEO**: título de 50-60 caracteres, descripción de 120-160, canonical (`https://facturales.es/<página>`; la home, `https://facturales.es/`), Open Graph y Twitter Card con imagen 1200x630, JSON-LD válido y coherente con la página (precios, preguntas visibles, fechas del artículo, migas), `sitemap.xml`, `robots.txt` y `noindex` en la 404.
- **Accesibilidad**: skip link y un único `<main id="main">`, jerarquía de encabezados sin saltos, `alt` útil, nombres accesibles en botones y enlaces, iconos decorativos con `aria-hidden`, sin `onclick` en línea y sin `outline: none !important`.
- **Movimiento y color**: `:focus-visible` y `prefers-reduced-motion` definidos, sin autoplay de menos de 6 s ni ScrollSmoother, sin naranjas sueltos y contraste de los tokens de color (>= 4,5:1).
- **Contenido veraz**: ninguna de las afirmaciones retiradas por la política de más abajo.

Los datos de SEO se escriben a mano en el `<head>` de cada página (el bloque `<!-- SEO -->`): si cambias un título, un precio, una pregunta o una fecha, actualiza también su meta, su JSON-LD y `sitemap.xml`; `check-site.py` detecta las incoherencias. Para páginas nuevas añade también la URL al sitemap.

## Accesibilidad y movimiento

- Foco visible global (`:focus-visible`, anillo oscuro con halo blanco). No lo quites en componentes nuevos.
- Con `prefers-reduced-motion: reduce` no se crea ninguna animación de scroll (`home.js`), WOW no se inicializa y el CSS apaga animaciones y transiciones sin dejar contenido oculto. El cubo del hero gira una vuelta y se queda quieto, y no se muestra por debajo de 768 px.
- El panel móvil es un diálogo modal: cerrado va `inert`, abierto atrapa el foco, Escape lo cierra y el fondo se vuelve `inert`.
- Colores: `--accent` (naranja de marca) solo para texto e iconos sobre fondos oscuros; `--accent-strong` (`--theme-strong`) como fondo con texto blanco; `--accent-text` (`--theme-text`) para texto naranja sobre fondos claros; `--text-dim` para el texto atenuado de los titulares. No introduzcas naranjas sueltos.
- Móvil (<= 575 px): texto de 16 px, objetivos táctiles de 44 px y secciones de 56 px de espacio vertical.

## Política de contenido veraz

La app real (repositorio `facturales`) es la fuente de verdad. Antes de afirmar algo en la landing, compruébalo con `grep` en `src/` de la app. Si la app no lo cumple, no se publica, y **no se pone "próximamente"**.

- **Veri\*Factu / AEAT**: nunca "homologado", "100% legal", "certificado", "configurado de serie" ni que Facturales envía registros a la AEAT. Fórmula permitida: "Estamos preparando Facturales para Veri\*Factu, obligatorio a partir de 2027 (1 de enero de 2027 sociedades; 1 de julio de 2027 resto). Cada factura emitida es inalterable y se numera de forma correlativa." Las normas se citan por su nombre (p. ej. "Real Decreto 1007/2023") y sin URL si no se ha podido verificar.
- **Funciones que no existen**: stock/inventario, integraciones con Trello, Mailchimp o Slack, albaranes, proformas, estados "visto/aceptado" o firma en presupuestos, categorización por IA en el OCR, recordatorios automáticos de pago, facturas recurrentes, conexión bancaria, "Academia", informes PDF automáticos. El tope mensual del plan (10 en Starter) cuenta solo **facturas emitidas**: la app no cuenta ni limita los presupuestos, así que no se dice que "comparten" el tope ni que sean "ilimitados" (se copia el texto de planes de la app: "10 facturas / mes", "Facturas ilimitadas").
- **Gratis y tarjeta**: no hay plan gratuito y el alta pide método de pago. Se dice "Prueba 14 días" o "14 días de prueba gratuita · cancela cuando quieras". Prohibido "sin tarjeta", "gratis para siempre" y "acceso gratuito".
- **Precios** (iguales a los de la app, siempre más IVA): Starter 6,45 €/mes (4,95 € con facturación anual), Pro 11,95 € (8,95 €), Ilimitado 23,95 € (17,95 €). El ahorro anual real es del 23-25 %: "Ahorra hasta un 25 %".
- **Prueba social**: ni testimonios con nombres genéricos, ni cifras sin respaldo (clientes, valoraciones, horas ahorradas), ni "n.º 1". Las maquetas de interfaz llevan la nota "Datos de ejemplo". Sin `aggregateRating` en el JSON-LD.
- **Urgencia**: nada de cuentas atrás ni "ofertas de lanzamiento".
- **Identidad legal**: el pie dice "© Facturales · AVENUE DIGITAL GROUP, S.L." y enlaza a `https://app.facturales.es/aviso-legal`, `/politica-de-privacidad`, `/politica-de-cookies` y `/condiciones-legales`. No se publican NIF ni datos personales.
- **CTAs**: usan las rutas canónicas de la app, `https://app.facturales.es/signup` y `https://app.facturales.es/signin` (sin `.html`), con solo tres textos: "Prueba 14 días", "Crear cuenta" e "Iniciar sesión".

## Convenciones

- Todo el texto visible está en **español correcto** (tildes, ¿?, ¡!) y los títulos en *sentence case*.
- Sin analítica, trackers, fuentes de Google, CDN ni iframes de terceros.
- Mensajes de commit en español, pequeños y descriptivos.
- Para revisar cambios de interfaz importantes se usa el agente `premium-ui-reviewer` (`.claude/agents/premium-ui-reviewer.md`).
