# CLAUDE.md

Guía para Claude Code (claude.ai/code) al trabajar en este repositorio.

## Qué es esto

Landing de **Facturales** (facturales.es), una aplicación de facturación para autónomos y pymes en España. La aplicación vive en `app.facturales.es`; este repositorio es **solo el sitio de marketing estático**. El titular legal es AVENUE DIGITAL GROUP, S.L.

## Arquitectura

- **Sitio estático**: sin build, sin bundler, sin SSR ni dependencias de npm. Cada página es un `.html` de la raíz que se sirve tal cual.
- **Base visual**: plantilla "Neotix" (ThemeForest) muy adaptada. Solo debe quedar su cabecera de licencia en `assets/css/main.css`; los textos, páginas y componentes son de Facturales.
- **Menú y cabecera**: viven en `assets/js/header-include.js`, que los inyecta con `document.write()` (cabecera, menú de escritorio y panel móvil). Para cambiar la navegación hay que editar **ese fichero**, no cada página. El script deduce la raíz del sitio de su propia URL, así que también funciona desde rutas anidadas (p. ej. la página 404).
- **Barra superior, pie y el resto del marcado común** están copiados en cada HTML. Si cambias uno, cámbialo en todas las páginas (hay un script de comprobación, ver más abajo).
- **Estilos**: `assets/css/main.css` es la única hoja propia (más `orbit-cta.css` para el diagrama de las fichas). Los tokens de color y tipografía están en `:root` de `main.css`.
- **Lógica**: `assets/js/main.js` (menús, sliders, animaciones GSAP) y `assets/js/orbit-cta.js` (diagrama de las fichas).
- **Tipografías autoalojadas** en `assets/fonts/` (Inter y Plus Jakarta Sans, licencia OFL). No se usa ningún CDN ni servicio de terceros: el sitio no hace peticiones externas.

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

`scripts/check-site.py` revisa, para cada `.html`: balance de `<div>` y anidado de etiquetas, `lang="es"`, título y meta description únicos, un único `<h1>`, enlaces y recursos locales existentes, ausencia de `href="#"`, restos de plantilla (Brevon, Gramentheme, Neotix, lorem ipsum), peticiones a hosts externos y las afirmaciones prohibidas por la política de contenido (más abajo).

## Política de contenido veraz

La app real (repositorio `facturales`) es la fuente de verdad. Antes de afirmar algo en la landing, compruébalo con `grep` en `src/` de la app. Si la app no lo cumple, no se publica, y **no se pone "próximamente"**.

- **Veri\*Factu / AEAT**: nunca "homologado", "100% legal", "certificado", "configurado de serie" ni que Facturales envía registros a la AEAT. Fórmula permitida: "Estamos preparando Facturales para Veri\*Factu, obligatorio a partir de 2027 (1 de enero de 2027 sociedades; 1 de julio de 2027 resto). Cada factura emitida es inalterable y se numera de forma correlativa." Las normas se citan por su nombre (p. ej. "Real Decreto 1007/2023") y sin URL si no se ha podido verificar.
- **Funciones que no existen**: stock/inventario, integraciones con Trello, Mailchimp o Slack, albaranes, proformas, estados "visto/aceptado" o firma en presupuestos, categorización por IA en el OCR, recordatorios automáticos de pago, facturas recurrentes, conexión bancaria, "Academia", informes PDF automáticos. Los presupuestos **comparten** el tope mensual de documentos del plan (no son "ilimitados" en Starter).
- **Gratis y tarjeta**: no hay plan gratuito y el alta pide método de pago. Se dice "Prueba 14 días" o "14 días de prueba gratuita · cancela cuando quieras". Prohibido "sin tarjeta", "gratis para siempre" y "acceso gratuito".
- **Precios** (iguales a los de la app, siempre más IVA): Starter 6,45 €/mes (4,95 € con facturación anual), Pro 11,95 € (8,95 €), Ilimitado 23,95 € (17,95 €). El ahorro anual real es del 23-25 %: "Ahorra hasta un 25 %".
- **Prueba social**: ni testimonios con nombres genéricos, ni cifras sin respaldo (clientes, valoraciones, horas ahorradas), ni "n.º 1". Las maquetas de interfaz llevan la nota "Datos de ejemplo".
- **Urgencia**: nada de cuentas atrás ni "ofertas de lanzamiento".
- **Identidad legal**: el pie dice "© Facturales · AVENUE DIGITAL GROUP, S.L." y enlaza a `https://app.facturales.es/aviso-legal`, `/politica-de-privacidad`, `/politica-de-cookies` y `/condiciones-legales`. No se publican NIF ni datos personales.
- **CTAs**: usan las rutas canónicas de la app, `https://app.facturales.es/signup` y `https://app.facturales.es/signin` (sin `.html`), con solo tres textos: "Prueba 14 días", "Crear cuenta" e "Iniciar sesión".

## Convenciones

- Todo el texto visible está en **español correcto** (tildes, ¿?, ¡!) y los títulos en *sentence case*.
- Sin analítica, trackers, fuentes de Google, CDN ni iframes de terceros.
- Imágenes en `assets/img/`; portadas del blog en `assets/img/blog/`; logos en `assets/img/logo/`.
- Mensajes de commit en español, pequeños y descriptivos.
- Para revisar cambios de interfaz importantes se usa el agente `premium-ui-reviewer` (`.claude/agents/premium-ui-reviewer.md`).
