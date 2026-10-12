# CLAUDE.md

Guía para Claude Code (claude.ai/code) al trabajar en este repositorio.

## Qué es esto

Landing de **Facturales** (facturales.es), una aplicación de facturación para autónomos y pymes en España. La aplicación vive en `app.facturales.es`; este repositorio es **solo el sitio de marketing estático**. El titular legal es AVENUE DIGITAL GROUP, S.L.

## Arquitectura

- **Sitio estático**: sin build, sin bundler, sin SSR ni dependencias de npm. Cada página es un `.html` de la raíz que se sirve tal cual. Las URL canónicas llevan `.html` (no hay configuración de hosting con URL limpias).
- **Base visual**: plantilla "Neotix" (ThemeForest) muy adaptada. Solo debe quedar su cabecera de licencia en `assets/css/main.css`; los textos, páginas y componentes son de Facturales.
- **Cabecera y menú**: viven en `assets/js/header-include.js`, que con `document.write()` escribe la barra de prueba, la cabecera con el menú de escritorio y el panel de navegación móvil, todo a partir de los mismos datos de servicios. Para cambiar la navegación hay que editar **ese fichero**, no cada página. El script deduce la raíz del sitio de su propia URL, así que también funciona desde rutas anidadas (p. ej. la página 404), y marca la página actual con `aria-current="page"`.
- **Pie y marcado común** están copiados en cada HTML (pie legal, skip link, botón de subir, `<main id="main">`). Si cambias uno, cámbialo en todas las páginas; `scripts/check-site.py` avisa de los desajustes más habituales. El botón de subir va al final del `<body>`, tras el pie y antes de los scripts, para que el orden de tabulación lo deje después del contenido; `main.js` lo muestra tras un viewport de scroll.
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

No existe `contact.html` ni ninguna página de contacto con formulario: el contacto es `info@facturales.es`. Las 13 páginas de plantilla originales y la ficha de stock se eliminaron; no las recuperes (solo viven dentro de la copia congelada `v1/`, ver «Conmutador v1/v2»).

## Conmutador v1/v2 (temporal)

Para comparar a ojo lo que cambiaron las olas de la auditoría, el sitio lleva una píldora «v1 | v2» (abajo a la izquierda; se arrastra por el asa y recuerda dónde la dejas) que alterna entre la landing anterior y la actual **en la misma página**.

- **`v1/`** es una copia congelada de la landing de `add-template` antes de los cambios (ver `v1/SOURCE.txt`), generada con `python3 scripts/freeze-v1.py [ref]`. **No se edita ni se «arregla»**: conserva a propósito plantilla, claims retirados (gratis, cifras sin respaldo…) y fuentes de Google. Sus páginas llevan `noindex`, un script que en `facturales.es` redirige a la misma página del sitio actual (la copia no se sirve en producción) y el conmutador. `robots.txt` la excluye (`Disallow: /v1/`) y `check-site.py` no la revisa (`SKIP_DIRS`).
- **`assets/js/version-switcher.js`** (con `defer`, al final de las 15 páginas) pinta la píldora. Deduce la raíz del sitio de su propia URL, conserva página, búsqueda y hash, y si la otra versión no tiene esa página (el v1 tenía 13 de plantilla) lleva a su portada. En `facturales.es` no se muestra.
- `check-site.py` exige que el conmutador esté completo (script en todas las páginas, `v1/index.html` y `Disallow: /v1/`) o que no esté: así quitarlo no deja restos.

**Quitarlo** (un solo commit lo añadió, así que `git revert` lo deshace): borrar `v1/`, `assets/js/version-switcher.js` y `scripts/freeze-v1.py`; en cada `.html`, el comentario y el `<script>` del conmutador; `Disallow: /v1/` de `robots.txt`; y en `check-site.py`, `"v1"` de `SKIP_DIRS`, el conmutador de `FIRST_PARTY_ASSETS` y `check_switcher`.

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
- Colores: `--accent` (naranja de marca) solo para texto e iconos sobre fondos oscuros; `--accent-soft` (naranja claro, >= 7:1 sobre `--header`) para texto sobre fondos oscuros que pide más contraste que `--accent` (etiquetas pequeñas, enlaces en hover); `--accent-strong` (`--theme-strong`) como fondo con texto blanco, también al principio de los degradados que lleven texto blanco pequeño (el final es `--accent-dark`); `--accent-text` (`--theme-text`) para texto naranja sobre fondos claros; `--text-dim` para el texto atenuado de los titulares y las etiquetas de las maquetas claras (nada de `#999`); `--success-strong` para texto verde sobre claro (`--success` solo sobre oscuro). No introduzcas naranjas sueltos.
- Maquetas de interfaz: sus textos cumplen 4,5:1 como el resto (sobre fondo oscuro, blanco con alfa >= 0,6). La nota «Datos de ejemplo» (`.mockup-note`) es el marcador que exige la política de contenido: no se atenúa con `opacity` y no puede quedar cortada por el `overflow` de la maqueta.
- Teclado: WOW deja los elementos sin revelar con `visibility: hidden` en línea y un elemento oculto no recibe foco; `main.css` los pasa a `opacity: 0` con `visibility: visible` mientras no se revelan (la regla solo casa con el estilo en línea de WOW, así que sin JS o con movimiento reducido todo sigue visible). Comprueba con Tab que una página nueva no deja controles inalcanzables. Con Escape el submenú de Servicios pasa a `display: none` (no a `visibility`) para que un Tab inmediato no entre en enlaces que van a ocultarse.
- Titulares partidos con SplitText (`home.js`, versión sin opción `aria`): `splitHeading()` pone el texto completo en `aria-label` (solo valen titulares) y oculta el desglose con `aria-hidden`. Los pseudoelementos de icono (`+`/`-` del acordeón) llevan texto alternativo vacío (`content: "…" / ""`) para que no entren en el nombre del botón.
- Móvil (<= 575 px): texto de 16 px, objetivos táctiles de 44 px (enlaces de texto, puntos del carrusel, logo) y secciones de 56 px de espacio vertical. El panel móvil se desplaza entero (`.offcanvas__info`) en pantallas bajas; la lista del menú no tiene scroll propio.
- Home: el apilado con pin de «Lo que puedes hacer» solo existe desde 1400 px (por debajo cada panel mide más que la ventana); el carrusel de servicios va dentro de `.container`, con 4 tarjetas por vista y todas de la misma altura.

## Política de contenido veraz

La app real (repositorio `facturales`) es la fuente de verdad. Antes de afirmar algo en la landing, compruébalo con `grep` en `src/` de la app. Si la app no lo cumple, no se publica, y **no se pone "próximamente"**.

- **Veri\*Factu / AEAT**: nunca "homologado", "100% legal", "certificado", "configurado de serie" ni que Facturales envía registros a la AEAT. Fórmula permitida: "Estamos preparando Facturales para Veri\*Factu, obligatorio a partir de 2027 (1 de enero de 2027 sociedades; 1 de julio de 2027 resto). Cada factura emitida es inalterable y se numera de forma correlativa." Las normas se citan por su nombre (p. ej. "Real Decreto 1007/2023") y sin URL si no se ha podido verificar.
- **Funciones que no existen**: stock/inventario, integraciones con Trello, Mailchimp o Slack, albaranes, proformas, estados "visto/aceptado" o firma en presupuestos, categorización por IA en el OCR, recordatorios automáticos de pago, facturas recurrentes, conexión bancaria, "Academia", informes PDF automáticos. El tope mensual del plan (10 en Starter) cuenta solo **facturas emitidas**: la app no cuenta ni limita los presupuestos, así que no se dice que "comparten" el tope ni que sean "ilimitados" (se copia el texto de planes de la app: "10 facturas / mes", "Facturas ilimitadas").
- **Gratis y tarjeta**: no hay plan gratuito y el alta pide método de pago. Se dice "Prueba 14 días" o "14 días de prueba gratuita · cancela cuando quieras". Prohibido "sin tarjeta", "gratis para siempre" y "acceso gratuito".
- **Precios** (iguales a los de la app, siempre más IVA): Starter 6,45 €/mes (4,95 € con facturación anual), Pro 11,95 € (8,95 €), Ilimitado 23,95 € (17,95 €). El ahorro anual real es del 23-25 %: "Ahorra hasta un 25 %".
- **Prueba social**: ni testimonios con nombres genéricos, ni cifras sin respaldo (clientes, valoraciones, horas ahorradas), ni "n.º 1". Las maquetas de interfaz llevan la nota "Datos de ejemplo". Sin `aggregateRating` en el JSON-LD.
- **Urgencia**: nada de cuentas atrás ni "ofertas de lanzamiento".
- **Identidad legal**: el pie dice "© Facturales · AVENUE DIGITAL GROUP, S.L." y enlaza a `https://app.facturales.es/aviso-legal`, `/politica-de-privacidad`, `/politica-de-cookies` y `/condiciones-legales`. No se publican NIF ni datos personales.
- **CTAs**: usan las rutas canónicas de la app, `https://app.facturales.es/signup` y `https://app.facturales.es/signin` (sin `.html`), con solo tres textos: "Prueba 14 días", "Crear cuenta" e "Iniciar sesión". El CTA orbital de las fichas muestra el logo y el texto «Prueba 14 días» (su `aria-label` lo contiene). Los tres botones de plan de `pricing.html` llevan `aria-label="Prueba 14 días: plan X"` para distinguirse.

## Convenciones

- Todo el texto visible está en **español correcto** (tildes, ¿?, ¡!) y los títulos en *sentence case*.
- Sin analítica, trackers, fuentes de Google, CDN ni iframes de terceros.
- Mensajes de commit en español, pequeños y descriptivos.
- Para revisar cambios de interfaz importantes se usa el agente `premium-ui-reviewer` (`.claude/agents/premium-ui-reviewer.md`).
