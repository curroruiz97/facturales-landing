# Facturales · Arquitectura de contenidos SEO y CRO

> Informe 03 · Estrategia de contenidos + conversión · fecha de análisis: 18/10/2026
> Alcance: web de marketing `/home/user/facturales-landing` (HTML estático) contrastada con la app `/home/user/facturales` (React/Vite/Supabase).
> No se ha modificado ningún archivo de ninguno de los dos repositorios.
>
> El informe tiene tres bloques: **A. HALLAZGOS COMPROBADOS**, cada uno con su evidencia `archivo:línea`; **B. HIPÓTESIS**, que hay que validar con datos o con producto/legal; y **C. RECOMENDACIONES**: arquitectura, clusters, calendario, plantillas y CRO.

---

## 0. Resumen ejecutivo

1. **El producto es más amplio que la web.** La app tiene facturación con series, IVA/IGIC/IPSI, retenciones, rectificativas, recurrentes, importación y recibidas; además presupuestos, inventario, cobros con recordatorios automáticos, bancos por extracto, gastos con OCR, modelos 303 y 130, cierres, un rol Gestor, 2FA y apps. La web lo cuenta en 20 URLs indexables con poco texto (mediana de unas 400 palabras) y **ninguna página por intención comercial genérica** («programa de facturación», «software facturación autónomos»), por sector, por tipo de negocio, de comparativa ni de herramienta gratuita.
2. **El blog es débil en E-E-A-T y tiene errores.** Hay 3 artículos de 380–610 palabras firmados por «Equipo de Facturales», sin fuentes oficiales enlazadas, sin `dateModified` y sin revisor. Errores marcados para revisión legal: (a) la factura electrónica B2B ya tiene reglamento (RD 238/2026), pero el artículo dice que «depende del desarrollo reglamentario»; (b) el artículo de VERI*FACTU no cita el RD-ley 15/2025 ni el RD 1007/2023; (c) la «regla de los 4 NO» no sale de una fuente identificable; (d) el artículo de contabilidad anuncia «6 números» y enumera 7.
3. **Riesgo de coherencia con VERI*FACTU (P0, legal).** La app genera el registro con huella y el QR, pero **la remisión a la AEAT está pendiente**: el catálogo de integraciones la marca como «partial» y la declaración responsable sigue en borrador sin firmar. En la web, los artículos definen VERI*FACTU como «el sistema remite a la AEAT» y luego dicen «Facturales emite facturas con su registro VERI*FACTU». Hace falta un experto que revise la redacción y el uso de la leyenda «VERI*FACTU» en las facturas mientras no se remita.
4. **Atribución nula.** La landing no tiene analítica ni UTM. Los 79 enlaces a `/signup` van sin parámetros y los botones «Probar Pro/Starter/Ilimitado» no preseleccionan plan. La app no lee `utm_*` ni `document.referrer`, aunque `signUp()` ya acepta `metadata` (`auth.service.ts:99-105`), así que guardar el origen es un cambio pequeño.
5. **Fricción real en el embudo.** El recorrido es signup → verificar email → completar perfil → `/planes` → Stripe Checkout (tarjeta) → app. La prueba de 14 días se activa dentro del Checkout de suscripción (`create-checkout-session/app.ts:85-95`). La web no avisa de que se pedirá método de pago, y CLAUDE.md prohíbe decir «sin tarjeta». El microcopy debe ser honesto («cancela antes del día 14 y no se cobra nada»; validarlo con producto).
6. **Propuesta.** Arquitectura con URLs limpias en ~95 páginas objetivo a 12 meses (no contenido masivo):
   - 8 pilares comerciales;
   - 12 landings de función;
   - 3 por tipo de negocio y 12 por sector;
   - 6 comparativas y 6 alternativas;
   - 10 plantillas, 1 generador y 6 calculadoras;
   - 8 guías pilar, unos 40 artículos, glosario y calendario fiscal.

   Más un calendario editorial de 4–8 piezas al mes pegado a la estacionalidad fiscal y un plan CRO con eventos, A/B tests y paso del origen orgánico a la app.

---

# A. HALLAZGOS COMPROBADOS

## A1. Funciones que existen en la app (fuente de verdad para el copy)

| Área | Qué hace (comprobado) | Evidencia | ¿Se puede promocionar? |
|---|---|---|---|
| Facturas | Emisión, borradores, emitidas, recibidas, vista previa, importación de facturas existentes | `facturales/src/app/App.tsx:150-158` | Sí |
| Facturas recurrentes | Semanal, mensual, bimestral, trimestral, semestral y anual. El servidor genera **borradores** (`generar_facturas_recurrentes`) | `src/features/recurrentes/domain/calendario.ts:1-17` | Sí (desde 17/10/2026, CLAUDE.md) |
| Presupuestos | Emisión, borradores, emitidos, vista previa y conversión | `App.tsx:145-149` | Sí |
| Inventario | Existencias, movimientos, precios en bloque, stock mínimo, valor del inventario y CSV | `src/features/inventario/domain/inventario.ts:1-4`, `App.tsx:140-142` | Sí (un solo almacén) |
| Cobros | Pendientes, previsión, antigüedad, por cliente y reparto. Tras el flag `feat_bancos` | `App.tsx:165-168`, `App.tsx:127` | Sí, como «Nuevo» (despliegue gradual, sin fechas) |
| Recordatorios automáticos | Edge function diaria (pg_cron) que envía por email con Resend | `supabase/functions/recordatorios-cobro/index.ts:1-5` | Sí. Ojo: en `cobros/domain/recordatorio.ts:1-3` sigue existiendo un recordatorio manual (mailto) |
| Bancos | Conciliar, cuentas, reglas, historial y conexiones (tras flag). La conexión directa está como «soon» | `App.tsx:172-177`, `integrations-catalog.ts` (id `banco`, status `soon`) | Extractos sí. Conexión directa solo como «Próximamente» |
| Gastos | Movimientos, proveedores, matriz y escaneo OCR (`analyze-expense-document`) | `App.tsx:160,169-171`, `supabase/functions/analyze-expense-document` | Sí («Nuevo») |
| Impuestos | Modelo 303 (IVA repercutido − soportado) y Modelo 130 acumulado (20 %) con retenciones | `src/features/fiscal/domain/fiscal-calc.ts:142-170,218-238` | Sí, como cálculo. **No presenta en la AEAT** |
| Cierres | Cierres mensuales y trimestrales; el gestor cierra meses | `App.tsx:184`, `workspace-role.ts:6,22-24` | Sí |
| Rol Gestor | Solo lectura con interfaz simplificada; contabiliza y cierra meses; inicio en `/cierres` | `src/services/workspace/workspace-role.ts:4-8,22-27`; roles en `src/services/team/team.service.ts:5` | **Sí: base de las landings para gestorías** |
| Facturae 3.2.2 | Descarga del XML **sin firmar** (la firma XAdES requiere certificado) | `src/features/documents/facturae/document-facturae.ts:1-8` | Sí, como «descarga Facturae». No «firmada» |
| VERI*FACTU | Registro de alta con huella SHA-256 encadenada y QR, **solo si `verifactu_enabled=true`**. El envío a la AEAT es un «paso posterior que requiere certificado (Tipo 017)» | `supabase/functions/emit-invoice-verifactu/index.ts:3-11`; `integrations-catalog.ts:79-85` (status `partial`) | Registro y QR sí. **Remisión no** |
| Declaración responsable | **BORRADOR, NO FIRMAR.** Pendientes: registro de anulación, XML conforme a la Orden HAC/1177/2024, remisión efectiva a la AEAT y firma XAdES | `docs/declaracion-responsable-fabricante.md:3,74-78` | **No** se puede decir «certificado» ni «homologado» |
| Seguridad | 2FA (TOTP), historial de cambios, eliminación de cuenta | `src/features/seguridad/components/DosPasosVg.tsx`, `App.tsx:204` | Sí |
| Nóminas | Tras el flag `feat_nominas`. «El motor solo simula hasta que un graduado social valide los parámetros» | `supabase/migrations/20261021100000_nominas_acceso.sql:21` | **No** (no crear páginas de nóminas) |
| DIAN (Colombia) | Existe pero queda fuera del mercado España | `App.tsx:185-187` | No (fuera de alcance) |
| Integraciones | Excel/CSV, PDF, Facturae, email, OCR y Stripe (solo para la suscripción). Gmail, Outlook, Slack y HubSpot como «soon» | `src/features/integrations/domain/integrations-catalog.ts:20-125` | Las activas sí; las «soon» no |
| Prueba de 14 días | `TRIAL_DAYS = 14` en Stripe Checkout (modo `subscription`), solo la primera vez | `supabase/functions/create-checkout-session/app.ts:21,85-95` | Sí. La tarjeta se pide en el Checkout (véase A4) |

### Planes y límites (comprobados en dos sitios)

| | Starter | Pro | Ilimitado (`business`) |
|---|---|---|---|
| Precio mensual / anual (€/mes + IVA) | 6,45 / 4,95 | 11,95 / 8,95 | 23,95 / 17,95 |
| Clientes | 10 | 150 | Ilimitados |
| Productos | 30 | 150 | Ilimitados |
| Facturas/mes | 10 | Ilimitadas | Ilimitadas |
| OCR/mes | 10 | 75 | 300 |
| Usuarios (copy) | 1 | 3 | Ilimitados |
| Soporte | Email | Chat + email | Prioritario (chat, email, teléfono) |

Evidencia: `src/services/plans/plans-config.service.ts:14-63` (copy y precios) y `src/services/billing-limits/billing-limits.service.ts:25-30` (límites aplicados: clientes, productos, facturas y OCR). El descuento anual real es 23–25 %: (6,45−4,95)/6,45 = 23,3 %, (11,95−8,95)/11,95 = 25,1 %, (23,95−17,95)/23,95 = 25,1 %. «Hasta −25 %» es correcto (`index.html:197`, `pricing.html:41`). Nota: el precio puede editarse en BD (`subscription_plan_configs`). La web debe seguir los valores por defecto (CLAUDE.md).

## A2. Inventario de páginas indexables (20 URL del `sitemap.xml`)

El recuento de palabras es solo texto visible del HTML. El header y el footer se inyectan por JS (`assets/js/header-include.js`, `footer-include.js`) y no cuentan. Se obtuvo con un script propio sobre cada archivo.

| Página | Palabras | Intención cubierta | Keyword implícita | H1 | CTAs a signup (texto) | Enlaces internos en el cuerpo | Schema |
|---|---|---|---|---|---|---|---|
| `index.html` | 1.849 | Comercial / marca | «suite financiera autónomos pymes» (sin volumen claro) | «Facturas, bancos e impuestos de tu negocio, en un solo lugar.» | 5: hero (`:43`), 3 de plan (`:206,214,222`), CTA final (`:257`) | 13 | Organization, SoftwareApplication, Offer×3, FAQPage(9) |
| `funciones.html` | **280** | Navegacional / descubrimiento | «funciones programa facturación» | «Una suite financiera completa…» | 1 | 12 | Ninguno |
| `pricing.html` | 627 | Transaccional | «precio programa facturación» | «Un precio claro…» | 4 | **2** | FAQPage(6) |
| `faq.html` | 906 | Informacional / objeciones | — | «Preguntas frecuentes» | 1 | 3 | FAQPage(25) |
| `contact.html` | **89** | Navegacional | — | «Hablemos.» | 0 | 1 | Ninguno |
| `about.html` | **156** | Marca / confianza | — | «Hacemos que las finanzas…» | 1 | 3 | Ninguno |
| `crea-envia-facturas.html` | 760 | Comercial por función | «programa para hacer facturas», «facturación VERI*FACTU» | «Facturas correctas a la primera, listas para VERI*FACTU.» | 2 | 6 | FAQPage(5) |
| `crea-envia-presupuestos.html` | 327 | Comercial por función | «programa presupuestos» | «Del presupuesto a la factura…» | 2 | 6 | FAQPage(3) |
| `bancos-conciliacion.html` | 444 | Comercial por función | «conciliación bancaria» | «Concilia tu banco…» | 2 | 6 | FAQPage(4) |
| `cobros.html` | 529 | Comercial por función | «control de cobros», «recordatorio de pago» | «Cobra a tiempo sin perseguir a nadie.» | 2 | 6 | FAQPage(3) |
| `escanea-gastos.html` | 399 | Comercial por función | «escanear tickets gastos OCR» | «Cada gasto con su justificante…» | 2 | 6 | FAQPage(3) |
| `impuestos.html` | 337 | Comercial por función | «modelo 303 y 130 autónomos» | «El trimestre, con los números ya hechos.» | 2 | 6 | FAQPage(3) |
| `tu-negocio-bajo-control.html` | 342 | Comercial por función | «panel financiero pyme» | «Cómo va tu negocio, sin abrir una hoja de cálculo.» | 2 | 6 | FAQPage(3) |
| `gestiona-clientes.html` | **278** | Comercial por función | «gestión de clientes facturación» | «Tus clientes, con todo lo que les has facturado.» | 2 | 6 | FAQPage(2) |
| `gestiona-tu-stock.html` | 538 | Comercial por función | «programa control de stock», «inventario autónomos» | «Tu catálogo y tu stock, siempre al día.» | 2 | 6 | FAQPage(4) |
| `factura-personalizada.html` | **276** | Comercial por función | «plantilla factura personalizada» | «Facturas con tu marca…» | 2 | 6 | FAQPage(2) |
| `news-grid.html` | 214 | Hub de blog | — | «Guías claras sobre facturación…» | 1 | 5 | Ninguno (falta Blog/CollectionPage) |
| `verifactu-2027-guia-autonomos-pymes.html` | 608 | Informacional | «verifactu 2027», «verifactu autónomos» | Sí | 1 | 5 | Article (autor Organization) |
| `factura-electronica-vs-verifactu.html` | 384 | Informacional | «factura electrónica vs verifactu» | Sí | 1 | 5 | Article |
| `contabilidad-negocio-7-pasos.html` | 404 | Informacional | «cómo llevar la contabilidad de un negocio» | Sí | 1 | 5 | Article |

### Observaciones transversales comprobadas

- **Un solo texto de CTA en toda la web**: «Empieza gratis 14 días». En precios hay además «Probar X 14 días». Todos apuntan a `https://app.facturales.es/signup` sin parámetros: 79 apariciones (`grep` sobre `*.html` y `*.js`). Los botones de plan (`index.html:206,214,222`) no llevan `?plan=`, así que la intención de plan se pierde.
- **Enlazado interno plantillado**: cada página de función tiene exactamente 6 destinos únicos (3 «Funciona mejor junto a» + funciones + index + pricing). No hay enlaces contextuales dentro del texto hacia guías ni artículos. `pricing.html` solo enlaza a `contact.html` e `index.html` en el cuerpo: no enlaza a ninguna función ni a la FAQ.
- **Las páginas de función no enlazan al blog**, y el blog solo enlaza a `funciones.html` e `index.html`. Por ejemplo, el artículo de VERI*FACTU no enlaza a `crea-envia-facturas.html`, que es la página con H1 «listas para VERI*FACTU».
- **`faq.html` responde bien a las objeciones** (25 preguntas): migración, VERI*FACTU, recurrentes, impuestos, banca «Próximamente», no presenta modelos, roles, datos en la UE, 2FA, exportar/eliminar, prueba, permanencia, IVA (`faq.html:28` JSON-LD).
- **Prueba social permitida disponible**: capturas reales marcadas como tales (3 en `index.html`, `crea-envia-facturas.html`, `cobros.html` y `gestiona-tu-stock.html`), «Alojados en la UE», 2FA, historial de cambios, «sin permanencia», rol Gestor y VERI*FACTU (registro y QR). **No hay** testimonios, cifras de clientes ni valoraciones (correcto según CLAUDE.md).
- **Identidad legal invisible**: la empresa titular (AVENUE DIGITAL GROUP, S.L., Valladolid) solo figura en el borrador de declaración y en las páginas legales de la app (`facturales/src/app/pages/legal/LegalContent.tsx:463`). En las páginas reales de la landing no aparece (solo en las plantillas demo `index-2.html` e `index-4.html`). Es una señal de confianza que se está desaprovechando: empresa española con sede física.
- **`about.html` tiene 156 palabras** y ninguna persona, historia, fecha de fundación ni dirección. **`contact.html` tiene 89 palabras** y el formulario va por mailto (CLAUDE.md, `facturales.js`).
- **Blog sin hub temático**: `news-grid.html` hace de índice, pero su URL no es descriptiva, no tiene categorías ni schema, y existen copias noindex (`news.html`, `news-details.html`).
- **Title y meta description**: los títulos van de 21 a 72 caracteres. En `funciones.html` (72) se puede truncar. Varias descripciones pasan de 160 caracteres (`index.html` 193, `funciones.html` 198, `faq.html` 187). Los títulos de módulo están orientados a marca/función, no a la consulta («Clientes y contactos · Facturales» en vez de «Programa de gestión de clientes para autónomos»).
- **Navegación inyectada con `document.write`**: los enlaces del menú y del footer no están en el HTML inicial (`header-include.js:5`). Google renderiza JS, pero el enlazado interno principal depende de ese render. Lo detalla el informe técnico; aquí importa porque los hubs nuevos deben quedar enlazados **en HTML**.

## A3. Exactitud de los 3 artículos (para revisión de un experto legal)

### Artículo 1: `verifactu-2027-guia-autonomos-pymes.html` (publicado el 03/02/2026, sin fecha de actualización)

| # | Afirmación | Línea | Estado | Comentario |
|---|---|---|---|---|
| 1.1 | «01/01/2027: entidades que presenten Impuesto sobre Sociedades. 01/07/2027: el resto» | `:77-78` | **Correcta en lo sustancial**, pero sin fuente | Coincide con el RD-ley 15/2025, de 2 de diciembre (BOE 03/12/2025, en vigor 04/12/2025), convalidado por el Congreso (Resolución de 11/12/2025, BOE 16/12/2025, según Garrigues; **confirmar en el BOE**). Falta citar la norma y que la obligación para los productores de software rige desde el 29/07/2025. Falta matizar que el art. 3.1.a) también incluye a otros contribuyentes del IS, no solo «sociedades» (revisión legal). |
| 1.2 | «La AEAT lo resume con la "regla de los 4 NO"» | `:72` | **Dudosa / sin fuente** | No se ha localizado esa denominación en fuentes oficiales. Sustituir por la lista de exclusiones del art. 3 del RD 1007/2023 (SII, territorios forales con su propio sistema —TicketBAI/Batuz—, facturación íntegramente manual, etc.) con enlace a la FAQ de la AEAT. |
| 1.3 | «no tener domicilio fiscal en territorios forales» como exclusión | `:72` | **Impreciso** | La exclusión depende de la normativa foral aplicable (País Vasco/Navarra), no solo del domicilio. Revisión legal. |
| 1.4 | «Las facturas generadas con un SIF deben llevar código QR… tanto VERI*FACTU como no verificables» | `:82` | Correcto en lo sustancial | Añadir que la **leyenda «VERI*FACTU» solo procede si se remiten los registros** (punto crítico, véase 1.6). |
| 1.5 | «La modalidad no verificable … exige medidas adicionales de control y conservación» | `:~88` | Incompleto | Falta lo concreto: firma electrónica de los registros y registro de eventos. |
| 1.6 | CTA «Facturales emite facturas con su registro VERI*FACTU y su QR» | `:102` | **Riesgo de coherencia (P0)** | El mismo artículo define VERI*FACTU como remisión a la AEAT (`:66`), y la app **todavía no remite** (`emit-invoice-verifactu/index.ts:10-11`; `integrations-catalog.ts:82-84`; declaración `:76`). El lector puede entender que Facturales ya remite. CLAUDE.md prohíbe afirmar «envío automático a la AEAT». Proponer: «genera el registro de facturación con huella encadenada y el QR de cotejo; la remisión a la AEAT se activará al completar el alta como colaborador social». **Validar con legal**, junto con el uso de la leyenda «VERI*FACTU» en el PDF mientras no se remite. |
| 1.7 | Autor «Equipo de Facturales», sin fuentes, sin `dateModified` | `:29,40` | E-E-A-T débil | Tema YMYL fiscal: necesita autor o revisor con credenciales (asesor fiscal colegiado), enlaces al BOE y a la AEAT, y fecha de revisión. |
| 1.8 | Extensión de 608 palabras para la keyword más competida del nicho | — | Profundidad insuficiente | Las SERP de «verifactu» las dominan guías de más de 2.000 palabras con FAQ, sanciones (art. 201 bis LGT: 50.000 € por ejercicio para quien use software no conforme; 150.000 € para productores; **verificar**), calendario y tabla de modalidades. |

### Artículo 2: `factura-electronica-vs-verifactu.html` (10/02/2026)

| # | Afirmación | Línea | Estado | Comentario |
|---|---|---|---|---|
| 2.1 | Plazos SIF 01/01/2027 y 01/07/2027 | `:58-59` | Correcta (véase 1.1) | Sin fuente. |
| 2.2 | «Su efectividad [B2B] depende del desarrollo reglamentario» | `:63` | **DESACTUALIZADA** | El **RD 238/2026** (Consejo de Ministros 24/03/2026; BOE 31/03/2026 según fuentes secundarias) desarrolla la Ley 18/2022 «Crea y Crece». Los plazos (12 meses para empresas de más de 8 M€ de facturación y 24 meses para el resto) cuentan desde una **Orden Ministerial** que regula la solución pública de facturación electrónica; según un borrador entraría en vigor el 01/10/2026. **El experto debe confirmar en el BOE si la Orden está publicada** y fijar las fechas resultantes (aprox. oct-2027 grandes / oct-2028 resto si la Orden entró el 01/10/2026). |
| 2.3 | No menciona que Facturae 3.2.2 de la app se descarga **sin firmar** ni qué formatos admitirá la solución pública | — | Omisión | Riesgo de expectativa: el lector puede pensar que Facturales ya cubre la B2B. Hay que redactar con cautela (`document-facturae.ts:7`). |
| 2.4 | Extensión de 384 palabras | — | Thin content | Ampliar a guía pilar (véase C4). |
| 2.5 | Mismo CTA que 1.6 | `:76` | Igual que 1.6 | — |

### Artículo 3: `contabilidad-negocio-7-pasos.html` (17/02/2026)

| # | Afirmación | Línea | Estado | Comentario |
|---|---|---|---|---|
| 3.1 | «Cuadro de mando mínimo (6 números)» y enumera 7 (ventas, gastos, margen bruto, IVA estimado, cobros pendientes, tesorería, previsión 30 días) | `:82` y siguiente | **Error** | Corregir a 7 o fusionar dos. |
| 3.2 | «Contabilidad» para autónomos | Todo el artículo | Matiz conceptual | Un autónomo en estimación directa simplificada no lleva contabilidad conforme al Código de Comercio, sino **libros registro** (ingresos, gastos, bienes de inversión). El artículo debería distinguir autónomo y sociedad. Revisión de un asesor. |
| 3.3 | «Sin categorías claras, pierdes deducciones» | Errores típicos | Genérico | Conviene enlazar a una guía de gastos deducibles. |
| 3.4 | Paso 5 (conciliación) y CTA | `:94` | Coherente con producto | Enlazar a `bancos-conciliacion.html` (hoy no se enlaza). |

**Patrón común**: los 3 artículos tienen fecha de febrero de 2026, las fechas de «Sigue leyendo» no tienen `dateModified`, el `og:image` es genérico, no hay tabla de contenidos ni FAQ con schema, y el único enlace a producto es «Ver funciones».

## A4. Atribución, embudo técnico y analítica

| Hallazgo | Evidencia |
|---|---|
| La landing no tiene ningún script de analítica (ni GA4, GTM, Plausible, Umami ni Clarity) | `grep -rliE "gtag|googletagmanager|plausible|umami|clarity|analytics"` sobre `*.html` y `*.js`: solo coincide con `bootstrap.bundle.min.js` (falso positivo) |
| Los enlaces a signup no llevan UTM ni plan | 79 × `https://app.facturales.es/signup` sin query |
| La app no lee `utm_*`, `gclid` ni `document.referrer` | `grep -rniE "utm_|document\.referrer|referrer"` en `facturales/src`: solo aparecen atributos `rel="noreferrer"` |
| `signUp()` admite `metadata` y la guarda en `auth.users.raw_user_meta_data` | `src/services/auth/auth.service.ts:99-105`; llamado en `src/app/pages/hooks/use-acceso.ts:135-138` con `buildSignUpMetadata(firstName, lastName)` |
| Recorrido tras el signup: `/verify-email` → `/confirm-email` → `/complete-profile` → `/planes` → Stripe Checkout | `App.tsx:189-197`; `src/app/pages/domain/perfil-negocio.ts:53` (`AFTER_PROFILE_ROUTE = "/planes"`) |
| La prueba vive dentro de Stripe Checkout `mode: "subscription"` con `trial_period_days: 14`, solo la primera vez. El Checkout pide método de pago por defecto | `supabase/functions/create-checkout-session/app.ts:85-103` |
| Google sign-in disponible | `auth.service.ts:120-135` |
| El registro está protegido con captcha | `auth.service.ts:97` (`obtenerTokenCaptcha("signup")`) |
| El panel de administración ya tiene estadísticas por plan (activos, en prueba, cancelados, MRR) | `plans-config.service.ts:155-185` |

---

# B. HIPÓTESIS (a validar)

| ID | Hipótesis | Cómo validarla |
|---|---|---|
| H1 | La caída más grande del embudo está entre `/planes` y el Checkout completado, porque se pide tarjeta sin aviso previo en la web | Medir los eventos de C6.5 durante 4 semanas. Comparar las sesiones de signup con las suscripciones en `trialing` (`admin_get_plan_stats`) |
| H2 | Los botones «Probar Pro 14 días» convierten peor de lo que podrían porque el plan elegido se pierde | Pasar `?plan=pro&periodo=anual` y preseleccionar en `/planes`. Test A/B |
| H3 | El tráfico orgánico no comercial (blog) apenas convierte por falta de CTAs contextuales y de lead magnets intermedios | Instrumentar `cta_click` con `cta_location` y comparar la tasa por tipo de página |
| H4 | Las keywords «programa de facturación gratis», «plantilla factura» y «calculadora IVA» concentran mucho volumen TOFU que hoy no se captura | Validar con Search Console y una herramienta de keywords (Ahrefs/SE Ranking no estaban autorizados en esta sesión: hay que conectarlos) |
| H5 | El límite de usuarios (1/3/ilimitados) **no se aplica en el backend** (solo se aplican clientes, productos, facturas y OCR en `billing-limits.service.ts:25-30`). Además, no está claro si el Gestor ocupa plaza | Confirmar con producto antes de prometer «invita a tu gestoría gratis» o «en Starter» |
| H6 | Las migraciones de automatizaciones tienen fecha 23–24/10/2026 (`supabase/migrations/20261023150000_automatizaciones_programacion.sql`), posterior a hoy (18/10). Puede que los recordatorios automáticos aún no estén desplegados en producción, aunque CLAUDE.md los da por disponibles desde el 17/10 | Confirmar el despliegue antes de campañas que los destaquen |
| H7 | Una página «Facturales para gestorías» con el rol Gestor puede abrir un canal B2B2C (las gestorías recomiendan software a sus clientes) con un CAC bajo | Piloto con 5–10 gestorías. Medir altas con `utm_source=gestoria` |
| H8 | La mención explícita de la empresa española (razón social, sede en Valladolid, datos en la UE) mejora la confianza en precios y signup | A/B en el bloque de confianza de `pricing` |
| H9 | La búsqueda de marca de competidores («alternativa a Holded», «Quipu vs …») es de alta intención y baja competencia en long tail | SERP manual + GSC tras publicar 2 páginas piloto |

---

# C. RECOMENDACIONES

## C1. Principios

1. **Calidad sobre volumen.** Cada página nueva debe aportar algo que no esté en el top 10: capturas reales, ejemplos numéricos, plantilla útil o herramienta.
2. **Ninguna promesa sin evidencia en la app.** Lista de «sí» y «no» en A1. Claims prohibidos: testimonios, nº de clientes, valoraciones, «sin tarjeta», «envío automático a la AEAT», «certificado/homologado VERI*FACTU», «Facturae firmada», nóminas, conexión bancaria directa disponible, «30 %».
3. **Revisión experta obligatoria** en todo lo fiscal o legal (YMYL): autor con nombre y revisor (asesor fiscal colegiado o graduado social según el tema), fuentes BOE/AEAT enlazadas, «Última revisión: dd/mm/aaaa» y `dateModified`.
4. **URLs limpias sin `.html`** con el patrón carpeta + `index.html` (`/precios/index.html` se sirve como `/precios/`), que funciona en cualquier hosting estático sin reescrituras. Redirecciones 301 desde las URLs `.html` actuales (depende del hosting: `_redirects`, `vercel.json` u `.htaccess`; si no hay soporte, un `<link rel=canonical>` y un meta refresh como último recurso, no recomendado).
5. **Hub & spoke en HTML.** Los hubs enlazan a todos sus spokes y cada spoke enlaza a su hub, a 2–3 hermanos y a 1 landing comercial, con enlaces escritos en el HTML (no inyectados).

## C2. Arquitectura SEO ideal (sitemap jerárquico)

```
/                                   Home (marca + «programa de facturación y finanzas para autónomos y pymes»)
├── /software-facturacion/          PILAR comercial: «programa de facturación»
├── /programa-facturacion-autonomos/  PILAR por tipo: autónomos
├── /software-facturacion-pymes/    PILAR por tipo: pymes
├── /gestorias/                     PILAR por tipo: gestorías y asesorías (rol Gestor)
├── /verifactu/                     PILAR normativo-comercial: software VERI*FACTU
├── /factura-electronica/           PILAR normativo: factura electrónica B2B / Facturae
├── /precios/                       (renombra pricing.html)
├── /funciones/                     hub de funciones (renombra funciones.html)
│   ├── /funciones/facturas/                  (crea-envia-facturas)
│   ├── /funciones/facturas-recurrentes/      NUEVA (hoy es ancla #recurrentes)
│   ├── /funciones/presupuestos/              (crea-envia-presupuestos)
│   ├── /funciones/inventario/                (gestiona-tu-stock)
│   ├── /funciones/cobros/                    (cobros)
│   ├── /funciones/recordatorios-de-pago/     NUEVA (hoy es ancla cobros#recordatorios)
│   ├── /funciones/conciliacion-bancaria/     (bancos-conciliacion)
│   ├── /funciones/gastos/                    (escanea-gastos)
│   ├── /funciones/impuestos/                 (impuestos) → spokes 303/130 en guías
│   ├── /funciones/panel/                     (tu-negocio-bajo-control)
│   ├── /funciones/clientes/                  (gestiona-clientes)
│   ├── /funciones/diseno-factura/            (factura-personalizada)
│   ├── /funciones/equipo-y-gestoria/         NUEVA (roles; enlaza a /gestorias/)
│   └── /funciones/seguridad/                 NUEVA (2FA, UE, historial, exportar)
├── /sectores/                      hub
│   └── /sectores/[sector]/         12 landings (véase C2.3)
├── /comparativas/                  hub
│   └── /comparativas/facturales-vs-[competidor]/
├── /alternativas/                  hub
│   └── /alternativas/[competidor]/
├── /recursos/                      hub (centro de recursos)
│   ├── /recursos/plantillas/                         hub de plantillas
│   │   ├── /recursos/plantillas/factura/             Excel, Word, PDF
│   │   ├── /recursos/plantillas/factura-autonomo/
│   │   ├── /recursos/plantillas/factura-con-irpf/
│   │   ├── /recursos/plantillas/factura-rectificativa/
│   │   ├── /recursos/plantillas/factura-proforma/
│   │   ├── /recursos/plantillas/presupuesto/
│   │   ├── /recursos/plantillas/presupuesto-reformas/
│   │   ├── /recursos/plantillas/recibo/
│   │   ├── /recursos/plantillas/control-de-stock/    Excel
│   │   └── /recursos/plantillas/control-de-gastos/   Excel
│   ├── /herramientas/generador-facturas/             generador online gratis (lead magnet)
│   ├── /calculadoras/                                hub
│   │   ├── /calculadoras/iva/
│   │   ├── /calculadoras/precio-sin-iva/            (desglose de IVA)
│   │   ├── /calculadoras/retencion-irpf-factura/
│   │   ├── /calculadoras/modelo-130/
│   │   ├── /calculadoras/cuota-autonomos/            (tramos 2026/2027, revisión de experto)
│   │   └── /calculadoras/margen-y-precio-de-venta/
│   └── /calendario-fiscal/                           calendario 2026-2027 (+ .ics)
├── /guias/                         hub de guías evergreen (pilares informacionales)
│   ├── /guias/verifactu/                      (migración y ampliación del artículo 1)
│   ├── /guias/factura-electronica-b2b/        (migración y ampliación del artículo 2)
│   ├── /guias/como-hacer-una-factura/
│   ├── /guias/modelo-303/
│   ├── /guias/modelo-130/
│   ├── /guias/gastos-deducibles-autonomos/
│   ├── /guias/morosidad-y-reclamacion-de-facturas/
│   └── /guias/contabilidad-autonomos-y-pymes/ (migración y ampliación del artículo 3)
├── /blog/                          (renombra news-grid.html) + /blog/categoria/[cluster]/
│   └── /blog/[slug]/
├── /glosario/                      hub A–Z
│   └── /glosario/[termino]/        (40–60 términos, sin canibalizar las guías)
├── /sobre-nosotros/  /contacto/  /preguntas-frecuentes/
└── (legales en app.facturales.es: sin cambios)
```

### C2.1 Mapeo de páginas existentes (renombrar + 301)

| Actual | Nueva URL | Acción de contenido |
|---|---|---|
| `/index.html` y `/` | `/` | Mantener; reforzar la keyword «programa de facturación» en H2 y title |
| `/pricing.html` | `/precios/` | Añadir enlaces a funciones, bloque de confianza y FAQ de tarjeta/prueba |
| `/funciones.html` | `/funciones/` | Ampliar de 280 a ~900 palabras con resumen por función, capturas y enlaces |
| `/faq.html` | `/preguntas-frecuentes/` | Mantener y enlazar cada respuesta a su landing o guía |
| `/contact.html` | `/contacto/` | Añadir datos de empresa y tiempos de respuesta |
| `/about.html` | `/sobre-nosotros/` | Ampliar con equipo, historia, empresa, cumplimiento y sede |
| `/crea-envia-facturas.html` | `/funciones/facturas/` | Separar las recurrentes en su propia URL |
| `/crea-envia-presupuestos.html` | `/funciones/presupuestos/` | Ampliar a ~700 palabras |
| `/bancos-conciliacion.html` | `/funciones/conciliacion-bancaria/` | — |
| `/cobros.html` | `/funciones/cobros/` | Separar recordatorios |
| `/escanea-gastos.html` | `/funciones/gastos/` | — |
| `/impuestos.html` | `/funciones/impuestos/` | Enlazar a las guías 303/130 y a la calculadora 130 |
| `/tu-negocio-bajo-control.html` | `/funciones/panel/` | — |
| `/gestiona-clientes.html` | `/funciones/clientes/` | Ampliar (278 palabras) |
| `/gestiona-tu-stock.html` | `/funciones/inventario/` | — |
| `/factura-personalizada.html` | `/funciones/diseno-factura/` | Enlazar a `/recursos/plantillas/factura/` |
| `/news-grid.html` | `/blog/` | Categorías por cluster y schema `Blog` |
| `/verifactu-2027-guia-autonomos-pymes.html` | `/guias/verifactu/` | Reescribir como pilar de más de 2.500 palabras con revisión legal |
| `/factura-electronica-vs-verifactu.html` | `/blog/factura-electronica-vs-verifactu/` | Actualizar con el RD 238/2026 y la Orden; enlazar a los dos pilares |
| `/contabilidad-negocio-7-pasos.html` | `/blog/contabilidad-negocio-7-pasos/` | Corregir y enlazar a `/guias/contabilidad-autonomos-y-pymes/` |
| `news.html`, `news-details.html`, demos | — | Mantener noindex o eliminar. Fuera del sitemap |

### C2.2 Tabla de páginas (URL · keywords · intención · plantilla · CTA · enlaces · prioridad · esfuerzo)

Esfuerzo: S ≤ 1 día · M 2–4 días · L 1–2 semanas · XL más de 2 semanas (incluye revisión experta y diseño). Las keywords son **orientativas**: validar volumen y dificultad con datos reales (H4).

**Pilares comerciales y por tipo de negocio**

| URL | Keyword principal | Secundarias | Intención | Plantilla | CTA principal | Entrantes ← / Salientes → | Prio | Esf. |
|---|---|---|---|---|---|---|---|---|
| `/software-facturacion/` | programa de facturación | software de facturación, programa para hacer facturas, programa facturación online | Comercial | Pilar comercial (T1 ampliada) | Empieza 14 días (con `?plan`) | ← home, funciones, blog, todas las guías · → 12 funciones, /verifactu/, /precios/, comparativas | P0 | L |
| `/programa-facturacion-autonomos/` | programa de facturación para autónomos | app facturas autónomos, facturar como autónomo, factura con IRPF | Comercial | Landing por tipo | Probar Starter/Pro | ← home, /guias/como-hacer-una-factura/, calculadoras IRPF/130, glosario · → /funciones/impuestos/, plantillas, /sectores/* | P0 | M |
| `/software-facturacion-pymes/` | software de facturación para pymes | programa de gestión pymes, facturación y stock pyme | Comercial | Landing por tipo | Probar Pro/Ilimitado | ← home, /funciones/inventario/, /funciones/equipo-y-gestoria/ · → inventario, cobros, conciliación, equipo | P0 | M |
| `/gestorias/` | software para gestorías / programa para asesorías con clientes | acceso gestoría facturación clientes, compartir facturas con gestor | Comercial B2B | Landing por tipo + bloque de alta de colaborador | «Invita a tu gestoría» / contacto | ← funciones equipo, /funciones/impuestos/, guía 303 · → rol Gestor, cierres, ZIP justificantes, export | P1 | M |
| `/verifactu/` | software verifactu / programa verifactu | verifactu autónomos, adaptarse a verifactu | Comercial-normativa | Landing normativa (estado real: registro + QR; remisión «al completar el alta»; texto revisado por legal) | Empieza 14 días | ← /guias/verifactu/, todos los artículos del cluster · → /funciones/facturas/, /guias/verifactu/, calendario | P0 | M (bloqueado por legal) |
| `/factura-electronica/` | programa factura electrónica | Facturae, factura electrónica autónomos | Comercial-normativa | Landing normativa (Facturae 3.2.2 descarga sin firma; B2B «cuando sea exigible») | Empieza 14 días | ← /guias/factura-electronica-b2b/ · → /funciones/facturas/ | P2 | M |
| `/precios/` | precio programa de facturación | Facturales precio, planes | Transaccional | Precios (existente mejorado) | Probar [plan] con `?plan=` | ← todas · → funciones, FAQ, comparativas | P0 | S |

**Landings de función** (`/funciones/*`): plantilla T1, CTA «Empieza 14 días» + secundario «Ver precios».

| URL | Keyword principal | Secundarias | Prio | Esf. |
|---|---|---|---|---|
| `/funciones/` | funciones programa facturación | — | P1 | M |
| `/funciones/facturas/` | programa para hacer facturas | facturas con IRPF, series de facturación, factura rectificativa programa | P0 | S |
| `/funciones/facturas-recurrentes/` | facturas recurrentes | facturación recurrente automática, factura periódica | P0 | M |
| `/funciones/presupuestos/` | programa de presupuestos | presupuesto a factura, app presupuestos autónomos | P1 | M |
| `/funciones/inventario/` | programa control de stock | inventario pyme, stock mínimo, facturación con stock | P0 | S |
| `/funciones/cobros/` | control de cobros | facturas pendientes de cobro, antigüedad de deuda, previsión de cobros | P1 | S |
| `/funciones/recordatorios-de-pago/` | recordatorio de pago factura | email recordatorio pago, reclamar factura impagada | P0 | M |
| `/funciones/conciliacion-bancaria/` | conciliación bancaria | conciliar banco facturas, importar extracto bancario | P1 | S |
| `/funciones/gastos/` | escanear tickets | app gastos autónomos OCR, justificantes de gastos | P1 | S |
| `/funciones/impuestos/` | programa modelo 303 y 130 | calcular IVA trimestral, 130 autónomos | P0 | S |
| `/funciones/panel/` | cuadro de mando pyme | panel financiero negocio | P3 | S |
| `/funciones/clientes/` | gestión de clientes facturación | base de datos clientes autónomo | P3 | S |
| `/funciones/diseno-factura/` | factura personalizada con logo | diseño de factura | P2 | S |
| `/funciones/equipo-y-gestoria/` | compartir facturación con gestoría | roles usuarios facturación | P1 | M |
| `/funciones/seguridad/` | software facturación seguro | datos en la UE, verificación en dos pasos | P2 | S |

**Sectores** (`/sectores/[sector]/`): plantilla T2. La lógica de producto real decide qué función se destaca en cada uno.

| Sector (URL) | Keyword principal | Por qué encaja (función real) | Plantilla descargable asociada | Prio | Esf. |
|---|---|---|---|---|---|
| `/sectores/comercio/` | programa facturación y stock para tienda | Inventario: descuento al facturar, stock mínimo, precios en bloque | control de stock | P1 | M |
| `/sectores/distribuidores/` | programa facturación distribuidor | Inventario + series + cobros por cliente | — | P2 | M |
| `/sectores/reformas/` | programa presupuestos reformas | Presupuesto → factura, catálogo de partidas, cobros | presupuesto de reformas | P1 | M |
| `/sectores/fontaneros-electricistas/` | programa facturas fontanero / electricista | Presupuestos en el móvil, catálogo de materiales con stock, recordatorios | presupuesto | P1 | M |
| `/sectores/consultores/` | programa facturación consultores | Recurrentes (iguala/retainer), IRPF 15/7 %, 130 | factura con IRPF | P1 | M |
| `/sectores/academias/` | programa facturación academia | Recurrentes mensuales por alumno, recordatorios de cobro. **Ojo**: exención de IVA en enseñanza; revisión fiscal | recibo | P1 | M |
| `/sectores/mantenimiento/` | facturación contratos de mantenimiento | Recurrentes trimestrales/anuales, cobros | — | P2 | M |
| `/sectores/diseñadores-freelance/` → `/sectores/disenadores/` | facturas diseñador freelance | Presupuesto, factura con IRPF, marca propia | factura autónomo | P2 | M |
| `/sectores/desarrolladores-informaticos/` | facturar como programador autónomo | Recurrentes (soporte), IRPF, clientes UE (**revisar operaciones intracomunitarias**: no prometer modelo 349) | factura | P2 | M |
| `/sectores/fisioterapeutas-salud/` | programa facturación fisioterapeuta | Facturas exentas de IVA (revisión fiscal), recurrentes por bonos, clientes | recibo | P2 | M |
| `/sectores/agencias-marketing/` | facturación agencia marketing | Recurrentes (fees), equipo multiusuario, cobros | — | P3 | M |
| `/sectores/talleres/` | programa facturación taller | Presupuesto → factura, stock de recambios | presupuesto | P3 | M |

Exclusiones deliberadas: hostelería/TPV (no hay TPV), sanitario con historia clínica, transportistas con módulos/estimación objetiva (Facturales calcula el 130 en estimación directa; `fiscal-calc.ts:159-170`), comercio en recargo de equivalencia (verificar soporte antes; hay referencias en `invoice-import.service.ts` y en el editor de documentos, pero no se ha comprobado el cálculo completo).

**Comparativas y alternativas** (plantillas T3/T4). Candidatos según el mercado español: Holded, Quipu, Billin, Contasimple, Anfix, Sage (Sage Active/Despachos) y FacturaDirecta. Elegir 6 tras revisar la SERP.

| URL | Keyword | Prio | Esf. |
|---|---|---|---|
| `/comparativas/` (hub con metodología) | comparativa programas de facturación | P1 | M |
| `/comparativas/facturales-vs-holded/` | facturales vs holded | P1 | M |
| `/comparativas/facturales-vs-quipu/` | facturales vs quipu | P1 | M |
| `/comparativas/facturales-vs-billin/` | — | P2 | M |
| `/comparativas/facturales-vs-contasimple/` | — | P2 | M |
| `/comparativas/facturales-vs-excel/` | facturar con excel vs programa | P1 | S |
| `/alternativas/holded/` | alternativa a holded | P1 | M |
| `/alternativas/quipu/`, `/alternativas/billin/`, `/alternativas/excel/`, `/alternativas/contasimple/`, `/alternativas/anfix/` | alternativa a X | P2 | M |

**Recursos y herramientas** (plantillas T7/T8)

| URL | Keyword | CTA | Prio | Esf. |
|---|---|---|---|---|
| `/herramientas/generador-facturas/` | generador de facturas gratis / hacer factura online gratis | Descargar PDF → «Guárdala y emítela con VERI*FACTU en Facturales» | P0 | XL |
| `/recursos/plantillas/factura/` | plantilla factura (excel / word / pdf) | Descarga directa + generador | P0 | M |
| `/recursos/plantillas/factura-autonomo/` | modelo factura autónomo | — | P0 | M |
| `/recursos/plantillas/factura-con-irpf/` | factura con retención IRPF plantilla | — | P1 | S |
| `/recursos/plantillas/presupuesto/` | plantilla presupuesto | — | P0 | M |
| `/recursos/plantillas/presupuesto-reformas/` | presupuesto de reforma plantilla | — | P1 | S |
| `/recursos/plantillas/factura-rectificativa/`, `/factura-proforma/`, `/recibo/` | — | — | P2 | S |
| `/recursos/plantillas/control-de-stock/` | plantilla control de stock excel | «Cuando se te quede pequeño Excel» → /funciones/inventario/ | P1 | S |
| `/recursos/plantillas/control-de-gastos/` | plantilla control gastos autónomo excel | → /funciones/gastos/ | P2 | S |
| `/calculadoras/iva/` | calculadora IVA | → generador / signup | P0 | M |
| `/calculadoras/precio-sin-iva/` | quitar IVA a un precio | — | P1 | S |
| `/calculadoras/retencion-irpf-factura/` | calcular retención IRPF factura | → plantilla con IRPF | P0 | M |
| `/calculadoras/modelo-130/` | calcular modelo 130 | → /funciones/impuestos/ | P1 | M |
| `/calculadoras/cuota-autonomos/` | calculadora cuota autónomos 2027 | Revisión de un graduado social; tablas oficiales con fecha | P1 | M |
| `/calculadoras/margen-y-precio-de-venta/` | calcular precio de venta con margen | → inventario | P2 | S |
| `/calendario-fiscal/` | calendario fiscal autónomos 2027 | Suscripción a recordatorios (email) + .ics | P0 | M |

**Guías, blog y glosario**: véanse los clusters (C3) y el calendario (C4). `/glosario/` en P2 (esfuerzo M para el hub y S por término).

## C3. Modelo hub & spoke (clusters con enlazado explícito)

Regla: **spoke → hub** (enlace contextual en el primer tercio + caja «Guía completa»), **spoke → 2 hermanos**, **spoke → 1 landing comercial** (CTA contextual), y **hub → todos los spokes** (índice). La comercial enlaza a la guía como «Entiende la norma» y la guía a la comercial como «Hazlo con Facturales».

### Cluster 1 · VERI*FACTU (P0, ventana hasta 01/07/2027)
- **Hub informacional**: `/guias/verifactu/` · **Hub comercial**: `/verifactu/`
- Spokes:
  - `/blog/verifactu-fechas-obligatorias/` (sociedades 01/01/2027, resto 01/07/2027; RD-ley 15/2025)
  - `/blog/verifactu-autonomos-que-tengo-que-hacer/`
  - `/blog/verifactu-vs-no-verifactu-modalidades/`
  - `/blog/qr-verifactu-factura/`
  - `/blog/sanciones-verifactu/` (revisión legal)
  - `/blog/verifactu-excel-word-puedo-seguir/` (alta intención: «¿puedo seguir facturando con Excel?»)
  - `/blog/verifactu-ticketbai-sii-quien-no-esta-obligado/`
  - `/blog/factura-electronica-vs-verifactu/` (existente)
  - `/glosario/sif/`, `/glosario/huella-hash/`, `/glosario/registro-de-facturacion/`
- Comerciales enlazadas: `/funciones/facturas/`, `/precios/`. Herramienta: `/calendario-fiscal/`.
- Condición: **todo el cluster pasa revisión legal** y respeta el estado real (registro + QR; remisión pendiente).

### Cluster 2 · Facturación
- **Hub**: `/guias/como-hacer-una-factura/` · **Comercial**: `/software-facturacion/`
- Spokes:
  - requisitos de una factura (RD 1619/2012)
  - factura simplificada vs completa
  - factura rectificativa
  - factura proforma
  - numeración y series
  - factura con IRPF
  - factura sin IVA (exenciones)
  - IGIC/IPSI (Canarias, Ceuta y Melilla)
  - factura a cliente extranjero (revisión fiscal)
  - plazo para emitir una factura
  - cuánto tiempo guardar facturas
- Recursos: plantillas de factura, generador, calculadoras IVA/IRPF.
- Comerciales: `/funciones/facturas/`, `/funciones/facturas-recurrentes/`, `/funciones/diseno-factura/`, `/funciones/presupuestos/`.

### Cluster 3 · Impuestos trimestrales
- **Hub**: `/calendario-fiscal/` + `/guias/modelo-303/` + `/guias/modelo-130/` (hub doble) · **Comercial**: `/funciones/impuestos/`
- Spokes:
  - cómo rellenar el 303 paso a paso
  - IVA deducible: qué gastos
  - 130 en estimación directa simplificada
  - el 130 cuando el 70 % o más de tus ingresos lleva retención (exención; **revisar**)
  - modelo 390 (resumen anual)
  - modelo 111 (si tienes trabajadores o profesionales)
  - modelo 115 (alquiler)
  - qué pasa si presento fuera de plazo
  - checklist del cierre trimestral
- Herramientas: calculadora 130, calculadora IVA. Rol Gestor → `/gestorias/`.
- Regla de copy: «calcula las cifras; tú o tu gestoría presentáis» (`faq.html:59`, `impuestos.html:63`).

### Cluster 4 · Cobros y morosidad
- **Hub**: `/guias/morosidad-y-reclamacion-de-facturas/` · **Comercial**: `/funciones/cobros/` + `/funciones/recordatorios-de-pago/`
- Spokes:
  - plazos legales de pago (Ley 3/2004: 30/60 días; revisión legal)
  - interés de demora y 40 € de costes de cobro
  - plantilla de email de recordatorio de pago (lead magnet)
  - cómo reclamar una factura impagada (requerimiento, monitorio)
  - IVA de facturas impagadas: modificación de la base imponible (revisión fiscal)
  - previsión de tesorería
  - antigüedad de deuda: qué es y cómo leerla

### Cluster 5 · Gastos
- **Hub**: `/guias/gastos-deducibles-autonomos/` · **Comercial**: `/funciones/gastos/`
- Spokes:
  - tickets vs facturas: ¿se deducen?
  - dietas deducibles
  - suministros con la vivienda como oficina
  - vehículo
  - cómo digitalizar tickets (validez de la copia digital; revisión legal)
  - categorías de gastos
  - plantilla de control de gastos
  - conciliación bancaria (puente con `/funciones/conciliacion-bancaria/`)

### Cluster 6 · Inventario
- **Hub**: `/guias/control-de-stock-pequeno-negocio/` · **Comercial**: `/funciones/inventario/`
- Spokes:
  - stock mínimo: cómo calcularlo
  - valoración de inventario (precio medio / FIFO; explicar qué usa la app)
  - inventario en Excel vs programa
  - roturas de stock
  - margen y precio de venta (calculadora)
  - plantilla de control de stock
- Sectores enlazados: comercio, distribuidores, talleres, fontaneros.
- Límite de copy: **un solo almacén**.

### Cluster 7 · Autónomos
- **Hub**: `/programa-facturacion-autonomos/` (comercial) + `/guias/contabilidad-autonomos-y-pymes/`
- Spokes:
  - darse de alta como autónomo (paso a paso)
  - cuota de autónomos por ingresos reales (calculadora)
  - primera factura como autónomo
  - libros registro obligatorios
  - IRPF 7 % nuevos autónomos
  - gastos deducibles (puente al cluster 5)
  - calendario fiscal del autónomo
  - glosario (RETA, IAE, modelo 036/037)
- Sectores: consultores, diseñadores, desarrolladores, fisioterapeutas.

### Cluster 8 · Pymes
- **Hub**: `/software-facturacion-pymes/` + `/guias/gestion-financiera-pyme/`
- Spokes:
  - tesorería y previsión
  - cierre mensual en pyme
  - cómo trabajar con tu gestoría (puente a `/gestorias/`)
  - control de cobros en B2B
  - factura electrónica B2B para pymes (RD 238/2026)
  - VERI*FACTU para sociedades (01/01/2027)
  - roles y permisos del equipo
  - KPIs financieros de una pyme

**Enlaces transversales obligatorios**: todos los artículos con fechas fiscales → `/calendario-fiscal/`; todos los de «factura» → generador y plantillas; todas las comerciales → la guía de su cluster; la home → los 8 hubs (bloque «Recursos» en el HTML).

## C4. Calendario editorial (nov 2026 → oct 2027)

Capacidad realista: 4–8 piezas al mes. Cada pieza fiscal o legal lleva **redactor + revisor experto** (AF = asesor fiscal colegiado; AL = abogado mercantil/tributario; GS = graduado social; PM = producto, que valida que la función existe). Objetivo de conversión: S = signup directo, L = lead (descarga/email), A = activación (usuario en prueba).

**Contexto fiscal de referencia**:
- Trimestrales: 1–20 de abril, julio y octubre, y 1–30 de enero (4T + resúmenes anuales).
- Renta: abril–junio.
- VERI*FACTU: sociedades 01/01/2027, resto 01/07/2027 (RD-ley 15/2025, convalidado; confirmar en el BOE).
- Factura electrónica B2B: plazos desde la Orden Ministerial (confirmar).

| Mes | Pieza (formato) | Keyword | Cluster | Conv. | Responsable / revisión | Prio |
|---|---|---|---|---|---|---|
| **Nov 2026** | Reescritura de `/guias/verifactu/` (pilar de más de 2.500 palabras, FAQ, fuentes BOE/AEAT) | verifactu | VERI*FACTU | S | Contenidos + AL + PM | P0 |
| | `/verifactu/` landing comercial | software verifactu | VERI*FACTU | S | Producto + AL | P0 |
| | Corrección de los 3 artículos existentes (A3) + migración a URLs limpias | — | Varios | — | Contenidos + AF/AL | P0 |
| | `/software-facturacion/` pilar comercial | programa de facturación | Facturación | S | Contenidos + PM | P0 |
| | `/recursos/plantillas/factura/` (Excel/Word/PDF) | plantilla factura | Facturación | L | Diseño + AF (campos obligatorios) | P0 |
| | Artículo «VERI*FACTU para sociedades: lo que tienes que tener el 1 de enero» | verifactu sociedades 2027 | VERI*FACTU / Pymes | S | Contenidos + AL | P0 |
| **Dic 2026** | `/calendario-fiscal/` 2027 + .ics + alta de recordatorios por email | calendario fiscal 2027 | Impuestos | L | Contenidos + AF | P0 |
| | `/calculadoras/iva/` | calculadora iva | Facturación | L | Dev + AF | P0 |
| | `/funciones/facturas-recurrentes/` | facturas recurrentes | Facturación | S | PM | P0 |
| | Artículo «Cierre de año para autónomos: checklist» | cierre fiscal autónomo | Autónomos | S | AF | P1 |
| | `/programa-facturacion-autonomos/` | programa facturación autónomos | Autónomos | S | Contenidos + PM | P0 |
| | Artículo «Inventario a 31 de diciembre: cómo hacer el recuento» (enganche con cierre/Black Friday) | inventario fin de año | Inventario | S | PM | P2 |
| **Ene 2027** | `/guias/modelo-303/` (4T) | modelo 303 | Impuestos | S | AF | P0 |
| | Artículo «Modelo 390: resumen anual del IVA» | modelo 390 | Impuestos | S | AF | P1 |
| | `/calculadoras/retencion-irpf-factura/` | calcular retención irpf factura | Facturación / Autónomos | L | Dev + AF | P0 |
| | Artículo «Ya es 2027: tu checklist VERI*FACTU si eres sociedad (y si eres autónomo, 6 meses)» | verifactu enero 2027 | VERI*FACTU | S | AL | P0 |
| | `/funciones/recordatorios-de-pago/` | recordatorio de pago factura | Cobros | S | PM | P0 |
| | `/gestorias/` | software para gestorías | Pymes / Gestorías | S/B2B | Ventas + PM | P1 |
| **Feb 2027** | `/herramientas/generador-facturas/` (MVP) | generador de facturas gratis | Facturación | L→S | Dev + diseño + AF | P0 |
| | `/comparativas/` hub + metodología + `/comparativas/facturales-vs-holded/` | facturales vs holded | Comparativas | S | Contenidos + revisión de exactitud | P1 |
| | `/alternativas/holded/` | alternativa a holded | Comparativas | S | Ídem | P1 |
| | `/guias/morosidad-y-reclamacion-de-facturas/` | reclamar factura impagada | Cobros | S | AL | P1 |
| | Artículo «Plantilla de email para reclamar un pago (3 niveles)» (lead magnet) | email recordatorio pago | Cobros | L | Contenidos + AL | P1 |
| **Mar 2027** | `/guias/modelo-130/` | modelo 130 | Impuestos | S | AF | P0 |
| | `/calculadoras/modelo-130/` | calcular modelo 130 | Impuestos | L | Dev + AF | P1 |
| | `/sectores/consultores/` + `/sectores/reformas/` | — | Sectores | S | PM | P1 |
| | Artículo «Checklist del cierre trimestral (1T)» | cierre trimestral autónomo | Impuestos | S | AF | P1 |
| | `/recursos/plantillas/presupuesto/` + `/presupuesto-reformas/` | plantilla presupuesto | Facturación | L | Diseño | P0 |
| **Abr 2027** (1T + Renta) | Artículo «Modelo 303 del 1T: errores frecuentes» (actualización del pilar) | 303 primer trimestre | Impuestos | S | AF | P1 |
| | `/guias/gastos-deducibles-autonomos/` (vinculado a la Renta) | gastos deducibles autónomos | Gastos | S | AF | P0 |
| | Artículo «Renta del autónomo: qué datos de tu facturación necesitas» | renta autónomos | Autónomos | S | AF | P1 |
| | `/sectores/comercio/` + `/recursos/plantillas/control-de-stock/` | programa stock tienda | Inventario | S/L | PM | P1 |
| | `/comparativas/facturales-vs-quipu/` + `/alternativas/quipu/` | — | Comparativas | S | Contenidos | P2 |
| **May 2027** | Artículo «VERI*FACTU para autónomos: quedan 2 meses» (urgencia) | verifactu autónomos julio 2027 | VERI*FACTU | S | AL | P0 |
| | Artículo «¿Puedo seguir facturando con Excel o Word después del 1 de julio?» | facturar con excel verifactu | VERI*FACTU | S | AL | P0 |
| | `/comparativas/facturales-vs-excel/` + `/alternativas/excel/` | — | Facturación | S | Contenidos | P1 |
| | `/sectores/academias/` + `/sectores/fontaneros-electricistas/` | — | Sectores | S | PM + AF (exenciones) | P1 |
| | `/calculadoras/cuota-autonomos/` | cuota autonomos 2027 | Autónomos | L | Dev + GS | P1 |
| **Jun 2027** | Actualización masiva del cluster VERI*FACTU (fechas, FAQ, capturas del estado de remisión si ya existe) | — | VERI*FACTU | S | AL + PM | P0 |
| | Artículo «Migra tu facturación en una tarde: importar clientes, productos y facturas» | cambiar programa facturación | Facturación | S/A | PM | P1 |
| | `/guias/factura-electronica-b2b/` (con el estado de la Orden) | factura electrónica obligatoria | Facturación / Pymes | S | AL | P1 |
| | `/sectores/mantenimiento/` + `/sectores/disenadores/` | — | Sectores | S | PM | P2 |
| **Jul 2027** (2T + VERI*FACTU resto) | Artículo «Hoy entra VERI*FACTU para todos: qué cambia en tu factura» | verifactu obligatorio | VERI*FACTU | S | AL | P0 |
| | Artículo «Modelo 303 y 130 del 2T» (actualización de pilares) | — | Impuestos | S | AF | P1 |
| | Artículo «Plazos legales de pago y morosidad (Ley 3/2004)» | plazo pago facturas ley | Cobros | S | AL | P2 |
| | Glosario: primeros 20 términos | — | Transversal | — | Contenidos + AF | P2 |
| **Ago 2027** (bajo volumen) | Artículo «Facturas recurrentes: cómo automatizar cuotas y contratos» | facturación recurrente | Facturación | S | PM | P2 |
| | Artículo «Previsión de tesorería para septiembre» | previsión tesorería | Cobros / Pymes | S | AF | P2 |
| | `/funciones/equipo-y-gestoria/` + guía «Cómo trabajar con tu gestoría» | — | Pymes | S | PM | P2 |
| | Mantenimiento: auditoría de enlaces, actualización de precios de competidores | — | — | — | Contenidos | P1 |
| **Sep 2027** (vuelta) | Artículo «Vuelta al trabajo: pon al día tus facturas, cobros y gastos en una mañana» | — | Autónomos | S/A | Contenidos | P2 |
| | `/sectores/desarrolladores-informaticos/` + `/sectores/fisioterapeutas-salud/` | — | Sectores | S | PM + AF | P2 |
| | Artículo «Conciliación bancaria paso a paso con extracto Excel/CSV» | conciliación bancaria | Gastos / Pymes | S | PM | P2 |
| | Artículo «Antes del 20 de octubre: checklist 3T» | — | Impuestos | S | AF | P1 |
| **Oct 2027** (3T) | Actualización del calendario fiscal 2028 (borrador) | calendario fiscal 2028 | Impuestos | L | AF | P1 |
| | Artículo «IVA de facturas impagadas: cómo recuperarlo» | modificar base imponible impago | Cobros | S | AF | P2 |
| | `/comparativas/facturales-vs-billin/` (o según la SERP) | — | Comparativas | S | Contenidos | P2 |
| | Revisión anual de todas las guías (`dateModified`) | — | — | — | Contenidos + expertos | P0 |

Black Friday / cierre de año: Facturales no hace descuentos inventados. Si hay promoción, usar **solo** «hasta −25 % en anual», que es estructural, no una oferta. Contenido para el comercio: «Prepara tu stock para Black Friday» (noviembre, inventario, P2).

## C5. Plantillas de página (wireframes textuales sobre el design system `fx-*`)

Todas usan `body.fx`, el header y el footer compartidos, Onest, iconos Lucide de 2 px, `--fx-acento` en los CTA (texto `--fx-sobre-acento`), un único `h1`, `.fx-claro` solo en lectura larga, y capturas reales con la etiqueta «Captura real … con datos de ejemplo». Componentes existentes: `fx-btn`, `fx-card`, `fx-badge`, `fx-section`, mockups, `<details>` FAQ, pricing, forms y `fx-post`/prosa.

### T1 · Landing de funcionalidad (`/funciones/[x]/`)
1. **Breadcrumb** (Inicio › Funciones › X) + JSON-LD `BreadcrumbList`.
2. **Hero**: badge («Nuevo» si es Bancos/Cobros/Gastos/Gráficas) · H1 orientado a la keyword («Programa de control de stock para pymes y autónomos») · subtítulo con el beneficio · CTA primario «Empieza 14 días» (`?plan=pro&utm_content=hero`) · secundario «Ver precios» · microcopy de confianza (véase C6.3) · captura real.
3. **Problema → resultado** (3 tarjetas con dolor y solución).
4. **«Así se ve en la app»**: 2–3 capturas con pie.
5. **«Qué puedes hacer»**: grid de 6–9 `fx-card` (ya existe).
6. **Cómo funciona** en 3 pasos.
7. **Para quién**: enlaces a 2–3 sectores y al tipo de negocio.
8. **Bloque de cumplimiento** (si aplica): VERI*FACTU registro + QR, Facturae, datos en la UE.
9. **Límites por plan** de la función (p. ej., OCR 10/75/300) con enlace a precios.
10. **FAQ** de 4–6 preguntas (`FAQPage`), incluidas las objeciones.
11. **«Aprende más»**: 3 enlaces a la guía del cluster y a artículos.
12. **«Funciona mejor junto a»** (ya existe).
13. **CTA final** (ya existe) con `utm_content=cta_final`.

### T2 · Landing de sector (`/sectores/[x]/`)
1. Breadcrumb.
2. Hero: H1 «Programa de facturación para [sector]» · subtítulo con 2 tareas del sector · CTA · captura con datos de ejemplo del sector (generar en el workflow `capturas` con datos sintéticos del sector).
3. «Lo que te quita tiempo hoy» (3 dolores específicos).
4. «Cómo lo resuelve Facturales»: 3–4 funciones reales con su enlace a `/funciones/*`.
5. **Ejemplo práctico** (p. ej., presupuesto de reforma de baño → factura con 2 hitos; o academia con 30 alumnos y recurrente mensual + recordatorio).
6. Fiscalidad del sector (caja `fx-claro` revisada por AF: IVA aplicable, exenciones, IRPF), con aviso de «información general».
7. Plantilla descargable del sector (lead magnet).
8. Plan recomendado (por volumen: clientes/productos).
9. FAQ del sector.
10. CTA final.

Regla: **sin casos de cliente inventados**. Los ejemplos se presentan como «ejemplo» con datos ficticios.

### T3 · Comparativa (`/comparativas/facturales-vs-x/`)
1. H1 «Facturales vs X: comparativa [mes año]».
2. **Caja de transparencia**: «Somos Facturales. Comparamos con datos públicos de X consultados el dd/mm/aaaa (enlaces abajo). Si algo ha cambiado, escríbenos a info@facturales.es y lo corregimos en 5 días hábiles.»
3. **Resumen en 3 líneas**: para quién es mejor cada uno (honesto: reconocer dónde gana X, p. ej. contabilidad completa, integraciones o banca conectada hoy).
4. **Tabla de funciones** (✓ / ✗ / «Próximamente» / «No verificado»), solo con criterios verificables. Cada celda de X lleva su fuente.
5. **Tabla de precios** comparando planes equivalentes, IVA aparte, con la fecha de consulta y una captura archivada.
6. Diferencias clave (3–5 bloques).
7. «Cuándo elegir X» y «cuándo elegir Facturales».
8. Migración: importar clientes, productos, facturas y extractos (`faq.html:28`).
9. FAQ.
10. CTA + **fuentes** (lista de URLs con fecha).

### T4 · Alternativa (`/alternativas/x/`)
1. H1 «Alternativas a X para autónomos y pymes ([año])».
2. Caja de transparencia (igual que T3).
3. Por qué la gente busca alternativa: motivos **genéricos y verificables** (precio, complejidad, funciones), sin citar reseñas ni inventar quejas.
4. Lista de 4–6 alternativas **incluyendo a terceros** (con Facturales primero, pero honesto), con tabla resumen y fuentes.
5. Ficha de Facturales: qué hace y qué no (conexión bancaria «Próximamente», sin contabilidad completa…).
6. Cómo migrar desde X.
7. FAQ + CTA + fuentes.

### T5 · Guía pilar (`/guias/[x]/`)
1. Breadcrumb · H1 · **cabecera E-E-A-T**: autor (nombre, rol, foto, enlace a la bio), «Revisado por [nombre, nº de colegiado]», «Publicado el» / «Actualizado el», tiempo de lectura.
2. **Resumen** (caja «En 30 segundos», 3–5 bullets con fechas clave).
3. Índice (tabla de contenidos con anclas).
4. Secciones H2 con ejemplos numéricos, tablas y cajas «Ojo» y «Ejemplo».
5. CTA intermedio contextual (no intrusivo): «Facturales genera el registro y el QR en cada factura» (texto aprobado por legal).
6. Herramienta incrustada o enlazada (calculadora o calendario).
7. FAQ (`FAQPage`).
8. **Fuentes oficiales** (BOE, AEAT, Seguridad Social) con fecha de consulta.
9. Artículos del cluster (spokes).
10. CTA final + lead magnet (checklist PDF).

Superficie `.fx-claro` para la lectura. JSON-LD `Article` con `author` Person, `reviewedBy` (en `WebPage`), `dateModified` y `citation`.

### T6 · Artículo (`/blog/[slug]/`)
Como T5 pero más corto (900–1.800 palabras):
- cabecera de autor/revisor y fechas;
- resumen;
- cuerpo;
- 1 CTA contextual hacia una landing de función;
- caja «Guía completa» hacia el hub;
- 2 artículos relacionados;
- fuentes.

### T7 · Plantilla descargable (`/recursos/plantillas/[x]/`)
1. H1 «Plantilla de [factura] gratis en Excel, Word y PDF».
2. **Vista previa** (imagen real de la plantilla) + 3 botones de descarga (formato y tamaño). **Descarga directa sin email**: el email es opcional para recibir actualizaciones (menos fricción, más enlaces).
3. «Cómo rellenarla» (campos obligatorios según el RD 1619/2012, revisado por AF).
4. Ejemplo rellenado.
5. Errores frecuentes.
6. **Puente a producto**: «Una plantilla no genera registro VERI*FACTU. Desde el 01/07/2027, si facturas con un programa, este debe cumplir el reglamento» (texto revisado por legal) → `/herramientas/generador-facturas/` y signup.
7. FAQ (¿vale Word para VERI*FACTU?, ¿puedo poner mi logo?).
8. Plantillas relacionadas.

Eventos: `template_download{formato}`.

### T8 · Herramienta gratuita (generador y calculadoras)
1. H1 + subtítulo («Sin registrarte»).
2. **Herramienta arriba del todo** (above the fold en desktop), formulario `fx-form` accesible (labels, errores en vivo, objetivos de 44 px).
3. Resultado inmediato: desglose (base, IVA, IRPF, total) con «Copiar» y, en el generador, «Descargar PDF».
4. **Paso a producto tras obtener valor**: «Guarda este cliente y emite la siguiente en 1 clic» → signup con `utm_campaign=generador` (y, si se puede, `?prefill` del cliente; véase C6.4).
5. Explicación de la fórmula y ejemplos (contenido SEO bajo la herramienta).
6. FAQ, fuentes y fecha de los tipos aplicados.

Técnico: JS vanilla en `facturales.js` o un módulo propio, **sin dependencias** (coherente con CLAUDE.md). El generador crea el PDF en el cliente (no sube datos; decirlo como argumento de privacidad). Avisar de que el PDF generado **no es un registro VERI*FACTU** (texto legal).

## C6. CRO

### C6.1 Embudo orgánico y métricas

| Etapa | Definición | Métrica | Dónde se mide |
|---|---|---|---|
| Visita | Sesión orgánica en la landing | Sesiones por tipo de página/cluster | Analítica de la landing (a implantar; recomendada sin cookies: Plausible/Umami, o GA4 con consentimiento) |
| Interacción | Scroll ≥ 50 %, uso de herramienta, descarga, toggle de precios, FAQ abierta | % de sesiones con interacción | Landing |
| Intención | Clic en un CTA a signup | CTR de CTA por ubicación | Landing (`cta_click`) |
| Signup | Cuenta creada (`auth.signUp` OK) | Signups / clics | App |
| Verificación | Email confirmado | % confirmados | App (`/confirm-email`) |
| Perfil | `/complete-profile` completo | % | App |
| Prueba | Checkout completado con trial | Trials / signups | Stripe webhook (`stripe-webhook`) |
| Activación | **Primera factura emitida** (o primer presupuesto o extracto importado) en 7 días | % activados | App |
| Pago | Primera cuota cobrada (fin de la prueba) | Trial → pago | Stripe |
| Retención | Activo en el mes 2–3 | | App |

### C6.2 Hipótesis de mejora por página

| Página | Problema observado | Cambio propuesto | Métrica |
|---|---|---|---|
| Home | Un solo texto de CTA; los botones de plan no pasan el plan; no hay enlace a recursos | (1) `?plan=` en los botones de plan; (2) CTA secundario «Ver cómo funciona» hacia el bloque de capturas; (3) bloque «Recursos gratis» (generador, plantillas, calendario) para el tráfico no listo; (4) franja de confianza bajo el hero: «Datos en la UE · Verificación en dos pasos · Sin permanencia · Registro VERI*FACTU y QR en cada factura · Empresa española» | CTR hero, signup/visita |
| Precios | Solo 2 enlaces internos; la tabla no muestra Inventario, Recurrentes, Recordatorios, Bancos, Cobros ni Gastos; no explica cómo funciona la tarjeta | (1) Añadir filas a la tabla; (2) FAQ «¿Me pedís tarjeta?» con texto honesto aprobado («Para activar la prueba introduces un método de pago; no se cobra nada si cancelas antes del día 14» — **validar con producto el comportamiento exacto de Stripe**); (3) «¿Qué plan necesito?»: selector de 3 preguntas (clientes, facturas/mes, usuarios) que recomienda plan; (4) bloque «Para gestorías» → `/gestorias/`; (5) datos de la empresa | Clic en plan, trial |
| Funciones | 280 palabras; es un índice | Ampliar con un resumen por función, una captura y «para quién»; filtro por necesidad (facturar / cobrar / impuestos / stock) | CTR a landings |
| Landings de función | CTA idéntico arriba y abajo; sin CTA contextual intermedio; sin enlace a guías | CTA intermedio tras «Así se ve en la app»: «Pruébalo con tus datos: importa tus clientes en Excel» (función real); bloque «Límites por plan»; enlaces a la guía; microcopy bajo el CTA | CTR intermedio |
| `crea-envia-facturas` | El H1 promete «listas para VERI*FACTU» | Mantenerlo solo si legal lo aprueba; añadir «Qué hace hoy Facturales con VERI*FACTU» (registro, huella, QR; remisión al completar el alta) | Confianza, menos tickets |
| `cobros` y recordatorios | La función estrella del 17/10 está dentro de otra página | Landing propia con ejemplo del email que se envía (captura real) y el calendario configurable | Signups atribuidos |
| `gestiona-tu-stock` | — | CTA «Importa tu catálogo en Excel» + plantilla de control de stock como puente | Descarga → signup |
| FAQ | Bien de objeciones; pocos enlaces | Enlace de cada respuesta a su landing o guía; CTA por sección | CTR |
| Blog/guías | CTA genérico «Ver funciones» | CTA contextual por cluster + lead magnet (checklist VERI*FACTU PDF, calendario .ics) + caja lateral sticky en desktop | Leads/visita |
| About | 156 palabras, sin personas | Equipo con nombres y fotos reales, razón social, sede, «cómo verificamos el contenido fiscal», compromiso con los datos | Tiempo, CTR a precios |
| Contacto | mailto; 89 palabras | Formulario real (sin backend: servicio de formularios en la UE, o `mailto` con plantilla), tiempos de respuesta por plan (email / chat / teléfono según el plan) y enlace a la FAQ | Contactos, menos rebote |

### C6.3 Bloques de confianza permitidos (reutilizables)

- **Seguridad**: «Datos alojados en la UE» · «Verificación en dos pasos» · «Historial de cambios» · «Exporta o elimina tu cuenta cuando quieras» (`App.tsx:204`).
- **Cumplimiento**: «Registro de facturación con huella encadenada y QR en cada factura» · «Descarga en Facturae 3.2.2» (sin «firmada»). Remisión a la AEAT: solo «al completar el alta» o «Próximamente», según legal.
- **Comercial**: «Sin permanencia» · «14 días de prueba» · «Precios + IVA, sin sorpresas» · «Hasta −25 % en anual».
- **Producto real**: capturas reales con datos de ejemplo · «Rol Gestor: tu gestoría entra con su usuario, consulta, exporta y cierra los meses».
- **Empresa**: «Facturales es un producto de AVENUE DIGITAL GROUP, S.L. (Valladolid)», si el negocio lo aprueba.
- **Prohibido**: testimonios, logos de clientes, nº de usuarios, estrellas, «certificado/homologado», «sin tarjeta», «envío automático a la AEAT», banca conectada.

Microcopy bajo el CTA (proponer a producto/legal; elegir según el comportamiento real del Checkout):
- A: «14 días de prueba · Sin permanencia · Cancela cuando quieras»
- B: «Pruébalo 14 días. Si cancelas antes, no pagas nada.» (solo si es exacto)

### C6.4 Lead magnets (por orden de impacto / esfuerzo)

1. **Generador de facturas online** (P0, XL): genera el PDF en el cliente. Tras la descarga: «Crea tu cuenta y emite esta misma factura con registro VERI*FACTU». Opcional: guardar el borrador en `localStorage` y pasarlo a la app por `?import=` (lo valida producto; sin datos personales en la URL, mejor un handoff con `postMessage` o un endpoint).
2. **Plantillas de factura y presupuesto** (P0, M): descarga directa.
3. **Calendario fiscal 2027** con `.ics` y recordatorio por email antes de cada trimestre (P0, M), que da la base de nurturing.
4. **Checklist VERI*FACTU (PDF)** para autónomos y sociedades (P0, S, tras la revisión legal).
5. **Calculadoras** IVA / IRPF / 130 / cuota de autónomos (P0–P1).
6. **Plantillas de email de recordatorio de pago** (P1, S): puente directo a los recordatorios automáticos.
7. **Plantilla Excel de control de stock** (P1, S): puente a inventario.
8. **Kit para gestorías** (P2): guía de cómo invitar a clientes, rol Gestor y cierre de meses.

### C6.5 Eventos a medir (nombres propuestos)

Landing:
- `page_view{page_type, cluster}`
- `cta_click{cta_text, cta_location: hero|mid|plan_card|final|header|article_inline|sidebar, plan?, periodo?}`
- `pricing_toggle{periodo}`
- `plan_select{plan}`
- `faq_open{pregunta}`
- `tool_start{tool}`, `tool_complete{tool}`
- `template_download{plantilla, formato}`
- `lead_submit{magnet}`
- `outbound_signup{utm_*}`
- `scroll_depth{25,50,75,100}`
- `screenshot_zoom`

App:
- `signup_view{plan_param, utm_*}`
- `signup_submit`, `signup_success{method: email|google}`
- `email_confirmed`
- `profile_completed`
- `plans_view{preselected_plan}`
- `checkout_start{plan, interval}`
- `trial_started` (webhook)
- `first_invoice_issued`, `first_quote_issued`, `first_bank_import`, `first_ocr_scan`
- `team_invite{role}`
- `recurring_created`, `reminder_enabled`
- `trial_converted` / `trial_canceled`

### C6.6 Tests A/B propuestos (en orden)

| # | Página | Variante | Hipótesis | Métrica primaria |
|---|---|---|---|---|
| 1 | Precios y home | Preselección de plan (`?plan=pro&periodo=anual` → `/planes` con plan marcado) vs control | H2 | Checkout iniciado / clic en plan |
| 2 | Hero de la home | CTA «Empieza gratis 14 días» vs «Prueba Facturales 14 días» vs «Crea tu primera factura» | Orientar a la activación mejora la calidad del signup | Signup → primera factura |
| 3 | Bajo el CTA | Microcopy A vs B vs nada | Reduce la ansiedad por el pago | Trial iniciado |
| 4 | Precios | Con o sin bloque «Empresa española + datos en la UE + 2FA» | H8 | Clic en plan |
| 5 | Guías | CTA contextual intermedio vs solo final | H3 | CTR a signup desde el blog |
| 6 | Plantillas | Descarga directa vs descarga con email opcional | El email opcional no reduce descargas y crea una lista | Descargas, leads |
| 7 | Generador | CTA tras la descarga «Guárdala en Facturales» vs «Emite con VERI*FACTU» | ¿El cumplimiento motiva más que la comodidad? | Signup/uso |
| 8 | Precios | Anual por defecto (actual `aria-pressed="true"`) vs mensual por defecto | Efecto en el ARPA y la conversión | Trial + mix anual |

Con poco tráfico, usar tests secuenciales o bayesianos con duración mínima de 2 ciclos de negocio (2–4 semanas) y no más de un test por página.

### C6.7 Paso del origen orgánico a la app (atribución end-to-end)

**Hoy**: ninguna atribución (A4).

**Propuesta mínima, sin cookies de terceros**:

1. **Landing (`assets/js/facturales.js`)**: en la primera visita, leer `utm_source/medium/campaign/content/term`, `gclid`, `document.referrer` y la página de entrada. Guardar *first touch* y *last touch* en `localStorage` (con try/catch). Al hacer clic en cualquier `a[href^="https://app.facturales.es/signup"]`, reescribir el `href` añadiendo:
   - `utm_source` (si no hay: `google`/`bing` según el referrer, o `direct`), `utm_medium=organic|referral|cpc`, `utm_campaign=<cluster>`, `utm_content=<cta_location>`;
   - `lp=<ruta de entrada>` y `ref=<host del referrer>`;
   - `plan=<starter|pro|business>` y `periodo=<mensual|anual>` cuando el botón sea de plan.

   Mantener los enlaces estáticos ya etiquetados en HTML como respaldo sin JS (p. ej. `?utm_source=facturales.es&utm_medium=web&utm_content=hero`).
2. **App, `/signup`** (`use-acceso.ts`): al montar, leer `location.search` y persistir `{utm_*, lp, ref, plan, periodo, landing_ts}` en `sessionStorage` (sobrevive a la verificación de email en la misma pestaña; para otra pestaña o dispositivo, ver el punto 3).
3. **Guardarlo con la cuenta**: ampliar `buildSignUpMetadata(firstName, lastName)` (`use-acceso.ts:135`) para incluir `acquisition: {…}` en `options.data`, que ya se envía en `auth.service.ts:103`. Así queda en `raw_user_meta_data` aunque se confirme el email desde otro dispositivo. Para **Google OAuth** (`auth.service.ts:120-135`), guardar el origen en `sessionStorage` antes de redirigir y escribirlo en el perfil tras el callback (p. ej. en `complete-profile`). Opcional: tabla `user_acquisition` con RLS (solo el propio usuario inserta una vez; admin lee).
4. **`/planes`**: si viene `plan`/`periodo`, preseleccionarlos (H2).
5. **Stripe**: añadir `acquisition_source`/`campaign` a `metadata` en `create-checkout-session` (`app.ts:94,103`) para cruzar MRR por canal en `admin_get_plan_stats` / AdminFinance.
6. **Privacidad**: los UTM y la página de entrada no son datos personales por sí solos, pero al asociarlos a la cuenta pasan a serlo. Mencionarlo en la política de privacidad (finalidad: analítica de captación; base: interés legítimo) y no guardar el referrer completo con query, solo el host.
7. **Analítica de la landing**: una herramienta sin cookies (Plausible/Umami, alojada en la UE) evita el banner y es coherente con «datos en la UE». Si se usa GA4, hace falta consentimiento (CMP) antes de cargarla.

### C6.8 Activación (lo que pasa tras el signup y condiciona el pago)

- Checklist de primeros pasos en la app: datos fiscales → logo → primer cliente (o importar Excel) → primera factura → activar recordatorios → invitar a la gestoría.
- Emails de onboarding durante la prueba: día 0 (bienvenida y crear factura), día 2 (importar clientes), día 5 (recurrentes y recordatorios), día 9 (impuestos 303/130 e invitar a la gestoría), día 12 (aviso de fin de prueba, transparente). Reutilizar Resend (`recordatorios-cobro` ya lo usa). Lo diseña otro equipo.
- Adaptar el onboarding según el origen (`utm_campaign`): quien viene de inventario empieza por el catálogo; quien viene de VERI*FACTU, por los datos fiscales y la primera factura.

## C7. Reglas para comparativas y alternativas honestas y verificables

1. Una **fecha de consulta** visible en la cabecera y en cada celda de precio.
2. Una **fuente** por cada dato del competidor (URL de su página de precios o de su documentación) y una **captura archivada** interna (y/o enlace a archive.org) de esa fecha.
3. Solo criterios **objetivos y verificables**: precio de lista sin IVA, límites del plan, existencia documentada de una función. No opiniones, reseñas de terceros ni «más fácil».
4. Si un dato no se puede verificar: «No verificado» en lugar de ✗.
5. Reconocer dónde gana el competidor (p. ej., contabilidad completa, banca conectada hoy, integraciones, nóminas).
6. Para Facturales, mostrar el estado real: «Próximamente» para banca conectada, remisión a la AEAT según legal, sin nóminas.
7. Revisión cada trimestre y tras cualquier cambio de precios (alerta). Responsable con nombre.
8. Revisión jurídica previa sobre publicidad comparativa (Ley 34/1988 General de Publicidad, art. 10, y Ley 3/1991 de Competencia Desleal, art. 10): comparación objetiva, de bienes homogéneos, sin denigrar.
9. No usar logos ni marcas de forma que sugiera afiliación. Usar el nombre en texto.
10. Canal de corrección público («¿Ves un error? Escríbenos»).

## C8. Gobernanza de contenido (E-E-A-T)

- **Autores**: página `/sobre-nosotros/equipo/` con bios reales. Schema `Person` con `sameAs` (LinkedIn).
- **Revisores**: acuerdo con 1 asesor fiscal colegiado (impuestos, VERI*FACTU, facturación), 1 abogado (morosidad, publicidad comparativa, B2B) y 1 graduado social (cuota de autónomos). Mostrar «Revisado por» con fecha.
- **Política editorial** visible: cómo se elaboran y actualizan las guías, fuentes oficiales y fe de erratas.
- **Calendario de revisión**: guías fiscales cada 6 meses y tras cada cambio normativo; comparativas cada trimestre.
- **Checklist de claims** antes de publicar: contrastar contra A1 + CLAUDE.md, y que PM firme que la función existe en producción.
- **Datos estructurados**:
  - `Article`/`BlogPosting` con `author` Person, `dateModified` y `citation`;
  - `FAQPage` (ya existe en landings);
  - `BreadcrumbList`;
  - `SoftwareApplication` con `offers` en las landings comerciales;
  - `HowTo` no (Google lo ha retirado de los resultados enriquecidos);
  - `DefinedTerm` en el glosario.

## C9. Roadmap resumido (prioridades)

**P0, 0–6 semanas**
- Revisión legal del copy VERI*FACTU (web + artículos + leyenda en el PDF de la app).
- Corrección de los 3 artículos.
- Analítica sin cookies + UTM/atribución (C6.7, puntos 1–3).
- `?plan=` en los botones de plan y preselección en `/planes`.
- FAQ honesta sobre el método de pago.
- Migración a URLs limpias con 301.
- Pilares `/software-facturacion/`, `/programa-facturacion-autonomos/`, `/verifactu/` y `/guias/verifactu/`.
- Plantilla de factura y calendario fiscal.
- `/funciones/facturas-recurrentes/` y `/funciones/recordatorios-de-pago/`.

**P1, 6–16 semanas**
- Generador de facturas.
- Calculadoras IVA, IRPF y 130.
- `/gestorias/`, `/software-facturacion-pymes/`.
- 4 sectores.
- Hub de comparativas + Holded/Quipu/Excel.
- Guías 303/130 y morosidad.
- About y contacto ampliados.
- Test A/B 1–3.

**P2, 4–9 meses**: resto de sectores, comparativas y alternativas, glosario, guía de factura electrónica B2B, cuota de autónomos, gastos deducibles e inventario.

**P3**: panel, clientes, agencias y talleres; actualización anual.

---

## D. Preguntas abiertas para producto y legal

1. ¿Puede la web decir «facturas listas para VERI*FACTU» y mostrar la leyenda «VERI*FACTU» en el PDF mientras no se remite a la AEAT? ¿Fecha prevista del alta Tipo 017 y de la remisión? (`declaracion-responsable-fabricante.md:74-78`)
2. ¿El Checkout de la prueba exige tarjeta siempre? ¿Se cobra automáticamente el día 15? Hace falta para redactar la FAQ de pago.
3. ¿El rol Gestor cuenta como usuario del plan? ¿Se aplica el límite 1/3 de usuarios en el backend? (H5)
4. ¿Los recordatorios automáticos y las recurrentes están desplegados en producción para todos o tras un flag? (H6)
5. ¿Hay soporte completo para el recargo de equivalencia, operaciones intracomunitarias o exentas? Condiciona los sectores comercio, desarrolladores y salud.
6. ¿Se aprueba mencionar la razón social y la sede en el marketing?
7. Hosting de la landing: ¿admite 301 y URLs limpias? (determina la migración)

---

## Fuentes externas consultadas (18/10/2026)

- [Cuatrecasas: Ampliado el plazo para la adaptación de los SIF (RDL 15/2025)](https://www.cuatrecasas.com/es/spain/fiscalidad/art/rdl15-sistemas-informaticos-facturacion-plazo)
- [Garrigues: Se retrasa la entrada en vigor de Verifactu (convalidación, BOE 16/12/2025)](https://www.garrigues.com/es_ES/noticia/retrasa-entrada-vigor-verifactu)
- [RSM: VeriFactu aplazado hasta 2027 (PDF)](https://www.rsm.global/spain/sites/default/files/media/VeriFactu%20aplazado%20hasta%202027.pdf)
- [Spendesk: Factura electrónica B2B obligatoria: RD 238/2026, plazos](https://www.spendesk.com/es/blog/factura-electronica-b2b-obligatoria/)
- [PwC Periscopio: La facturación electrónica B2B ya está aquí](https://periscopiofiscalylegal.pwc.es/?p=21417)
- [B2Brouter: Plazos de obligatoriedad de la factura electrónica B2B](https://www.b2brouter.net/es/plazos-obligatoriedad-factura-electronica-b2b/)

> Aviso: las fuentes normativas son secundarias. Un experto debe confirmar en el BOE el texto del RD-ley 15/2025 y su convalidación, el RD 238/2026 y el estado de la Orden Ministerial de la solución pública de facturación electrónica. Los volúmenes de keywords no se han medido (no había herramientas de SEO autorizadas en la sesión).
