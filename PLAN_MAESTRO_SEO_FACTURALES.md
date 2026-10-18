# PLAN MAESTRO SEO · FACTURALES

> **Versión:** 1.0 · **Fecha:** 18/10/2026 · **Ámbito:** `facturales.es` (repo `facturales-landing`, HTML estático) y, donde afecta al SEO o a la medición, `app.facturales.es` (repo `facturales`).
> **Estado:** PROPUESTA PENDIENTE DE VALIDACIÓN. **No se ha modificado código ni desplegado nada.** Ninguna tarea de este plan debe ejecutarse hasta que el propietario valide las decisiones de la §2.
> **Elaborado con:** 5 auditorías paralelas (SEO técnico, keywords y competencia, arquitectura de contenidos y CRO, GEO y autoridad, legal/fiscal y medición). Datos de mercado de **SE Ranking (base Google España, octubre de 2026)**, mediciones propias con **Lighthouse 12.8 y Playwright**, `curl` contra producción, lectura de ambos repositorios y fuentes primarias (BOE, sede de la AEAT, Ministerio de Hacienda, EUR-Lex, AEPD). Los informes completos están en `docs/seo/auditoria-2026-10/`.

---

## Índice

0. [Cómo usar este documento](#0-cómo-usar-este-documento)
1. [Resumen ejecutivo](#1-resumen-ejecutivo)
2. [Decisiones que necesita el propietario (bloqueantes)](#2-decisiones-que-necesita-el-propietario-bloqueantes)
3. [FASE 1 — Auditoría](#3-fase-1--auditoría)
4. [FASE 2 — Fundamentos técnicos](#4-fase-2--fundamentos-técnicos)
5. [FASE 3 — Arquitectura estratégica](#5-fase-3--arquitectura-estratégica)
6. [FASE 4 — Contenidos y autoridad](#6-fase-4--contenidos-y-autoridad)
7. [FASE 5 — GEO y diferenciación](#7-fase-5--geo-y-diferenciación)
8. [FASE 6 — Medición y crecimiento](#8-fase-6--medición-y-crecimiento)
9. [CRO: del tráfico orgánico al cliente de pago](#9-cro-del-tráfico-orgánico-al-cliente-de-pago)
10. [Roadmap consolidado y priorización](#10-roadmap-consolidado-y-priorización)
11. [Checklist técnico](#11-checklist-técnico)
12. [Backlog ejecutable por archivo](#12-backlog-ejecutable-por-archivo)
13. [Pruebas de validación (scripts)](#13-pruebas-de-validación-scripts)
14. [Qué NO hacer](#14-qué-no-hacer)
15. [Anexos y fuentes](#15-anexos-y-fuentes)

---

## 0. Cómo usar este documento

### 0.1 Etiquetas de evidencia (obligatorias en todo el plan)

| Etiqueta | Significado |
|---|---|
| **[COMPROBADO]** | Verificado el 18/10/2026 con evidencia reproducible: `archivo:línea`, comando y salida, dato de SE Ranking o norma en fuente primaria. |
| **[DATO-SR]** | Métrica de SE Ranking (volumen, KD, CPC, tráfico estimado, backlinks, cuota de voz en IA). Es una estimación del índice de SE Ranking: sirve para comparar, no como verdad absoluta. |
| **[HIPÓTESIS]** | Inferencia razonable sin verificar. Lleva al lado cómo validarla. |
| **[PREVISIÓN]** | Resultado futuro estimado (tráfico, registros, MRR). Siempre en rangos y con sus supuestos. |
| **[RECOMENDACIÓN]** | Acción propuesta. |

### 0.2 Prioridades, esfuerzo y riesgo

- **P0**: bloqueante o de riesgo legal/técnico grave. Antes de cualquier otra cosa.
- **P1**: alto impacto, siguiente bloque (0–8 semanas).
- **P2**: impacto medio o dependiente de P1 (2–6 meses).
- **P3**: mejoras menores o de largo plazo.
- **Esfuerzo**: S ≤ 1 día · M 2–4 días · L 1–2 semanas · XL > 2 semanas (incluye revisión experta y diseño).
- **Riesgo**: B (bajo), M (medio), A (alto): probabilidad de romper algo, perder posiciones o incurrir en un problema legal.

### 0.3 Reglas para ejecutar con Claude Code

1. Cada tarea tiene un **ID** (`T2.03`, `T3.10`…), los **archivos** que toca, sus **dependencias**, **criterios de aceptación** y una **prueba de validación**. El backlog completo está en la §12.
2. Ejecutar por fases y en el orden de dependencias. **Una rama y un PR por bloque coherente**, nunca un mega-PR.
3. Antes de cada PR: pasar las pruebas de la §13 que correspondan, y en cambios de UI significativos, el agente `premium-ui-reviewer` (lo exige `CLAUDE.md`).
4. **Ningún texto comercial o fiscal se publica sin pasar la checklist de claims (§6.6)**, que resume `CLAUDE.md` y los hallazgos legales de este plan.
5. Las tareas marcadas **⛔ BLOQUEADA** dependen de una decisión de la §2 y no deben empezarse sin ella.

---

## 1. Resumen ejecutivo

### 1.1 Diagnóstico en 10 puntos

1. **Facturales parte de cero en buscadores.** [DATO-SR] 16 keywords en el top 100, **ninguna en el top 10**, tráfico orgánico estimado **0**. La mejor posición es la 19 («facturale»). Hay **1 dominio referente** (avenuemedia.io, del propio grupo) frente a 1.861–5.567 de los competidores. Cuota de voz en búsquedas con IA (ChatGPT, Perplexity, Gemini, AI Overviews): **0 %**. **Consecuencia estratégica:** no hay posiciones que proteger, así que los cambios estructurales (URLs, arquitectura) son baratos *ahora* y caros dentro de un año.
2. **El riesgo nº 1 no es SEO, es legal: la web afirma un cumplimiento VERI\*FACTU que la app todavía no tiene.** [COMPROBADO] La app genera el registro con huella y el QR solo si el usuario activa VERI\*FACTU, **no remite registros a la AEAT** (`estado_envio='pendiente'`), y la declaración responsable es un borrador «NO FIRMAR». Aun así, la web dice en más de 10 sitios «¿Cumple con VERI\*FACTU?… lleva el código QR de cotejo», «listas para VERI\*FACTU» o «Cumplimiento VERI\*FACTU». La app imprime además el QR de la modalidad VERI\*FACTU y la leyenda «Factura verificable en la sede electrónica de la AEAT», que según la FAQ de la AEAT solo proceden si se remite. En un tema YMYL, esto es a la vez riesgo de publicidad engañosa, de sanción al productor (art. 201 bis LGT) y de pérdida de confianza de Google y de los LLM. **Hay que resolverlo antes de invertir en contenido VERI\*FACTU.**
3. **El calendario normativo acaba de cambiar y la web no lo refleja.** [COMPROBADO] El 05/10/2026 Hacienda anunció la *previsión* de aplazar VERI\*FACTU **hasta octubre de 2028** (aún sin BOE; los plazos vigentes siguen siendo 01/01/2027 para el IS y 01/07/2027 para el resto). La factura electrónica B2B ya tiene reglamento (**RD 238/2026**, BOE 31/03/2026) y orden de la solución pública (**Orden HAC/1028/2026**, BOE 05/10/2026), con plazos ≈ octubre de 2027 (> 8 M€) y ≈ octubre de 2028 (resto). El artículo de Facturales sobre factura electrónica dice que «depende del desarrollo reglamentario»: **está desactualizado**. Ser la fuente más clara y mejor fechada sobre este cambio es **la oportunidad de citación más rápida** del plan.
4. **La base técnica tiene fallos sencillos pero graves.** [COMPROBADO] `www.facturales.es` sirve el sitio con 200 (host duplicado); `/index.html` duplica la home y todas las páginas enlazan a él; en producción son públicos `CLAUDE.md`, los scripts `.py`, `partials/` y `package-lock.json`; la 404 es la genérica de Plesk en inglés; no hay HSTS ni `Cache-Control`; **producción va por detrás del repo** (los 23 HTML difieren).
5. **La navegación no existe para los bots que no ejecutan JavaScript.** [COMPROBADO] Cabecera y pie se inyectan con `document.write`. Sin JS la home pasa de 86 a 26 enlaces, desaparecen los enlaces legales y `about.html` queda huérfana. GPTBot, ClaudeBot, PerplexityBot y, en parte, Bing ven esa versión.
6. **El rendimiento es bueno pero mejorable.** [COMPROBADO] Lighthouse móvil 92–96, TBT 0, CLS ≈ 0. El LCP (2,3–2,8 s) es casi todo bloqueo de render: Google Fonts, `main.css` (205 KB, ~90 % sin usar, solo hace falta para el cubo del hero), `facturales-ds.css` y el `document.write`. En móvil se descarga con prioridad alta la captura de escritorio, que está oculta.
7. **La arquitectura no cubre la demanda con intención de compra.** [COMPROBADO] 20 URLs indexables, mediana de ~400 palabras. **No hay** páginas para «programa de facturación para autónomos», pymes, gestorías, VERI\*FACTU comercial, sectores, alternativas a competidores, herramientas gratuitas ni plantillas. Ningún `title` contiene «programa/software de facturación». Los nombres de URL (`news-grid.html`, `tu-negocio-bajo-control.html`) no corresponden a ninguna búsqueda.
8. **Los competidores ganan con activos, no con landings.** [DATO-SR] Holded (~60,6 k visitas/mes estimadas), Quipu (31 k), Billin (29 k), Anfix (27,5 k) y Contasimple (21,6 k) obtienen su tráfico de **calculadoras** (la de IVA de Anfix es el 10 % de su tráfico), **generadores de facturas**, **plantillas** (Quipu tiene más de 45), **guías de modelos AEAT**, **glosarios** y **listicles «mejores programas…»**. Las landings por sector y las páginas «alternativa a X» apenas las trabajan los grandes: ahí hay hueco, y un SaaS recién llegado (getrenn.com) ya es #1 en «alternativa a holded».
9. **Hay ventanas de baja dificultad y alta intención de contratación.** [DATO-SR] Por ejemplo: «programa facturacion verifactu» 480/mes, KD 20; «software verifactu» 590, KD 5 (competencia real media); «precios holded» 480, KD 33; «contasimple opiniones» 390, KD 16; «control de stock» 390, KD 8; «gestion de cobros» 320, KD 8; «factura recapitulativa» 590, KD 8; «modelo factura autonomo» 480, KD 7; «hacer factura online» 390, KD 6. **Las 14 SERPs analizadas muestran AI Overview**, así que el contenido debe estar escrito para ser citado.
10. **No se mide nada.** [COMPROBADO] Ni la landing ni la app tienen analítica. No hay verificación de Search Console en el DNS ni en el HTML. Los 79 enlaces a `/signup` van sin UTM ni plan. La app no guarda el origen del registro. La política de cookies de la app es una plantilla que no cumple la Guía de la AEPD. **Sin medición, ninguna de las previsiones de este plan es verificable.**

### 1.2 Las 7 decisiones estratégicas del plan

| # | Decisión | Por qué |
|---|---|---|
| D1 | **Primero la verdad, después el volumen.** Corregir el copy VERI\*FACTU y publicar el estado normativo exacto antes que cualquier otro contenido. | YMYL. Una sola afirmación falsa en el tema estrella invalida la autoridad de todo el clúster, ante Google, ante los LLM y ante los usuarios. |
| D2 | **Migrar ya a URLs limpias en español** (`/precios/`, `/funciones/control-de-stock/`, `/blog/…`), en un solo corte y junto con la cabecera y el pie estáticos. | Con 0 tráfico y 1 enlace, el coste de migrar es mínimo hoy. Las dos tareas tocan todos los archivos, así que conviene hacerlas a la vez. |
| D3 | **Mantener el sitio estático sin bundler**, pero añadir un *script de sincronización* que escriba la cabecera y el pie en cada HTML (fuente única en `partials/`) y genere el sitemap. | Respeta la arquitectura de `CLAUDE.md` («HTML servido directamente») y arregla el rastreo sin JS. |
| D4 | **Competir por intención, no por volumen**: segmentos (autónomos, pymes, gestorías), VERI\*FACTU comercial, alternativas, módulos con KD < 10 y sectores con encaje real de producto. | Es donde un dominio nuevo puede llegar al top 10 en meses y donde está el CPC alto (2–10 €). |
| D5 | **Captar la intención «gratis» con herramientas gratuitas reales** (generador de facturas, calculadoras, plantillas), nunca prometiendo «gratis» en el producto. | No hay plan gratuito. Estas herramientas son además los mayores captadores de enlaces de la competencia. |
| D6 | **GEO desde el día 1:** HTML legible sin JS, `llms.txt`, ficha «Facturales en datos», comparativas con tablas fechadas, autor y revisor con nombre, schema con `@id`, Bing + IndexNow, y presencia en los comparadores que ya citan los LLM. | Los LLM citan blogs de fabricantes y comparativas pequeñas, no medios grandes. Un actor pequeño puede entrar. |
| D7 | **Medir el embudo completo con fuente de verdad en la base de datos** (registro → activación → pago por canal *first-touch*), con analítica sin cookies en la landing y GA4 solo con consentimiento. | Coherente con «datos en la UE» y con la AEPD, y la única forma de atribuir MRR al SEO. |

### 1.3 Las 12 acciones con mayor retorno (orden de ejecución)

| # | Acción | Fase | Prio | Esfuerzo |
|---|---|---|---|---|
| 1 | Revisión legal y corrección del copy VERI\*FACTU (web + FAQ + JSON-LD); decisión sobre el QR y la leyenda de la app | 2 | P0 ⛔ | M |
| 2 | Actualizar la guía VERI\*FACTU (aplazamiento anunciado a oct-2028) y el artículo de factura electrónica (RD 238/2026 + Orden HAC/1028/2026), con revisor y fuentes | 4 | P0 | M |
| 3 | Host único (301 www → apex), `/index.html` → `/`, retirar archivos internos, 404 real, HSTS y caché | 2 | P0 | S |
| 4 | Despliegue reproducible con lista blanca de archivos (y que el repo coincida con producción) | 2 | P0 ⛔ | M |
| 5 | Search Console (propiedad de dominio), Bing Webmaster Tools + IndexNow, analítica sin cookies y eventos de CTA | 6 | P0 | S |
| 6 | Atribución *first-touch* en el registro (landing → `signUp` metadata → tabla `user_acquisition`) | 6 | P0 | M |
| 7 | Cabecera y pie en HTML estático + migración a URLs limpias con mapa de 301 | 2–3 | P1 | L |
| 8 | Titles, H1 y meta orientados a keyword en las 20 páginas, y reorientar 5 módulos con KD < 10 (stock, cobros, panel, clientes, gastos) | 3 | P1 | M |
| 9 | Landings nuevas: `/autonomos/`, `/programa-verifactu/` ⛔, `/funciones/facturas-recurrentes/`, `/funciones/recordatorios-de-pago/`, `/pymes/`, `/gestorias/` | 3 | P1 | L |
| 10 | Alternativas a Holded, Quipu, Contasimple y Billin con datos fechados y verificables | 4 | P1 | M |
| 11 | Generador de facturas y calculadora IVA + IRPF (activos de enlace y de captación «gratis») | 4 | P1 | XL |
| 12 | Señales de entidad: legales en HTML en `facturales.es`, schema `Organization` completo, LinkedIn, Capterra/GetApp/G2, fichas de tiendas, comparadores que citan los LLM | 5 | P1 | M |

### 1.4 Qué se puede esperar (resumen; detalle en la §8.6)

- **Verificable y dependiente solo de la ejecución:** en 30 días, base técnica corregida, medición operativa y copy legal saneado. En 90 días, 16–20 piezas nuevas o actualizadas y 10–20 dominios referentes de calidad. En 365 días, 70–90 piezas y 50–120 dominios referentes.
- **[PREVISIÓN] (rango P10–P90, muy incierta):** a 12 meses, 60.000–250.000 impresiones no marca al mes, 2.000–10.000 clics orgánicos al mes, 60–300 registros orgánicos al mes y 300–1.500 € de MRR orgánico nuevo acumulado. **Competir por el liderazgo del mercado es un objetivo de 24–36 meses**: Holded tiene ~150.000 keywords y 5.567 dominios referentes. Este plan pone los cimientos y gana primero los nichos donde se puede ganar.

---

## 2. Decisiones que necesita el propietario (bloqueantes)

Ninguna de estas decisiones es técnica: son de negocio, legales o de acceso. Las tareas marcadas ⛔ esperan a su respuesta.

| # | Decisión | Opciones | Recomendación | Bloquea |
|---|---|---|---|---|
| **B1** | **Estado VERI\*FACTU y cómo comunicarlo** | (a) Completar la remisión a la AEAT (XML de la Orden HAC/1177/2024, registro de anulación, certificado y alta de colaborador social) y **firmar la declaración responsable**. (b) Mientras tanto, retirar de las facturas reales el QR de la modalidad VERI\*FACTU y la leyenda «verificable», y comunicar «preparado para VERI\*FACTU / remisión en preparación». | **(b) inmediatamente y (a) como objetivo de producto**, con validación de un asesor fiscal o abogado tributario. El plazo de los productores de software venció el 29/07/2025 [COMPROBADO, DF 4.ª RD 1007/2023]. | T2.01, T3.12, T4.01, T5.04 y todo el clúster VERI\*FACTU |
| **B2** | **Acceso al hosting (Plesk/IONOS)** y quién despliega | Credenciales SFTP/SSH para una GitHub Action, Git de Plesk o despliegue manual con checklist | GitHub Action con `rsync` de una lista blanca de archivos | T2.05 (despliegue), T2.02–T2.04 (`.htaccess`) |
| **B3** | **Analítica** | (a) Solo Plausible/Umami sin cookies. (b) Solo GA4 con CMP. (c) Híbrido. | **(c) Híbrido:** Plausible/Umami (UE, sin banner) para el 100 % del tráfico, GA4 con Consent Mode v2 *básico* para el embudo, y métricas de negocio desde Supabase | T6.03–T6.06 |
| **B4** | **Revisor experto con nombre** (asesor fiscal colegiado; abogado para morosidad y publicidad comparativa; graduado social para cuotas) | Externo por horas / acuerdo de colaboración / perfil interno | Acuerdo con 1 asesor fiscal colegiado que firme como revisor (nombre y n.º de colegiado visibles) | Todo contenido YMYL (T4.x) |
| **B5** | **Identidad corporativa visible** (AVENUE DIGITAL GROUP, S.L., NIF B-70829601, Valladolid) en la web, el schema, `about` y `llms.txt` | Sí / No | **Sí**: es la señal de confianza más barata para un software financiero | T5.02, T5.03, T3.20 |
| **B6** | **Comportamiento real de la prueba de 14 días**: ¿el Checkout de Stripe exige tarjeta siempre? ¿Se cobra automáticamente el día 15? | — | Imprescindible para una FAQ honesta y para el microcopy de los CTA. El CTA actual dice «Empieza **gratis** 14 días» [HIPÓTESIS: puede ser ambiguo si se pide tarjeta] | T9.02, T9.03 |
| **B7** | **Límites y estado de funciones**: ¿el rol Gestor ocupa plaza de usuario? ¿Se aplica el límite de usuarios (1/3/∞)? ¿Recurrentes y recordatorios están en producción para todos? (algunas migraciones tienen fecha posterior a hoy) ¿Hay soporte completo de recargo de equivalencia y operaciones exentas? | — | Confirmar antes de publicar `/gestorias/`, sectores con exenciones de IVA y campañas de recordatorios | T3.15, T3.16, T4.20+ |
| **B8** | **Apps iOS/Android**: ¿están publicadas? [HIPÓTESIS: no se han encontrado fichas en las búsquedas] | — | Si existen, enlazarlas desde la web y añadirlas al `sameAs` | T5.03, T5.10 |
| **B9** | **Presupuesto** (horas internas + externos: revisor, diseño de plantillas, herramientas SEO, notas de prensa) | — | Ver la estimación de costes de la §10.3 | Ritmo de la Fase 4 |
| **B10** | **Cláusula de enlaces del aviso legal**: hoy «prohíbe expresamente los enlaces profundos» sin autorización escrita [COMPROBADO, `LegalContent.tsx:27`] | Eliminar / mantener | **Eliminar**: contradice cualquier estrategia de enlaces | T5.02 |

---

## 3. FASE 1 — Auditoría

> Duración: completada el 18/10/2026 (este documento). Falta **una semana de validación**: el propietario revisa la §2 y se confirman las hipótesis marcadas como «validar en semana 0».

### 3.1 Punto de partida en cifras

| Métrica | Valor | Fuente |
|---|---|---|
| URLs indexables (sitemap) | 20 | [COMPROBADO] `sitemap.xml` |
| Palabras por página (mediana, sin nav/footer) | ~400 (mín. 85 en `contact.html`) | [COMPROBADO] script on-page |
| Keywords en el top 100 / top 10 | 16 / 0 | [DATO-SR] |
| Tráfico orgánico estimado | 0 | [DATO-SR] |
| Dominios referentes / Domain InLink Rank | 1 (del grupo) / 6 | [DATO-SR] |
| Cuota de voz en IA (ES, 5 motores) | 0 % | [DATO-SR] AI Search Leaderboard |
| Lighthouse móvil (Performance / SEO / Accesibilidad / Buenas prácticas) | 92–96 / 100 / 100 / 100 | [COMPROBADO] |
| LCP móvil (simulado) | 2,3–2,8 s | [COMPROBADO] |
| Analítica / Search Console verificable / Bing WMT | No / No (sin TXT ni meta) / No | [COMPROBADO] |
| Producción = repo | No (23/23 HTML difieren; `logo-white.webp` da 404 en vivo) | [COMPROBADO] |

### 3.2 Hallazgos comprobados

#### 3.2.1 Técnico

| ID | Hallazgo | Evidencia | Gravedad |
|---|---|---|---|
| H-T01 | Host duplicado: `https://www.facturales.es/` → **200** con el mismo contenido. `http://www` → 301 a `https://www` (no al apex) | `curl -s -o /dev/null -w "%{http_code} %{redirect_url}"` | P0 |
| H-T02 | `/index.html` → 200, y **19 páginas enlazan a `index.html`** (logo, migas, nav), ninguna a `/` | `grep -c 'href="index.html"'` | P0 |
| H-T03 | Archivos internos públicos: `/CLAUDE.md`, `/update_articles.py` (23 KB), `/fix_title_case.py`, `/remove_comments.py`, `/partials/header.njk`, `/package-lock.json`, `/assets/scss/`, `.map`, `service copy.html`. Riesgo extra: **cualquier `.md` del repo, incluido este plan, quedaría público** con el método de despliegue actual | `curl` → 200 | P0 |
| H-T04 | 404 servida por la página genérica de Plesk (inglés). `404.html` existe pero no se usa y tiene rutas relativas | `curl https://facturales.es/no-existe-xyz` | P1 |
| H-T05 | Sin HSTS en el apex, sin `Cache-Control` en ningún recurso, `content-type` sin charset | `curl -sI` | P1 |
| H-T06 | Cabecera y pie solo vía `document.write` síncrono: sin JS la home pasa de 86 a 26 enlaces, 0 enlaces legales, `about.html` inalcanzable | Playwright con JS on/off | P1 |
| H-T07 | CSS bloqueante: Google Fonts (~0,85 s), `main.css` 205 KB con ~90 % sin usar (~0,6 s) y un `@import` redundante de Fonts en `main.css:18`, `facturales-ds.css` (~0,46 s), `header-include.js` (~0,31 s) | Lighthouse | P1 |
| H-T08 | Móvil: la captura de escritorio oculta (`display:none`) se descarga con `fetchpriority=high`, y la móvil visible lleva `loading=lazy`. En `crea-envia-facturas` es el elemento LCP (131 KiB desperdiciados) | Lighthouse + `facturales-ds.css:745-749` | P1 |
| H-T09 | JSON-LD válido y coherente con el texto visible, pero sin `@id`, `WebSite` ni `BreadcrumbList`. `pricing.html` no declara precios. Ofertas sin IVA, periodo ni plan anual. `Article` sin `dateModified` y con autor Organization. Logo = SVG del rombo | Inventario de JSON-LD | P1 |
| H-T10 | Ningún `title` contiene «programa/software de facturación». 9 meta descriptions superan los 160 caracteres (hasta 198). Estilo inconsistente («Title Case» en los artículos) | Tabla on-page | P1 |
| H-T11 | Rutas relativas en todo el sitio y lógica de página activa con `split("/").pop()` en los *includes*: **se rompen con URLs de carpeta** | `header-include.js:6`, `footer-include.js:6` | Condiciona la migración |
| H-T12 | `news.html` y `news-details.html`: `noindex` + canonical a `news-grid.html` (señales contradictorias). Plantillas demo en vivo con 200 (`lang="en"`, «Brevon…») | HTML | P2 |
| H-T13 | `facturales.es/confirm-email` y `/reset-password` (listadas como redirect URLs de Supabase en `facturales/docs/APIS_Y_DEPENDENCIAS.md:32`) dan 404 | `curl` | P1 (si se usan) |
| H-T14 | Sin `favicon.ico`, `apple-touch-icon` ni `manifest`. `/llms.txt` → 404 | `curl` | P3 |
| H-T15 | `sitemap.xml` correcto (exactamente las 20 indexables), pero con `lastmod` en bloque | `sitemap.xml` | P2 |
| H-T16 | **App correcta para SEO:** `X-Robots-Tag: noindex, nofollow, noarchive` en todas las rutas (`vercel.json`). Sin riesgo de duplicado. Efecto colateral: **las páginas legales solo existen en la app, con noindex y como SPA vacía sin JS** | `curl -sI` app | P1 (E-E-A-T) |
| H-T17 | Lo que está bien: canonicals absolutos y autorreferentes, un `h1` por página, `lang="es"`, OG completo, todas las imágenes con `alt`, WebP con `srcset` y dimensiones, sin contenido mixto, gzip y brotli activos | — | — |

#### 3.2.2 Contenido y arquitectura

| ID | Hallazgo | Evidencia |
|---|---|---|
| H-C01 | No hay páginas para la intención comercial principal: autónomos, pymes, gestorías, VERI\*FACTU comercial, sectores, alternativas, herramientas ni plantillas | Inventario de URLs |
| H-C02 | Páginas débiles: `funciones` (269–280 palabras, solo títulos), `about` (146–156, sin personas ni empresa), `contact` (85–89), `gestiona-clientes` (269–278), `factura-personalizada` (264–276) | Recuento |
| H-C03 | El blog no enlaza a ninguna página de módulo, y los módulos no enlazan al blog. `pricing.html` solo tiene 2 enlaces internos en el cuerpo | Grafo de enlaces |
| H-C04 | Tres artículos de 360–610 palabras para queries muy competidas, autor «Equipo de Facturales», sin fuentes oficiales, sin `dateModified` y sin revisor | Artículos |
| H-C05 | Errores en los artículos: la factura electrónica B2B «depende del desarrollo reglamentario» (desactualizado); la «regla de los 4 NO» se atribuye a la AEAT sin fuente; la exclusión foral está simplificada; falta el RD-ley 15/2025, las sanciones y la declaración responsable; el artículo de contabilidad anuncia «6 números» y enumera 7 y no distingue los libros registro del autónomo de la contabilidad de una sociedad | §3.2.3 |
| H-C06 | Canibalización VERI\*FACTU: home (h3), `crea-envia-facturas` (title), guía y artículo comparativo (ambos con h2 «Qué es VERI\*FACTU») | Tabla on-page |
| H-C07 | El producto es más amplio que la web: series, IVA/IGIC/IPSI, retenciones, rectificativas, importación, recibidas, cierres, rol Gestor, 2FA, Facturae 3.2.2 (sin firmar) | `facturales/src` (ver §5.6) |
| H-C08 | Un solo texto de CTA en toda la web («Empieza gratis 14 días»). Los botones de plan no pasan el plan elegido. La tabla de precios no lista inventario, recurrentes, recordatorios, bancos, cobros ni gastos | HTML |

#### 3.2.3 Legal y fiscal (YMYL)

| ID | Afirmación (archivo:línea) | Problema | Gravedad |
|---|---|---|---|
| H-L01 | «¿Cumple con VERI\*FACTU? Cada factura emitida genera su registro… y lleva el código QR de cotejo» (`faq.html:28` JSON-LD y `:47`; `index.html:30` JSON-LD y `:240`) | Solo ocurre si se activa VERI\*FACTU; sin remisión el QR «de cotejo» no permite cotejar; la pregunta implica cumplimiento pleno, contradicho por la declaración sin firmar | **ALTA** |
| H-L02 | «Facturales emite facturas con su registro VERI\*FACTU y su QR» (bloque CTA de los 3 artículos: `verifactu-2027…:102`, `factura-electronica-vs-verifactu.html:76`, `contabilidad-negocio-7-pasos.html:94`) | Los mismos artículos explican que VERI\*FACTU implica remitir a la AEAT, así que el lector deduce que Facturales remite | **ALTA** |
| H-L03 | «Su efectividad depende del desarrollo reglamentario» (`factura-electronica-vs-verifactu.html:63`) | Desactualizado: RD 238/2026 y Orden HAC/1028/2026 ya publicados | **ALTA** |
| H-L04 | «listas para VERI\*FACTU» (`crea-envia-facturas.html:39`, H1) | Da a entender conformidad | MEDIA-ALTA |
| H-L05 | «Cumplimiento VERI\*FACTU», «Registro VERI\*FACTU», «Factura con VERI\*FACTU» (`about.html:43`, `pricing.html:85`, `index.html:7,15,62,110,143`, `crea-envia-facturas.html:7,59,82`, `impuestos.html:50`, `funciones.html:46`) | Igual que H-L04, y en la meta description es una afirmación comercial en el SERP | MEDIA |
| H-L06 | Guía VERI\*FACTU (`verifactu-2027…:72-78`) | Falta el anuncio del 05/10/2026 (oct-2028). El título «en 2027» quedará obsoleto. «Regla de los 4 NO» sin fuente. Faltan: Canarias, Ceuta y Melilla **sí** están obligadas; el SII está excluido; sanciones; declaración responsable; app gratuita de la AEAT | MEDIA |
| H-L07 | App (fuera de la landing): QR con la URL `ValidarQR` de la modalidad VERI\*FACTU y leyenda «Factura verificable…» sin remisión (`facturales/src/domain/rules/fiscal/verifactu-qr.ts:18-21`, `VistaPreviaFacturaVg.tsx:200`, `InvoicePreviewPage.tsx:204`) | Contrario a la Orden HAC/1177/2024 y a la FAQ de la AEAT | **ALTA (producto)** |
| H-L08 | `facturales/docs/declaracion-responsable-fabricante.md`: borrador «NO FIRMAR TODAVÍA», modalidad VERI\*FACTU declarada | Plazo de los productores vencido el 29/07/2025 | **ALTA (empresa)** |
| H-L09 | `faq.html:50`: «Facturae 3.2.2, el formato que admite la Administración a través de FACe» | Correcto para B2G, pero un Facturae descargado **no** cumplirá por sí solo la obligación B2B del RD 238/2026 | BAJA |
| H-L10 | `impuestos.html:50`: modelo 130 | Faltan las excepciones: módulos (131) y profesionales con ≥ 70 % de ingresos con retención | BAJA |
| H-L11 | Política de cookies de la app (`LegalContent.tsx:459-500`) | Plantilla genérica: declara cookies analíticas y publicitarias que no existen, sin tabla ni panel de retirada. No cumple la Guía de la AEPD (2023) | MEDIA |
| H-L12 | Aviso legal (`LegalContent.tsx`) | Prohíbe los enlaces profundos; errata «app.factuales.es»; fuero en Madrid con domicilio en Valladolid; «TS FACTURALES» en la cláusula 12 | MEDIA |
| H-L13 | **Correcto, mantener:** «Facturales no presenta los modelos; calcula las cifras para que tú o tu gestoría los presentéis» (`impuestos.html:63`, `faq.html:59`); regímenes IVA/IGIC/IPSI; «hasta −25 %» (descuento real 23,3–25,1 %); precios iguales a `plans-config.service.ts` | — | — |

#### 3.2.4 Autoridad y GEO

| ID | Hallazgo | Evidencia |
|---|---|---|
| H-A01 | 1 dominio referente (avenuemedia.io, del grupo, anchor «Visitar»). Competidores: Holded 5.567 (DIR 82), Quipu 3.271 (74), Billin 2.462 (71), Anfix 2.258 (69), Contasimple 1.861 (73) | [DATO-SR] |
| H-A02 | **1.374 dominios** enlazan a ≥ 2 competidores y no a Facturales. Entre los alcanzables: emprendedores.es, cepymenews.es, autonomosyemprendedor.es, pymesyautonomos.com, elreferente.es, infoautonomos.com, castillayleoneconomica.es, portales TIC Negocios de las Cámaras, UPTA, CEAT, CEA, softwaredoit.es, comparasoft.es, startupxplore.com, App Store | [DATO-SR] link gap |
| H-A03 | Los activos que más enlaces captan en el sector son **plantillas** (presupuesto de Holded: 220 dominios; de Quipu: 214) y **glosarios** (una sola entrada del glosario de Billin: 323 dominios) | [DATO-SR] |
| H-A04 | Los LLM citan sobre todo **blogs de fabricantes** (Holded, Quipu, Billin, STEL, Factorial) y **comparativas pequeñas** (softwaredoit, cronomia, banktrack, revolucionatupyme, softwarepara, conavalsi, getrenn, factupro). No aparecen Xataka, Infoautónomos ni Capterra en los prompts revisados | [DATO-SR] respuestas guardadas |
| H-A05 | Facturales no aparece en **ninguna** de las ~25 comparativas «mejores programas de facturación 2026» que existen | Búsqueda web |
| H-A06 | Holded usa su condición de **colaborador social de la AEAT** como argumento citable en VERI\*FACTU | Respuestas de AI Overviews |
| H-A07 | `Organization` sin `sameAs`, `legalName`, `address` ni `vatID`. Sin perfiles sociales. No se han encontrado fichas en Capterra, G2, GetApp, Trustpilot, LinkedIn, Crunchbase, Wikidata, App Store ni Google Play [HIPÓTESIS para las tiendas: confirmar a mano] | Repo + búsqueda |
| H-A08 | Ni la landing ni la web muestran quién está detrás (razón social, NIF, domicilio): solo aparece en las páginas legales de la app, invisibles sin JS | `LegalContent.tsx`; `curl` |

#### 3.2.5 Medición y CRO

| ID | Hallazgo | Evidencia |
|---|---|---|
| H-M01 | 0 herramientas de analítica en la landing y en la app. La CSP de la app (`vercel.json:8-12`) bloquea los dominios de Google | `grep` |
| H-M02 | Sin TXT `google-site-verification` en el DNS ni meta en el HTML. [HIPÓTESIS] GSC podría estar verificado por archivo | DNS |
| H-M03 | El registro (`auth.service.ts:99-104`, `acceso.ts:99-107`) solo guarda nombre y apellidos: ni UTM, ni referrer, ni página de entrada. Pero `signUp()` ya acepta `metadata`, así que el cambio es pequeño | Código |
| H-M04 | Recorrido: signup → verificar email → completar perfil → `/planes` → Stripe Checkout (`trial_period_days: 14`, `create-checkout-session/app.ts:85-103`) → app. [HIPÓTESIS] El Checkout pide método de pago y la web no lo dice | Código |
| H-M05 | Las estadísticas por plan (activos, en prueba, cancelados, MRR) ya existen en el panel de administración (`plans-config.service.ts:155-185`) | Código |

### 3.3 Hipótesis a validar (semana 0)

| ID | Hipótesis | Cómo validarla | Responsable |
|---|---|---|---|
| HX01 | Apache procesa `.htaccess` detrás de nginx (Plesk) | Subir un `.htaccess` con `Header set X-Htaccess-Test "1"` y `curl -sI https://facturales.es/ \| grep -i x-htaccess`. Si no aparece, usar «Directivas adicionales de nginx» en Plesk | Dev |
| HX02 | Google tiene indexadas URLs no deseadas (www, `index.html`, `.py`, `CLAUDE.md`, plantillas demo, `conectado-a-gestor.html`) | GSC → Indexación y `site:facturales.es` | SEO |
| HX03 | El Checkout exige tarjeta y cobra el día 15 | Prueba en modo test de Stripe | Producto (B6) |
| HX04 | Los recordatorios automáticos y las recurrentes están en producción para todos | Comprobar flags y migraciones aplicadas en Supabase | Producto (B7) |
| HX05 | El rol Gestor no ocupa plaza y el límite de usuarios no se aplica en el backend | `billing-limits.service.ts` + prueba | Producto (B7) |
| HX06 | Los volúmenes «cabeza» anómalos de SE Ranking (p. ej. «conciliacion bancaria» = 10) están infraestimados | GSC tras 4–8 semanas + Keyword Planner | SEO |
| HX07 | Existen apps publicadas en App Store / Google Play | Búsqueda manual en las tiendas | Producto (B8) |
| HX08 | El tráfico con IA (chatgpt.com, perplexity.ai) empezará a aparecer cuando la navegación sea HTML estático y Bing indexe el sitio | Segmento de referrers + Bing WMT | SEO |

### 3.4 Matriz de riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Reclamación o sanción por comunicar un cumplimiento VERI\*FACTU inexistente | Media | Muy alto | B1 + T2.01 en la semana 1; revisión legal; checklist de claims |
| Publicar contenido fiscal erróneo o desactualizado (YMYL) | Alta sin protocolo | Alto | Protocolo editorial §6.5, revisor con nombre, alertas del BOE, SLA de 72 h |
| Romper recursos o enlaces en la migración de URLs (rutas relativas) | Media | Medio | Rutas absolutas primero (T2.08), validación con crawler y script de 301 (§13) |
| Exponer documentos internos (este plan incluido) en producción | Alta con el despliegue actual | Medio-alto | T2.03 + T2.05 (lista blanca) **antes del próximo despliegue** |
| Que se apruebe el aplazamiento a 2028 y baje la urgencia de búsqueda de «verifactu» en 2027 | Media-alta | Medio | Calendario con dos escenarios (§6.2); diversificar en factura electrónica, impuestos, cobros e inventario |
| Comparativas con datos de competidores erróneos (publicidad comparativa) | Media | Medio | Reglas §6.4: fuente y fecha por dato, «No verificado», revisión jurídica, canal de corrección |
| Contenido masivo o de baja calidad que dañe el sitio (actualización de contenido útil de Google) | Baja si se sigue el plan | Alto | Ritmo de 4–8 piezas al mes, cada una con un valor diferencial (§6.1) |
| Pérdida de datos de medición por rechazo de cookies | Alta | Medio | Analítica sin cookies + atribución propia en Supabase (B3) |

### 3.5 Competencia: qué hacen y dónde se les puede ganar

| Competidor | Tráfico orgánico est./mes · keywords [DATO-SR] | Dominios referentes | Qué les trae tráfico | Debilidad aprovechable |
|---|---|---|---|---|
| Holded (Visma) | 60,6 k · 150 k | 5.567 | Home (marca 28 %), blog de trámites, listicles «mejores programas» (#1 en «software de facturación»), generador de facturas, plantillas, calculadoras, `/es/autonomos` | Producto caro y complejo para el autónomo pequeño; casi no trabaja sectores |
| Quipu (TeamSystem) | 31 k · 126 k | 3.271 | Calculadora IVA, 45 plantillas, guías de modelos AEAT casilla a casilla, generador de facturas (#1), listicles VERI\*FACTU (#1 en «programa facturación verifactu») | Cambio de marca (TeamSystem Quipu): oportunidad en «quipu precios / opiniones / alternativa» |
| Billin / TS Facturas | 29 k · 148 k | 2.462 | Calculadoras, glosario masivo, generadores, landings de función (`/control-de-stock/`, `/programa-verifactu/`) | Cambio de marca a «TS Facturas»: confusión de marca aprovechable con páginas de alternativa |
| Anfix | 27,5 k · 99 k | 2.258 | Calculadoras (IVA = 10 % de su tráfico), diccionario, `/autonomos` | Poco contenido de sector y de comparativa |
| Contasimple (Cegid) | 21,6 k · 44 k | 1.861 | Home, calculadora IVA+IRPF (14 %), `/programa-facturacion-autonomos-gratis/`, silos temáticos ordenados | Dependencia de un acuerdo con Infoautónomos; «contasimple precios» KD 0 |
| getrenn.com (nuevo) | 1,8 k · 4 k | — | Blog transaccional: cómo hacer una factura, Excel, programa gratis, **#1 en «alternativa a holded»** | Demuestra que un dominio nuevo entra por el long tail comparativo |

**Dónde puede ganar Facturales a corto y medio plazo** (ESTIMACIÓN basada en los datos):
1. **Intención de cambio de proveedor** (alternativas y precios de competidores): ~2.900 búsquedas/mes, KD 0–33, SERPs con micro-SaaS.
2. **VERI\*FACTU comercial y estado normativo**: ~2.700 búsquedas/mes BOFU + un cambio normativo reciente que nadie ha actualizado bien. Condicionado a B1.
3. **Módulos con SERP débil** (stock, cobros, conciliación, panel, clientes, gastos): ~2.300/mes con KD < 10.
4. **Segmentos** (autónomos ~1.600/mes; gestorías, CPC 4–6 €), donde ganan landings de segmento y Facturales no tiene ninguna.
5. **Sectores** con encaje real (reformas, instaladores, comercio, consultores, academias, fisioterapia, talleres): long tail BOFU con CPC 2–5 € que los grandes no cubren.
6. **Activos gratuitos** (generador ~4.500/mes, plantillas ~4.000, guías fiscales de long tail ~4.500): tráfico + enlaces + captación de la intención «gratis».

**Dónde NO competir (de momento):** marcas de competidores como navegacional, «calcular iva» (22.400, KD 86), «modelo 303» (20.100, KD 95), «verifactu» cabeza (12.100, KD 86), «facturae», TicketBAI, TPV, nóminas, banca conectada, ERP.

---

## 4. FASE 2 — Fundamentos técnicos

> **Calendario:** semanas 1–4 (19/10 → 15/11/2026). **Objetivo:** un sitio rastreable sin JS, un solo host, sin archivos expuestos, rápido, medible, con copy legal saneado y listo para crecer en URLs limpias.
> **Principio:** nada de esto cambia la identidad visual. Los cambios de CSS (retirar `main.css`) se validan visualmente con `premium-ui-reviewer` y capturas antes/después.

### 4.1 Bloque A — Higiene urgente (semana 1)

#### T2.01 · Saneamiento del copy VERI\*FACTU ⛔ (B1) · P0 · M · Riesgo B
- **Archivos:** `index.html` (meta l.7, OG l.15, JSON-LD l.30, l.62, l.110, l.143, l.240), `faq.html` (JSON-LD l.28, l.47, l.50), `crea-envia-facturas.html` (l.7, l.39, l.59, l.82), `pricing.html:85`, `funciones.html:46`, `impuestos.html:50`, `about.html:43`, los bloques CTA de los 3 artículos y la FAQ de `CLAUDE.md`.
- **Texto propuesto** (validar con legal antes de aplicarlo; ajustar según la opción elegida en B1):
  - Pregunta: «¿Está Facturales preparado para VERI\*FACTU?»
  - Respuesta: «Sí, nos estamos preparando. Con VERI\*FACTU activado en Ajustes, Facturales genera al emitir cada factura su registro de facturación con huella encadenada y su código QR. Estamos completando la remisión de registros a la AEAT antes de que la obligación sea exigible: hoy, antes del 1/1/2027 para sociedades y del 1/7/2027 para el resto. Hacienda ha anunciado su aplazamiento a octubre de 2028, todavía sin publicar en el BOE.»
  - Sustituir «listas para VERI\*FACTU» → «preparadas para VERI\*FACTU»; «Cumplimiento VERI\*FACTU» → «Registro de facturación con huella y QR (VERI\*FACTU en preparación)»; en la meta de la home, «Factura con VERI\*FACTU» → «Facturación preparada para VERI\*FACTU».
  - Cuando la remisión funcione en producción y la declaración responsable esté firmada, volver a la redacción afirmativa y enlazar la declaración (T5.04).
- **Aceptación:** `grep -rniE "cumple con veri|listas para veri|cumplimiento veri|con su registro veri" *.html assets/js` = 0 coincidencias; el JSON-LD `FAQPage` coincide con el texto visible; legal ha dado el visto bueno por escrito.
- **Validación:** script de coherencia FAQ/JSON-LD (§13.4) y `grep` anterior.
- **Fuera de la landing (repo `facturales`, decisión B1):** no imprimir la leyenda «Factura verificable…» ni la URL `ValidarQR` en facturas reales mientras `estado_envio` no pueda llegar a «aceptado» (`src/domain/rules/fiscal/verifactu-qr.ts`, `VistaPreviaFacturaVg.tsx:200`, `InvoicePreviewPage.tsx:204`).

#### T2.02 · Host único y `/index.html` → `/` · P0 · S · Riesgo B · depende de B2/HX01
- **Servidor:** en Plesk, «Redirección SEO preferente 301» → *non-www*, o `.htaccess` (bloque completo en T2.04).
- **Repo:** `href="index.html"` → `href="/"` en las 20 páginas (migas), `assets/js/header-include.js` (logo y nav) y `assets/js/footer-include.js`. Ajustar la lógica de página activa para que `pathname === "/"` marque la home.
- **Aceptación:** `http://www.`, `https://www.` y `http://` redirigen con **un solo 301** a `https://facturales.es/…` conservando ruta y query; `/index.html` → 301 a `/`; `grep -c 'href="index.html"'` = 0 en las páginas reales.
- **Validación:** §13.1.

#### T2.03 · Retirar del servidor los archivos internos · P0 · S · Riesgo B
- **Borrar de producción:** `CLAUDE.md`, `*.py`, `package-lock.json`, `partials/`, `assets/scss/`, `assets/css/*.map`, `service copy.html`, `service-details copy.html`, `docs/`, cualquier `*.md`.
- **Repo:** mover los scripts Python sueltos (`fix_*.py`, `update_*.py`, `remove_comments.py`, `verify_title_case.py`) a `tools/legacy/` o eliminarlos si ya no se usan (confirmar con el propietario); eliminar `service copy.html` y `service-details copy.html`.
- **Defensa en profundidad** (`.htaccess`, ver T2.04): denegar `\.(py|md|njk|map|scss|lock|mjs)$`, `package(-lock)?\.json`, `/partials/`, `/docs/`, `/tools/`, `/scripts/`.
- **Aceptación:** todas las rutas de la lista devuelven 403/404/410.
- **Validación:** §13.2.

#### T2.04 · `.htaccess` (o directivas nginx) de base · P0 · S · Riesgo M (probar antes en staging) · depende de HX01
Archivo nuevo `/.htaccess` en el repo (se despliega). Contenido de partida (la sección de migración de URLs se añade en T3.03):

```apache
# ---- Facturales · .htaccess (gestionado en el repo) ----
AddDefaultCharset UTF-8
Options -Indexes
ErrorDocument 404 /404.html

RewriteEngine On

# 1) Un solo host y HTTPS, en un salto
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} ^www\. [NC]
RewriteRule ^(.*)$ https://facturales.es/$1 [R=301,L,NE]

# 2) /index.html -> /
RewriteCond %{THE_REQUEST} \s/index\.html[\s?] [NC]
RewriteRule ^index\.html$ / [R=301,L]

# 3) Rutas huérfanas conocidas
Redirect 301 /conectado-a-gestor.html https://facturales.es/funciones.html
Redirect 301 /news.html https://facturales.es/news-grid.html
Redirect 301 /news-details.html https://facturales.es/news-grid.html
# Solo si Supabase Auth las usa (verificar Site URL y plantillas de correo):
Redirect 301 /confirm-email https://app.facturales.es/confirm-email
Redirect 301 /reset-password https://app.facturales.es/reset-password

# 4) Plantillas demo: 410 Gone (confirmar antes en GSC que no reciben tráfico)
RedirectMatch gone ^/(index-[234]|team(-details)?|project(-details)?|service(-details)?)\.html$

# 5) Nada interno es público
<FilesMatch "\.(py|md|njk|map|scss|lock|mjs|sh)$|^package(-lock)?\.json$">
  Require all denied
</FilesMatch>
RedirectMatch 404 ^/(partials|docs|tools|scripts)(/|$)

# 6) Cabeceras
<IfModule mod_headers.c>
  Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  <FilesMatch "\.(css|js|woff2)$">
    Header set Cache-Control "public, max-age=31536000, immutable"
  </FilesMatch>
  <FilesMatch "\.(webp|png|svg|ico|jpg)$">
    Header set Cache-Control "public, max-age=604800"
  </FilesMatch>
  <FilesMatch "\.(html|xml|txt)$">
    Header set Cache-Control "no-cache"
  </FilesMatch>
</IfModule>
```

- **Requisito:** cada cambio de CSS/JS debe cambiar `?v=` (ya se hace con `?v=20261018`). Las imágenes no llevan versión, por eso tienen 7 días y no `immutable`.
- **HSTS:** sin `preload` hasta pasar 3 meses sin incidencias. `includeSubDomains` es compatible con `app.` (que ya envía HSTS).
- **Si `.htaccess` no se procesa (HX01):** trasladar las mismas reglas a «Directivas adicionales de nginx» en Plesk (`return 301`, `error_page 404 /404.html;`, `location ~ \.(py|md)$ { deny all; }`, `add_header`).
- **Aceptación y validación:** §13.1–§13.3.

#### T2.05 · Despliegue reproducible con lista blanca ⛔ (B2) · P0 · M · Riesgo B
- **Archivo nuevo:** `.github/workflows/deploy.yml`. Se dispara al hacer push en `main`: ejecuta `node scripts/build-check.mjs` (T2.07) y después `rsync` por SSH/SFTP **solo** de: `*.html`, `.htaccess`, `robots.txt`, `sitemap.xml`, `llms.txt`, `llms-full.txt`, `<clave-indexnow>.txt`, `favicon.ico`, `site.webmanifest` y `assets/{css,js,img,fonts,descargas}/**`. Excluye explícitamente `assets/scss`, `*.map` y `assets/js` de la plantilla que no se use.
- **Secretos:** `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_KEY`, `DEPLOY_PATH` en GitHub Secrets (los configura el propietario).
- **Paso posterior:** envío de IndexNow con las URLs cambiadas (T6.02).
- **Aceptación:** tras un push, producción coincide byte a byte con el repo en los archivos de la lista blanca (§13.5) y ningún archivo fuera de la lista llega al servidor.
- **Primer despliegue:** sube el estado actual del repo (hoy producción va por detrás).

### 4.2 Bloque B — Rastreo sin JS y arquitectura preparada (semanas 2–3)

#### T2.06 · Cabecera y pie en HTML estático (fuente única + sincronización) · P1 · M · Riesgo M
- **Diseño:**
  1. Extraer el HTML que hoy generan `header-include.js` y `footer-include.js` a `partials/header.html` y `partials/footer.html` (sustituyen a `partials/header.njk`).
  2. Cada página lleva marcadores: `<!-- fx:header -->…<!-- /fx:header -->` y `<!-- fx:footer -->…<!-- /fx:footer -->`.
  3. Nuevo `scripts/sync-partials.mjs` (Node ≥ 18, sin dependencias) que reescribe el contenido entre marcadores en **todos** los `.html` reales. Se ejecuta localmente antes de cada commit y en CI en modo `--check`, que falla si algún HTML está desincronizado. **Los HTML siguen siendo archivos servidos directamente**, así que se respeta la arquitectura de `CLAUDE.md`.
  4. La lógica de comportamiento (página activa, menú Producto, menú móvil con *focus trap*) pasa a `assets/js/facturales.js` (con `defer`), comparando `location.pathname`. Para no depender de JS, el script de sincronización puede escribir también `aria-current="page"` por página.
  5. Eliminar `document.write` y los `<script src="…-include.js">` síncronos.
- **Alternativa válida:** SSI de Apache/nginx (`<!--#include virtual="/partials/header.html" -->`). Se descarta como primera opción porque complica la previsualización local con `npx serve`.
- **Actualizar `CLAUDE.md`:** sección «Shared header/nav» → «edita `partials/*.html` y ejecuta `node scripts/sync-partials.mjs`».
- **Aceptación:** con JS desactivado, cada página tiene `<header>` con la navegación completa y `<footer>` con los enlaces legales; `about.html` es alcanzable desde la home; Lighthouse deja de listar los *includes* como bloqueantes; `premium-ui-reviewer` sin regresiones visuales (menú, móvil, Esc, foco).
- **Validación:** §13.6 (Playwright con JS on/off: enlaces sin JS ≈ con JS).

#### T2.07 · `scripts/build-check.mjs` (controles automáticos de calidad) · P1 · S · Riesgo B
Un solo script, sin dependencias, que en CI (y antes de desplegar) comprueba:
- `sync-partials --check` sin diferencias;
- un único `h1` por página indexable; `title` ≤ 65 caracteres; meta description entre 120 y 158; `lang="es"`;
- canonical absoluto, https, sin www e igual a la URL de publicación; `og:url` = canonical;
- JSON-LD parseable; preguntas de `FAQPage` presentes en el texto visible;
- todos los enlaces internos y recursos (`href`/`src`) resuelven a un archivo existente;
- todas las URLs del sitemap existen y son indexables, y ninguna página `noindex` está en el sitemap;
- **lista de claims prohibidos** (§6.6): «sin tarjeta», «30 %», «homologado», «certificado VERI\*FACTU», «envío automático a la AEAT», «presenta tus impuestos», «conexión bancaria» sin «Próximamente», testimonios…;
- `<img>` con `alt` y con `width`/`height`.

Genera además `sitemap.xml` con `lastmod` real por archivo (`git log -1 --format=%cs -- <archivo>`), sin `priority`.

#### T2.08 · Rutas absolutas desde la raíz · P1 · M · Riesgo M · prerrequisito de T3.03
- En todos los HTML, `partials/*`, `404.html` y CSS (`url(...)`): `assets/...` → `/assets/...`; `pricing.html` → `/pricing.html` (y, tras T3.03, a la URL nueva).
- **Aceptación:** `grep -rnE '(href|src)="(assets|[a-z0-9-]+\.html)' --include=*.html .` = 0 en las páginas reales; la página se ve igual servida desde una subcarpeta.

#### T2.09 · 404 propia · P1 · S · Riesgo B
- `404.html` con rutas absolutas, sin canonical, con `noindex`, enlaces a home, funciones, precios, blog y buscador de ayuda (FAQ). Activada con `ErrorDocument 404 /404.html`.
- **Aceptación:** `curl -s -o /dev/null -w "%{http_code}" https://facturales.es/no-existe` = 404 y el cuerpo contiene el texto propio.

### 4.3 Bloque C — Rendimiento (semanas 2–4)

#### T2.10 · Retirar `main.css` de las páginas reales · P1 · M · Riesgo M
- Extraer a `assets/css/fx-rombo.css` solo las reglas del cubo del hero (`.cubes-wrapper`, `.cube*`, `.shadow-*`, `.large-shadow*`, `@keyframes cube-spin`, `cube-float` y dependencias; `main.css` hacia las líneas ~4519 y ~8394) y cargarlo **solo en la home**. Mantener `prefers-reduced-motion`.
- Eliminar `<link … main.css>` del resto de páginas reales. `main.css` queda solo para las plantillas demo (que se retiran en T2.04).
- Si no se puede retirar en este bloque, como mínimo eliminar el `@import` de Google Fonts de `main.css:18`.
- **Aceptación:** capturas antes/después idénticas en 390 px y 1440 px de home, precios, un módulo y un artículo (revisión `premium-ui-reviewer`); Lighthouse sin `main.css` en «render-blocking».
- **Nota para `CLAUDE.md`:** actualizar la frase «`main.css`… keep it loaded» cuando se apruebe esta tarea.

#### T2.11 · Onest autoalojada · P1 · S · Riesgo B
- `assets/fonts/onest-var.woff2` (latín, variable 400–700), `@font-face` con `font-display: swap` en `facturales-ds.css` y `<link rel="preload" as="font" type="font/woff2" crossorigin href="/assets/fonts/onest-var.woff2">` en el `<head>`. Retirar los `preconnect` y el CSS de `fonts.googleapis.com`.
- **Beneficio extra:** elimina la transferencia de IP a Google (argumento RGPD, coherente con «datos en la UE»).

#### T2.12 · Imagen del hero adaptable (LCP móvil) · P1 · S · Riesgo B
- Sustituir el par `<img class="fx-solo-ancho">` + `<img class="fx-solo-estrecho">` de `.fx-adaptable` por `<picture>` con `<source media="(max-width: 699px)" srcset="…movil-400.webp 400w, …movil-780.webp 780w" sizes="272px">` y el `<img>` de escritorio como respaldo, con `fetchpriority="high"` y sin `lazy` en la imagen del primer pantallazo. Si el marco de teléfono exige marcado distinto: escritorio `loading="lazy"` sin `fetchpriority` y móvil `loading="eager" fetchpriority="high"`.
- Afecta a la home y a todas las páginas de módulo con `fx-adaptable`.
- **Aceptación:** en móvil, `crea-envia-facturas` no descarga `facturas-emitidas-1280.webp`; LCP ≤ 1,8 s.

#### T2.13 · Objetivo de rendimiento · P1
- **Aceptación global** (Lighthouse móvil, producción): Performance ≥ 97, LCP ≤ 1,8 s, CLS < 0,05, TBT < 50 ms en home, precios, un módulo y un artículo. En el campo (CrUX/GSC, cuando haya datos): ≥ 90 % de URLs «buenas» en LCP, INP y CLS.
- **Validación:** §13.7.

### 4.4 Bloque D — Datos estructurados y metadatos (semanas 2–4)

#### T2.14 · Grafo JSON-LD con `@id` en todas las páginas · P1 · M · Riesgo B · depende de B5
Un único `<script type="application/ld+json">` con `@graph` por página. Las entidades comunes se repiten con el **mismo `@id`**:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization", "@id": "https://facturales.es/#organization",
      "name": "Facturales", "legalName": "AVENUE DIGITAL GROUP, S.L.",
      "vatID": "ESB70829601", "url": "https://facturales.es/",
      "logo": {"@type": "ImageObject", "@id": "https://facturales.es/#logo",
               "url": "https://facturales.es/assets/img/logo/facturales-logo-512.png", "width": 512, "height": 512},
      "email": "info@facturales.es",
      "address": {"@type": "PostalAddress", "streetAddress": "Plaza Mayor 23, 1A", "postalCode": "47001",
                  "addressLocality": "Valladolid", "addressRegion": "Castilla y León", "addressCountry": "ES"},
      "contactPoint": [{"@type": "ContactPoint", "contactType": "customer support",
                        "email": "soporte@facturales.es", "availableLanguage": "es"}],
      "areaServed": "ES",
      "sameAs": []
    },
    {
      "@type": "WebSite", "@id": "https://facturales.es/#website", "url": "https://facturales.es/",
      "name": "Facturales", "inLanguage": "es-ES", "publisher": {"@id": "https://facturales.es/#organization"}
    },
    {
      "@type": "SoftwareApplication", "@id": "https://facturales.es/#software", "name": "Facturales",
      "applicationCategory": "BusinessApplication", "applicationSubCategory": "Software de facturación",
      "operatingSystem": "Web, iOS, Android", "url": "https://facturales.es/",
      "publisher": {"@id": "https://facturales.es/#organization"},
      "featureList": ["Facturas y presupuestos", "Facturas recurrentes", "Inventario y control de stock",
                      "Recordatorios de cobro automáticos", "Conciliación bancaria por extractos",
                      "Gastos con justificantes y OCR", "Cálculo de los modelos 303 y 130", "Descarga en Facturae"],
      "offers": [
        {"@type": "Offer", "name": "Starter (pago mensual)", "price": "6.45", "priceCurrency": "EUR",
         "priceSpecification": {"@type": "UnitPriceSpecification", "price": "6.45", "priceCurrency": "EUR",
                                "unitCode": "MON", "valueAddedTaxIncluded": false},
         "url": "https://facturales.es/precios/", "availability": "https://schema.org/InStock"}
      ]
    }
  ]
}
```

- **Ofertas:** las 6 combinaciones (Starter 6,45/4,95; Pro 11,95/8,95; Ilimitado 23,95/17,95 €/mes + IVA). El precio anual se expresa por mes con `billingDuration` o en el nombre («pago anual»). **Fuente única:** `facturales/src/services/plans/plans-config.service.ts`.
- **`sameAs`:** solo perfiles que existan (B8, T5.10). **Nunca** `aggregateRating` sin reseñas reales en la propia página.
- **Por página:** `WebPage` (o `CollectionPage`, `AboutPage`, `ContactPage`, `FAQPage`) con `isPartOf` → `#website`, `about` → `#software` y `breadcrumb` → `BreadcrumbList` (coincide con las migas visibles).
- **Artículos y guías:** `BlogPosting`/`Article` con `author` **Person** (página de autor), `reviewedBy` (en `WebPage`), `datePublished`, `dateModified` (reflejado en visible), `image` propia, `citation` (BOE/AEAT) y `about`.
- **Glosario:** `DefinedTermSet` + `DefinedTerm`. **Precios:** el `SoftwareApplication` completo. **FAQ:** mantener `FAQPage` (Google ya no muestra el rich result salvo en webs gubernamentales o sanitarias, pero ayuda a Bing y a los LLM).
- **Logo:** crear `assets/img/logo/facturales-logo-512.png` (PNG cuadrado a partir del archivo oficial, fondo sólido; **no** reconstruir el logo como texto, regla de `CLAUDE.md`).
- **Aceptación:** Rich Results Test y validator.schema.org sin errores en home, precios, un módulo, un artículo y la FAQ; ningún `@id` huérfano.

#### T2.15 · Titles, meta descriptions y H1 · P1 · S · Riesgo B
Propuesta (validada con [DATO-SR]; ajustar el copy al tono de marca):

| Página (URL nueva) | Title (≤ 65) | H1 | Keyword principal |
|---|---|---|---|
| `/` | Programa de facturación para autónomos y pymes · Facturales | Facturas, bancos e impuestos de tu negocio, en un solo lugar. *(mantener; añadir H2 con la keyword)* | programa de facturación |
| `/precios/` | Precios del programa de facturación · desde 4,95 €/mes · Facturales | Un precio claro para cada etapa de tu negocio. | precio programa facturación |
| `/funciones/` | Funciones del programa de facturación · Facturales | *(mantener)* | funciones programa facturación |
| `/funciones/facturacion/` | Programa para hacer facturas con IVA, IRPF y series · Facturales | Facturas correctas a la primera, **preparadas** para VERI\*FACTU. | programa para hacer facturas |
| `/funciones/presupuestos/` | Programa para hacer presupuestos y pasarlos a factura · Facturales | Del presupuesto a la factura sin volver a escribir nada. | programa para hacer presupuestos |
| `/funciones/control-de-stock/` | Control de stock y gestión de inventario · Facturales | Control de stock e inventario, siempre al día. | control de stock |
| `/funciones/gestion-de-cobros/` | Gestión de cobros y facturas pendientes · Facturales | Gestión de cobros: cobra a tiempo sin perseguir a nadie. | gestion de cobros |
| `/funciones/conciliacion-bancaria/` | Conciliación bancaria con extractos Excel o CSV · Facturales | Concilia tu banco con tus facturas y gastos en minutos. | conciliación bancaria |
| `/funciones/gastos-y-tickets/` | Escanear tickets y facturas de gastos con OCR · Facturales | Cada gasto con su justificante, sin perseguir tickets. | escanear facturas / tickets |
| `/funciones/impuestos-303-130/` | Modelo 303 y 130 calculados desde tus facturas · Facturales | El trimestre, con los números ya hechos. | programa modelo 303 y 130 |
| `/funciones/panel-financiero/` | Panel de control financiero para tu negocio · Facturales | Tu control financiero, sin abrir una hoja de cálculo. | control financiero / dashboard financiero |
| `/funciones/gestion-de-clientes/` | Gestión de clientes con facturación (CRM sencillo) · Facturales | Gestión de clientes con todo lo que les has facturado. | gestion de clientes |
| `/funciones/diseno-de-factura/` | Factura personalizada con tu logo y tus colores · Facturales | *(mantener)* | factura personalizada |

- **Meta descriptions:** 120–158 caracteres, con beneficio + prueba de 14 días + un diferencial verificable. Sin claims prohibidos.
- **Artículos:** «Sentence case» en español y ≤ 60 caracteres.
- **Aceptación:** `build-check` en verde (longitudes) y revisión manual del SERP previsualizado.

#### T2.16 · Iconos y manifest · P3 · S
`/favicon.ico` (32×32), `/apple-touch-icon.png` (180×180) a partir del rombo oficial, `site.webmanifest` (`name`, `icons`, `theme_color` `#020100`) y su `<link>` en el `<head>` (vía `partials/head-common.html`, sincronizado igual que la cabecera).

### 4.5 Bloque E — Confianza y entidad en el dominio principal (semanas 3–4)

#### T2.17 · Páginas legales en HTML estático en `facturales.es` · P1 · M · Riesgo B · depende de B5 y B10
- Publicar `/legal/aviso-legal/`, `/legal/privacidad/`, `/legal/cookies/` y `/legal/condiciones/` (texto canónico, revisado por legal), enlazadas desde el pie estático. La app puede enlazar a estas versiones o mantener las suyas, pero **una sola versión canónica**.
- **Correcciones obligatorias:** eliminar la cláusula de enlaces profundos (B10) y sustituirla por «Se permite enlazar a cualquier página de este sitio siempre que no se induzca a error sobre la relación con Facturales»; corregir «app.factuales.es», «TS FACTURALES» y el fuero (Valladolid frente a Madrid, decisión legal).
- **Política de cookies real** (sustituye a la plantilla de `LegalContent.tsx:459-500`): tabla con nombre, titular, finalidad y duración (Supabase en localStorage, Stripe, Cloudflare Turnstile, `fx_ft` si se aprueba, GA4 si se activa, cookie de consentimiento), bases jurídicas y cómo retirar el consentimiento.
- **Aceptación:** `curl -s https://facturales.es/legal/aviso-legal/ | grep -c "B70829601"` ≥ 1 (sin JS); el pie de todas las páginas enlaza a las 4 páginas.

#### T2.18 · `about.html` → «Sobre Facturales» con quién está detrás · P1 · S · depende de B5
Equipo (nombres y fotos reales si se aprueba), empresa (razón social, NIF, domicilio, año), cómo se elabora y revisa el contenido fiscal (enlace a la política editorial), compromisos de datos (UE, 2FA, exportación) y contacto. Schema `AboutPage`. Mínimo 500 palabras útiles. **Sin cifras de clientes ni testimonios.**

---

## 5. FASE 3 — Arquitectura estratégica

> **Calendario:** semanas 3–8 (02/11 → 13/12/2026) para la migración y las páginas P1; la ampliación sigue en la Fase 4.
> **Principios:** (1) una intención = una URL, sin canibalizar; (2) URLs cortas en español, en minúsculas, sin año en el slug y sin `.html`; (3) hubs enlazados desde el HTML estático (cabecera, pie y cuerpo); (4) ninguna página sin valor diferencial; (5) ninguna promesa sin evidencia en la app (§5.6).

### 5.1 Estructura de URLs objetivo

Implementación en hosting estático **sin reescrituras internas**: una carpeta por página con `index.html` (`/precios/index.html` se sirve como `/precios/`; Apache redirige `/precios` → `/precios/` con `DirectorySlash`).

```
/                                         Home · «programa de facturación» (marca + suite financiera)
├── /precios/
├── /preguntas-frecuentes/
├── /autonomos/                           Segmento · «programa de facturación para autónomos»
├── /pymes/                               Segmento · «programa de facturación para pymes»
├── /gestorias/                           Segmento B2B · «software para gestorías» (rol Gestor)
├── /programa-verifactu/                  Comercial · «software / programa VERI*FACTU»  ⛔ B1
├── /funciones/                           Hub de funciones
│   ├── facturacion/                      «programa para hacer facturas»
│   ├── facturas-recurrentes/             «facturas recurrentes»                    (NUEVA)
│   ├── presupuestos/                     «programa para hacer presupuestos»
│   ├── control-de-stock/                 «control de stock», «gestión de inventario»
│   ├── gestion-de-cobros/                «gestión de cobros»
│   ├── recordatorios-de-pago/            «recordatorio de pago»                    (NUEVA)
│   ├── conciliacion-bancaria/            «conciliación bancaria» (extractos; banca directa «Próximamente»)
│   ├── gastos-y-tickets/                 «escanear facturas / tickets»
│   ├── impuestos-303-130/                «programa modelo 303 y 130»
│   ├── panel-financiero/                 «control financiero», «dashboard financiero»
│   ├── gestion-de-clientes/              «gestión de clientes», «crm facturación»
│   ├── diseno-de-factura/                «factura personalizada»
│   ├── equipo-y-gestoria/                roles y permisos                          (NUEVA)
│   └── seguridad/                        UE, 2FA, historial, exportación           (NUEVA)
├── /sectores/                            Hub
│   └── {reformas, instaladores, comercio, consultores, academias, fisioterapeutas,
│        psicologos, abogados, talleres, peluquerias, disenadores, mantenimiento}/
├── /alternativas/                        Hub + metodología de comparación
│   └── {holded, quipu, contasimple, billin, anfix, facturadirecta, stel-order, excel}/
├── /herramientas/                        Hub
│   └── {generador-de-facturas, generador-de-presupuestos, calculadora-iva-irpf,
│        calculadora-modelo-130, validador-nif, calculadora-intereses-demora}/
├── /plantillas/                          Hub
│   └── {factura, factura-autonomo, factura-proforma, factura-rectificativa, presupuesto,
│        presupuesto-obra, recibo, control-de-stock, control-de-gastos, recordatorio-de-pago,
│        conciliacion-bancaria-excel}/
├── /guias/                               Hub de guías evergreen
│   └── {verifactu, factura-electronica, como-hacer-una-factura, datos-obligatorios-factura,
│        tipos-de-factura, factura-recapitulativa, factura-rectificativa, factura-proforma,
│        factura-simplificada, numeracion-facturas, retencion-irpf-factura,
│        iva-soportado-repercutido, modelo-303, modelo-130, modelo-347, modelo-390,
│        conciliacion-bancaria, gastos-deducibles-autonomos, morosidad-reclamar-facturas,
│        control-de-stock, flujo-de-caja, facturar-sin-ser-autonomo}/
├── /calendario-fiscal/                   Evergreen (el año va en el title, no en la URL) + .ics
├── /blog/                                Índice (sustituye a news-grid.html) + /blog/{slug}/
├── /glosario/                            Hub A–Z + /glosario/{termino}/ (30–50 términos, sin canibalizar guías)
├── /facturales-en-datos/                 Ficha oficial «fuente de verdad» (GEO)
├── /declaracion-responsable-verifactu/   Declaración del productor por versión  ⛔ B1 (solo firmada)
├── /sobre-nosotros/  /contacto/  /prensa/  /politica-editorial/  /autores/{slug}/
└── /legal/{aviso-legal, privacidad, cookies, condiciones}/
```

**Reglas anticanibalización** (intención principal por URL):

| Intención | URL dueña | No debe competir |
|---|---|---|
| programa / software de facturación (genérico) | `/` | `/funciones/facturacion/` se centra en «programa para hacer facturas» y funciones concretas |
| programa de facturación para autónomos | `/autonomos/` | Home y guías enlazan a ella con ese anchor |
| software / programa VERI\*FACTU | `/programa-verifactu/` | `/guias/verifactu/` responde «qué es, a quién afecta, fechas»; el blog cubre el long tail («verifactu gratis», «excel») |
| factura electrónica obligatoria | `/guias/factura-electronica/` | El artículo comparativo pasa a «diferencias VERI\*FACTU vs factura electrónica» |
| mejores programas de facturación | `/blog/mejores-programas-facturacion/` | Las alternativas se centran en un competidor cada una |
| control de stock (producto) / qué es y cómo hacerlo | `/funciones/control-de-stock/` / `/guias/control-de-stock/` | Enlace cruzado «Entiende el método» ↔ «Hazlo con Facturales» |

### 5.2 Migración de las 20 URLs actuales (mapa 1:1)

#### T3.03 · Migración a URLs limpias · P1 · L · Riesgo M · depende de T2.04, T2.06, T2.08
| Actual | Nueva | Cambio de contenido asociado |
|---|---|---|
| `/` (`/index.html`) | `/` | Title y H2 con «programa de facturación» (T2.15) |
| `/pricing.html` | `/precios/` | T3.11 |
| `/funciones.html` | `/funciones/` | Ampliar a ~900 palabras (T3.10) |
| `/faq.html` | `/preguntas-frecuentes/` | Enlazar cada respuesta a su landing o guía |
| `/contact.html` | `/contacto/` | Datos de empresa, tiempos de respuesta por plan |
| `/about.html` | `/sobre-nosotros/` | T2.18 |
| `/crea-envia-facturas.html` | `/funciones/facturacion/` | Recurrentes pasan a su propia URL |
| `/crea-envia-presupuestos.html` | `/funciones/presupuestos/` | Ampliar a ~700 palabras |
| `/bancos-conciliacion.html` | `/funciones/conciliacion-bancaria/` | — |
| `/cobros.html` | `/funciones/gestion-de-cobros/` | Recordatorios pasan a su propia URL |
| `/escanea-gastos.html` | `/funciones/gastos-y-tickets/` | — |
| `/impuestos.html` | `/funciones/impuestos-303-130/` | Excepciones del 130 (H-L10) |
| `/tu-negocio-bajo-control.html` | `/funciones/panel-financiero/` | — |
| `/gestiona-clientes.html` | `/funciones/gestion-de-clientes/` | Ampliar (hoy 278 palabras) |
| `/gestiona-tu-stock.html` | `/funciones/control-de-stock/` | — |
| `/factura-personalizada.html` | `/funciones/diseno-de-factura/` | Enlazar a `/plantillas/factura/` |
| `/news-grid.html`, `/news.html`, `/news-details.html` | `/blog/` | Categorías por clúster y schema `Blog` |
| `/verifactu-2027-guia-autonomos-pymes.html` | `/guias/verifactu/` | Reescritura pilar (T4.01) |
| `/factura-electronica-vs-verifactu.html` | `/blog/verifactu-vs-factura-electronica/` | Actualizado (T4.02) |
| `/contabilidad-negocio-7-pasos.html` | `/blog/como-llevar-la-contabilidad-de-un-negocio/` | Corregido (T4.03) |
| `/conectado-a-gestor.html` (borrada) | `/funciones/equipo-y-gestoria/` | — |

**Bloque `.htaccess` que sustituye a las secciones 2–3 de T2.04** (sin cadenas: cada URL antigua va directa a la final; para `http://www.` habrá 2 saltos, aceptable):

```apache
RewriteRule ^index\.html$                              /                                              [R=301,L]
RewriteRule ^pricing\.html$                            /precios/                                      [R=301,L]
RewriteRule ^funciones\.html$                          /funciones/                                    [R=301,L]
RewriteRule ^faq\.html$                                /preguntas-frecuentes/                         [R=301,L]
RewriteRule ^contact\.html$                            /contacto/                                     [R=301,L]
RewriteRule ^about\.html$                              /sobre-nosotros/                               [R=301,L]
RewriteRule ^crea-envia-facturas\.html$                /funciones/facturacion/                        [R=301,L]
RewriteRule ^crea-envia-presupuestos\.html$            /funciones/presupuestos/                       [R=301,L]
RewriteRule ^bancos-conciliacion\.html$                /funciones/conciliacion-bancaria/              [R=301,L]
RewriteRule ^cobros\.html$                             /funciones/gestion-de-cobros/                  [R=301,L]
RewriteRule ^escanea-gastos\.html$                     /funciones/gastos-y-tickets/                   [R=301,L]
RewriteRule ^impuestos\.html$                          /funciones/impuestos-303-130/                  [R=301,L]
RewriteRule ^tu-negocio-bajo-control\.html$            /funciones/panel-financiero/                   [R=301,L]
RewriteRule ^gestiona-clientes\.html$                  /funciones/gestion-de-clientes/                [R=301,L]
RewriteRule ^gestiona-tu-stock\.html$                  /funciones/control-de-stock/                   [R=301,L]
RewriteRule ^factura-personalizada\.html$              /funciones/diseno-de-factura/                  [R=301,L]
RewriteRule ^(news-grid|news|news-details)\.html$      /blog/                                         [R=301,L]
RewriteRule ^verifactu-2027-guia-autonomos-pymes\.html$ /guias/verifactu/                             [R=301,L]
RewriteRule ^factura-electronica-vs-verifactu\.html$   /blog/verifactu-vs-factura-electronica/        [R=301,L]
RewriteRule ^contabilidad-negocio-7-pasos\.html$       /blog/como-llevar-la-contabilidad-de-un-negocio/ [R=301,L]
RewriteRule ^conectado-a-gestor\.html$                 /funciones/equipo-y-gestoria/                  [R=301,L]
```

**Procedimiento de corte:**
1. Crawl previo (lista de URLs y estado) y copia del sitemap anterior.
2. Mover cada archivo a `carpeta/index.html` con `git mv` (conserva el historial); actualizar canonical, `og:url`, JSON-LD (`@id`, migas), enlaces internos, `partials/*`, `sitemap.xml` (solo URLs nuevas) y `llms.txt`. En la app, actualizar los enlaces a la landing si los hay (`grep -rn "facturales.es/" facturales/src`).
3. Probar el `.htaccess` antes en staging, o con 302 durante una hora y luego 301 (los 301 se cachean en el navegador).
4. Desplegar, ejecutar §13.8 (mapa de 301) y §13.9 (todas las URLs del sitemap = 200).
5. GSC: enviar el sitemap nuevo, «Inspeccionar URL» de las 10 principales; **no** usar la herramienta de cambio de dirección (es el mismo dominio). Bing: sitemap + IndexNow.
6. Monitorizar Indexación y Rendimiento cada semana durante 8 semanas. **Mantener los 301 de por vida.**
- **Aceptación:** 0 enlaces internos a URLs antiguas; 0 cadenas de redirección desde el apex; 100 % de las URLs del sitemap con 200 y canonical autorreferente.

### 5.3 Universo de keywords por clúster (resumen accionable)

Datos completos (~330 keywords, 22 clústeres) en `docs/seo/auditoria-2026-10/02-keywords-competencia.md`. Volumen/KD/CPC = [DATO-SR]; destino y prioridad = [RECOMENDACIÓN].

| Clúster | Volumen aprox./mes | Keywords clave (vol/KD) | URL dueña | Intención | Prio |
|---|---|---|---|---|---|
| **VERI\*FACTU comercial** | ~2.700 | programa facturacion verifactu 480/20 · software verifactu 590/5 · programa de facturacion con verifactu 210/28 (CPC 4,38) · verifactu programa 170/35 · programa verifactu 150/37 | `/programa-verifactu/` ⛔ | BOFU | P1 |
| **VERI\*FACTU informativo** | >5.000 (cabeza 12.100, KD 86) | que es verifactu 810/36 · verifactu autonomos 480/28 · entrada en vigor verifactu 390/33 · verifactu es obligatorio 360/34 · quien esta obligado a verifactu 210/6 · verifactu se retrasa 260/9 · verifactu retraso 210/11 | `/guias/verifactu/` | TOFU | P0 |
| **VERI\*FACTU long tail** | ~1.800 | verifactu gratis 610/17 · programa verifactu gratis 320/20 · software verifactu gratis 260/21 · aplicacion verifactu aeat 320/36 · verifactu excel 170/17 · no verifactu 320/34 | `/blog/verifactu-gratis/`, `/blog/facturar-con-excel-verifactu/`, `/blog/verifactu-vs-no-verifactu/` | MOFU | P1 |
| **Genéricos BOFU** | ~3.500 | programa de facturacion 590/63 · programa para hacer facturas 480/59 · software de facturacion 320/70 · programa de facturacion online 70/45 (CPC 9,85) | `/` y `/funciones/facturacion/` | BOFU | P1 (largo plazo) |
| **Autónomos** | ~1.600 | programa facturación autonomos 320/33 · programas facturas autonomos 260/23 · programa de facturacion para autonomos 210/43 · facturacion autonomos 110/23 | `/autonomos/` | BOFU | P1 |
| **Pymes / gestorías** | ~600 | programa de facturacion para pymes 70/33 · software para gestorias 50/15 (CPC 5,83) · gestoria online 440/22 | `/pymes/`, `/gestorias/` | BOFU | P1–P2 |
| **Alternativas y precios** | ~2.900 | precios holded 480/33 · contasimple opiniones 390/16 · holded opiniones 260/25 · quipu precios 260/21 · billin precios 260/28 · contasimple precios 210/0 · stel order precios 210/13 · alternativa a holded 90/5 | `/alternativas/{x}/` | BOFU | P1 |
| **Mejores programas** | ~1.000 | mejor programa de facturación 210/32 · mejores programas de facturacion 170/37 · programa de facturacion gratis 210/7 | `/blog/mejores-programas-facturacion/`, `/blog/programas-de-facturacion-gratis/` | MOFU | P1 |
| **Generador** | ~4.500 | hacer factura online gratis 590/29 · creador facturas 590/24 · crear factura 590/33 · hacer factura online 390/6 · generador de facturas 210/39 · hacer presupuesto online 140/17 | `/herramientas/generador-de-facturas/` (+ presupuestos) | BOFU | P1 |
| **Plantillas** | ~4.000 | modelo de factura 910/39 · modelo factura autonomo 480/7 · plantilla factura autonomo 480/25 · plantilla factura gratis 480/35 · plantilla factura proforma 210/8 · plantilla presupuesto 590/53 · presupuesto de obra 320/10 | `/plantillas/{x}/` | TOFU/MOFU | P1 |
| **Tipos y requisitos de factura** | ~4.000 | como hacer una factura 810/21 · factura recapitulativa 590/8 · que es factura proforma 390/9 · como hacer una factura rectificativa 390/9 · factura de abono 390/8 · datos de facturacion 390/18 · tipos de facturas 320/16 · factura con irpf 390/12 · numeracion facturas 70/9 | `/guias/{x}/` | TOFU/MOFU | P1 |
| **IVA/IRPF y calculadoras** | ~4.000 (sin cabezas) | iva soportado 760/9 · iva repercutido 660/8 · iva deducible 660/9 · calculadora irpf autonomos 590/9 · quitar iva 480/11 · como calcular el iva de una factura 260/15 | `/herramientas/calculadora-iva-irpf/`, `/guias/iva-soportado-repercutido/`, `/guias/retencion-irpf-factura/` | TOFU | P1 |
| **Modelos AEAT y calendario** | ~4.500 (sin cabezas) | modelo 347 880/18 · calendario fiscal 2026 720/26 (→ 2027) · declaracion trimestral autonomos 390/16 · modelo 390 370/17 · plazo modelo 303 210/0 · plazo modelo 130 170/0 · como rellenar modelo 130 170/5 | `/guias/modelo-*/`, `/calendario-fiscal/` | TOFU/MOFU | P1 |
| **Módulos con SERP débil** | ~2.300 | control de stock 390/8 · gestion de stock 260/9 · gestion de inventario 260/23 · gestion de cobros 320/8 · gestion de clientes 260/8 · control financiero 260/7 · dashboard financiero 110/6 · escanear facturas 70/7 · que es conciliacion bancaria 480/8 | `/funciones/{x}/` + guías de apoyo | MOFU/BOFU | **P1 (quick win)** |
| **Recurrentes y recordatorios** | ~250 | facturas recurrentes 50/9 · factura recurrente 50/8 · facturación recurrente 50/7 · cobros recurrentes 10/8 (CPC 7,15) · recordatorio de pago 40/10 · reclamar factura impagada 90/8 | `/funciones/facturas-recurrentes/`, `/funciones/recordatorios-de-pago/` | BOFU | P1 |
| **Factura electrónica** | ~2.100 (cabeza 9.900, KD 90) | factura electronica obligatoria 720/42 · que es la factura electronica 590/36 · factura electronica autonomos 390/29 · factura electronica b2b 210/17 | `/guias/factura-electronica/` | TOFU | P1 |
| **Cobros y morosidad** | ~1.500 | ley de morosidad 590/17 · morosidad 590/33 · facturas impagadas 70/12 | `/guias/morosidad-reclamar-facturas/` | TOFU | P2 |
| **Gastos** | ~1.200 | gastos deducibles autonomos 320/21 · gastos deducibles 260/9 · control de gastos 390/46 | `/guias/gastos-deducibles-autonomos/` | TOFU | P2 |
| **Sectores** | ~1.500 | programa de reformas 170/18 · presupuesto reforma 320/19 · software para peluquerías 140/8 · software fisioterapia 110/10 · software para psicologos 70/22 · software para abogados 50/9 · programa taller mecanico 70/22 | `/sectores/{x}/` | BOFU | P2 |

**Descartados** (sin encaje de producto o inalcanzables por ahora): TPV/hostelería, TicketBAI, integraciones WooCommerce/PrestaShop/Odoo, nóminas, ERP, «verifactu api», «kit digital verifactu» (solo si Facturales se adhiere), «modelo 036», «calcular iva» (cabeza), marcas de competidores como navegacional.

### 5.4 Inventario de páginas nuevas priorizadas

Puntuación = intención de compra (1–5) × alcanzabilidad (1–5) × volumen del clúster (1–3), sobre 75. Esfuerzo incluye redacción, revisión y diseño.

| ID | URL | Keyword principal | Plantilla | Punt. | Prio | Esf. | Dependencias |
|---|---|---|---|---|---|---|---|
| T3.10 | `/funciones/` (ampliada) | funciones programa facturación | Hub | 36 | P1 | M | T3.03 |
| T3.11 | `/precios/` (mejorada) | precio programa facturación | Precios | 48 | P1 | S | B6 |
| T3.12 | `/programa-verifactu/` | programa facturación verifactu | T1 + bloque normativo | 60 | P1 | M | **⛔ B1**, T4.01 |
| T3.13 | `/autonomos/` | programa facturación autónomos | T-Segmento | 60 | P1 | M | T3.03 |
| T3.14 | `/funciones/facturas-recurrentes/` | facturas recurrentes | T1 | 45 | P1 | M | B7 |
| T3.15 | `/funciones/recordatorios-de-pago/` | recordatorio de pago | T1 | 40 | P1 | M | B7 |
| T3.16 | `/gestorias/` | software para gestorías | T-Segmento B2B | 40 | P1 | M | B7 |
| T3.17 | `/pymes/` | programa de facturación para pymes | T-Segmento | 36 | P2 | M | — |
| T3.18 | Reorientar 5 módulos (stock, cobros, panel, clientes, gastos) | ver T2.15 | T1 | 50 | **P1** | M | T2.15 |
| T3.19 | `/funciones/equipo-y-gestoria/`, `/funciones/seguridad/` | roles; software facturación seguro | T1 | 24 | P2 | S | B7 |
| T3.20 | `/facturales-en-datos/` | qué es Facturales (GEO) | Ficha | — | P1 | S | B5 |
| T3.21 | `/sectores/` + 12 sectores (por lotes de 2–3) | programa de facturación para [sector] | T2 | 30–40 | P2 | M c/u | B7 (exenciones IVA) |
| T3.22 | `/alternativas/` + 8 páginas | alternativa a [x] / precios [x] | T4 | 55 | P1 | M c/u | §6.4 |

### 5.5 Reglas de enlazado interno (hub & spoke en HTML)

1. **Spoke → hub:** enlace contextual en el primer tercio + caja «Guía completa» al final.
2. **Spoke → 2 hermanos** del mismo clúster y **→ 1 página comercial** (CTA contextual).
3. **Hub → todos sus spokes** (índice en HTML).
4. **Comercial ↔ guía:** la comercial enlaza a la guía como «Entiende la norma»; la guía, a la comercial como «Hazlo con Facturales».
5. **Transversales obligatorios:** todo contenido con fechas fiscales → `/calendario-fiscal/`; todo lo que habla de «factura» → generador y plantillas; la home → los 8 hubs (bloque «Recursos») y `/autonomos/`, `/pymes/`, `/gestorias/`.
6. **Pie estático:** Producto (funciones principales, precios), Para quién (autónomos, pymes, gestorías, sectores), Recursos (guías, plantillas, herramientas, calendario fiscal, blog, glosario), Comparar (alternativas), Empresa (sobre nosotros, prensa, política editorial, contacto), Legal.
7. **Anchors descriptivos** («programa de control de stock», no «aquí» ni «ver más»). Variar sin sobreoptimizar: como máximo ~30 % de anchors exactos por URL.
8. **Migas** visibles en todas las páginas salvo la home, con `BreadcrumbList`.
9. **Clúster VERI\*FACTU:** no se publica ningún spoke hasta que el hub (T4.01) esté revisado por legal.
- **Aceptación:** `build-check` verifica que cada página nueva recibe ≥ 3 enlaces internos estáticos y que ninguna indexable queda huérfana (§13.6).

### 5.6 Fuente de verdad del producto (qué se puede prometer)

Comprobado en `facturales/src` el 18/10/2026. **Cualquier página nueva se contrasta con esta tabla y con `CLAUDE.md`.**

| Función | Se puede comunicar | Límite o matiz obligatorio |
|---|---|---|
| Facturas (series, IVA/IGIC/IPSI, retenciones, rectificativas, importación, recibidas) | Sí | — |
| Facturas recurrentes (semanal → anual) | Sí | Se generan como **borrador**; el usuario las emite |
| Presupuestos y conversión a factura | Sí | — |
| Inventario (stock, mínimo, movimientos, valor, CSV, descuento al facturar y devolución al anular) | Sí | **Un solo almacén** |
| Cobros (pendientes, previsión, antigüedad, por cliente) | Sí, como «Nuevo» | Despliegue gradual, sin fechas |
| Recordatorios automáticos de cobro (email desde el servidor) | Sí | Confirmar que están en producción para todos (B7) |
| Bancos | Extractos Excel/CSV y conciliación | Conexión directa **«Próximamente»** (agregador regulado) |
| Gastos con OCR | Sí, como «Nuevo» | Límites OCR por plan: 10/75/300 al mes |
| Impuestos | **Cálculo** de 303 y 130 | **No presenta** ante la AEAT. 130: estimación directa |
| Cierres y rol Gestor | Sí | Solo lectura, contabiliza y cierra meses. Plaza de usuario: confirmar (B7) |
| Facturae 3.2.2 | «Descarga en Facturae» | **Sin firmar**; no cubre por sí sola la obligación B2B |
| VERI\*FACTU | Según B1 | Hoy: registro con huella + QR si se activa; **remisión pendiente**; declaración sin firmar |
| Seguridad | UE (Irlanda), 2FA, historial, exportar o eliminar cuenta | — |
| Planes | Starter 6,45/4,95 · Pro 11,95/8,95 · Ilimitado 23,95/17,95 €/mes + IVA | Límites: clientes 10/150/∞, productos 30/150/∞, facturas/mes 10/∞/∞, OCR 10/75/300 |
| Prueba | 14 días, sin permanencia | Comportamiento de la tarjeta: B6 |
| **No comunicar** | Nóminas (solo simula), banca conectada como disponible, DIAN, integraciones «soon» (Gmail, Outlook, Slack, HubSpot), plan gratuito, «sin tarjeta», «−30 %», testimonios, cifras de clientes, valoraciones | — |

### 5.7 Plantillas de página (wireframes sobre el design system `fx-*`)

Todas usan `body.fx`, cabecera y pie compartidos, Onest, iconos Lucide de 2 px, CTA en `--fx-acento` con texto `--fx-sobre-acento`, un único `h1`, `.fx-claro` solo para lectura larga y capturas reales con la etiqueta «Captura real … con datos de ejemplo». **No se crea ningún componente nuevo con `main.css`.**

- **T1 · Landing de función** (`/funciones/x/`): migas → hero (badge «Nuevo» si aplica, H1 con la keyword, beneficio, CTA «Empieza tu prueba de 14 días» + «Ver precios», microcopy de confianza, captura real) → problema y resultado (3 tarjetas) → «Así se ve en la app» (2–3 capturas) → qué puedes hacer (grid `fx-card`) → cómo funciona en 3 pasos → para quién (sectores y segmento) → límites por plan → FAQ (4–6, `FAQPage`) → «Aprende más» (guía del clúster) → «Funciona mejor junto a» → CTA final.
- **T-Segmento** (`/autonomos/`, `/pymes/`, `/gestorias/`): H1 «Programa de facturación para autónomos» → 3 tareas del segmento resueltas con funciones reales (con enlaces) → ejemplo numérico (factura con IRPF del 15 % / 7 %, 303 y 130 del trimestre) → plan recomendado → bloque fiscal revisado («información general») → FAQ → CTA. En `/gestorias/`: rol Gestor, cierres, exportación, cómo invitar a la gestoría, contacto B2B.
- **T2 · Sector** (`/sectores/x/`): H1 «Programa de facturación para [sector]» → 3 dolores del sector → cómo lo resuelve Facturales (3–4 funciones reales) → **ejemplo práctico con datos ficticios** marcados como ejemplo → fiscalidad del sector (caja revisada por el asesor: IVA, exenciones, IRPF) → plantilla descargable del sector → plan recomendado → FAQ → CTA. **Sin casos de cliente inventados.** Capturas con datos sintéticos del sector generadas con el flujo `capturas` del repo de la app.
- **T3/T4 · Alternativa** (`/alternativas/x/`): ver reglas §6.4.
- **T5 · Guía pilar** (`/guias/x/`): migas → H1 → cabecera E-E-A-T (autor con foto y bio, «Revisado por [nombre, n.º de colegiado]», «Publicado» / «Actualizado») → «En 30 segundos» (3–5 viñetas con fechas) → índice → secciones H2 en forma de pregunta, con tablas, ejemplos numéricos y cajas «Ojo» → tabla de estado normativo (si aplica) → CTA contextual aprobado → herramienta enlazada → FAQ → **fuentes oficiales con fecha de consulta** → spokes del clúster → CTA final + *lead magnet*.
- **T6 · Artículo** (`/blog/x/`): como T5 en 900–1.800 palabras, con 1 CTA contextual hacia una función y una caja «Guía completa».
- **T7 · Plantilla** (`/plantillas/x/`): H1 «Plantilla de [x] gratis en Excel, Word y PDF» → vista previa real + 3 botones de descarga **directa sin email** (email opcional para actualizaciones) → cómo rellenarla (campos obligatorios según el RD 1619/2012, revisado) → ejemplo rellenado → errores frecuentes → puente al producto («una plantilla no genera registro de facturación; si facturas con un programa, este debe cumplir el Reglamento de sistemas de facturación», texto revisado por legal) → FAQ → relacionadas. Archivos en `assets/descargas/` (versionados).
- **T8 · Herramienta** (`/herramientas/x/`): H1 + «Sin registrarte» → **herramienta en el primer pantallazo** (formulario accesible, objetivos de 44 px, errores en vivo) → resultado inmediato (desglose base/IVA/IRPF/total, copiar, PDF en el generador) → CTA tras obtener valor («Guarda este cliente y emite la siguiente en Facturales») → explicación de la fórmula y ejemplos → FAQ, fuentes y fecha de los tipos aplicados. JS vanilla sin dependencias; el PDF se genera en el navegador (sin subir datos: argumento de privacidad). Aviso: un PDF suelto no es un registro de facturación.

---

## 6. FASE 4 — Contenidos y autoridad

> **Calendario:** del mes 1 al 12 (noviembre de 2026 → octubre de 2027), en paralelo con las Fases 3, 5 y 6.
> **Ritmo:** 4–8 piezas al mes (nuevas o actualizaciones sustanciales). **Nunca contenido masivo**: cada pieza debe superar en algo concreto al top 10 actual.

### 6.1 Estándar de calidad de cada pieza (definición de «hecho»)

Una pieza solo se publica si cumple **todo**:
1. **Valor diferencial** respecto al top 10: un ejemplo numérico resuelto, una plantilla o herramienta, capturas reales, una tabla fechada con fuentes o un dato propio.
2. **Respuesta citable** a la pregunta principal en las primeras 40–60 palabras.
3. **Fuentes primarias** enlazadas (BOE consolidado, sede de la AEAT, Seguridad Social, EUR-Lex) con fecha de consulta.
4. **Autor con nombre** y, si es YMYL, **revisor colegiado** con nombre (B4), «Publicado» / «Actualizado» visibles y en el JSON-LD.
5. **Checklist de claims** superada (§6.6) y producto validado por quien conoce la app (la función existe en producción).
6. **Enlazado** según §5.5 y CTA contextual (no intrusivo).
7. `build-check` en verde y Lighthouse sin regresiones.
8. Longitud determinada por la intención, no por un mínimo arbitrario: guías pilar de 1.800–3.000 palabras; artículos de 900–1.800; landings de 700–1.200; herramientas y plantillas, lo que haga falta encima y debajo de la herramienta.

### 6.2 Actualizaciones urgentes de contenido existente (semanas 1–3)

#### T4.01 · Guía VERI\*FACTU → `/guias/verifactu/` · P0 · M · depende de B1 (para el bloque de producto) y B4
- **Title:** «VERI\*FACTU: qué es, a quién afecta y fechas (actualizado oct. 2026)». H1 sin año fijo.
- **Contenido nuevo:**
  - «En 30 segundos»: qué es, a quién afecta, fechas vigentes y anunciadas.
  - **Tabla de estado normativo** (componente `fx-estado-norma`, §6.5.3): vigente (RD-ley 15/2025: antes del 01/01/2027 para el IS y del 01/07/2027 para el resto) frente a **anunciado** (nota de Hacienda del 05/10/2026: octubre de 2028, sin BOE).
  - Quién está obligado y quién no (art. 3 RD 1007/2023): SII excluido; País Vasco y Navarra con su normativa foral; **Canarias, Ceuta y Melilla incluidas**; sin exclusión por recargo de equivalencia ni módulos si se usa un SIF.
  - Modalidades: VERI\*FACTU (remisión) frente a NO VERI\*FACTU (firma de registros y registro de eventos). La leyenda «VERI\*FACTU» solo existe en la modalidad verificable.
  - Requisitos comunes: registro de alta y anulación, huella SHA-256 encadenada, QR en todas las facturas, declaración responsable del productor.
  - **Sanciones** (art. 201 bis LGT): 150.000 € por ejercicio y tipo de sistema al productor; 50.000 € por ejercicio al usuario.
  - «No existe software homologado»: la AEAT no homologa; el productor firma una declaración responsable por versión. Cómo pedírsela al proveedor.
  - La **aplicación gratuita de la AEAT** y cuándo basta (honesto: capta la intención «gratis»).
  - Qué no cambia aunque se aplace (integridad, inalterabilidad, trazabilidad…).
  - Relación con la factura electrónica B2B y convergencia anunciada.
  - FAQ (8–10 preguntas), fuentes y bloque de revisión.
- **Retirar:** la «regla de los 4 NO» (sin fuente) o citar el documento exacto.
- **Bloque de producto:** solo el texto aprobado en B1.
- **Paquete de difusión:** nota de prensa breve «VERI\*FACTU se aplaza a 2028: qué cambia y qué no» para autonomosyemprendedor.es, cepymenews.es y castillayleoneconomica.es (T4.40).
- **Aceptación:** revisión firmada por el asesor; tabla de estado con enlaces al BOE y a la nota de Hacienda; `dateModified` = fecha real; 0 claims prohibidos.

#### T4.02 · Factura electrónica → `/guias/factura-electronica/` + artículo comparativo · P0 · M · depende de B4
- **Guía pilar** «Factura electrónica obligatoria: fechas, quién y cómo (RD 238/2026)»: Ley 18/2022, RD 238/2026 (BOE 31/03/2026), Orden HAC/1028/2026 (BOE 05/10/2026, en vigor el 06/10/2026); calendario ≈ octubre de 2027 (> 8 M€), ≈ octubre de 2028 (resto) y ≈ octubre de 2029 (estados de pago de las personas físicas); formatos (UBL, CII, EDIFACT y Facturae, sobre EN 16931); solución pública de la AEAT y copia fiel en UBL; estados (rechazo, pago, vencimiento); exclusiones (simplificadas, consumidores, no establecidos); ViDA (Directiva (UE) 2025/516, 01/07/2030). Publicar «octubre de 2027 / 2028» sin día exacto hasta que la AEAT lo concrete.
- **Artículo** `/blog/verifactu-vs-factura-electronica/`: tabla comparativa con columna de estado normativo y convergencia anunciada.
- **Producto:** «Descarga en Facturae 3.2.2 (sin firmar)». Para la obligación B2B: «iremos informando de cómo se integrará Facturales» (H-L09). **No** prometer la conexión con la solución pública.

#### T4.03 · Contabilidad → `/blog/como-llevar-la-contabilidad-de-un-negocio/` · P1 · S
Corregir «6 números» → 7; distinguir libros registro (autónomo en estimación directa) frente a contabilidad conforme al Código de Comercio (sociedad); conservación (4 años LGT, 6 años Código de Comercio; destruir papel solo con digitalización certificada); enlaces a conciliación, gastos, impuestos y panel.

#### T4.04 · FAQ y páginas de producto · P1 · S
`faq.html:50` (Facturae y B2B), `impuestos.html:50` (excepciones del 130), tabla de precios con inventario, recurrentes, recordatorios, bancos, cobros y gastos (según el plan), y FAQ de tarjeta y prueba (B6).

### 6.3 Calendario editorial (noviembre de 2026 → octubre de 2027)

**Contexto fiscal 2027** [HIPÓTESIS de cómputo sobre las normas de cada modelo; la AEAT publica el calendario oficial en diciembre]: 4T 2026 → 111/115 hasta el 20/01; 303, 390, 130/131 y 180/190 hasta el **01/02/2027** (el 30 y el 31/01 caen en fin de semana); 347 hasta el **01/03/2027**; 1T **20/04**; Renta 2026 de abril al **30/06**; 2T **20/07**; 3T **20/10/2027**. Factura electrónica B2B > 8 M€: ≈ **octubre de 2027**; solución pública de la AEAT disponible ≈ 2 meses antes.

**Dos escenarios VERI\*FACTU** (revisar el BOE cada semana):
- **Escenario A — no se publica el aplazamiento:** rigen el 01/01/2027 (IS) y el 01/07/2027 (resto). Las piezas marcadas **[A]** salen como están.
- **Escenario B — el BOE publica el aplazamiento a octubre de 2028:** actualizar el hub y la nota en < 72 h, sustituir las piezas **[A]** por las **[B]** (convergencia VERI\*FACTU + factura electrónica 2028) y reforzar el clúster de factura electrónica (> 8 M€ en octubre de 2027).

Leyenda de revisores: **AF** asesor fiscal colegiado · **AL** abogado · **GS** graduado social · **PM** producto (valida que la función existe) · **Conv.**: S = registro directo, L = lead (descarga o email), A = activación.

| Mes | Pieza | URL | Keyword (vol/KD) [DATO-SR] | Clúster | Conv. | Rev. |
|---|---|---|---|---|---|---|
| **Nov 2026** | Noticia citable «VERI\*FACTU se aplaza a 2028: qué se sabe y qué no» + nota de prensa | `/blog/verifactu-aplazamiento-2028/` | verifactu se retrasa 260/9 · verifactu retraso 210/11 | VERI\*FACTU | S | AF |
| | Reescritura del hub VERI\*FACTU (T4.01) | `/guias/verifactu/` | que es verifactu 810/36 · verifactu autonomos 480/28 | VERI\*FACTU | S | AF+PM |
| | Guía de factura electrónica + artículo comparativo (T4.02) | `/guias/factura-electronica/` | factura electronica obligatoria 720/42 | Factura electrónica | S | AF |
| | Landing de autónomos | `/autonomos/` | programa facturación autonomos 320/33 | Autónomos | S | PM+AF |
| | Facturas recurrentes | `/funciones/facturas-recurrentes/` | facturas recurrentes 50/9 (+2 variantes) | Facturación | S | PM |
| | Alternativa a Holded | `/alternativas/holded/` | precios holded 480/33 · alternativa a holded 90/5 | Alternativas | S | AL |
| **Dic 2026** | Calendario fiscal 2027 + `.ics` + aviso por email antes de cada trimestre | `/calendario-fiscal/` | calendario fiscal 2026→2027 720/26 | Impuestos | L | AF |
| | Modelo 347 (se presenta en febrero) | `/guias/modelo-347/` | modelo 347 880/18 | Impuestos | S | AF |
| | Recordatorios de pago | `/funciones/recordatorios-de-pago/` | recordatorio de pago 40/10 | Cobros | S | PM |
| | Plantillas de factura y de factura de autónomo (Excel, Word, PDF) | `/plantillas/factura/`, `/plantillas/factura-autonomo/` | modelo factura autonomo 480/7 · modelo de factura 910/39 | Plantillas | L | AF |
| | Factura recapitulativa | `/guias/factura-recapitulativa/` | factura recapitulativa 590/8 | Facturación | S | AF |
| | Alternativa a Contasimple | `/alternativas/contasimple/` | contasimple opiniones 390/16 · precios 210/0 | Alternativas | S | AL |
| **Ene 2027** | Modelo 303 (plazos, casillas, errores) | `/guias/modelo-303/` | plazo modelo 303 210/0 · como rellenar 260/36 | Impuestos | S | AF |
| | Modelo 130 | `/guias/modelo-130/` | plazo modelo 130 170/0 · como rellenar 170/5 | Impuestos | S | AF |
| | Modelo 390 | `/guias/modelo-390/` | modelo 390 370/17 | Impuestos | S | AF |
| | Calculadora IVA + IRPF | `/herramientas/calculadora-iva-irpf/` | calculadora irpf autonomos 590/9 · quitar iva 480/11 | IVA/IRPF | L | AF |
| | Landing de gestorías | `/gestorias/` | software para gestorias 50/15 (CPC 5,83) | Gestorías | S/B2B | PM |
| | Alternativa a Quipu | `/alternativas/quipu/` | quipu precios 260/21 | Alternativas | S | AL |
| | **[A]** «Ya es 2027: checklist VERI\*FACTU para sociedades» · **[B]** «VERI\*FACTU y factura electrónica en 2028: hoja de ruta» | `/blog/…` | verifactu 2026/2027 | VERI\*FACTU | S | AF |
| **Feb 2027** | Generador de facturas (MVP) | `/herramientas/generador-de-facturas/` | hacer factura online gratis 590/29 · creador facturas 590/24 · hacer factura online 390/6 | Generador | L→S | AF+PM |
| | Factura proforma + plantilla | `/guias/factura-proforma/` | que es factura proforma 390/9 · plantilla 210/8 | Facturación | L | AF |
| | Factura rectificativa y de abono | `/guias/factura-rectificativa/` | como hacer una factura rectificativa 390/9 · factura de abono 390/8 | Facturación | S | AF |
| | Listicle honesto «Mejores programas de facturación 2027» | `/blog/mejores-programas-facturacion/` | mejor programa de facturación 210/32 · mejores… 170/37 | Comparativas | S | AL |
| | Morosidad y cómo reclamar + plantilla de email de recordatorio | `/guias/morosidad-reclamar-facturas/`, `/plantillas/recordatorio-de-pago/` | ley de morosidad 590/17 · reclamar factura impagada 90/8 | Cobros | L | AL |
| | Alternativa a Billin / TS Facturas | `/alternativas/billin/` | billin precios 260/28 | Alternativas | S | AL |
| **Mar 2027** | Cómo hacer una factura + datos obligatorios | `/guias/como-hacer-una-factura/`, `/guias/datos-obligatorios-factura/` | como hacer una factura 810/21 · datos de facturacion 390/18 | Facturación | S | AF |
| | Tipos de factura (hub) | `/guias/tipos-de-factura/` | tipos de facturas 320/16 | Facturación | S | AF |
| | Landing de pymes | `/pymes/` | programa de facturacion para pymes 70/33 | Pymes | S | PM |
| | Sector reformas + plantilla de presupuesto de obra | `/sectores/reformas/`, `/plantillas/presupuesto-obra/` | presupuesto de obra 320/10 · programa de reformas 170/18 | Sectores | S/L | PM+AF |
| | Generador de presupuestos | `/herramientas/generador-de-presupuestos/` | hacer presupuesto online 140/17 · presupuesto online gratis 110/17 | Generador | L | PM |
| | Conciliación bancaria con ejemplo + plantilla Excel | `/guias/conciliacion-bancaria/`, `/plantillas/conciliacion-bancaria-excel/` | que es conciliacion bancaria 480/8 | Bancos | L | AF |
| **Abr 2027** | Gastos deducibles del autónomo (Renta) | `/guias/gastos-deducibles-autonomos/` | gastos deducibles autonomos 320/21 | Gastos | S | AF |
| | IVA soportado, repercutido y deducible | `/guias/iva-soportado-repercutido/` | iva soportado 760/9 · repercutido 660/8 · deducible 660/9 | IVA/IRPF | S | AF |
| | Retención de IRPF en la factura (15 % / 7 %) | `/guias/retencion-irpf-factura/` | factura con irpf 390/12 · factura con retencion 260/13 | IVA/IRPF | S | AF |
| | Sector comercio + plantilla de control de stock | `/sectores/comercio/`, `/plantillas/control-de-stock/` | programa para tiendas 70/11 · plantilla inventario excel 140/48 | Sectores/Inventario | S/L | PM |
| | Sector instaladores (fontaneros, electricistas) | `/sectores/instaladores/` | factura fontanero/electricista 40/5–6 · software electricistas 30/16 | Sectores | S | PM |
| | Actualización 1T de las guías 303 y 130 | — | — | Impuestos | S | AF |
| **May 2027** | «¿Puedo seguir facturando con Excel o Word?» | `/blog/facturar-con-excel-verifactu/` | factura con excel 480/27 · verifactu excel 170/17 | VERI\*FACTU | S | AF |
| | Alternativa a Excel | `/alternativas/excel/` | — | Alternativas | S | PM |
| | «Programas de facturación gratis: qué limitan y cuándo compensa pagar» (incluye la app de la AEAT) | `/blog/programas-de-facturacion-gratis/` | programa de facturacion gratis 210/7 | Comparativas | S | AL |
| | «VERI\*FACTU gratis: app de la AEAT frente a un programa» ⛔ B1 | `/blog/verifactu-gratis/` | verifactu gratis 610/17 · programa verifactu gratis 320/20 | VERI\*FACTU | S | AF |
| | Sectores consultores y academias | `/sectores/consultores/`, `/sectores/academias/` | software consultoria 10/8 · software para academias 30/22 | Sectores | S | PM+AF (exención IVA enseñanza) |
| | Calculadora del modelo 130 | `/herramientas/calculadora-modelo-130/` | calcular modelo 130 (s/d) | Impuestos | L | AF |
| **Jun 2027** | **[A]** Actualización masiva del clúster VERI\*FACTU (julio) · **[B]** Hoja de ruta de convergencia 2028 | — | — | VERI\*FACTU | S | AF+PM |
| | VERI\*FACTU frente a NO VERI\*FACTU | `/blog/verifactu-vs-no-verifactu/` | no verifactu 320/34 | VERI\*FACTU | S | AF |
| | «Cambia de programa de facturación en una tarde» (importar clientes, productos y facturas) | `/blog/cambiar-de-programa-de-facturacion/` | — | Facturación | S/A | PM |
| | Sectores fisioterapeutas y psicólogos (exenciones) | `/sectores/fisioterapeutas/`, `/sectores/psicologos/` | software fisioterapia 110/10 · software para psicologos 70/22 | Sectores | S | PM+AF |
| | Glosario: primeros 15 términos | `/glosario/` | — | Transversal | — | AF |
| **Jul 2027** | **[A]** «Desde hoy, VERI\*FACTU para todos» · **[B]** «Factura electrónica para empresas de más de 8 M€: 3 meses» | `/blog/…` | verifactu obligatorio 320/44 · factura electronica b2b 210/17 | VERI\*FACTU / F. electrónica | S | AF |
| | Control de stock y stock mínimo | `/guias/control-de-stock/` | control de stock 390/8 · stock minimo 110/6 | Inventario | S | PM |
| | Sector abogados | `/sectores/abogados/` | software para abogados 50/9 | Sectores | S | AL |
| | Alternativa a Anfix | `/alternativas/anfix/` | anfix precios 110/18 | Alternativas | S | AL |
| | Validador de NIF/CIF/NIE | `/herramientas/validador-nif/` | — (activo de enlace) | Herramientas | L | PM |
| | Glosario: +15 términos | `/glosario/` | — | Transversal | — | AF |
| **Ago 2027** | «Facturas recurrentes para cuotas y contratos» | `/blog/facturas-recurrentes-cuotas/` | facturación recurrente 50/7 | Facturación | S | PM |
| | Sectores talleres y peluquerías | `/sectores/talleres/`, `/sectores/peluquerias/` | programa taller mecanico 70/22 · software para peluquerías 140/8 | Sectores | S | PM |
| | Alternativas a FacturaDirecta y STEL Order | `/alternativas/facturadirecta/`, `/alternativas/stel-order/` | facturadirecta precios 110/0 · stel order precios 210/13 | Alternativas | S | AL |
| | Mantenimiento: refresco de precios de competidores, auditoría de enlaces | — | — | — | — | — |
| **Sep 2027** | Estudio propio (encuesta con asociación) «Morosidad y VERI\*FACTU en autónomos 2027» | `/estudios/…` | — (activo de PR) | Cobros | L | AL + metodología |
| | Solución pública de factura electrónica (si ya está disponible) | `/guias/factura-electronica/` (actualización) | — | F. electrónica | S | AF |
| | Sectores diseñadores y mantenimiento | `/sectores/disenadores/`, `/sectores/mantenimiento/` | facturacion freelance 20/9 | Sectores | S | PM |
| | Numeración de facturas + facturar sin ser autónomo | `/guias/numeracion-facturas/`, `/guias/facturar-sin-ser-autonomo/` | numeracion 70/9 · puedo facturar sin ser autónomo 390/31 | Facturación | S | AF |
| | Checklist 3T | `/blog/…` | declaracion trimestral autonomos 390/16 | Impuestos | S | AF |
| **Oct 2027** | Factura electrónica obligatoria (> 8 M€): guía del día D | `/guias/factura-electronica/` + noticia | factura electronica obligatoria 720/42 | F. electrónica | S | AF |
| | Calendario fiscal 2028 (borrador) | `/calendario-fiscal/` | calendario fiscal | Impuestos | L | AF |
| | Calculadora de intereses de demora (Ley 3/2004) | `/herramientas/calculadora-intereses-demora/` | — | Cobros | L | AL |
| | Flujo de caja (guía + plantilla) | `/guias/flujo-de-caja/` | flujo de caja 720/57 | Panel | S | AF |
| | **Revisión anual** de todas las guías (`dateModified` solo si hay cambios reales) | — | — | Todos | — | AF/AL |

Total: ~75 piezas en 12 meses (incluye actualizaciones sustanciales). Las landings de la Fase 3 (T3.10–T3.22) y las mejoras de módulos (T3.18) van aparte y se priorizan antes.

### 6.4 Reglas de comparativas y alternativas (honestas y verificables)

1. **Fecha de consulta** visible en la cabecera y junto a cada precio.
2. **Una fuente por dato** del competidor (su página oficial) y **captura archivada** interna o enlace a archive.org de esa fecha.
3. Solo **criterios objetivos**: precio de lista sin IVA, límites del plan y existencia documentada de una función. Nada de «más fácil» ni de reseñas de terceros.
4. Dato no verificable → «No verificado», nunca ✗.
5. **Reconocer dónde gana el competidor** (contabilidad completa, banca conectada hoy, integraciones, nóminas…) y mostrar el estado real de Facturales (banca «Próximamente», VERI\*FACTU según B1, sin nóminas).
6. Caja de transparencia: «Somos Facturales. Comparamos con datos públicos de [X] consultados el dd/mm/aaaa. Si algo ha cambiado, escríbenos a info@facturales.es y lo corregimos en 5 días hábiles.»
7. **Revisión jurídica previa** sobre publicidad comparativa (Ley 34/1988 General de Publicidad, art. 10; Ley 3/1991 de Competencia Desleal, art. 10): objetiva, de bienes homogéneos y sin denigrar.
8. No usar logos ni signos de la marca ajena que sugieran afiliación: el nombre, en texto.
9. Revisión trimestral y tras cualquier cambio de precios (alerta). Responsable con nombre.
10. Estructura (plantilla T4): H1 «Alternativas a [X] para autónomos y pymes (2027)» → caja de transparencia → resumen en 3 líneas → tabla de funciones y precios → por qué se busca una alternativa (motivos genéricos verificables: precio, complejidad, funciones) → 4–6 alternativas **incluidos terceros**, con Facturales primero → ficha honesta de Facturales (qué hace y qué no) → cómo migrar desde [X] → FAQ → fuentes.
- **Ventaja de precio verificable** [COMPROBADO para Facturales; competidores SERP-3º sin verificar]: Starter 4,95 €/mes anual o 6,45 € mensual + IVA, en la franja baja frente a Holded (~14,50–15 €), Quipu (12–14 €), Contasimple (~8,30 €) o Billin (6,60–8 €). **Verificar cada precio en la web oficial antes de publicar.**

### 6.5 Protocolo editorial YMYL

#### 6.5.1 Flujo
1. **Redacción** con fuentes primarias obligatorias (BOE, sede de la AEAT, DGT/consultas vinculantes, EUR-Lex, diputaciones forales) y **ficha de fuentes** por pieza (norma, artículo, URL del BOE consolidado, fecha de consulta).
2. **Revisión técnica** por el asesor colegiado (B4), identificado con nombre, número de colegiado y página de autor (`Person`).
3. **Revisión de producto** (PM): toda mención a Facturales se contrasta con la tabla §5.6.
4. **Publicación** con bloque de revisión, `dateModified`, `reviewedBy` y tabla de estado normativo si aplica.

#### 6.5.2 Componente `fx-revision`
```
Última revisión: 18 de octubre de 2026 · Revisado por: [Nombre Apellido], asesor fiscal colegiado n.º XXXX ([Colegio])
Fuentes oficiales: RD 1007/2023 (BOE consolidado) · RD-ley 15/2025 · Nota del Ministerio de Hacienda de 05/10/2026 · FAQ VERI*FACTU de la AEAT
Próxima revisión prevista: enero de 2027, o antes si cambia el BOE.
```

#### 6.5.3 Componente `fx-estado-norma` (badges `fx-badge` con texto, nunca solo color)
| Obligación | Estado | Fecha | Norma |
|---|---|---|---|
| VERI\*FACTU (contribuyentes del IS) | Vigente | Antes del 01/01/2027 | RD 1007/2023, DF 4.ª (RD-ley 15/2025) |
| VERI\*FACTU (autónomos y resto) | Vigente | Antes del 01/07/2027 | ídem |
| Aplazamiento de VERI\*FACTU | **Anunciado, sin norma** | Octubre de 2028 | Nota del Ministerio de Hacienda, 05/10/2026 |
| Factura electrónica B2B (> 8 M€) | Aprobado, pendiente de aplicación | ≈ octubre de 2027 | RD 238/2026 + Orden HAC/1028/2026 |
| Factura electrónica B2B (resto) | Aprobado, pendiente de aplicación | ≈ octubre de 2028 | ídem |
| ViDA intracomunitario | Aprobado (UE) | 01/07/2030 | Directiva (UE) 2025/516 |

#### 6.5.4 Cadencia y vigilancia
- **Semanal:** alertas de **Mi BOE** (textos «1007/2023», «238/2026», «sistemas informáticos de facturación», «facturación electrónica», «cotización»; sección I; Ministerio de Hacienda), RSS del BOE, página VERI\*FACTU de la AEAT (vigilar «Página actualizada» con un *diff* tipo Visualping), notas de prensa de Hacienda y referencias del Consejo de Ministros. **Si hay cambio: actualizar en menos de 72 h** las páginas afectadas (guías, FAQ, JSON-LD, `llms.txt`, `/facturales-en-datos/`) y registrarlo en un *changelog* interno.
- **Mensual:** fechas, enlaces y coherencia del copy con el producto.
- **Trimestral:** revisión completa de las guías fiscales por el asesor. `dateModified` solo si hay cambios reales.
- **Fijo:** enero (orden de cotización, PGE, tipos, calendario del contribuyente), marzo y abril (Renta), octubre (anteproyecto de PGE).
- **Datos que no se publican hasta que estén en el BOE:** tramos de cuota de autónomos 2027, fechas exactas de la factura electrónica, aplazamiento de VERI\*FACTU como hecho.

#### 6.5.5 Disclaimers
- Pie de artículo fiscal: «Contenido informativo actualizado a la fecha indicada. No constituye asesoramiento fiscal ni jurídico. La normativa cambia: consulta el BOE, la sede de la AEAT o a tu asesor antes de decidir.»
- Normas anunciadas: «Las fechas marcadas como "anunciadas" aún no tienen rango normativo. Actualizaremos este contenido cuando se publiquen en el BOE.»
- Páginas de impuestos: «Facturales calcula importes orientativos a partir de tus registros. No presenta declaraciones ante la AEAT.»

### 6.6 Checklist de claims (obligatoria antes de publicar cualquier texto)

| ¿Dice…? | Regla |
|---|---|
| Testimonios, logos de clientes, nº de clientes, valoraciones o estrellas | **Prohibido** (`CLAUDE.md`) |
| «Sin tarjeta» | **Prohibido** (`CLAUDE.md`). Microcopy de la prueba según B6 |
| «Gratis» referido al producto | Solo «14 días de prueba». «Gratis» solo para herramientas y plantillas realmente gratuitas |
| Descuento anual | Solo «hasta −25 %». Nunca 30 % |
| Precios | Exactamente los de `plans-config.service.ts`, con «+ IVA» y «/mes» |
| Presentación de impuestos | Solo «calcula el 303 y el 130». Nunca «presenta» ni «envía a la AEAT» |
| VERI\*FACTU | Solo el texto aprobado en B1. Nunca «homologado», «certificado» ni «cumple» sin declaración firmada |
| Conexión bancaria | Solo «Próximamente». Hoy, extractos Excel/CSV |
| Inventario | Mencionar «un solo almacén» donde proceda |
| Recurrentes | «Se generan como borrador y tú las emites» |
| Facturae | «Descarga en Facturae 3.2.2». Nunca «firmada» ni «cumple la factura electrónica obligatoria» |
| Bancos, Cobros, Gastos, Gráficas | «Nuevo», sin fechas de despliegue |
| Nóminas, DIAN, integraciones «soon» | No mencionar |
| Capturas | Reales, con «Captura real … con datos de ejemplo» |
| Fechas normativas | Con estado (vigente / aprobado / anunciado) y fuente enlazada |

`build-check` (T2.07) automatiza la detección de los términos prohibidos; la revisión humana es igualmente obligatoria.

### 6.7 Autoridad y enlaces (sin técnicas penalizables)

#### 6.7.1 Activos enlazables (por orden)
1. **Tracker normativo** «Calendario VERI\*FACTU y factura electrónica» (hub + cronología de aplazamientos), actualizado con cada cambio: noticia viva que enlazan medios y gestorías.
2. **Herramientas:** generador de facturas y de presupuestos, calculadora IVA + IRPF, calculadora del 130, validador de NIF/CIF/NIE (algoritmo público), calculadora de intereses de demora. Opcional: validador del formato del QR (decodifica la URL de cotejo y enlaza a la AEAT, **sin simular la verificación oficial**).
3. **Plantillas** descargables (las de presupuesto captan 214–220 dominios en Holded y Quipu [DATO-SR]).
4. **Glosario** selectivo de 30–50 términos de facturación e impuestos (una sola entrada del glosario de Billin capta 323 dominios [DATO-SR]).
5. **Estudio propio:** primero una **encuesta** con una asociación (≥ 400 respuestas, ficha técnica publicada, datos en CSV). El «barómetro» con datos agregados de la app **solo** con base jurídica revisada (Facturales es encargado del tratamiento de los datos de los clientes de sus usuarios), anonimización irreversible y k-anonimato (≥ 50 cuentas por celda).
6. **Página de prensa** `/prensa/`: datos de empresa, logos oficiales, capturas reales, portavoz con bio y foto, notas con fecha.

#### 6.7.2 Plan de captación por trimestre

| Trimestre | Objetivos | Tácticas | Meta de dominios referentes nuevos (no del grupo) |
|---|---|---|---|
| **T1 (nov–ene)** | Entidad + directorios de calidad + comparadores citados por LLM | Capterra/GetApp/Software Advice, G2, LinkedIn, Crunchbase, fichas de App Store/Google Play (B8), softwaredoit.es, cronomia.com, comparasoft.es, softwarepara.net, elreferente.es, startupxplore.com, startups-espanolas.es. Nota de prensa sobre el aplazamiento de VERI\*FACTU a autonomosyemprendedor.es, cepymenews.es y castillayleoneconomica.es. Cámara de Comercio de Valladolid | 10–20 |
| **T2 (feb–abr)** | Inclusión en comparativas de terceros + partners | Pitch con ficha, precios fechados y acceso de prueba a revolucionatupyme.com, economia3.com, rankiabusiness.com, wwwhatsnew.com, conversoriaecnae.es, banktrack.com. Programa de partners para gestorías (ficha enlazable por partner, sin intercambio masivo). Portales TIC Negocios de las Cámaras. UPTA y CEAT (convenio de ventajas, webinar VERI\*FACTU) | 15–30 |
| **T3 (may–jul)** | Medios por datos y herramientas | Generador y calculadoras como gancho para pymesyautonomos.com, emprendedores.es e ionos.es (guías para autónomos). Encuesta con una asociación. Podcasts de autónomos. Canal de YouTube con tutoriales (AI Overviews cita mucho YouTube) | 15–30 |
| **T4 (ago–oct)** | Autoridad nacional | Estudio propio a Cinco Días, El Economista y Expansión Pymes. Portavoz para la factura electrónica (octubre de 2027). Wikidata (con al menos una fuente independiente). Universidad de Valladolid (licencias para emprendedores) | 10–40 |

La lista completa de **52 objetivos** con tipo, dificultad, táctica y prioridad está en `docs/seo/auditoria-2026-10/04-geo-autoridad.md` §5.4. El *link gap* en bruto (1.374 dominios) está disponible a petición (no se versiona).

#### 6.7.3 Reseñas reales
Email automático 30–45 días después de la activación (≥ 5 facturas emitidas), con enlace directo a una plataforma (rotando Capterra, G2, tiendas). **Prohibido** condicionar incentivos a una reseña positiva, reseñas de empleados o del grupo, o comprarlas (Directiva Ómnibus, TRLGDCU, políticas de las plataformas). Responder a todas, también a las negativas. **No** marcar `aggregateRating` en la web hasta tener reseñas propias verificables en la página.

---

## 7. FASE 5 — GEO y diferenciación

> **Calendario:** base técnica en las semanas 1–4; contenido y entidad, del mes 1 al 6; seguimiento mensual continuo.
> **Sin garantías:** ningún motor de IA publica cómo elige sus fuentes. Lo que sigue aumenta la probabilidad de ser recuperado, entendido y citado, y se mide (§7.7). No se promete ningún resultado.

### 7.1 Cómo eligen fuentes hoy los motores con IA en este nicho [DATO-SR]

- **Cuota de voz en IA (ES, octubre de 2026):** Sage 25,4 %, Holded 20,3 %, Quipu 14,4 %, Anfix 12,0 %, Billin 9,1 %, Factorial 8,0 %, STEL Order 5,5 %, Contasimple 3,6 %, FacturaDirecta 1,5 %, **Facturales 0 %**.
- **Fuentes citadas:** blogs de fabricantes (listicles «mejores programas…»), comparadores pequeños (softwaredoit, cronomia, softwarepara, banktrack, revolucionatupyme, conavalsi), micro-SaaS con comparativas en tabla (getrenn, factupro), la AEAT y YouTube.
- **Implicaciones:** (1) hace falta contenido propio comparativo y factual en formato tabla; (2) hay que estar en las listas de terceros que ya se citan; (3) Bing importa (ChatGPT search y Copilot se apoyan en su índice); (4) el contenido tiene que ser legible **sin JavaScript**.

### 7.2 Base técnica GEO (semanas 1–4)

| ID | Tarea | Archivos | Aceptación |
|---|---|---|---|
| T5.01 | Cabecera y pie en HTML estático | = T2.06 | Enlaces sin JS ≈ con JS |
| T5.02 | Legales en HTML en el dominio principal, sin cláusula anti-enlaces | = T2.17 | Razón social y NIF visibles sin JS |
| T5.03 | `Organization` completo y grafo `@id` | = T2.14 | Validador sin errores; `sameAs` solo con perfiles reales |
| T5.05 | `robots.txt` explícito para bots de IA | `robots.txt` | Ver §7.3 |
| T5.06 | `llms.txt` y `llms-full.txt` | raíz | 200 `text/plain`; contenido = §7.4; `llms-full.txt` regenerado en cada despliegue |
| T5.07 | Bing Webmaster Tools + IndexNow | = T6.02 | 100 % del sitemap indexado en Bing |

### 7.3 `robots.txt` propuesto (T5.05)

**Recomendación:** permitir los bots de búsqueda y de recuperación **y también los de entrenamiento**. Para una marca sin notoriedad, aparecer en índices y modelos vale más que el clic que pueda perderse; el sitio de marketing no tiene nada que proteger.

```
# Facturales — política de rastreo (revisada 2026-10)
User-agent: *
Allow: /
Disallow: /partials/

# Búsqueda y respuesta en tiempo real (citas con enlace)
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Claude-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Perplexity-User
Allow: /

# Entrenamiento (decisión de marca: permitido)
User-agent: GPTBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: CCBot
Allow: /

Sitemap: https://facturales.es/sitemap.xml
```

| Bot | Para qué sirve | Si se bloquea |
|---|---|---|
| OAI-SearchBot / ChatGPT-User | Citas de ChatGPT search y lecturas a petición del usuario | Desaparece de las citas de ChatGPT. **No bloquear** |
| GPTBot / ClaudeBot / CCBot | Entrenamiento | No afecta a las citas, pero reduce el conocimiento «de memoria» sobre la marca |
| PerplexityBot / Perplexity-User | Índice y lecturas de Perplexity (el motor que más cita) | **No bloquear** |
| Google-Extended | Gemini (apps y Vertex). **No controla AI Overviews ni AI Mode**, que dependen de Googlebot | Bloquearlo apenas protege nada |
| Bingbot | Bing, Copilot y base de ChatGPT search | Sería catastrófico |

(`/partials/` deja de existir en producción tras T2.03; la línea se mantiene por si acaso. **robots.txt no es un control de acceso**: la protección real está en `.htaccess`.)

### 7.4 `llms.txt` propuesto (T5.06)

Validar cada dato contra la app y contra B1 antes de publicar. URLs ya migradas (T3.03).

```markdown
# Facturales

> Facturales es un software en la nube de facturación y gestión financiera para autónomos y pymes en España. Reúne facturas y presupuestos, facturas recurrentes, inventario, cobros con recordatorios automáticos, conciliación bancaria por extractos, gastos con justificantes y el cálculo de los modelos 303 y 130. Funciona en el navegador (app.facturales.es) [y en iOS y Android: solo si B8 lo confirma]. Datos alojados en la Unión Europea. Lo desarrolla AVENUE DIGITAL GROUP, S.L. (NIF B70829601, Valladolid, España).

Datos verificados a [fecha]. Precios sin IVA.

## Hechos clave
- Para quién: autónomos y pymes que facturan en España (IVA, IGIC e IPSI).
- Precios (€/mes + IVA, pago mensual / pago anual): Starter 6,45 / 4,95 · Pro 11,95 / 8,95 · Ilimitado 23,95 / 17,95. Prueba de 14 días. Sin permanencia. Hasta −25 % con pago anual.
- Límites: clientes 10 / 150 / ilimitados; productos 30 / 150 / ilimitados; facturas al mes 10 / ilimitadas / ilimitadas; OCR de gastos al mes 10 / 75 / 300.
- VERI*FACTU: [texto aprobado en B1; p. ej. «Genera el registro de facturación con huella encadenada y el código QR. La remisión de registros a la AEAT está en preparación.»]
- Inventario: stock por producto, alertas de stock mínimo, movimientos, descuento automático al emitir la factura y devolución al anularla. Un solo almacén.
- Facturas recurrentes: se generan como borrador en cada periodo; el usuario las emite.
- Recordatorios de cobro automáticos: calendario configurable, enviados por email desde el servidor.
- Bancos: importación de extractos Excel o CSV y conciliación. Conexión bancaria directa: próximamente.
- Impuestos: calcula los modelos 303 y 130. No presenta declaraciones ante la AEAT.
- Formatos: PDF y descarga en Facturae 3.2.2.

## Limitaciones
- Sin conexión bancaria directa todavía (solo extractos).
- Inventario con un único almacén.
- Sin plan gratuito permanente (prueba de 14 días).
- Sin presentación telemática de impuestos.

## Páginas de referencia
- [Facturales en datos](https://facturales.es/facturales-en-datos/): ficha oficial con hechos, precios fechados, funciones y limitaciones
- [Precios](https://facturales.es/precios/)
- [Funciones](https://facturales.es/funciones/)
- [Preguntas frecuentes](https://facturales.es/preguntas-frecuentes/)
- [Guía VERI*FACTU (estado normativo actualizado)](https://facturales.es/guias/verifactu/)
- [Guía de factura electrónica obligatoria](https://facturales.es/guias/factura-electronica/)
- [Sobre Facturales y datos de empresa](https://facturales.es/sobre-nosotros/)
- [Aviso legal](https://facturales.es/legal/aviso-legal/)

## Para quién
- [Autónomos](https://facturales.es/autonomos/) · [Pymes](https://facturales.es/pymes/) · [Gestorías](https://facturales.es/gestorias/)

## Funciones
- [Facturación](https://facturales.es/funciones/facturacion/) · [Facturas recurrentes](https://facturales.es/funciones/facturas-recurrentes/) · [Presupuestos](https://facturales.es/funciones/presupuestos/) · [Control de stock](https://facturales.es/funciones/control-de-stock/) · [Gestión de cobros](https://facturales.es/funciones/gestion-de-cobros/) · [Recordatorios de pago](https://facturales.es/funciones/recordatorios-de-pago/) · [Conciliación bancaria](https://facturales.es/funciones/conciliacion-bancaria/) · [Gastos y tickets](https://facturales.es/funciones/gastos-y-tickets/) · [Impuestos 303 y 130](https://facturales.es/funciones/impuestos-303-130/)

## Contacto
- info@facturales.es · soporte@facturales.es · Registro: https://app.facturales.es/signup

## Optional
- [Blog](https://facturales.es/blog/) · [Plantillas](https://facturales.es/plantillas/) · [Herramientas](https://facturales.es/herramientas/) · [Alternativas](https://facturales.es/alternativas/)
```

- **`llms-full.txt`:** concatenación en Markdown limpio (sin navegación) de *Facturales en datos*, precios, FAQ, guía VERI\*FACTU y guía de factura electrónica, generada en cada despliegue con un script (`scripts/build-llms.mjs`) y con la cabecera «Generado el AAAA-MM-DD a partir de facturales.es».
- [HIPÓTESIS] El efecto directo de `llms.txt` en las citas es aún bajo (ningún gran motor ha confirmado que lo use para posicionar), pero cuesta poco y lo leen agentes y herramientas.

### 7.5 Páginas «fuente de verdad»

| ID | Página | Contenido | Prio |
|---|---|---|---|
| T3.20 / T5.08 | `/facturales-en-datos/` | Párrafo inicial citable de 40–60 palabras; **ficha técnica** (titular, NIF, domicilio, año de lanzamiento, plataformas, alojamiento en la UE, pagos con Stripe, formatos, estado VERI\*FACTU según B1); **precios con fecha** y límites; «qué hace / qué no hace»; **changelog** fechado (p. ej. «17/10/2026: inventario, recurrentes y recordatorios automáticos»); fuentes oficiales; bloque «Cómo citar». Schema `WebPage` + `SoftwareApplication` + `Organization` | P1 |
| T5.04 ⛔ B1 | `/declaracion-responsable-verifactu/` | Declaración responsable **por versión**, según los ejemplos de la AEAT (nombre del SIF, versión, componentes, modalidad, productor con NIF y domicilio, fecha y lugar) e histórico de versiones. Debe estar también en la app (Ayuda › Acerca de). **Solo cuando esté firmada.** Es obligación legal y además contenido muy citable | P1 |
| T4.01 | `/guias/verifactu/` | Hub con tabla de estado normativo (§6.5.3) | P0 |
| T3.22 | `/alternativas/*` y listicle | Formato que hoy citan los LLM: tabla al principio, criterios explícitos, fechas y fuentes | P1 |
| — | `/glosario/*` | `DefinedTerm`: huella, registro de facturación, SIF, factura rectificativa, recapitulativa, proforma, Facturae, FACe, modelo 303, modelo 130, recargo de equivalencia, conciliación bancaria… | P2 |

### 7.6 Formato citable (aplica a todas las páginas)

- Responder en las **primeras 40–60 palabras** con una frase autocontenida.
- **Un dato por frase, con fecha y fuente** («Según el art. 3 del RD 1007/2023…»).
- **Tablas HTML reales** (no imágenes) para precios, calendarios y comparativas.
- H2/H3 en forma de pregunta y FAQ al final (`FAQPage`).
- «Actualizado el…» visible y `dateModified` coherente.
- Autor persona con credenciales y revisor colegiado.
- Nada importante detrás de pestañas generadas por JS (los `<details>` nativos sí se leen).
- Nombres consistentes de la entidad («Facturales», «software de facturación de AVENUE DIGITAL GROUP, S.L.») en todas partes: web, schema, perfiles y notas de prensa.

### 7.7 Entidad fuera del sitio

| ID | Perfil | Acción | Prio |
|---|---|---|---|
| T5.10 | LinkedIn Company Page | Web, sede, sector; fundador vinculado | P1 |
| T5.10 | Crunchbase, elreferente.es, startupxplore.com | Perfil gratuito y coherente | P1 |
| T5.10 | Capterra/GetApp/Software Advice, G2 | Fichas de vendedor con capturas reales; campaña de reseñas reales (§6.7.3) | P1 |
| T5.10 | App Store / Google Play (B8) | Ficha optimizada con enlace a la web y la política de privacidad; enlazarlas desde la web | P1 |
| T5.11 | Wikidata | Elemento «Facturales» (instancia de: software; desarrollador; web oficial; país) cuando haya al menos una fuente independiente | P2 |
| T5.12 | Google Business Profile | Opcional (empresa de software con domicilio social real) | P3 |
| T5.13 | YouTube | 3–6 tutoriales cortos («cómo emitir una factura», «qué es el QR de la factura», «control de stock») | P2 |
| — | AEAT: acuerdo de colaboración social | Si Facturales va a remitir registros en nombre de clientes (B1). No es un enlace, pero sí una mención legítima y citable | P2 |

Al publicar cada perfil, añadirlo al `sameAs` (T2.14).

### 7.8 Seguimiento de menciones en IA (método reproducible)

- **Set fijo de 30 prompts** (10 de categoría, 10 de VERI\*FACTU y normativa, 5 de comparación, 5 de marca). Por ejemplo: «mejor programa de facturación para autónomos en España», «software verifactu para autónomos», «alternativa a Holded barata», «programa de facturación gratis», «programa de facturación con control de stock», «programa para facturas recurrentes», «recordatorios de cobro automáticos», «cuándo es obligatorio verifactu», «verifactu aplazamiento 2028», «qué es la declaración responsable verifactu», «qué es Facturales», «Facturales opiniones», «Facturales vs Quipu».
- **Motores:** ChatGPT (con búsqueda), Perplexity, Gemini, Google AI Overviews/AI Mode y Copilot. Sesión limpia, ubicación España, idioma español. **Cadencia mensual.**
- **Registro** (hoja compartida): fecha, motor, prompt, ¿menciona a Facturales? (y posición), ¿cita una URL de facturales.es? (¿cuál?), competidores mencionados, fuentes citadas y **exactitud** de lo que dice sobre Facturales (correcto / incorrecto / desactualizado).
- **Herramientas:** proyecto de seguimiento en IA de SE Ranking con el mismo set y la marca con alias; Bing Webmaster Tools; analítica con segmento de referrers `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com` y `utm_source=chatgpt.com`; canal `ai_assistant` en la atribución propia (§8.4).

---

## 8. FASE 6 — Medición y crecimiento

> **Calendario:** semanas 1–3 la base (antes de publicar contenido nuevo, para tener línea base); después, revisión semanal, mensual y trimestral.
> **Principio:** las métricas de negocio (registros, activación, pago, MRR) salen **siempre de la base de datos**, nunca de la analítica web.

### 8.1 Search Console y Bing

#### T6.01 · Google Search Console · P0 · S
1. **Propiedad de dominio** `facturales.es` verificada por DNS (TXT en IONOS): cubre apex, www y app.
2. Propiedades de prefijo `https://facturales.es/` y `https://app.facturales.es/` (esta última para vigilar que no se indexe nada privado).
3. Enviar `sitemap.xml`. Inspección de URL tras cada publicación importante.
4. Vincular con la analítica y con Looker Studio.
5. **Semana 0:** revisar «Indexación de páginas» para validar HX02 y limpiar con 301/410.
- **Aceptación:** propiedad verificada, sitemap «Correcto» con todas las URLs descubiertas.

#### T6.02 · Bing Webmaster Tools + IndexNow · P0 · S
- Importar desde GSC y enviar el sitemap.
- **IndexNow:** clave en `https://facturales.es/<clave>.txt`; en el paso posterior al despliegue (T2.05), `POST https://api.indexnow.org/indexnow` con `{"host":"facturales.es","key":"<clave>","keyLocation":"https://facturales.es/<clave>.txt","urlList":[…URLs cambiadas…]}`. Google no usa IndexNow; para Google basta el sitemap.
- **Aceptación:** 100 % del sitemap indexado en Bing en ≤ 30 días.

### 8.2 Analítica (decisión B3: modelo híbrido recomendado)

#### T6.03 · Analítica sin cookies en la landing · P0 · S
- **Plausible** (UE) o **Umami** autoalojado: un script `defer` en `partials/head-common.html`. Sin banner (sin cookies ni identificadores persistentes), 100 % del tráfico.
- **Objetivos:** `cta_click`, `pricing_toggle`, `faq_open`, `tool_use`, `template_download`, `contact_submit`, `outbound_click`.

#### T6.04 · GA4 con Consent Mode v2 (embudo detallado) · P1 · M
- **Un único flujo GA4** para `facturales.es` y `app.facturales.es` (misma cookie `_ga` en `.facturales.es`); `checkout.stripe.com` en referencias no deseadas.
- **Consent Mode v2 básico:** todo `denied` por defecto, no carga nada hasta el consentimiento (lo más defendible ante la AEPD).
- **CMP** con «Rechazar» en la primera capa con la misma prominencia que «Aceptar», sin casillas premarcadas, panel por finalidades, enlace permanente «Configurar cookies» en el pie y elección compartida entre landing y app (cookie en `.facturales.es`, máximo 24 meses).
- **App:** actualizar la CSP de `vercel.json` (`script-src`, `connect-src`, `img-src` con los dominios de Google) o servir GTM desde un dominio propio.
- **Política de cookies** reescrita (T2.17).

### 8.3 Eventos y conversiones (nombres exactos)

| Evento | Dónde | Parámetros | Conversión |
|---|---|---|---|
| `cta_click` | Landing (`facturales.js`, delegación en `a[href*="app.facturales.es/signup"]`) | `cta_id`, `cta_location` (`header`, `hero`, `mid`, `pricing_card`, `article_inline`, `article_end`, `footer`, `mobile_menu`), `cta_text`, `plan`, `billing_period`, `page_type`, `cluster` | Micro |
| `pricing_toggle` | Landing (`facturales.js`, función `aplicar`) | `billing_period` | — |
| `faq_open` | Landing (`<details>`) | `faq_question`, `page_type` | — |
| `tool_use` | Herramientas | `tool_id`, `tool_step` (`start`, `result`, `pdf`) | Micro |
| `template_download` | Plantillas | `template_id`, `format` | Lead |
| `lead_submit` | Calendario fiscal, checklists | `magnet` | Lead |
| `contact_submit` | Contacto | `form_id` | Micro |
| `signup_start` | App, al montar `/signup` | `plan_hint`, `source` | — |
| `sign_up` | App, tras `authService.signUp` correcto (`use-acceso.ts:135-138`) y desde el servidor | `method` (`email`, `google`), `user_id` (hash del UUID, **nunca el email**) | **Principal** |
| `email_confirmed` | App `/confirm-email` | — | — |
| `trial_start` | Servidor (`stripe-webhook`, `customer.subscription.created` con `status=trialing`) | `plan`, `billing_period`, `trial_days` | Sí |
| `activation_first_invoice` | Servidor (trigger al emitir la primera factura) | `days_since_signup`, `verifactu_enabled` | **Activación** |
| `activation_milestone` | App | `milestone` (`first_client`, `first_quote`, `first_bank_import`, `first_ocr_scan`, `recurring_created`, `reminder_enabled`, `team_invite`) | — |
| `purchase` | Servidor (`stripe-webhook`, `invoice.paid`) vía Measurement Protocol | `transaction_id`, `value` (sin IVA), `currency=EUR`, `items[{item_id: plan, item_variant: billing_period}]`, `subscription_type` (`new`, `renewal`, `upgrade`) | **Sí** |
| `subscription_cancel` | Servidor | `plan`, `tenure_days` | — |

### 8.4 Atribución *first-touch* en el registro

#### T6.05 · Landing: captura y decoración de enlaces · P0 · S
- Nuevo módulo en `assets/js/facturales.js`: en la primera visita, guardar *first touch* y *last touch* (`utm_*`, `gclid`/`msclkid`, **solo el dominio** del referrer, página de entrada, fecha). Preferente: `localStorage` (con try/catch) o una cookie de primera parte `fx_ft` en `.facturales.es` de 90 días **solo si legal la aprueba** (o si se condiciona al consentimiento).
- Al hacer clic en un CTA de signup, añadir a la URL `utm_source`/`utm_medium`/`utm_campaign` (= clúster)/`utm_content` (= `cta_location`), `lp` (ruta de entrada), `ref` (dominio de referencia) y, en los botones de plan, `plan` y `periodo`.
- Respaldo sin JS: los enlaces estáticos llevan `data-cta-location` y `data-plan` y, si se quiere, `?utm_source=facturales.es&utm_medium=web&utm_content=hero`.

#### T6.06 · App: guardar el origen con la cuenta · P0 · M (repo `facturales`)
1. `/signup` (`src/app/pages/hooks/use-acceso.ts`): al montar, leer la query y guardar `{utm_*, lp, ref, plan, periodo, ts}` en `sessionStorage`.
2. `buildSignUpMetadata()` (`src/app/pages/domain/acceso.ts:99`): añadir `acquisition: {…}` a `options.data`, que ya se envía en `auth.service.ts:103` y queda en `raw_user_meta_data`.
3. **Google OAuth** (`auth.service.ts:120-135`): guardar el origen en `sessionStorage` antes de redirigir y escribirlo tras el callback (p. ej. en `/complete-profile`).
4. Migración `supabase/migrations/<fecha>_user_acquisition.sql`: tabla `public.user_acquisition (user_id uuid pk references auth.users, ft_* text, lt_* text, signup_cta text, signup_plan_hint text, ga_client_id text, created_at)` con RLS (inserción única del propio usuario; lectura para él y para admin) y trigger en `auth.users` que copia desde `raw_user_meta_data->'acquisition'`.
5. Vista `v_signup_channel`: `organic_search` (google, bing, duckduckgo, ecosia sin utm), **`ai_assistant`** (chatgpt.com, perplexity.ai, copilot.microsoft.com, gemini.google.com), `paid` (gclid o `utm_medium=cpc`), `referral`, `direct`, `email`, `social`.
6. `/planes`: preseleccionar `plan` y `periodo` si llegan (test A/B 1, §9.4).
7. Stripe: añadir `acquisition_channel` y `campaign` a `metadata` en `create-checkout-session` para cruzar MRR por canal en el panel de administración.
8. Privacidad: actualizar la política (finalidad: analítica de captación; base: interés legítimo, documentado). Nunca guardar el referrer completo con query.
- **Aceptación:** el 100 % de los registros nuevos tiene una fila en `user_acquisition` con canal asignado; una prueba end-to-end (landing → signup → checkout de prueba) deja rastro completo.

### 8.5 Dashboards y cadencia

#### T6.07 · Looker Studio · P1 · M
1. **SEO orgánico (GSC):** clics, impresiones, CTR y posición por **clúster** (campo CASE por patrón de URL o query: VERI\*FACTU, factura electrónica, facturación genérica, autónomos/pymes/gestorías, alternativas, herramientas y plantillas, guías fiscales, módulos, marca); **marca frente a no marca** (regex `facturales|factura les`); CTR de queries en posiciones 1–10 (títulos a mejorar); distribución de posiciones (1–3, 4–10, 11–20, 21–50); páginas con variación a 28 días.
2. **Embudo orgánico → pago** (analítica + Supabase en solo lectura o exportación diaria): sesiones orgánicas → `cta_click` → `sign_up` (BD) → `activation_first_invoice` (BD) → `trial_start` → primer `purchase` → MRR por canal *first-touch* y por página de entrada.
3. **Contenido YMYL:** fecha de última revisión por pieza, días desde la revisión, alertas de más de 90 días sin revisar.
4. **Técnico:** Core Web Vitals (CrUX/PageSpeed API), indexadas frente a no indexadas, errores 404 y 5xx.
5. **Autoridad y GEO:** dominios referentes (SE Ranking), menciones de marca y set de 30 prompts.

#### T6.08 · Seguimiento de posiciones · P1 · S
Proyecto en SE Ranking con Google España (móvil y escritorio) y Bing, grupos de keywords por clúster (§5.3, 100–150 keywords prioritarias), competidores (Holded, Quipu, Billin, Contasimple, Anfix, FacturaDirecta, STEL Order, getrenn) y auditoría mensual del sitio.

**Cadencia de revisión:**
- **Semanal (30 min):** GSC (picos, caídas, queries nuevas, errores de indexación), registros por canal, alertas normativas, posiciones de las keywords P1.
- **Mensual:** informe por clúster, CTR y títulos; embudo completo; enlaces conseguidos; menciones en IA; contenidos a actualizar; repriorizar el calendario editorial.
- **Trimestral:** revisión de OKR (§8.6), auditoría técnica, revisión YMYL completa con el asesor, recalibrar previsiones y presupuesto.

### 8.6 Objetivos SMART y KPIs (30 / 60 / 90 / 180 / 365 días)

Fechas de referencia: **30 d = 17/11/2026 · 60 d = 17/12/2026 · 90 d = 16/01/2027 · 180 d = 16/04/2027 · 365 d = 18/10/2027.**

#### 8.6.1 Métricas verificables (dependen solo de la ejecución)

| Plazo | Técnico y medición | Contenido y legal | Autoridad y GEO |
|---|---|---|---|
| **30 d** | Host único, archivos internos retirados, 404 propia, HSTS y caché (T2.02–T2.04, T2.09). Despliegue automatizado y producción = repo (T2.05). GSC + Bing + IndexNow (T6.01–T6.02). Analítica y `cta_click` en producción (T6.03). Atribución en `user_acquisition` (T6.05–T6.06) | **0 afirmaciones ALTA de la §3.2.3 sin corregir.** Guía VERI\*FACTU y guía de factura electrónica actualizadas y revisadas. ≥ 4 piezas nuevas o actualizadas | LinkedIn, Crunchbase y fichas de Capterra/G2 creadas. `robots.txt` y `llms.txt` publicados. Primera medición del set de 30 prompts (línea base) |
| **60 d** | Cabecera y pie estáticos (T2.06); migración a URLs limpias completada con 0 enlaces rotos (T3.03); Lighthouse móvil ≥ 97 y LCP ≤ 1,8 s en las 4 páginas tipo (T2.13); grafo JSON-LD sin errores (T2.14) | 10–12 piezas acumuladas; titles y meta de las 20 páginas (T2.15); 5 módulos reorientados (T3.18); `/autonomos/`, recurrentes y recordatorios publicados; 100 % de las piezas fiscales con revisor visible | 5–10 dominios referentes nuevos de calidad (no del grupo); alta en 4 comparadores citados por LLM |
| **90 d** | ≥ 95 % de las URLs del sitemap indexadas en Google y Bing; dashboards de Looker Studio activos (T6.07); seguimiento de posiciones operativo (T6.08) | 16–20 piezas; calendario fiscal 2027 y 1 herramienta (calculadora IVA + IRPF) publicados; ≥ 3 alternativas publicadas | 10–20 dominios referentes; inclusión en ≥ 2 comparativas de terceros; ≥ 10 reseñas reales |
| **180 d** | CWV «buenas» en ≥ 90 % de las URLs (datos de campo) | 35–45 piezas; generador de facturas publicado; 2 revisiones YMYL trimestrales hechas; 0 afirmaciones desactualizadas en la auditoría | 25–40 dominios referentes (≥ 8 de medios o instituciones con DIR ≥ 50); 5 comparativas de terceros; 25 reseñas; 6/7 perfiles de entidad |
| **365 d** | Sin incidencias técnicas abiertas P0/P1 | 70–90 piezas; clústeres completos (VERI\*FACTU, factura electrónica, facturación, impuestos, cobros, inventario, autónomos, pymes); estudio propio publicado | 50–120 dominios referentes; 12 comparativas de terceros; 80 reseñas; Wikidata |

#### 8.6.2 Métricas de resultado ([PREVISIÓN], rango P10–P90, muy incierta)

| Plazo | Impresiones no marca/mes (GSC) | Clics orgánicos/mes | Keywords en el top 10 | Registros orgánicos/mes (*first-touch*) | Clientes de pago orgánicos nuevos/mes | MRR orgánico nuevo acumulado | Cuota de voz IA | Menciones en el set de 150 (30 × 5) |
|---|---|---|---|---|---|---|---|---|
| 30 d | 1.000–5.000 | 20–100 | 0–5 | 0–5 | 0–1 | 0–15 € | 0 % | 0–2 |
| 60 d | 3.000–12.000 | 50–300 | 2–12 | 2–12 | 0–2 | 5–35 € | 0–0,2 % | 1–5 |
| 90 d | 5.000–25.000 | 100–600 | 5–25 | 5–25 | 1–4 | 10–60 € | 0–0,3 % | 2–8 |
| 180 d | 20.000–80.000 | 500–2.500 | 20–80 | 20–80 | 3–12 | 50–250 € | 0,2–0,5 % | 5–12 |
| 365 d | 60.000–250.000 | 2.000–10.000 | 60–250 | 60–300 | 8–40 | 300–1.500 € | 0,5–2 % | 15–30 |

**Supuestos:** CTR medio inicial del 1,5–4 % con posiciones medias de 15–40; de visita a registro, 1,5–3 % en páginas de producto y 0,3–1 % en el blog; de registro a pago, 8–15 % (depende de B6); ARPU de ~10 €/mes (mezcla Starter/Pro, mensual/anual); 4–8 piezas al mes y campaña de enlaces activa; sin presupuesto de pago. **Riesgo de calendario:** si el aplazamiento a 2028 se publica, la demanda de «verifactu» bajará en 2027 y repuntará en 2028; la factura electrónica (octubre de 2027 para > 8 M€) será el nuevo pico. Recalibrar cada trimestre con datos reales.

#### 8.6.3 Objetivos SMART

- **O1 · Exactitud YMYL:** antes del **15/11/2026**, el 100 % de las afirmaciones fiscales de la web tendrá fuente primaria enlazada y revisión de un asesor colegiado, y habrá 0 afirmaciones de cumplimiento VERI\*FACTU no respaldadas por una declaración responsable firmada. *Medición:* auditoría con `build-check` + revisión manual.
- **O2 · Medición:** antes del **17/11/2026**, el 100 % de los registros nuevos tendrá *first-touch* en `user_acquisition` y el embudo orgánico → registro → pago será visible en Looker Studio.
- **O3 · Base técnica:** antes del **17/12/2026**, el sitio estará en URLs limpias, rastreable sin JS (enlaces sin JS ≥ 90 % de los enlaces con JS) y con Lighthouse móvil ≥ 97 en las 4 páginas tipo.
- **O4 · Visibilidad:** antes del **16/04/2027**, ≥ 20.000 impresiones no marca al mes en GSC y ≥ 20 keywords de los clústeres P1 en el top 10 de Google España (SE Ranking).
- **O5 · Autoridad:** antes del **16/04/2027**, ≥ 25 dominios referentes nuevos (no del grupo), de los que ≥ 8 son medios o instituciones con DIR ≥ 50.
- **O6 · GEO:** antes del **18/10/2027**, Facturales aparece en ≥ 15 de las 150 respuestas del set de prompts y la exactitud de lo que dicen los LLM sobre Facturales es ≥ 90 %.
- **O7 · Negocio ([PREVISIÓN]):** antes del **18/10/2027**, ≥ 100 registros orgánicos al mes y ≥ 10 altas de pago orgánicas al mes, medidas en Supabase.

---

## 9. CRO: del tráfico orgánico al cliente de pago

### 9.1 Embudo y métricas

| Etapa | Definición | Métrica | Fuente |
|---|---|---|---|
| Visita | Sesión orgánica en la landing | Sesiones por clúster y tipo de página | Analítica sin cookies |
| Interacción | Herramienta, descarga, FAQ, conmutador de precios, scroll ≥ 50 % | % de sesiones con interacción | Analítica |
| Intención | Clic en un CTA de registro | CTR por `cta_location` | `cta_click` |
| Registro | Cuenta creada | Registros / clics | Supabase |
| Verificación y perfil | Email confirmado; perfil completado | % | App |
| Prueba | Checkout con prueba de 14 días | Pruebas / registros | Stripe webhook |
| **Activación** | **Primera factura emitida** (o primer presupuesto o extracto importado) en 7 días | % activados | BD |
| Pago | Primer cobro al acabar la prueba | Prueba → pago | Stripe |
| Retención | Activo en los meses 2–3 | % | BD |

### 9.2 Cambios por página (hipótesis a validar con datos)

| ID | Página | Cambio | Métrica |
|---|---|---|---|
| T9.01 | Home y precios | `?plan=` y `periodo=` en los botones de plan; preselección en `/planes` (T6.06) | Checkout iniciado |
| T9.02 ⛔ B6 | Precios | FAQ honesta «¿Me pedís tarjeta para la prueba?» con el comportamiento real de Stripe | Prueba iniciada |
| T9.03 ⛔ B6 | Todos los CTA | Microcopy bajo el CTA: A «14 días de prueba · Sin permanencia · Cancela cuando quieras» o B «Pruébalo 14 días. Si cancelas antes, no pagas nada» (solo si es exacto). Revisar «Empieza **gratis** 14 días» | CTR / prueba |
| T9.04 | Precios | Tabla con inventario, recurrentes, recordatorios, bancos, cobros y gastos por plan; selector «¿Qué plan necesito?» (clientes, facturas al mes, usuarios); bloque «Para gestorías»; datos de la empresa | Clic en plan |
| T9.05 | Home | Franja de confianza bajo el hero (datos en la UE · verificación en dos pasos · sin permanencia · empresa española · registro de facturación con QR, según B1); bloque «Recursos gratis» (generador, plantillas, calendario) para el tráfico que aún no está listo | CTR del hero |
| T9.06 | Landings de función | CTA intermedio tras «Así se ve en la app» (p. ej. «Importa tus clientes desde Excel»), bloque de límites por plan, enlace a la guía del clúster | CTR intermedio |
| T9.07 | Guías y blog | CTA contextual por clúster + *lead magnet* (checklist VERI\*FACTU en PDF, calendario `.ics`) + caja lateral fija en escritorio | Leads/visita |
| T9.08 | Contacto | Formulario real (servicio en la UE o `mailto` con plantilla), tiempos de respuesta por plan, enlace a la FAQ | Contactos |

### 9.3 Bloques de confianza permitidos

- **Seguridad:** «Datos alojados en la UE» · «Verificación en dos pasos» · «Historial de cambios» · «Exporta o elimina tu cuenta cuando quieras».
- **Cumplimiento:** según B1 («Registro de facturación con huella encadenada y QR»; remisión «en preparación») · «Descarga en Facturae 3.2.2».
- **Comercial:** «Sin permanencia» · «14 días de prueba» · «Precios + IVA, sin sorpresas» · «Hasta −25 % en anual».
- **Producto real:** capturas reales con datos de ejemplo · «Tu gestoría entra con su propio usuario, consulta, exporta y cierra los meses».
- **Empresa** (B5): «Facturales es un producto de AVENUE DIGITAL GROUP, S.L. (Valladolid)».

### 9.4 Tests A/B (uno por página; secuenciales o bayesianos, mínimo 2–4 semanas)

| # | Página | Variante | Métrica primaria |
|---|---|---|---|
| 1 | Precios y home | Preselección de plan frente a control | Checkout iniciado |
| 2 | Hero de la home | «Empieza tu prueba de 14 días» frente a «Crea tu primera factura» | Registro → primera factura |
| 3 | Bajo el CTA | Microcopy A frente a B frente a nada | Prueba iniciada |
| 4 | Precios | Con o sin bloque «Empresa española + datos en la UE + 2FA» | Clic en plan |
| 5 | Guías | CTA contextual intermedio frente a solo final | CTR a registro |
| 6 | Plantillas | Descarga directa frente a descarga con email opcional | Descargas y leads |
| 7 | Generador | CTA tras la descarga «Guárdala en Facturales» frente a la variante de cumplimiento (según B1) | Registro |
| 8 | Precios | Anual por defecto (actual) frente a mensual por defecto | Prueba + mezcla anual |

Con el tráfico inicial, los tests no tendrán potencia estadística hasta el mes 4–6. Hasta entonces, priorizar cambios de mejora evidente y medir antes/después.

### 9.5 Activación (lo que pasa después del registro y condiciona el pago)

Fuera del alcance de la landing, pero imprescindible para que el SEO se traduzca en MRR (repo `facturales`, propuesta para producto):
- Checklist de primeros pasos: datos fiscales → logo → primer cliente (o importación Excel) → primera factura → activar recordatorios → invitar a la gestoría.
- Emails durante la prueba (Resend, ya usado por `recordatorios-cobro`): día 0 (bienvenida y primera factura), día 2 (importar clientes), día 5 (recurrentes y recordatorios), día 9 (303/130 e invitar a la gestoría), día 12 (aviso transparente de fin de prueba).
- Onboarding adaptado al origen (`utm_campaign`): quien llega por inventario empieza por el catálogo; quien llega por VERI\*FACTU, por los datos fiscales y la primera factura.

---

## 10. Roadmap consolidado y priorización

### 10.1 Calendario por semanas y meses

| Periodo | Fase | Entregables | Hito de control |
|---|---|---|---|
| **Semana 0** (19–25/10/2026) | 1 | Validación de este plan; respuestas a B1–B10; validar HX01–HX08; contratar o asignar revisor (B4) | Plan aprobado |
| **Semana 1** (26/10–01/11) | 2, 6 | T2.01 ⛔ (copy VERI\*FACTU), T2.02–T2.04 (host, internos, `.htaccess`), T6.01–T6.03 (GSC, Bing, analítica) | 0 afirmaciones ALTA; GSC verificado |
| **Semana 2** (02–08/11) | 2, 4, 6 | T2.05 ⛔ (despliegue), T4.01–T4.02 (guías VERI\*FACTU y factura electrónica), noticia + nota de prensa, T6.05–T6.06 (atribución) | Producción = repo; guías revisadas publicadas |
| **Semanas 3–4** (09–22/11) | 2, 3, 5 | T2.06–T2.09 (cabecera/pie estáticos, build-check, rutas absolutas, 404), T2.10–T2.12 (rendimiento), T2.14 (JSON-LD), T2.17–T2.18 (legales, sobre nosotros), T5.05–T5.06 (robots, llms.txt) | **Hito 30 d** (17/11) |
| **Semanas 5–6** (23/11–06/12) | 3 | **T3.03 migración a URLs limpias** + T2.15 (titles) + T3.18 (5 módulos) | 0 enlaces rotos; 301 validados |
| **Semanas 7–8** (07–20/12) | 3, 4 | `/autonomos/`, recurrentes, recordatorios, `/alternativas/holded/` y `/contasimple/`, calendario fiscal 2027, `/facturales-en-datos/` | **Hito 60 d** (17/12) |
| **Mes 3** (ene 2027) | 3, 4, 5 | Guías 303/130/390, calculadora IVA + IRPF, `/gestorias/`, alternativa a Quipu; perfiles de entidad; comparadores | **Hito 90 d** (16/01) |
| **Meses 4–6** (feb–abr) | 4, 5 | Generador de facturas y presupuestos, guías de tipos de factura, listicle, `/pymes/`, primeros sectores, plantillas, partners de gestorías, pitch a comparativas de terceros | **Hito 180 d** (16/04) |
| **Meses 7–9** (may–jul) | 4, 5 | Clúster VERI\*FACTU según escenario A/B, sectores, guías de inventario y cobros, glosario, YouTube, encuesta | Revisión trimestral |
| **Meses 10–12** (ago–oct) | 4, 5, 6 | Factura electrónica (octubre de 2027), estudio propio y PR nacional, calendario 2028, revisión anual | **Hito 365 d** (18/10/2027) |

### 10.2 Matriz de priorización de iniciativas

Impacto SEO y retorno comercial: 1–5. Coste: € (< 500 €), €€ (500–3.000 €), €€€ (> 3.000 €), con horas internas aparte. [ESTIMACIÓN]

| Iniciativa | Impacto SEO | Retorno comercial | Esfuerzo | Coste externo | Riesgo | Prioridad |
|---|---|---|---|---|---|---|
| Saneamiento legal VERI\*FACTU (T2.01, B1) | 4 | 5 (evita daño) | M | €€ (asesor) | B (de hacerlo) / A (de no hacerlo) | **P0** |
| Higiene técnica (host, internos, 404, cabeceras) | 4 | 3 | S | — | B | **P0** |
| Despliegue reproducible con lista blanca | 3 | 3 | M | — | B | **P0** |
| Medición + atribución | 2 (indirecto) | 5 | M | € (analítica, CMP) | B | **P0** |
| Guías VERI\*FACTU y factura electrónica actualizadas | 5 | 4 | M | €€ (revisión) | M (YMYL) | **P0** |
| Cabecera y pie estáticos | 4 | 2 | M | — | M | P1 |
| Migración a URLs limpias | 3 (medio plazo) | 2 | L | — | M | P1 |
| Titles, meta y 5 módulos con KD < 10 | 5 | 4 | M | — | B | **P1 (quick win)** |
| Landings de segmento (autónomos, pymes, gestorías) | 5 | 5 | L | € | B | P1 |
| `/programa-verifactu/` | 5 | 5 | M | € | M (depende de B1) | P1 ⛔ |
| Recurrentes y recordatorios (landings) | 3 | 4 | M | — | B | P1 |
| Alternativas (8 páginas) | 4 | 5 | M c/u | € (revisión jurídica) | M | P1 |
| Rendimiento (main.css, fuentes, LCP) | 3 | 2 | M | — | M (visual) | P1 |
| Grafo JSON-LD + entidad | 3 | 2 | M | — | B | P1 |
| Legales en HTML + sobre nosotros | 3 | 3 | M | € (legal) | B | P1 |
| Generador de facturas y presupuestos | 5 | 4 | XL | €–€€ | M | P1 |
| Calculadoras | 4 | 3 | M | — | B | P1 |
| Plantillas (10) | 4 | 3 | M | € (diseño) | B | P1 |
| Guías fiscales de long tail (~20) | 4 | 3 | L | €€ (revisión) | M (YMYL) | P1–P2 |
| Sectores (12) | 3 | 4 | M c/u | € (revisión fiscal de exenciones) | M | P2 |
| Directorios y comparadores citados por LLM | 3 | 3 | S | — / € | B | P1 |
| Digital PR (notas, encuesta, estudio) | 4 | 3 | L | €€ | M | P2 |
| Glosario (30–50 términos) | 3 | 1 | M | € | B | P2 |
| Partners de gestorías | 3 | 5 | L | — | B | P2 |
| YouTube | 2 | 2 | M | € | B | P2 |

### 10.3 Estimación de recursos [ESTIMACIÓN]

| Partida | 0–3 meses | 3–12 meses | Comentario |
|---|---|---|---|
| Desarrollo (landing + app) | 80–120 h | 120–200 h | Base técnica, migración, atribución, herramientas |
| Contenido (redacción + edición) | 60–90 h | 300–450 h | 4–8 piezas al mes |
| Revisión experta (asesor/abogado/graduado social) | 10–20 h | 40–80 h | La mayor partida externa; imprescindible en YMYL |
| Diseño (plantillas, capturas por sector, OG por artículo) | 10–20 h | 40–60 h | Respetar el design system |
| Herramientas | SE Ranking (ya disponible), Plausible/Umami (~10–20 €/mes o autoalojado), CMP (0–15 €/mes), Looker Studio (gratis) | ídem | Sin herramientas de pago nuevas imprescindibles |
| Digital PR | 0–500 € | 1.000–3.000 € | Distribución de notas, encuesta con asociación; nunca enlaces comprados sin `rel="sponsored"` |

---

## 11. Checklist técnico

Marcar al completar. Cada línea remite a su tarea y a su prueba.

**Indexación y servidor**
- [ ] Un solo host: www y http → 301 en un salto a `https://facturales.es` (T2.02 · §13.1)
- [ ] `/index.html` → 301 a `/`; 0 enlaces internos a `index.html` (T2.02)
- [ ] Archivos internos (md, py, njk, map, scss, lock, partials, docs, tools, scripts) → 403/404 (T2.03 · §13.2)
- [ ] `.htaccess` o directivas nginx versionados en el repo (T2.04)
- [ ] 404 propia con código 404 real (T2.09)
- [ ] HSTS, `nosniff`, `Referrer-Policy`, `Cache-Control` por tipo y charset UTF-8 (T2.04 · §13.3)
- [ ] Plantillas demo → 410; `news*.html` → 301 (T2.04)
- [ ] `/confirm-email` y `/reset-password` resueltos (T2.04, verificar Supabase Auth)
- [ ] Despliegue automatizado con lista blanca; producción = repo (T2.05 · §13.5)

**Rastreo y enlazado**
- [ ] Cabecera y pie en HTML estático; sin `document.write` (T2.06 · §13.6)
- [ ] Rutas absolutas desde la raíz (T2.08)
- [ ] URLs limpias + mapa 1:1 de 301 sin cadenas (T3.03 · §13.8)
- [ ] Sitemap con solo URLs indexables, `lastmod` real y sin `priority` (T2.07 · §13.9)
- [ ] Ninguna página indexable huérfana; cada página nueva con ≥ 3 enlaces internos estáticos (§5.5)
- [ ] Migas visibles + `BreadcrumbList` (T2.14)
- [ ] `robots.txt` con política de bots de IA (T5.05)
- [ ] `llms.txt` y `llms-full.txt` (T5.06)

**On-page y datos estructurados**
- [ ] Un `h1` por página; titles ≤ 65; descriptions 120–158 (T2.15 · `build-check`)
- [ ] Grafo JSON-LD con `@id`: Organization (con `legalName`, `vatID`, `address`, `sameAs` reales), WebSite, SoftwareApplication (6 ofertas sin IVA), WebPage, BreadcrumbList, Article/BlogPosting (autor Person, `dateModified`, `reviewedBy`) (T2.14)
- [ ] Logo PNG 512×512 a partir del archivo oficial (T2.14)
- [ ] FAQ visible = `FAQPage` (§13.4)
- [ ] `favicon.ico`, `apple-touch-icon`, `site.webmanifest` (T2.16)

**Rendimiento**
- [ ] `main.css` fuera de las páginas reales; cubo en `fx-rombo.css` solo en la home (T2.10)
- [ ] Onest autoalojada con `preload` (T2.11)
- [ ] `<picture>` en el hero adaptable; sin descargar la captura oculta en móvil (T2.12)
- [ ] Lighthouse móvil ≥ 97, LCP ≤ 1,8 s, CLS < 0,05 en las 4 páginas tipo (T2.13 · §13.7)

**Confianza, legal y medición**
- [ ] 0 afirmaciones ALTA de la §3.2.3 (T2.01, T4.01–T4.02)
- [ ] Legales en HTML en `facturales.es`, sin cláusula anti-enlaces, con política de cookies real (T2.17)
- [ ] Sobre nosotros con empresa y equipo (T2.18)
- [ ] GSC (dominio + prefijos), Bing, IndexNow (T6.01–T6.02)
- [ ] Analítica sin cookies + eventos; GA4 con Consent Mode v2 y CMP si se aprueba (T6.03–T6.04)
- [ ] Atribución *first-touch* en `user_acquisition` y canal `ai_assistant` (T6.05–T6.06)
- [ ] Dashboards y seguimiento de posiciones (T6.07–T6.08)

---

## 12. Backlog ejecutable por archivo

Repo `L` = `facturales-landing`; repo `A` = `facturales` (app). Semana = semana desde la aprobación del plan.

| ID | Tarea | Repo · archivos principales | Depende de | Prio | Esf. | Sem. |
|---|---|---|---|---|---|---|
| T2.01 | Copy VERI\*FACTU saneado | L · `index.html`, `faq.html`, `crea-envia-facturas.html`, `pricing.html`, `funciones.html`, `impuestos.html`, `about.html`, 3 artículos, `CLAUDE.md` · A · `verifactu-qr.ts`, `VistaPreviaFacturaVg.tsx`, `InvoicePreviewPage.tsx` (según B1) | **B1** | P0 | M | 1 |
| T2.02 | Host único e `index.html` → `/` | L · `.htaccess`, 20 HTML, `header-include.js`, `footer-include.js` | B2, HX01 | P0 | S | 1 |
| T2.03 | Retirar archivos internos | L · servidor, `fix_*.py`, `update_*.py`, `remove_comments.py`, `verify_title_case.py`, `service copy.html`, `service-details copy.html` | B2 | P0 | S | 1 |
| T2.04 | `.htaccess` de base | L · `.htaccess` (nuevo) | HX01 | P0 | S | 1 |
| T2.05 | Despliegue con lista blanca + IndexNow | L · `.github/workflows/deploy.yml` (nuevo) | **B2**, T2.07 | P0 | M | 2 |
| T2.06 | Cabecera y pie estáticos | L · `partials/header.html`, `partials/footer.html`, `partials/head-common.html`, `scripts/sync-partials.mjs` (nuevos), todos los HTML, `facturales.js`; retirar `header-include.js`, `footer-include.js`, `partials/header.njk`; `CLAUDE.md` | — | P1 | M | 3 |
| T2.07 | Controles de calidad + sitemap | L · `scripts/build-check.mjs` (nuevo), `sitemap.xml`, `.github/workflows/check.yml` | — | P1 | S | 3 |
| T2.08 | Rutas absolutas | L · todos los HTML, `partials/*`, `404.html`, CSS | — | P1 | M | 3 |
| T2.09 | 404 propia | L · `404.html`, `.htaccess` | T2.08 | P1 | S | 3 |
| T2.10 | Retirar `main.css` | L · `assets/css/fx-rombo.css` (nuevo), `main.css`, todos los HTML, `CLAUDE.md` | — | P1 | M | 3–4 |
| T2.11 | Onest autoalojada | L · `assets/fonts/onest-var.woff2` (nuevo), `facturales-ds.css`, `partials/head-common.html` | T2.06 | P1 | S | 3–4 |
| T2.12 | `<picture>` en el hero adaptable | L · `index.html` y páginas con `fx-adaptable`, `facturales-ds.css` | — | P1 | S | 3–4 |
| T2.14 | Grafo JSON-LD | L · todos los HTML, `assets/img/logo/facturales-logo-512.png` (nuevo) | B5 | P1 | M | 3–4 |
| T2.15 | Titles, meta y H1 | L · 20 HTML | — | P1 | S | 5 |
| T2.16 | Iconos y manifest | L · `favicon.ico`, `apple-touch-icon.png`, `site.webmanifest` (nuevos) | T2.06 | P3 | S | 6 |
| T2.17 | Legales en HTML | L · `legal/*/index.html` (nuevos), `partials/footer.html` · A · `LegalContent.tsx` | B5, B10 | P1 | M | 4 |
| T2.18 | Sobre nosotros | L · `about.html` → `sobre-nosotros/index.html` | B5 | P1 | S | 4 |
| T3.03 | Migración a URLs limpias | L · `git mv` de 20 páginas a carpetas, `.htaccess`, `sitemap.xml`, `llms.txt`, `partials/*`, JSON-LD | T2.04, T2.06, T2.08 | P1 | L | 5–6 |
| T3.10 | `/funciones/` ampliada | L · `funciones/index.html` | T3.03 | P1 | M | 7 |
| T3.11 | `/precios/` mejorada | L · `precios/index.html` | B6 | P1 | S | 7 |
| T3.12 | `/programa-verifactu/` | L · nueva | **B1**, T4.01 | P1 | M | 8+ |
| T3.13 | `/autonomos/` | L · nueva | T3.03 | P1 | M | 7 |
| T3.14 | `/funciones/facturas-recurrentes/` | L · nueva | B7 | P1 | M | 7 |
| T3.15 | `/funciones/recordatorios-de-pago/` | L · nueva | B7 | P1 | M | 8 |
| T3.16 | `/gestorias/` | L · nueva | B7 | P1 | M | 10 |
| T3.17 | `/pymes/` | L · nueva | — | P2 | M | 18 |
| T3.18 | Reorientar 5 módulos | L · stock, cobros, panel, clientes, gastos | T2.15 | P1 | M | 5–6 |
| T3.19 | Equipo/gestoría y seguridad | L · nuevas | B7 | P2 | S | 30+ |
| T3.20 | `/facturales-en-datos/` | L · nueva | B5 | P1 | S | 8 |
| T3.21 | Sectores (lotes) | L · `/sectores/*` | B7, B4 | P2 | M c/u | 20+ |
| T3.22 | Alternativas (8) | L · `/alternativas/*` | §6.4, B4 | P1 | M c/u | 6+ |
| T4.01 | Hub VERI\*FACTU | L · `guias/verifactu/index.html` | B4 (B1 para el bloque de producto) | P0 | M | 2 |
| T4.02 | Factura electrónica | L · `guias/factura-electronica/`, artículo comparativo | B4 | P0 | M | 2 |
| T4.03 | Artículo de contabilidad corregido | L · artículo | — | P1 | S | 3 |
| T4.04 | FAQ y producto (Facturae, 130, tabla de precios) | L · `faq.html`, `impuestos.html`, `pricing.html` | B6 | P1 | S | 3 |
| T4.10+ | Calendario editorial (§6.3) | L · nuevas | Protocolo §6.5 | P1–P2 | — | 6–52 |
| T4.40 | Notas de prensa y PR | — | T4.01 | P1 | S | 2+ |
| T5.05 | `robots.txt` | L · `robots.txt` | — | P1 | S | 3 |
| T5.06 | `llms.txt` + `llms-full.txt` | L · `llms.txt`, `scripts/build-llms.mjs` (nuevo) | B1, B5 | P1 | S | 4 |
| T5.04 | Declaración responsable pública | L · nueva · A · Ayuda › Acerca de | **B1 (firmada)** | P1 | S | — |
| T5.10–13 | Perfiles de entidad | Externos + `sameAs` | B8 | P1–P3 | S | 4–12 |
| T6.01 | Search Console | DNS (IONOS) | — | P0 | S | 1 |
| T6.02 | Bing + IndexNow | L · `<clave>.txt`, deploy | T2.05 | P0 | S | 1–2 |
| T6.03 | Analítica sin cookies | L · `partials/head-common.html` (o cada `<head>` antes de T2.06), `facturales.js` | B3 | P0 | S | 1 |
| T6.04 | GA4 + Consent Mode + CMP | L · `head-common`, `footer` · A · `index.html`, `vercel.json` (CSP) | B3 | P1 | M | 4 |
| T6.05 | Atribución en la landing | L · `facturales.js`, `data-cta-location`/`data-plan` en los CTA | — | P0 | S | 2 |
| T6.06 | Atribución en la app | A · `use-acceso.ts`, `acceso.ts`, `auth.service.ts`, `supabase/migrations/…_user_acquisition.sql`, `create-checkout-session`, `/planes` | T6.05 | P0 | M | 2 |
| T6.07 | Looker Studio | Externo | T6.01–T6.06 | P1 | M | 6 |
| T6.08 | Posiciones (SE Ranking) | Externo | — | P1 | S | 2 |
| T9.01–08 | CRO | L · home, precios, landings, guías, contacto · A · `/planes` | B6, T6.05 | P1 | S–M | 6+ |

---

## 13. Pruebas de validación (scripts)

Ejecutables desde la raíz del repo de la landing. Sustituir `BASE` por la URL de staging cuando proceda.

### 13.1 Redirecciones de host
```bash
for u in http://www.facturales.es/ https://www.facturales.es/ http://facturales.es/ https://facturales.es/index.html; do
  curl -s -o /dev/null -w "$u -> %{http_code} %{redirect_url}\n" "$u"
done
# Esperado: 301 https://facturales.es/ en los cuatro (un solo salto)
```

### 13.2 Archivos internos no públicos
```bash
for p in CLAUDE.md PLAN_MAESTRO_SEO_FACTURALES.md fix_title_case.py update_articles.py partials/header.njk \
         package-lock.json assets/css/main.css.map assets/scss/main.scss "service%20copy.html" docs/ scripts/; do
  printf "%s " "$p"; curl -s -o /dev/null -w "%{http_code}\n" "https://facturales.es/$p"
done
# Esperado: 403, 404 o 410 en todos
```

### 13.3 Cabeceras
```bash
curl -sI https://facturales.es/ | grep -iE "strict-transport|x-content-type|referrer-policy|cache-control|content-type"
curl -sI "https://facturales.es/assets/css/facturales-ds.css?v=$(grep -o 'facturales-ds.css?v=[0-9]*' index.html | head -1 | cut -d= -f2)" | grep -i cache-control
# Esperado: HSTS presente; HTML "no-cache"; CSS "max-age=31536000, immutable"; charset=utf-8
```

### 13.4 Coherencia FAQ visible / JSON-LD
```bash
python3 -I - <<'PY'
import json, re, glob, html
for f in glob.glob("**/*.html", recursive=True):
    s = open(f, encoding="utf-8").read()
    text = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", " ", s, flags=re.S)))
    text = re.sub(r"\s+", " ", text)
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        data = json.loads(block)
        nodes = data.get("@graph", [data])
        for n in nodes:
            if n.get("@type") == "FAQPage":
                for q in n["mainEntity"]:
                    if q["name"] not in text:
                        print("FALTA EN VISIBLE:", f, "->", q["name"])
print("ok")
PY
```

### 13.5 Producción = repo
```bash
for f in index.html sitemap.xml robots.txt; do
  curl -s "https://facturales.es/$f" | cmp -s - "$f" && echo "OK $f" || echo "DIFIERE $f"
done
```

### 13.6 Rastreo sin JavaScript (enlaces con JS ≈ sin JS)
```bash
# Sin JS: enlaces internos en el HTML servido
for u in / /precios/ /sobre-nosotros/ /guias/verifactu/; do
  n=$(curl -s "https://facturales.es$u" | grep -oE 'href="/[^"]*"' | sort -u | wc -l)
  echo "$u enlaces internos sin JS: $n"
done
# Esperado: >= 25 en cada página y presencia de /sobre-nosotros/ y /legal/aviso-legal/
curl -s https://facturales.es/ | grep -c 'href="/legal/aviso-legal/"'   # >= 1
```
Comparación completa con Playwright (Chromium preinstalado en `/opt/pw-browsers`): cargar cada página con `javaScriptEnabled: true` y `false` y comparar el número de `a[href^="/"]` únicos; la diferencia debe ser < 10 %.

### 13.7 Rendimiento
```bash
CHROME_PATH=$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome | head -1) \
npx lighthouse https://facturales.es/ --form-factor=mobile --only-categories=performance,seo \
  --output=json --output-path=./lh-home.json --quiet --chrome-flags="--headless=new"
node -e 'const r=require("./lh-home.json");console.log("perf",r.categories.performance.score*100,"LCP",r.audits["largest-contentful-paint"].displayValue,"CLS",r.audits["cumulative-layout-shift"].displayValue)'
# Repetir para /precios/, /funciones/facturacion/ y /guias/verifactu/. Esperado: perf >= 97, LCP <= 1,8 s
```

### 13.8 Mapa de 301 de la migración
```bash
# redirects.tsv: "ruta_antigua<TAB>ruta_nueva", una línea por URL de la §5.2
while IFS=$'\t' read -r old new; do
  r=$(curl -s -o /dev/null -w "%{http_code} %{redirect_url}" "https://facturales.es/$old")
  [ "$r" = "301 https://facturales.es$new" ] && echo "OK  $old" || echo "MAL $old -> $r (esperado $new)"
done < redirects.tsv
```

### 13.9 Sitemap sano
```bash
curl -s https://facturales.es/sitemap.xml | grep -o '<loc>[^<]*' | sed 's/<loc>//' | while read -r u; do
  code=$(curl -s -o /tmp/p.html -w "%{http_code}" "$u")
  canon=$(grep -o '<link rel="canonical" href="[^"]*"' /tmp/p.html | cut -d'"' -f4)
  noidx=$(grep -ci 'name="robots" content="[^"]*noindex' /tmp/p.html)
  [ "$code" = 200 ] && [ "$canon" = "$u" ] && [ "$noidx" = 0 ] || echo "PROBLEMA $u ($code, canonical=$canon, noindex=$noidx)"
done
# Esperado: sin salida
```

### 13.10 Claims prohibidos
```bash
grep -rniE "sin tarjeta|30 ?%|homologad|certificad[oa] (por|veri)|cumple con veri|listas para veri|env[ií]o autom[aá]tico a la aeat|presenta(mos)? (tus|los) (impuestos|modelos)|testimonio|clientes satisfechos|★" \
  --include=*.html --include=*.js --include=*.txt . | grep -v "^./docs/" || echo "ok"
```

---

## 14. Qué NO hacer

**Técnicas que pueden provocar penalizaciones o pérdida de confianza:**
- Contenido masivo o generado sin revisión para «cubrir keywords» (páginas de ciudad × sector, variantes casi idénticas, glosario de cientos de términos genéricos).
- Comprar enlaces, PBN, intercambios recíprocos masivos, directorios de baja calidad, notas de prensa patrocinadas sin `rel="sponsored"`.
- Reseñas falsas, de empleados o del grupo, o incentivadas solo si son positivas; `aggregateRating` sin reseñas reales en la página.
- *Cloaking*, texto oculto, *keyword stuffing* en titles o anchors.
- Páginas de alternativas que imiten la marca ajena, denigren o usen datos no verificados.
- Cambiar `dateModified` sin cambios reales para parecer «fresco».
- FAQ en JSON-LD que no estén visibles en la página.

**Reglas de marca y producto (`CLAUDE.md`) que este plan no toca:**
- Identidad visual: logo oficial (nunca reconstruido como texto), Onest, tokens `--fx-*`, cubo animado del hero como único elemento en movimiento, `.fx-claro` solo para lectura larga, capturas reales marcadas como tales.
- Claims prohibidos: testimonios, cifras de clientes, valoraciones, «sin tarjeta», presentación automática a la AEAT, banca conectada como disponible, «−30 %».
- Precios: exactamente los de `plans-config.service.ts`; prueba de 14 días.
- Accesibilidad: un `h1`, foco visible, objetivos ≥ 44 px, contraste AA, `lang="es"`, `prefers-reduced-motion`.

**Riesgos operativos:**
- No desplegar el repo entero al servidor: **este plan y los informes de auditoría quedarían públicos** (incluyen análisis legales internos). Desplegar solo con lista blanca (T2.05) y con el `.htaccess` de T2.04.
- No publicar fechas normativas «anunciadas» como vigentes.
- No ejecutar la migración de URLs sin rutas absolutas y sin la prueba §13.8.

---

## 15. Anexos y fuentes

### 15.1 Informes de auditoría (detalle completo)

| Archivo | Contenido |
|---|---|
| `docs/seo/auditoria-2026-10/01-tecnico.md` | Auditoría técnica: cabeceras, rastreo con/sin JS, grafo de enlaces, on-page por página, JSON-LD, Lighthouse, URLs, app, recomendaciones P0–P3 con validación |
| `docs/seo/auditoria-2026-10/02-keywords-competencia.md` | ~330 keywords en 22 clústeres (SE Ranking), competidores y sus páginas top, brechas, 14 SERPs analizadas, matriz de oportunidades |
| `docs/seo/auditoria-2026-10/03-contenidos-cro.md` | Funciones reales de la app con evidencia, inventario de contenido, errores de los artículos, arquitectura, clústeres, calendario base, plantillas de página, CRO y atribución |
| `docs/seo/auditoria-2026-10/04-geo-autoridad.md` | Backlinks frente a competidores, link gap, cuota de voz en IA y fuentes citadas, comparativas de terceros, señales de entidad, estrategia GEO, 52 objetivos de enlace, KPIs |
| `docs/seo/auditoria-2026-10/05-legal-medicion.md` | Marco normativo VERI\*FACTU, factura electrónica y ViDA con fuentes primarias, revisión jurídica de la web (archivo:línea), protocolo YMYL, plan de medición y KPIs |

> Estos informes son la evidencia del plan. Contienen análisis legales internos: **no deben desplegarse** (T2.03–T2.05).

### 15.2 Fuentes primarias citadas (consultadas el 18/10/2026)

- RD 1007/2023 (consolidado): https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840
- RD-ley 15/2025: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-24446
- Orden HAC/1177/2024: https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138
- Nota del Ministerio de Hacienda, 05/10/2026 (previsión de aplazamiento a octubre de 2028): https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf
- Sede de la AEAT, VERI\*FACTU: https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html
- AEAT, FAQ de declaración responsable: https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/certificacion-sistemas-informaticos-declaracion-responsable.html
- AEAT, FAQ de colaboración social: https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/colaboracion-social.html
- RD 238/2026 (factura electrónica B2B): https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-7295
- Orden HAC/1028/2026 (solución pública de facturación electrónica): https://www.boe.es/buscar/act.php?id=BOE-A-2026-20587
- Directiva (UE) 2025/516 (ViDA): https://eur-lex.europa.eu/eli/dir/2025/516/oj
- Orden HAC/1526/2024 (supresión del modelo 037): https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410
- Orden PJC/297/2026 (cotización 2026): https://www.boe.es/eli/es/o/2026/03/30/pjc297
- Guía de cookies de la AEPD: https://www.aepd.es/guias/guia-cookies.pdf

> Antes de publicar cualquier dato normativo, el revisor debe volver a confirmarlo en la fuente primaria: algunos datos (convalidación del RD-ley 15/2025, fechas exactas de aplicación del RD 238/2026) se han contrastado parcialmente con fuentes secundarias, como se indica en el informe 05.

### 15.3 Datos de mercado

SE Ranking Data API (base `es`, octubre de 2026): `getDomainOverviewByCountry`, `getDomainPages`, `getDomainKeywords`, `getKeywordsMetrics` (~815 keywords consultadas, ~560 con dato), `getSimilarKeywords`, `getRelatedKeywords`, `getDomainKeywordsComparison`, `getSerpResults` (14 SERPs), `getBacklinksSummary`, `getBacklinksRefDomains`, `getAiSearchLeaderboard`, `getAiSearchPromptsByBrand`. Limitaciones: tildes normalizadas, algunos volúmenes de cabeza anómalos, KD que a veces subestima el SERP real, tráfico estimado útil solo para comparar dominios.

### 15.4 Historial del documento

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 18/10/2026 | Primera versión: auditoría completa y plan de 12 meses. Pendiente de validación (§2) |
