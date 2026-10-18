# 02 · Keywords y competencia SEO: Facturales (facturales.es)

**Fecha:** 18/10/2026 · **Mercado:** Google España (base de datos SE Ranking `es`, snapshot de octubre de 2026) · **Idioma:** español

## 0. Fuentes y cómo leer este informe

| Etiqueta | Qué significa |
|---|---|
| **DATO** | Viene de la API de SE Ranking (Data API, base `es`): volumen mensual, KD (dificultad 0-100), CPC (€), tráfico orgánico estimado, nº de keywords, páginas top, comparativas de dominios y SERPs reales (escritorio, ES, rastreadas el 18/10/2026). |
| **ESTIMACIÓN** | Es criterio mío: intención, etapa del embudo, página de destino, prioridad, el «s/d + alta/media/baja» cuando SE Ranking no tiene volumen, y cualquier conclusión estratégica. |
| **SERP-3º** | Datos que aparecen en snippets de terceros dentro de las SERP (por ejemplo, precios de competidores). No los he verificado en origen. |

**Llamadas hechas:** `getDomainOverviewByCountry` (16 dominios), `getDomainCompetitors` (getquipu.com, 405 dominios), `getDomainPages` (holded, quipu, billin, anfix, contasimple, facturadirecta, stelorder, declarando, getrenn), `getDomainKeywords` (facturales.es), `getKeywordsMetrics` (unas 815 keywords consultadas en 4 lotes, ~560 con dato), `getSimilarKeywords` y `getRelatedKeywords` (programa de facturacion, verifactu, conciliacion bancaria), `getDomainKeywordsComparison` (holded∩quipu; quipu−facturales) y 14 SERPs reales. Los JSON en bruto están en `[scratchpad de la auditoría, no versionado]/data/`.

**Limitaciones de los datos (importante):**
1. SE Ranking normaliza las tildes. Las variantes acentuadas suelen devolver «sin datos» o la misma cifra que la forma sin tilde. Las he usado sin tilde.
2. Hay volúmenes de cabeza que parecen anómalos o infraestimados. Por ejemplo, «conciliacion bancaria» = 10 cuando la variante «que es conciliacion bancaria» = 480, y «facturacion online» = 10. En varias keywords la serie mensual tiene meses a 0, lo que apunta a datos incompletos. Los marco como «anómalo» y doy una ESTIMACIÓN cualitativa.
3. El KD de SE Ranking subestima a veces la competencia real. «software verifactu» tiene KD 5, pero en su SERP están la AEAT, Holded, Wolters Kluwer, Sage o Delsol. Cuando el SERP lo contradice, lo indico.
4. SE Ranking clasifica casi todo como intención «I» (informacional), incluso «software de facturación». Por eso la columna de intención de las tablas es mi ESTIMACIÓN.
5. El tráfico orgánico de SE Ranking es una estimación conservadora (CTR × volumen de keywords en top 100). Sirve para comparar dominios entre sí, no como tráfico absoluto real.

---

## 1. Resumen ejecutivo

1. **Facturales hoy es prácticamente invisible en búsqueda orgánica (DATO).** Tiene 16 keywords en el top 100, tráfico estimado 0 y ninguna en el top 10. La mejor es «facturale» en la posición 19, y 12 de las 16 están entre la 51 y la 100. Sus mejores páginas son la home («facturas empresa», 320/mes, posición 48) y `tu-negocio-bajo-control.html` («control facturas», posición 44). No hay base que proteger, así que conviene plantearlo como un dominio que empieza de cero.
2. **El mercado se lo reparten cuatro jugadores con mucho contenido informacional (DATO):** Holded (~60,6 k visitas/mes estimadas, 150 k keywords), Quipu (31 k; ahora «TeamSystem Quipu»), Billin (29 k; ahora «TS Facturas, antes Billin», también de TeamSystem) y Anfix (27,5 k). Por detrás están Contasimple (21,6 k, que es quien más vale por visita: 24,6 k € de tráfico equivalente), Declarando (17 k), STEL Order (14,6 k) y FacturaDirecta (10,6 k, con el 84 % del tráfico en la home).
3. **El tráfico de los competidores no viene de las landings de producto.** Viene de herramientas gratuitas (calculadora de IVA, generador de facturas, plantillas Excel/Word/PDF), glosarios, guías de modelos AEAT (303/130/036) y artículos tipo «mejores programas de…». Las keywords transaccionales puras tienen poco volumen en SE Ranking («programa de facturacion» 590, «software de facturacion» 320, «programa facturacion autonomos» 260), pero CPC altos (3-10 €).
4. **Hay ventanas de baja dificultad y alta intención de contratación (DATO + ESTIMACIÓN):**
   - **VeriFactu comercial:** «programa facturacion verifactu» 480 KD 20; «software verifactu» 590 KD 5 (competencia real media); «programa verifactu gratis» 320 KD 20; «verifactu autonomos» 480 KD 28.
   - **Alternativas y precios de competidores:** «alternativa a holded» 90 KD 5; «precios holded» 480 KD 33; «contasimple opiniones» 390 KD 16; «billin precios» 260 KD 28; «quipu precios» 260 KD 21. En «alternativa a holded» rankean webs pequeñas y recientes (getrenn #1, yofacturo #3).
   - **Long tail de tipos de factura con KD < 10:** factura recapitulativa 590 KD 8; que es factura proforma 390 KD 9; factura rectificativa (cómo hacer) 390 KD 9; factura de abono 390 KD 8; modelo factura autónomo 480 KD 7; plantilla albarán 590 KD 8.
   - **Módulos nuevos de Facturales con SERP informacional débil:** control de stock 390 KD 8; gestión de cobros 320 KD 8; que es conciliación bancaria 480 KD 8; facturas recurrentes 50 KD 9 (CPC 2,55).
5. **Todos los SERPs analizados (14/14) muestran AI Overview** y casi todos PAA, vídeo y reseñas. Para competir hace falta contenido citable: definiciones cortas, tablas, pasos numerados y FAQ con schema, además de páginas de producto con prueba visual (capturas reales).
6. **Referencia útil de un recién llegado: getrenn.com (DATO).** Con solo 4 k keywords ya es #1 en «alternativa a holded» y está en el top 10 de «programa facturacion autonomos». Su estrategia: blog transaccional (cómo hacer una factura, plantilla Excel, programa de facturación gratis, alternativas a Holded). Muestra que un dominio nuevo puede entrar por el long tail comparativo en pocos meses.

---

## 2. Visibilidad de facturales.es (DATO SE Ranking, ES, oct-2026)

| Métrica | Valor |
|---|---|
| Keywords orgánicas (top 100) | 16 (9 nuevas y 5 perdidas este mes) |
| Tráfico orgánico estimado | 0 |
| Top 1-5 / 6-10 / 11-20 / 21-50 / 51-100 | 0 / 0 / 1 / 4 / 12 |
| Paid (Ads) | Sin anuncios detectados |

| Keyword | Pos. | Vol. | KD | URL |
|---|---|---|---|---|
| facturale | 19 | 10 | 8 | / |
| facturesas | 34 | 10 | 10 | / |
| control facturas | 44 | 40 | 17 | /tu-negocio-bajo-control.html |
| facturaciones | 45 | 30 | 49 | / |
| facturas empresa | 48 | 320 | 28 | / |
| facturación crm | 51 | 40 | 9 | /gestiona-clientes.html |
| facturacion de clientes | 53 | 20 | 21 | / |
| facturas empresas | 56 | 320 | 41 | / |
| controlar facturas | 58 | 40 | 29 | /tu-negocio-bajo-control.html |
| facturas contables | 58 | 40 | 7 | / |
| facturas de empresas | 59 | 90 | 12 | / |
| facturas de clientes | 62 | 20 | 21 | /gestiona-clientes.html |
| crm facturacion | 62 | 40 | 9 | /gestiona-clientes.html |
| factureras | 64 | 10 | 10 | / |
| control facturacion | 80 | 40 | 14 | /tu-negocio-bajo-control.html |
| facturas digitales express | 87 | 10 | 16 | / |

**Lectura (ESTIMACIÓN):** Google empieza a asociar el dominio a «facturas/facturación de empresa», pero no tiene ninguna página optimizada para una keyword con demanda clara. La marca «facturales» aún no tiene volumen medible (s/d en SE Ranking).

---

## 3. Competidores

### 3.1 Panorama (DATO SE Ranking, ES, oct-2026)

| Dominio | Tráfico org. est./mes | Keywords org. | Top 1-5 | Top 6-10 | Valor tráfico (€) | Keywords Ads | Nota |
|---|---|---|---|---|---|---|---|
| holded.com | 60.566 | 149.917 | 43.577 | 21.491 | 42.257 | 14.904 | Líder. Grupo Visma (SERP-3º) |
| sumup.com (todo el dominio, ES) | 32.849 | 74.948 | 24.294 | 11.004 | 26.254 | 326 | Absorbió Debitoor; tráfico mezclado con TPV/pagos |
| getquipu.com | 30.999 | 126.342 | 44.665 | 20.221 | 14.378 | 51 | Ahora «TeamSystem Quipu» |
| billin.net | 29.149 | 147.978 | 27.328 | 13.705 | 17.836 | 5.189 | Ahora «TS Facturas, antes Billin» (TeamSystem) |
| anfix.com | 27.473 | 98.790 | 24.223 | 13.811 | 8.741 | 800 | Calculadoras + diccionario |
| contasimple.com | 21.596 | 44.300 | 7.595 | 5.132 | 24.634 | 1.981 | Ahora «Cegid Contasimple» (SERP-3º); mayor valor por visita |
| infoautonomos.com | 20.313 | 134.505 | 30.474 | 15.634 | 7.500 | 0 | Medio informativo, no competidor de producto directo |
| declarando.es | 17.112 | 68.226 | 15.319 | 9.882 | 11.749 | 5.074 | Software + asesoría |
| stelorder.com | 14.564 | 82.797 | 17.055 | 9.013 | 8.014 | 230 | ERP para servicios técnicos; calendarios laborales |
| ayudatpymes.com | 11.011 | 91.420 | 23.087 | 9.958 | 4.417 | 197 | Asesoría online |
| facturadirecta.com | 10.626 | 14.535 | 2.309 | 1.325 | 19.168 | 27 | 84 % del tráfico en la home (marca + genéricas) |
| b2brouter.net | 9.589 | 12.439 | 3.241 | 2.382 | 11.546 | 66 | Factura electrónica B2B / FACe |
| cuentica.com | 6.868 | 33.416 | 8.711 | 5.793 | 3.486 | 0 | Autónomos con asesoría |
| getbillage.com | 5.841 | 42.457 | 5.024 | 3.322 | 3.142 | 0 | |
| getrenn.com | 1.779 | 4.004 | 1.330 | 1.010 | 2.362 | 18 | Nuevo, crece rápido (1.880 keywords nuevas este mes) |
| banktrack.com | 972 | 16.662 | 2.826 | 1.356 | 2.496 | 6 | Listicles «mejores software…» |
| txerpa.com | 967 | 13.081 | 1.393 | 868 | 538 | 0 | |
| **facturales.es** | **0** | **16** | 0 | 0 | 0 | 0 | |

Otros dominios que comparten keywords con Quipu (DATO, `getDomainCompetitors`; tráfico ES estimado): wolterskluwer.com (a3factura) 72,7 k · taxdown.es 90 k · factorial.es 68,3 k · sage.com 41,9 k · teamsystem.es 33,4 k · supercontable.com 31,9 k · cegid.com 20,1 k · appvizer.es 29,9 k · qonto.com 20,8 k · debitoor.es 2,4 k (marca casi abandonada) · alegra.com 1,8 k · openges.es 3,9 k. En los SERPs también aparecen con frecuencia sdelsol.com (Factusol/Contasol), facturascloud.com, facturascripts.com (open source, 990 búsquedas de marca), visionwin.com, idesoft.es, mnprogram.com, odoo.com y un número creciente de micro-SaaS y blogs de afiliación (yofacturo, factupro, facturaz, ninded, facturaclara, guiapymedigital, declaralia…).

### 3.2 Qué páginas les traen tráfico (DATO `getDomainPages`, ordenado por tráfico)

**Holded** (60,6 k):
| Página | Tráfico | Tipo |
|---|---|---|
| /es (home) | 17.185 (28 %) | Marca |
| /es/blog/sistema-red | 6.185 | Blog informativo (Seguridad Social) |
| app.holded.com/login | 3.110 + 1.251 | Navegacional |
| /es/blog/que-es-una-espj | 2.021 | Glosario fiscal |
| /es/autonomos | 918 | **Landing por segmento** |
| /es/blog/plan-negocio-ejemplo, ideas-negocio… | 600-940 | Blog generalista emprendedor |
| /es/blog/plantillas-de-almacenes-e-inventarios | 550 | **Plantillas descargables** |
| /es/herramientas/calculadoras-interes-compuesto | 533 | **Calculadora** |
| /es/crea-tu-factura | 516 | **Generador de facturas gratis** |
| /es/blog/programas-inventario | 462 | **Listicle «Top 8 software de inventario»** |
| /es/blog/los-mejores-programas-de-facturacion | 412 | **Listicle comparativo** (es #1 en «software de facturacion») |
| /es/blog/factura-electronica | 397 | Guía |
| /es/precios | 349 | Precios |
| /es/blog/facturas-ejemplos · plantillas-facturas-excel · plantilla-factura-autonomo · plantilla-presupuesto · plantillas-de-facturas-proforma · recibo-pago | 167-325 c/u | **Plantillas** |
| /es/programa-facturacion · /es/programa-contabilidad · /es/erp | 197-323 | Landings de producto |
| /es/blog/tabla-irpf (3.696 keywords) | 226 | Guía fiscal |

Arquitectura: `/es/{producto}` (programa-facturacion, programa-contabilidad, gestion-de-inventarios, erp, autonomos), `/es/programa-facturacion/{feature}` (portal-cliente), `/es/blog/{slug}`, `/es/guias/{slug}`, `/es/herramientas/{calculadora}`, `/es/crea-tu-factura` y `/es/crea-tu-presupuesto`, más páginas «alternativa a X» en `/ca/guies/alternativa-haz-tu-factura`. Tiene también `/es/programa-facturacion-verifactu` y `/es/blog/mejores-programas-facturacion-verifactu`, que es #1 en «programa facturacion verifactu».

**Quipu** (31 k):
| Página | Tráfico | Tipo |
|---|---|---|
| /blog/plantilla-nomina-modelo-y-ejemplo | 1.941 | Plantilla |
| / (home) | 1.817 | Marca + «programa de facturacion» #1 |
| /blog/calculadora-de-iva-de-una-cantidad-y-de-un-total | 1.706 | **Calculadora IVA** |
| /blog/modelos-y-plantillas-de-factura («45 plantillas…») | 940 (1.672 keywords) | **Plantillas factura** |
| /blog/plantilla-presupuesto-descargar | 656 | Plantilla presupuesto |
| /blog/modelo-recibo-pago-plantilla | 590 | Plantilla |
| /blog/calcular-el-finiquito… | 445 (4.082 keywords) | Calculadora |
| /blog/como-darse-de-alta-como-autonomo | 437 | Guía autónomo |
| /blog/que-es-el-modelo-036 · /como-rellenar-el-modelo-303 · /modelo-600 | 195-415 | **Modelos AEAT casilla a casilla** |
| /blog/modelos-y-plantillas-factura-autonomo | 413 | Plantilla autónomo |
| /blog/hoja-excel-ingresos-gastos-plantilla (4.089 keywords) | 382 | Plantilla gastos |
| /blog/codigos-entidades-bancarias | 367 | **Buscador / herramienta** |
| /es/generador-facturas-gratis-online | 255 (871 keywords) | **Generador facturas** (#1 en «generador de facturas») |
| /blog/calculadora-iva-irpf-factura | 224 | Calculadora |
| /blog/plantilla-gestion-de-cobros-y-pagos | 159 | Plantilla cobros |
| /es/autonomos | Landing (#1 «programa facturación autonomos») | Landing por segmento |
| /blog/mejores-programas-para-verifactu · /blog/sistema-verifactu-gratis | (#1 en programa facturacion verifactu, programa/software verifactu gratis) | **Listicles VeriFactu** |

Arquitectura: casi todo vive en `/blog/{slug}`, con landings en `/es/{segmento}` y herramientas en `/es/generador-…`. También tiene «alternativas a X» en el blog (`/blog/mejores-alternativas-contasimple/`).

**Billin / TS Facturas** (29 k): home 5.188 (17,8 %); `/calculadoras/` (calculadora-como-sacar-el-iva 910; simulador-prestamos 559; calcular-base-imponible 228; calculadora-letra-dni 241; calculadora-iva 205); un **glosario masivo** `/glosario/{término}` (eurostoxx 571, debe-y-haber 245, certificado-censal 189, cotizar 184…); blog de trámites (sistema-red 1.178; consultar declaraciones 526); `/generadores/crear-factura-gratis/` y `/generadores/generador-presupuestos/`; landings de feature `/control-de-stock/`, `/creacion-presupuesto/`, `/sistema-verifactu/`, `/programa-verifactu/`, `/programa-facturacion-autonomos/`, `/programa-facturacion-gratuito/`; y comparativa `/blog/billin-holded-alternativas/`.

**Anfix** (27,5 k): las calculadoras dominan (`/calculadora-iva` 2.789 = 10 %; `/calculadora-irpf` 513; `/calculadora-imv` 420; `/calculadora-sueldo-neto` 342; `/calculadora-tae` 273; finiquito 258), seguidas de `/diccionario/{término}` (jubilación 2.212; trabajador por cuenta ajena 697; gestión de cuentas 545) y un blog de guías (que-es-stripe 1.619; sistema RED 1.123; modelo 303 259). La landing `/autonomos` está en el top 5 de «programa facturacion autonomos». También tiene `/generador-de-facturas` y `/facturacion/presupuestos`.

**Contasimple** (21,6 k): home 6.237 (29 %, posicionada por «software de gestión para pymes»); `/diccionario-empresarial/agencia-tributaria/` 3.884; `/calculadoras-financieras/calculadora-facturas-iva-irpf-autonomos-pymes/` 2.967; **`/programa-facturacion-autonomos-gratis/` 1.118 (1.732 keywords, valor 3.475 €)**, que es #2/#3 en «programa de facturacion gratis», «programa facturacion autonomos» y «software de facturacion»; `/programa-contabilidad-autonomos-pymes/` 470; `/modelos-factura-generador-gratis-online/` 411; `/academia/como-crear-facturas-formato-facturae/` 348; `/reglamento-verifactu/` 242; `/programa-facturacion-autonomos-gratis/programa-presupuestos/` 229; `/generador-de-presupuestos-gratis-online/` 167; `/modelos-tributarios-hacienda-aeat/presentacion-modelo-303-iva/` 163; `/factura-electronica-obligatoria/` (con subpágina `/factura-face/`); `/conciliacion-bancaria/`; `/software-gestion-almacen-control-stock-inventarios/`. Su arquitectura temática (silos `/factura-electronica-obligatoria/…`, `/modelos-tributarios-hacienda-aeat/…`) es la más ordenada del grupo y la más fácil de replicar.

**Declarando** (17 k): blog de notificaciones de Hacienda 1.328; `/tramites-autonomos/sistema-red` 1.309; `/facturas/ejemplos-facturas` 822; `/plantilla-presupuesto` 646; `/facturas/hacer-factura-online` 538 (generador); `/modelo-303` (top 10); `/verifactu/mejores-programas-verifactu` y `/verifactu/verifactu-gratis`; `/factura-electronica` (top 10). Silos `/facturas/`, `/verifactu/`, `/factura-electronica/`, `/glosario/`.

**STEL Order** (14,6 k): home 2.683; blog generalista (sociedad anónima 789; calculadora de vacaciones 783; calendarios laborales por comunidad 730 + 239); listicles comerciales (`mejores-programas-gestion-empresarial` 415 con valor 1.356 €; `los-10-mejores-programas-de-facturacion…` 227; `mejores-programas-tpv` 201); y páginas «X: qué es y alternativas» (`factorial-que-es-y-alternativas` 243; `holded-que-es-y-alternativas` 183). También tiene `/crear-factura-gratis/`.

**FacturaDirecta** (10,6 k): la home concentra el 84 % (8.926; 3.362 keywords, valor 18.344 €) gracias a la marca y a genéricas. Además, glosario `/glosario/{término}` y `/verifactu/` (78), un visor Facturae (`viewer.facturadirecta.com`) y guías.

**getrenn.com** (1,8 k, nuevo): `/es/blog/como-hacer-una-factura` 339; `/excel-facturacion` 185; certificados AEAT 178; `/programa-de-facturacion-gratis` 100 (408 keywords); `/gestoria-autonomos-precios` 66; `/mejor-app-para-hacer-facturas-gratis` 59; y `/alternativas-holded` (#1 en el SERP).

### 3.3 Qué hacen distinto (ESTIMACIÓN a partir de los DATOS)

| Estrategia | Quién la usa | Peso en su tráfico | ¿Le sirve a Facturales? |
|---|---|---|---|
| Calculadoras (IVA, IRPF, IVA+IRPF en factura, finiquito, sueldo neto) | Anfix, Quipu, Contasimple, Billin | Muy alto: calculadora IVA de Anfix = 10 %; la de Contasimple = 14 % | **Sí**: calculadora IVA+IRPF de factura y «quitar IVA», con CTA a la prueba |
| Generador de facturas / presupuestos gratis | Holded, Quipu, Contasimple, Billin, Declarando, STEL, Anfix | Medio (250-540 visitas por página, CPC alto) | **Sí**, prioridad alta (capta la intención «gratis» que la prueba de 14 días no cubre) |
| Plantillas descargables (factura Excel/Word/PDF, autónomo, proforma, presupuesto, albarán, recibo, ingresos/gastos, inventario, cobros y pagos) | Quipu (más de 45 plantillas), Holded, Declarando | Alto y estable | **Sí** |
| Glosario o diccionario masivo | Billin, Anfix, FacturaDirecta, Contasimple, Declarando | Alto en volumen, poca intención | Solo selectivo: 30-50 términos de facturación e impuestos, sin generalismos |
| Modelos AEAT casilla a casilla (303, 130, 036, 347, 390, 349) | Quipu, Anfix, Contasimple, Declarando, Holded, Billin, Cuentica | Medio-alto | **Sí** para 303/130/390/347/349; encaja con «Impuestos: 303/130 calculados» |
| Calendario fiscal / laboral | STEL (laboral), AEAT | Estacional | Sí, «Calendario fiscal 2027 para autónomos» |
| Landings por segmento (autónomos / pymes / gestorías) | Holded, Quipu, Anfix, Billin, a3 | Media; son las que rankean en BOFU | **Sí, imprescindible** |
| Landings por sector («programa de facturación para X») | Casi nadie entre los grandes. Lo hacen verticales (hero-software, focoenobra, planreforma) y TPVs | Volúmenes pequeños pero CPC 2-5 € | **Sí, hueco claro** (long tail) |
| Páginas «Alternativa a X» / «X vs Y» / «X: qué es y alternativas» | STEL, Billin, Quipu, micro-SaaS | Bajo volumen, intención muy alta, KD bajo | **Sí, quick win** |
| Listicles «mejores programas de facturación / VeriFactu / presupuestos / inventario» | Todos (se incluyen a sí mismos los primeros) | Ocupan el top 3 de los genéricos BOFU | **Sí**, con una comparativa honesta y transparente |
| Blog generalista de emprendimiento / RR. HH. (ideas de negocio, nóminas, finiquito, sistema RED) | Holded, Quipu, STEL | Mucho tráfico, poca conversión | No (salvo trámites del autónomo muy ligados a la facturación) |
| Silo VeriFactu (qué es, gratis, mejores programas, programa VeriFactu) | Holded, Quipu, Billin, Declarando, Contasimple, Delsol | Creciente | **Sí, prioridad 1** |

---

## 4. Universo de keywords (~330 keywords, 22 clusters)

**Columnas:** Vol = volumen mensual ES · KD = dificultad 0-100 · CPC en € (**DATO SE Ranking**, salvo «s/d»). Intención (T transaccional, C comercial, I informacional, N navegacional), embudo (BOFU/MOFU/TOFU), destino y prioridad (P1 alta, P2 media, P3 baja, — no trabajar) son **ESTIMACIÓN**.

**Páginas existentes:** `/` (home), `crea-envia-facturas`, `crea-envia-presupuestos`, `bancos-conciliacion`, `cobros`, `escanea-gastos`, `impuestos`, `tu-negocio-bajo-control`, `gestiona-clientes`, `gestiona-tu-stock`, `factura-personalizada`, `pricing`, `funciones`, `faq`, `verifactu-2027-guia-autonomos-pymes`, `factura-electronica-vs-verifactu`, `contabilidad-negocio-7-pasos`. Las propuestas nuevas van marcadas con **[N]**.

### C1 · Software / programa de facturación (genéricos BOFU)
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| programa de facturacion | 590 | 63 | 5,04 | T | BOFU | / (home) + [N] /programa-de-facturacion | P1 (largo plazo) |
| programa de factura | 370 | 61 | 4,05 | T | BOFU | / | P2 |
| programa facturacion | 330 | 62 | 4,50 | T | BOFU | / | P2 |
| software de facturacion | 320 | 70 | 4,50 | T | BOFU | / | P2 |
| softwares de facturacion | 320 | 44 | 5,21 | T | BOFU | / | P2 |
| software de factura | 320 | 59 | 3,87 | T | BOFU | / | P3 |
| software facturacion | 260 | 54 | 4,10 | T | BOFU | / | P2 |
| software de facturación (con tilde) | 210 | 60 | 5,39 | T | BOFU | / | P2 |
| programa para hacer facturas | 480 | 59 | 3,68 | T | BOFU | crea-envia-facturas | P1 |
| programas para hacer facturas | 480 | 55 | 3,68 | T | BOFU | crea-envia-facturas | P2 |
| programa para hacer una factura | 480 | 56 | 3,68 | T | BOFU | crea-envia-facturas | P2 |
| programa de facturacion online | 70 | 45 | 9,85 | T | BOFU | / | P2 (CPC máximo del set) |
| programas de facturacion online | 50 | 52 | 8,00 | T | BOFU | / | P3 |
| software facturacion online | 40 | 68 | 7,14 | T | BOFU | / | P3 |
| facturacion online | 10 (anómalo; est. media) | 58 | 2,66 | T | BOFU | / | P3 |
| programa de facturacion electronica | 210 | 39 | 2,75 | T | BOFU | [N] /programa-factura-electronica | P2 |
| software facturacion electronica | 260 | 33 | 3,82 | T | BOFU | [N] /programa-factura-electronica | P2 |
| software factura electronica | 260 | 41 | 3,82 | T | BOFU | ídem | P2 |
| programas de facturacion electronica | 70 | 56 | 5,06 | T | BOFU | ídem | P3 |
| programa de facturacion y contabilidad | 170 | 37 | 4,27 | T | BOFU | funciones / impuestos | P2 |
| programas de contabilidad y facturacion | 170 | 24 | 4,27 | T | BOFU | funciones | P2 |
| programa de facturacion para pymes | 70 | 33 | 4,69 | T | BOFU | [N] /pymes | P2 |
| programas de facturacion para pymes | 70 | 29 | 4,69 | T | BOFU | [N] /pymes | P2 |
| programa de facturacion para empresas | 50 | 53 | 9,16 | T | BOFU | [N] /pymes | P3 |
| programas de facturacion para empresas | 50 | 44 | 9,16 | T | BOFU | [N] /pymes | P3 |
| comprar programa de facturacion | 70 | 48 | 3,46 | T | BOFU | pricing | P3 |
| programa de facturacion sencillo | 40 | 55 | 2,03 | T | BOFU | / | P3 |
| programas de facturacion en la nube | 20 | 37 | 3,70 | T | BOFU | / | P3 |
| cuanto cuesta un programa de facturacion | 20 | 30 | 1,68 | C | MOFU | pricing (FAQ) | P2 |
| programa de facturacion y control de stock | 10 | 35 | 3,43 | T | BOFU | gestiona-tu-stock | P2 |
| programa de inventario y facturacion | 10 | 29 | — | T | BOFU | gestiona-tu-stock | P3 |
| programa de facturacion para mac | 30 | 8 | 2,82 | T | BOFU | faq / [N] /programa-facturacion-mac | P3 |
| software de gestión | 440 | 24 | 3,65 | C | MOFU | funciones | P3 |
| programa de gestion | 390 | 42 | 3,43 | C | MOFU | funciones | P3 |
| software de gestion empresarial | 320 | 33 | 3,73 | C | MOFU | funciones | P3 |
| erp para pymes | 320 | 23 | 5,11 | C | MOFU | — (Facturales no es un ERP) | — |
| programa de contabilidad | 360 | 38 | 2,43 | C | MOFU | impuestos | P3 |
| software contabilidad | 390 | 31 | 3,30 | C | MOFU | impuestos | P3 |

### C2 · «Gratis»
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| programa para hacer facturas gratis | 480 | 41 | 1,87 | T | BOFU | [N] /generador-de-facturas + listicle | P1 |
| programa gratis para hacer facturas | 480 | 24 | 1,87 | T | BOFU | ídem | P1 |
| programa gratuito para hacer facturas | 480 | 32 | 1,87 | T | BOFU | ídem | P2 |
| facturacion programa gratis | 360 | 41 | 1,28 | T | BOFU | ídem | P2 |
| programa de facturacion gratis | 210 | 7 | 3,19 | T | BOFU | [N] /blog/programas-facturacion-gratis | P1 |
| programas de facturacion gratuitos | 210 | 49 | 2,29 | C | MOFU | ídem | P2 |
| programa facturacion electronica gratis | 260 | 29 | 1,93 | T | BOFU | [N] /programa-factura-electronica | P2 |
| programa factura electronica gratis | 260 | 6 | 1,93 | T | BOFU | ídem | P2 |
| programas de facturacion gratis para autonomos | 90 | 40 | 2,18 | C | MOFU | [N] listicle | P2 |
| programa de facturacion para autonomos gratis | 90 | 48 | 2,18 | C | MOFU | ídem | P2 |
| mejores programas de facturacion gratis | 90 | 28 | 1,73 | C | MOFU | ídem | P2 |
| mejores programas de facturacion gratuitos | 90 | 36 | 1,78 | C | MOFU | ídem | P2 |
| programa de facturacion gratis descargar | 50 | 40 | 2,07 | T | BOFU | — (Facturales es web/app, no se descarga) | P3 |
| programa de facturacion electronica gratis | 50 | 41 | 1,48 | T | BOFU | /programa-factura-electronica | P3 |
| factura online gratis | 480 | 31 | 2,24 | T | BOFU | [N] /generador-de-facturas | P1 |
| facturas online gratis | 480 | 40 | 2,24 | T | BOFU | ídem | P1 |
| facturas gratis | 170 | 31 | 2,67 | T | BOFU | ídem | P2 |
| holded gratis | 140 | 28 | 1,71 | C | MOFU | [N] /alternativas/holded | P2 |
| contasimple gratis | 390 | 21 | 2,29 | C | MOFU | [N] /alternativas/contasimple | P2 |
| billin gratis | 30 | 11 | 2,09 | C | MOFU | [N] /alternativas/billin | P3 |
| factusol gratis | 590 | 19 | 1,66 | N/C | MOFU | [N] /alternativas/factusol | P3 |
| contasol gratis | 590 | 21 | 1,62 | N/C | MOFU | — (programa de contabilidad de escritorio) | P3 |

> ESTIMACIÓN: Facturales no tiene plan gratuito (prueba de 14 días). Lo coherente es captar la intención «gratis» con **herramientas gratis** (generador, plantillas, calculadoras) y un listicle honesto, sin prometer «gratis» en las landings de producto.

### C3 · Autónomos, pymes y app
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| programa facturación autonomos | 320 | 33 | 2,97 | T | BOFU | [N] /autonomos | P1 |
| programa facturacion autonomos | 260 | 33 | 3,23 | T | BOFU | [N] /autonomos | P1 |
| programa facturas autonomos | 260 | 41 | 3,23 | T | BOFU | [N] /autonomos | P1 |
| programas facturas autonomos | 260 | 23 | 3,23 | T | BOFU | [N] /autonomos | P1 |
| programa de facturacion para autonomos | 210 | 43 | 3,16 | T | BOFU | [N] /autonomos | P1 |
| programas de facturacion para autonomos | 110 | 33 | 3,78 | T | BOFU | [N] /autonomos | P1 |
| facturacion autonomos | 110 | 23 | 3,63 | T | BOFU | [N] /autonomos | P1 |
| facturacion para autonomos | 40 | 34 | 3,55 | T | BOFU | [N] /autonomos | P2 |
| software de facturacion para autonomos | 10 | 25 | 3,82 | T | BOFU | [N] /autonomos | P2 |
| programa contabilidad autonomos | 110 | 0 | 2,37 | T | BOFU | impuestos | P2 |
| contabilidad para autonomos | 110 | 7 | 2,72 | C | MOFU | contabilidad-negocio-7-pasos / impuestos | P2 |
| programa de contabilidad para autonomos | 90 | 22 | 1,91 | T | BOFU | impuestos | P2 |
| programa de gestion para autonomos | 10 | 33 | — | T | BOFU | [N] /autonomos | P3 |
| app facturas | 140 | 36 | 2,87 | T | BOFU | [N] /app-facturacion | P2 |
| aplicacion para hacer facturas | 110 | 24 | 3,95 | T | BOFU | [N] /app-facturacion | P2 |
| app para hacer facturas | 70 | 19 | 4,30 | T | BOFU | [N] /app-facturacion | P2 |
| app para facturar | 50 | 29 | 3,61 | T | BOFU | ídem | P2 |
| app de facturas | 40 | 27 | 4,95 | T | BOFU | ídem | P3 |
| aplicacion de facturacion | 40 | 35 | 3,83 | T | BOFU | ídem | P3 |
| app facturacion | 30 | 37 | 3,25 | T | BOFU | ídem | P3 |
| aplicacion facturas | 30 | 34 | 5,57 | T | BOFU | ídem | P3 |
| app facturacion autonomos | 20 | 34 | 2,86 | T | BOFU | ídem | P3 |
| app facturas autonomos | 20 | 41 | 2,86 | T | BOFU | ídem | P3 |

### C4 · Comparativas, alternativas y precios de la competencia
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| mejor programa de facturación | 210 | 32 | 3,46 | C | MOFU | [N] /blog/mejores-programas-facturacion | P1 |
| mejores programas de facturacion | 170 | 37 | 5,71 | C | MOFU | ídem | P1 |
| mejor programa de facturacion para autonomos | 70 | 28 | 2,75 | C | MOFU | ídem (sección autónomos) | P1 |
| mejor programa de facturacion | 30 | 29 | 3,40 | C | MOFU | ídem | P2 |
| precios holded | 480 | 33 | 1,36 | C | MOFU | [N] /alternativas/holded (tabla de precios) | P1 |
| holded opiniones | 260 | 25 | 1,89 | C | MOFU | [N] /alternativas/holded | P2 |
| alternativa a holded | 90 | 5 | 2,80 | C | BOFU | [N] /alternativas/holded | P1 |
| alternativas a holded | 90 | 5 | 2,80 | C | BOFU | ídem | P1 |
| holded alternativas | 30 | 5 | 2,49 | C | BOFU | ídem | P1 |
| holded vs quipu | 30 | 6 | 2,72 | C | MOFU | [N] /comparativas/holded-vs-quipu | P2 |
| holded o quipu | 20 | 0 | 2,15 | C | MOFU | ídem | P2 |
| holded vs contasimple | 10 | 9 | 1,50 | C | MOFU | ídem (hub de comparativas) | P3 |
| contasimple opiniones | 390 | 16 | 2,19 | C | MOFU | [N] /alternativas/contasimple | P1 |
| contasimple precios | 210 | 0 | 1,97 | C | MOFU | ídem | P1 |
| quipu precios | 260 | 21 | 0,59 | C | MOFU | [N] /alternativas/quipu | P1 |
| quipu opiniones | 110 | 16 | 1,36 | C | MOFU | ídem | P2 |
| billin precios | 260 | 28 | 1,36 | C | MOFU | [N] /alternativas/billin | P1 |
| anfix precios | 110 | 18 | 0,46 | C | MOFU | [N] /alternativas/anfix | P2 |
| anfix opiniones | 50 | 15 | 2,95 | C | MOFU | ídem | P2 |
| facturadirecta precios | 110 | 0 | 2,20 | C | MOFU | [N] /alternativas/facturadirecta | P2 |
| facturadirecta opiniones | 70 | 16 | 4,30 | C | MOFU | ídem | P2 |
| stel order precios | 210 | 13 | 1,57 | C | MOFU | [N] /alternativas/stel-order | P2 |
| declarando precios | 170 | 16 | 1,87 | C | MOFU | [N] /alternativas/declarando | P3 (incluye asesoría, otro modelo) |
| alternativa a quipu / a contasimple / a billin | 0 (s/d; est. baja) | 7-10 | — | C | BOFU | /alternativas/* | P2 |
| programas de facturacion precios | 10 | 39 | — | C | MOFU | pricing / listicle | P3 |
| verifactu holded | 260 | 26 | 0,98 | C | MOFU | /alternativas/holded (bloque VeriFactu) | P2 |
| billin verifactu | 210 | 18 | 1,42 | C | MOFU | /alternativas/billin | P3 |
| verifactu contasimple | 70 | 36 | 1,63 | C | MOFU | /alternativas/contasimple | P3 |
| verifactu quipu | 30 | 11 | 0 | C | MOFU | /alternativas/quipu | P3 |
| **Marcas competidoras (navegacional; no atacar en SEO):** holded 135.000 KD 88 · contasimple 47.500 · b2brouter 27.800 · quipu 18.100 · stel order 14.800 · a3factura 10.800 · factusol 8.100 · facturadirecta 8.100 · anfix 5.700 · declarando 5.400 · facturascripts 990 · billin 880 · cuentica 590 · invoice ninja 590 · contasol 540 · facturaplus 390 · mgest 390 · sumup facturas 390 · sage facturacion 260 · odoo facturacion 260 · txerpa 140 · factura plus 140 · zoho invoice 30 · debitoor 10 | | | | N | — | — | — |

> Precios de competidores que aparecen en snippets del SERP (**SERP-3º**, sin verificar): Holded «desde 15 €/mes» (yofacturo) o «~14,50 €/mes» (recibia); Anfix 4,99 €/mes anual (getrenn, guiapymedigital); Billin/TS Facturas 6,60 €/mes anual o 8 € mensual; Contasimple 8,30 €/mes; Quipu 12-14 €/mes; a3factura desde 9,95 €/mes. **Facturales Starter 4,95 €/mes anual / 6,45 € mensual (+IVA)** está en la franja baja, un argumento natural para las páginas de alternativas. Antes de publicar hay que verificar cada precio en la web oficial del competidor y fechar la tabla.

### C5 · VeriFactu
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| verifactu | 12.100 | 86 | 1,30 | I | TOFU | verifactu-2027-guia-autonomos-pymes (pilar) | P2 (difícil) |
| verifactu aeat | 2.900 | 98 | 1,13 | I/N | TOFU | — (manda la AEAT) | P3 |
| verifactu que es | 1.500 | 81 | 0,57 | I | TOFU | guía VeriFactu | P2 |
| veri factu | 1.000 | 90 | 1,14 | I | TOFU | guía VeriFactu | P3 |
| aeat verifactu | 920 | 74 | 1,73 | I/N | TOFU | guía | P3 |
| que es verifactu | 810 | 36 | 0,15 | I | TOFU | guía (H2 «Qué es VERI*FACTU») | P1 |
| verifactu gratis | 610 | 17 | 1,13 | C | MOFU | [N] /blog/verifactu-gratis | P1 |
| software verifactu | 590 | 5 (real: media) | 2,40 | T | BOFU | [N] /programa-verifactu | P1 |
| reglamento verifactu | 590 | 39 | 0,20 | I | TOFU | guía | P2 |
| ley antifraude | 590 | 46 | 0,08 | I | TOFU | guía | P3 |
| como funciona verifactu | 480 | 39 | 0,65 | I | TOFU | guía | P2 |
| verifactu autonomos | 480 | 28 | 1,05 | I/C | MOFU | guía (sección autónomos) o [N] /verifactu-autonomos | P1 |
| programa facturacion verifactu | 480 | 20 | 2,65 | T | BOFU | [N] /programa-verifactu | **P1** |
| programa factura verifactu | 480 | 37 | 2,65 | T | BOFU | ídem | P1 |
| programa facturación verifactu | 480 | 46 | 2,65 | T | BOFU | ídem | P1 |
| kit digital verifactu | 480 | 13 | 1,11 | I | MOFU | blog (solo si es verdad que aplica; si no, nada) | P3 |
| verifactu api | 480 | 8 | 3,35 | T | BOFU | — (perfil desarrollador) | — |
| facturacion verifactu | 410 | 44 | 1,88 | T | BOFU | /programa-verifactu | P2 |
| ley verifactu | 390 | 53 | 0,58 | I | TOFU | guía | P3 |
| entrada en vigor verifactu | 390 | 33 | 0,22 | I | TOFU | guía (bloque de fechas) | P1 |
| verifactu es obligatorio | 360 | 34 | 0,23 | I | TOFU | guía | P1 |
| verifactu obligatorio | 320 | 44 | 0,24 | I | TOFU | guía | P2 |
| no verifactu | 320 | 34 | 0,70 | I | MOFU | [N] /blog/verifactu-vs-no-verifactu | P2 |
| verifactu descargar | 320 | 17 | 1,61 | T | BOFU | /programa-verifactu (FAQ «no se descarga») | P2 |
| programa verifactu gratis | 320 | 20 | 1,24 | C | MOFU | /blog/verifactu-gratis | P1 |
| verifactu para autonomos | 320 | 29 | 1,46 | I/C | MOFU | guía | P1 |
| normativa verifactu | 320 | 60 | 0,58 | I | TOFU | guía | P3 |
| aplicacion verifactu aeat | 320 | 36 | 1,41 | I | MOFU | /blog/verifactu-gratis (app AEAT frente a software) | P2 |
| obligación verifactu | 320 | 38 | 0,30 | I | TOFU | guía | P2 |
| software verifactu gratis | 260 | 21 | 1,41 | C | MOFU | /blog/verifactu-gratis | P1 |
| verifactu y factura electronica | 260 | 34 | 0,29 | I | TOFU | factura-electronica-vs-verifactu | P1 |
| verifactu se retrasa / verifactu retraso | 260 / 210 | 9 / 11 | 0 | I | TOFU | guía (sección de aplazamientos) | P1 |
| programa de facturacion con verifactu | 210 | 28 | 4,38 | T | BOFU | /programa-verifactu | P1 |
| programa de facturación verifactu | 210 | 38 | 2,99 | T | BOFU | ídem | P1 |
| quien esta obligado a verifactu | 210 | 6 | 0,05 | I | TOFU | guía | P1 |
| verifactu cuando es obligatorio | 210 | 44 | 0,14 | I | TOFU | guía | P2 |
| verifactu 2026 | 170 | 4 | 0,86 | I | TOFU | guía | P2 |
| verifactu factura simplificada | 170 | 17 | 1,10 | I | MOFU | guía / [N] factura simplificada | P2 |
| verifactu programa | 170 | 35 | 3,25 | T | BOFU | /programa-verifactu | P1 |
| verifactu excel | 170 | 17 | 1,49 | I | MOFU | [N] /blog/facturar-en-excel-verifactu | P1 |
| verifactu hosteleria | 170 | 7 | 1,78 | I | MOFU | — (TPV; no es el foco) | P3 |
| programa verifactu | 150 | 37 | 2,29 | T | BOFU | /programa-verifactu | P1 |
| verifactu software | 140 | 39 | 2,99 | T | BOFU | ídem | P1 |
| verifactu qr | 90 | 11 | 0,92 | I | MOFU | guía (bloque QR) | P2 |
| software homologado verifactu | 70 | 23 | 2,00 | C | MOFU | /programa-verifactu (FAQ: no existe homologación, existe declaración responsable) | P2 |
| registro de facturacion | 70 | 17 | 2,13 | I | MOFU | guía | P3 |
| software de facturación verifactu | 50 | 3 | 0 | T | BOFU | /programa-verifactu | P1 |
| sistema verifactu | 50 | 46 | 1,38 | I | TOFU | guía | P3 |
| ley antifraude facturacion | 50 | 20 | 0,84 | I | TOFU | guía | P3 |
| verifactu requisitos | 40 | 3 | 0 | I | MOFU | guía | P2 |
| verifactu sanciones / multas | 20 / 10 | 13 / 14 | 0 | I | MOFU | guía (sección de sanciones) | P2 |
| verifactu 2027 | 10 | 16 | 1,01 | I | TOFU | guía (ya optimizada en el slug) | P2 |
| verifactu woocommerce / prestashop / odoo / stripe | 260 / 260 / 390 / 210 | 6-12 | 1,7-3,3 | T | BOFU | — (integraciones que Facturales no tiene) | — |
| tpv con verifactu | 260 | 4 | 2,29 | T | BOFU | — (no es TPV) | — |
| ticketbai / ticket bai | 4.400 / 1.900 | 75 / 88 | 1,0 / 0,8 | I | TOFU | — salvo que se soporte TicketBAI | — |
| sii aeat | 8.100 | 89 | 2,93 | N | TOFU | — | — |

> **Cuidado con los claims (ESTIMACIÓN):** el CLAUDE.md prohíbe afirmar «presentación automática a la AEAT». En `/programa-verifactu` hay que describir con exactitud lo que hace la app (registros, huella, QR, modalidad) y no prometer que presenta modelos.

### C6 · Factura electrónica (Ley Crea y Crece, B2B)
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| facturae | 14.800 | 98 | 2,51 | N/I | TOFU | — | — |
| factura electronica | 9.900 | 90 | 2,02 | I | TOFU | [N] /factura-electronica (pilar) | P2 |
| ley crea y crece | 1.000 | 92 | 0,42 | I | TOFU | — | P3 |
| factura electronica obligatoria | 720 | 42 | 0,68 | I | TOFU | [N] /blog/factura-electronica-obligatoria | P1 |
| que es la factura electronica | 590 | 36 | 0,10 | I | TOFU | /factura-electronica | P1 |
| factura electronica autonomos | 390 | 29 | 1,00 | I/C | MOFU | /blog/factura-electronica-obligatoria (sección autónomos) | P1 |
| como hacer una factura electronica | 320 | 27 | 1,97 | I | MOFU | /factura-electronica | P2 |
| factura electronica obligatoria autonomos | 260 | 29 | 0,89 | I | MOFU | ídem | P1 |
| face factura electronica | 220 | 32 | 0,68 | I | TOFU | — (B2G; solo si se soporta FACe) | P3 |
| factura electronica b2b | 210 | 17 | 1,61 | I | MOFU | /blog/factura-electronica-obligatoria | P1 |
| ley crea y crece factura electronica | 140 | 31 | 0,30 | I | TOFU | ídem | P2 |
| digitalizar facturas | 140 | 23 | 2,06 | C | MOFU | escanea-gastos | P2 |
| factura electronica obligatoria 2026 / 2027 | s/d (est. media-alta, estacional) | — | — | I | TOFU | ídem | P2 |

### C7 · Presupuestos
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| presupuesto | 18.100 | 100 | 0,70 | I | — | — | — |
| plantilla presupuesto | 590 | 53 | 0,96 | I | TOFU | [N] /plantillas/presupuesto | P2 |
| modelo de presupuesto | 590 | 50 | 0,79 | I | TOFU | ídem | P2 |
| modelo presupuesto | 480 | 47 | 0,86 | I | TOFU | ídem | P2 |
| presupuesto excel | 390 | 54 | 0,46 | I | TOFU | ídem | P3 |
| plantilla presupuesto word | 320 | 47 | 0,92 | I | TOFU | ídem | P3 |
| presupuesto de obra | 320 | 10 | 1,68 | I | MOFU | [N] /blog/como-hacer-presupuesto-de-obra | P1 |
| como hacer un presupuesto de obra | 320 | 7 | 1,20 | I | MOFU | ídem | P1 |
| presupuesto reforma | 320 | 19 | 1,84 | I | MOFU | ídem + [N] /sectores/reformas | P1 |
| programas para hacer presupuestos gratis | 210 | 22 | 1,53 | C | MOFU | crea-envia-presupuestos + generador | P1 |
| programa para hacer presupuestos gratis | 210 | 22 | 1,53 | C | MOFU | ídem | P1 |
| programa para hacer presupuestos | 170 | 22 | 2,61 | T | BOFU | crea-envia-presupuestos | P1 |
| plantilla de presupuesto excel | 170 | 51 | 0,90 | I | TOFU | /plantillas/presupuesto | P3 |
| programa de reformas | 170 | 18 | 0 | T | BOFU | [N] /sectores/reformas | P2 |
| hacer presupuesto online | 140 | 17 | 2,58 | T | BOFU | [N] /generador-de-presupuestos | P1 |
| plantilla presupuesto gratis | 140 | 53 | 0,87 | I | TOFU | /plantillas/presupuesto | P3 |
| plantilla presupuesto obra | 110 | 22 | 1,13 | I | MOFU | /plantillas/presupuesto (variante obra) | P2 |
| presupuesto online gratis | 110 | 17 | 1,70 | T | BOFU | /generador-de-presupuestos | P1 |
| plantilla presupuesto reforma | 90 | 14 | 0,86 | I | MOFU | /plantillas/presupuesto | P2 |
| generador de presupuestos | 90 | 16 | 1,68 | T | BOFU | /generador-de-presupuestos | P1 |
| programa de presupuestos | 70 | 27 | 2,24 | T | BOFU | crea-envia-presupuestos | P2 |
| programa presupuestos obra / programa de presupuestos de obra | 70 / 70 | 23 / 24 | 2,16 / 3,15 | T | BOFU | /sectores/reformas | P2 |
| crear presupuesto online | 50 | 26 | 3,44 | T | BOFU | /generador-de-presupuestos | P2 |
| app para hacer presupuestos | 40 | 13 | 2,05 | T | BOFU | crea-envia-presupuestos | P2 |
| programa de presupuestos gratis | 40 | 28 | 1,67 | C | MOFU | generador | P3 |
| como hacer un presupuesto | 30 | 49 | 0,86 | I | TOFU | /blog | P3 |
| plantilla presupuesto pintura | 30 | 7 | 0,72 | I | MOFU | /plantillas/presupuesto | P3 |
| como hacer un presupuesto para un cliente | 20 | 10 | 0,72 | I | MOFU | /blog | P3 |

### C8 · Plantillas y modelos de factura, tipos de factura, albarán y recibo
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| factura proforma | 8.000 | 81 | 0,06 | I | TOFU | [N] /guias/factura-proforma | P2 |
| plantilla factura | 1.900 | 88 | 1,20 | I | TOFU | [N] /plantillas/factura (hub) | P2 |
| factura rectificativa | 1.900 | 92 | 0,05 | I | TOFU | [N] /guias/factura-rectificativa | P2 |
| factura simplificada | 1.600 | 73 | 0,11 | I | TOFU | [N] /guias/factura-simplificada | P2 |
| modelo factura | 1.300 | 82 | 0,98 | I | TOFU | /plantillas/factura | P3 |
| modelo de factura | 910 | 39 | 0,95 | I | TOFU | /plantillas/factura | P1 |
| factura recapitulativa | 590 | 8 | 0,27 | I | TOFU | [N] /guias/factura-recapitulativa | **P1** |
| plantilla factura gratis | 480 | 35 | 1,25 | I | TOFU | /plantillas/factura | P1 |
| plantilla factura autonomo | 480 | 25 | 0,86 | I | MOFU | [N] /plantillas/factura-autonomo | P1 |
| modelo factura autonomo | 480 | 7 | 0,77 | I | MOFU | ídem | **P1** |
| ejemplo factura autonomo | 480 | 22 | 0,50 | I | MOFU | ídem | P1 |
| modelo factura excel | 480 | 39 | 0,88 | I | TOFU | /plantillas/factura (Excel) | P2 |
| factura con excel | 480 | 27 | 0,93 | I | MOFU | /blog/facturar-en-excel-verifactu | P1 |
| factura excel | 390 | 28 | 1,00 | I | TOFU | /plantillas/factura | P2 |
| plantilla factura word gratis | 390 | 32 | 0,89 | I | TOFU | /plantillas/factura (Word) | P2 |
| que es factura proforma | 390 | 9 | 0,01 | I | TOFU | /guias/factura-proforma | P1 |
| como hacer una factura rectificativa | 390 | 9 | 0,07 | I | MOFU | /guias/factura-rectificativa | P1 |
| factura de abono | 390 | 8 | 0,06 | I | TOFU | /guias/factura-rectificativa (sección abono) | P1 |
| modelo factura word | 320 | 33 | 0,92 | I | TOFU | /plantillas/factura | P2 |
| modelo de factura excel | 320 | 31 | 0,93 | I | TOFU | ídem | P2 |
| tipos de facturas | 320 | 16 | 0,74 | I | TOFU | [N] /guias/tipos-de-factura (hub) | P1 |
| factura sin iva | 260 | 22 | 0,61 | I | MOFU | [N] /guias/factura-sin-iva-exenta | P2 |
| plantilla factura proforma | 210 | 8 | 0,96 | I | MOFU | /guias/factura-proforma (descarga) | P1 |
| plantilla factura pdf | 210 | 43 | 0,91 | I | TOFU | /plantillas/factura | P3 |
| modelo de factura word | 170 | 30 | 0,85 | I | TOFU | ídem | P3 |
| factura simplificada requisitos | 140 | 16 | 0,03 | I | MOFU | /guias/factura-simplificada | P1 |
| factura alquiler local | 140 | 7 | 0,77 | I | MOFU | [N] /plantillas/factura-alquiler | P2 |
| plantilla de factura word / gratis / excel | 110 / 110 / 90 | 29 / 35 / 36 | ~1 | I | TOFU | /plantillas/factura | P3 |
| modelo factura word gratis | 90 | 32 | 1,03 | I | TOFU | ídem | P3 |
| facturas excel gratis | 70 | 39 | 0,79 | I | TOFU | ídem | P3 |
| factura de alquiler | 70 | 8 | 0,63 | I | MOFU | /plantillas/factura-alquiler | P2 |
| factura de servicios | 70 | 13 | 1,90 | I | MOFU | /plantillas/factura | P2 |
| modelo factura rectificativa | 70 | 11 | 0,42 | I | MOFU | /guias/factura-rectificativa | P2 |
| plantilla factura simplificada | 50 | 16 | 1,16 | I | MOFU | /guias/factura-simplificada | P2 |
| factura abogado / psicologo / fontanero / electricista | 50 / 40 / 40 / 40 | 7 / 7 / 5 / 6 | 0,9-2,4 | I/C | MOFU | /sectores/* (plantilla + programa) | P2 |
| modelo factura sin iva | 40 | 39 | 0,41 | I | MOFU | /guias/factura-sin-iva-exenta | P3 |
| plantilla factura rectificativa | 30 | 7 | 0,99 | I | MOFU | /guias/factura-rectificativa | P2 |
| factura editable | 30 | 36 | 0,96 | I | TOFU | /plantillas/factura | P3 |
| plantilla factura con iva e irpf | 20 | 17 | 0,55 | I | MOFU | /plantillas/factura-autonomo | P2 |
| modelo de factura pdf | 20 | 26 | 0,95 | I | TOFU | /plantillas/factura | P3 |
| albaran | 9.900 | 94 | 1,24 | I | TOFU | — | P3 |
| plantilla albaran | 590 | 8 | 1,07 | I | MOFU | [N] /plantillas/albaran | P1 (solo si la app emite albaranes; si no, P3) |
| modelo albaran | 210 | 8 | 1,53 | I | MOFU | ídem | P2 |
| nota de entrega | 210 | 9 | 0,74 | I | TOFU | ídem | P3 |
| albaran y factura diferencia | 30 | 8 | 0 | I | TOFU | ídem | P3 |
| recibo de pago | 810 | 55 | 0,68 | I | TOFU | [N] /plantillas/recibo | P3 |
| plantilla recibo | 320 | 44 | 0,92 | I | TOFU | ídem | P3 |

### C9 · Generador de facturas online
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| factura online | 1.300 | 92 | 2,66 | T | BOFU | [N] /generador-de-facturas | P2 |
| hacer factura | 880 | 52 | 2,67 | T | BOFU | ídem | P2 |
| hacer factura online gratis | 590 | 29 | 2,06 | T | BOFU | ídem | **P1** |
| hacer facturas online gratis | 590 | 30 | 2,26 | T | BOFU | ídem | P1 |
| creador facturas | 590 | 24 | 2,79 | T | BOFU | ídem | **P1** |
| creador factura | 590 | 33 | 3,12 | T | BOFU | ídem | P1 |
| crear factura | 590 | 33 | 3,12 | T | BOFU | ídem | P1 |
| crea facturas | 590 | 38 | 3,12 | T | BOFU | ídem | P2 |
| hacer factura online | 390 | 6 | 2,72 | T | BOFU | ídem | **P1** |
| hacer facturas online | 390 | 42 | 2,72 | T | BOFU | ídem | P2 |
| crear factura online | 260 | 33 | 2,69 | T | BOFU | ídem | P1 |
| generador de facturas | 210 | 39 | 2,32 | T | BOFU | ídem | P1 |
| creador de facturas | 140 | 33 | 3,62 | T | BOFU | ídem | P2 |
| generador de facturas gratis | 70 | 30 | 2,61 | T | BOFU | ídem | P2 |
| generador de facturas online | 40 | 39 | 2,56 | T | BOFU | ídem | P2 |
| generador de facturas online gratis | s/d (est. media) | — | — | T | BOFU | ídem | P2 |

> En el SERP de «generador de facturas» (DATO) aparecen invoice-generator.com, Flowlu, Zoho (Play Store), InvoiceHome y Canva; Quipu (#6), Billin (#7), Holded (#8), Contasimple, Declarando y Anfix. La herramienta tiene que funcionar sin registro, calcular IVA, IRPF y recargo de equivalencia, descargar PDF y aclarar qué factura cumple VERI*FACTU y cuál no (un PDF suelto no es un SIF). Esa aclaración es a la vez el gancho para la prueba.

### C10 · Cómo hacer una factura: requisitos y datos obligatorios
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| como hacer una factura | 810 | 21 | 1,40 | I | MOFU | [N] /guias/como-hacer-una-factura | **P1** |
| direccion de facturacion | 810 | 10 | 0,40 | I | TOFU | glosario | P2 (poca intención) |
| datos de facturacion | 390 | 18 | 1,09 | I | TOFU | /guias/datos-obligatorios-factura | P1 |
| como hacer una factura sin ser autonomo | 390 | 24 | 0,74 | I | TOFU | [N] /guias/facturar-sin-ser-autonomo | P2 |
| puedo facturar sin ser autónomo | 390 | 31 | 0,05 | I | TOFU | ídem | P2 |
| como hacer una factura autonomo | 170 | 15 | 1,17 | I | MOFU | /guias/como-hacer-una-factura | P1 |
| datos obligatorios factura | 140 | 20 | 0 | I | MOFU | [N] /guias/datos-obligatorios-factura | P1 |
| requisitos factura / requisitos de una factura | 110 / 90 | 22 / 21 | 0,3 | I | MOFU | ídem | P1 |
| factura sin ser autonomo | 110 | 25 | 0,42 | I | TOFU | /guias/facturar-sin-ser-autonomo | P3 |
| como numerar facturas / numeracion facturas | 70 / 50 | 8 / 9 | 0,06 | I | MOFU | [N] /guias/numeracion-facturas | P1 |
| libro registro de facturas | 70 | 12 | 0,59 | I | MOFU | impuestos / [N] guía de libros registro | P2 |
| libro registro facturas emitidas / recibidas | 40 / 40 | 12 / 12 | 1,30 / 0 | I | MOFU | ídem | P2 |
| que debe llevar una factura | 20 | 21 | 0,39 | I | MOFU | /guias/datos-obligatorios-factura | P2 |

### C11 · IVA e IRPF en factura (calculadoras)
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| calcular iva | 22.400 | 86 | 0,01 | I | TOFU | [N] /calculadora-iva-irpf | P2 (muy difícil, mucho volumen) |
| calculadora iva | 14.800 | 86 | 0,01 | I | TOFU | ídem | P2 |
| calculadora de iva | 3.200 | 71 | 0,01 | I | TOFU | ídem | P2 |
| recargo de equivalencia | 4.400 | 80 | 0,02 | I | TOFU | /guias | P3 |
| inversion del sujeto pasivo | 1.300 | 80 | 0,02 | I | TOFU | /guias | P3 |
| que es el iva | 1.100 | 96 | 0,08 | I | TOFU | — | — |
| iva intracomunitario | 1.000 | 76 | 0,12 | I | TOFU | /guias | P3 |
| irpf autonomos | 880 | 21 | 0,11 | I | TOFU | [N] /guias/retencion-irpf-factura | P2 |
| iva soportado | 760 | 9 | 0,02 | I | TOFU | [N] /guias/iva-soportado-repercutido | **P1** |
| iva repercutido | 660 | 8 | 0,02 | I | TOFU | ídem | **P1** |
| iva deducible | 660 | 9 | 0,28 | I | TOFU | ídem | P1 |
| calculadora irpf autonomos | 590 | 9 | 0,42 | I | MOFU | /calculadora-iva-irpf | P1 |
| quitar iva | 480 | 11 | 0,01 | I | TOFU | /calculadora-iva-irpf (modo «quitar IVA») | P1 |
| iva trimestral | 480 | 19 | 0,89 | I | MOFU | /guias/modelo-303 | P2 |
| tipos de iva | 410 | 17 | 0,25 | I | TOFU | /guias | P2 |
| exento de iva | 390 | 44 | 0 | I | TOFU | /guias/factura-sin-iva-exenta | P3 |
| factura con irpf | 390 | 12 | 0,16 | I | MOFU | /guias/retencion-irpf-factura | P1 |
| como calcular el iva de una factura | 260 | 15 | 0,02 | I | MOFU | /calculadora-iva-irpf | P1 |
| factura con retencion | 260 | 13 | 0,15 | I | MOFU | /guias/retencion-irpf-factura | P1 |
| factura intracomunitaria | 170 | 16 | 0,23 | I | MOFU | /guias | P2 |
| retencion irpf autonomos | 170 | 13 | 0,13 | I | MOFU | /guias/retencion-irpf-factura | P1 |
| calcular irpf factura | 170 | 9 | 1,09 | I | MOFU | /calculadora-iva-irpf | P1 |
| iva autonomos | 150 | 4 | 0,01 | I | TOFU | /guias/iva-soportado-repercutido | P2 |
| irpf factura autonomo | 140 | 8 | 0,23 | I | MOFU | /guias/retencion-irpf-factura | P1 |
| retencion irpf factura | 110 | 12 | 0,16 | I | MOFU | ídem | P1 |
| calcular iva de una factura | 50 | 20 | 0,01 | I | MOFU | calculadora | P2 |
| retencion 7 autonomos | 40 | 11 | 0,05 | I | MOFU | /guias/retencion-irpf-factura | P2 |
| calculadora iva irpf | 20 | 10 | 0,05 | I | MOFU | calculadora | P2 |

### C12 · Modelos AEAT y calendario fiscal
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| modelo 036 | 40.500 | 76 | 0,28 | I | TOFU | — (alta censal, poco ligado al producto) | P3 |
| modelo 303 | 20.100 | 95 | 0,81 | I | TOFU | [N] /guias/modelo-303 | P2 (dominado por la AEAT) |
| modelo 130 | 9.900 | 85 | 0,53 | I | TOFU | [N] /guias/modelo-130 | P2 |
| modelo 111 | 9.900 | 93 | 0,15 | I | TOFU | [N] /guias/modelo-111 | P3 |
| modelo 100 | 8.000 | 91 | 0,91 | I | TOFU | — | P3 |
| modelo 115 | 5.400 | 97 | 0,13 | I | TOFU | — | P3 |
| modelo 349 | 4.400 | 45 | 0,44 | I | TOFU | [N] /guias/modelo-349 | P2 |
| modelo 037 | 4.400 | 87 | 0,70 | I | TOFU | — | — |
| modelo 303 iva | 1.500 | 89 | 0,60 | I | TOFU | /guias/modelo-303 | P3 |
| modelo 347 | 880 | 18 | 0,07 | I | TOFU | [N] /guias/modelo-347 | **P1** |
| calendario fiscal 2026 | 720 | 26 | 0 | I | TOFU | [N] /calendario-fiscal-2027 (publicar en dic-2026) | P1 |
| calendario del contribuyente | 470 | 27 | 0 | I | TOFU | ídem | P2 |
| declaracion trimestral autonomos | 390 | 16 | 1,28 | I | MOFU | impuestos + /guias/modelo-303 | P1 |
| modelo 390 | 370 | 17 | 0,49 | I | TOFU | [N] /guias/modelo-390 | P1 |
| calendario fiscal | 330 | 27 | 0 | I | TOFU | /calendario-fiscal-2027 | P2 |
| estimacion directa simplificada | 290 | 16 | 0,06 | I | TOFU | /guias/modelo-130 | P2 |
| como rellenar modelo 303 / modelo 303 como rellenar | 260 / 260 | 36 / 37 | 0,35 | I | MOFU | /guias/modelo-303 | P1 |
| plazo modelo 303 / modelo 303 plazo | 210 / 210 | 0 / 26 | 0 | I | MOFU | /guias/modelo-303 (bloque de plazos) | **P1** |
| cuando se presenta el modelo 130 | 210 | 24 | 0,05 | I | MOFU | /guias/modelo-130 | P1 |
| como rellenar modelo 130 / modelo 130 como rellenar | 170 / 170 | 0 / 5 | 0,28 | I | MOFU | /guias/modelo-130 | **P1** |
| plazo modelo 130 | 170 | 0 | 0,07 | I | MOFU | /guias/modelo-130 | **P1** |
| pagos fraccionados irpf | 170 | 13 | 0 | I | MOFU | /guias/modelo-130 | P1 |
| modelo 130 autonomos | 150 | 31 | 0,15 | I | MOFU | /guias/modelo-130 | P1 |
| plazo presentacion modelo 303 | 140 | 26 | 0 | I | MOFU | /guias/modelo-303 | P1 |
| calendario fiscal autonomos | 70 | 20 | 0 | I | TOFU | /calendario-fiscal-2027 | P2 |
| cuando se presenta el modelo 303 | 70 | 27 | 0 | I | MOFU | /guias/modelo-303 | P2 |
| casillas modelo 303 / modelo 303 casillas | 40 / 20 | 16 / 20 | 0 | I | MOFU | /guias/modelo-303 | P2 |

### C13 · Conciliación bancaria y extractos
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| extracto bancario | 4.400 | 96 | 1,29 | I/N | TOFU | — | — |
| que es conciliacion bancaria (+ «que es una…», «…que es»: mismo cluster) | 480 | 8 | 0,21 | I | TOFU | [N] /guias/conciliacion-bancaria | **P1** |
| conciliacion bancaria | 10 (anómalo; est. alta, ~1-3 k) | 8 | 1,86 | I | TOFU | /guias/conciliacion-bancaria | P1 |
| norma 43 | 480 | 8 | 0 | I | MOFU | /guias/conciliacion-bancaria (sección de formatos) solo si la app importa N43; si no, explicar Excel/CSV | P2 |
| cuaderno 43 | 170 | 7 | 0 | I | MOFU | ídem | P3 |
| conciliaciones bancarias | 110 | 16 | 2,26 | I | TOFU | /guias/conciliacion-bancaria | P1 |
| como hacer conciliaciones bancarias | 110 | 11 | 2,26 | I | MOFU | ídem | P1 |
| conciliacion bancaria ejemplo / ejemplos | 90 / 90 | 9 / 16 | 0,57 | I | MOFU | ídem (ejemplo resuelto) | P1 |
| conciliacion bancaria excel | 70 | 16 | 1,07 | I | MOFU | ídem + plantilla | P1 |
| como hacer una conciliacion bancaria | 40 | 12 | 0,37 | I | MOFU | ídem | P2 |
| conciliar bancos | 40 | 8 | 3,29 | C | MOFU | bancos-conciliacion | P2 |
| conciliacion de cuentas | 40 | 9 | 3,00 | I | TOFU | /guias/conciliacion-bancaria | P3 |
| conciliacion bancaria automatica | 10 | 8 | 0 | C | MOFU | bancos-conciliacion (sin prometer conexión bancaria directa: «Próximamente») | P2 |
| programa conciliacion bancaria | 10 | 14 | 0 | T | BOFU | bancos-conciliacion | P2 |
| software conciliacion bancaria | s/d (est. baja-media; CPC alto) | — | — | T | BOFU | bancos-conciliacion | P2 |
| recibos sepa / remesas sepa | 260 / 50 | 8 / 8 | 0,27 / 1,69 | I | MOFU | — (salvo que la app genere remesas) | P3 |

### C14 · Gastos, tickets y deducibles
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| control de gastos | 390 | 46 | 1,27 | C | MOFU | escanea-gastos | P2 |
| control de gastos excel | 320 | 41 | 0,51 | I | TOFU | [N] /plantillas/control-gastos | P2 |
| gastos deducibles autonomos | 320 | 21 | 0,11 | I | TOFU | [N] /guias/gastos-deducibles-autonomos | P1 |
| gastos deducibles | 260 | 9 | 0,39 | I | TOFU | ídem | P1 |
| app control de gastos | 260 | 39 | 0,34 | T | BOFU | escanea-gastos | P2 |
| nota de gastos | 210 | 9 | 2,03 | I | MOFU | escanea-gastos / plantilla | P2 |
| app gastos | 170 | 39 | 0,35 | T | BOFU | escanea-gastos | P3 |
| plantilla ingresos y gastos / libro de ingresos y gastos | 90 / 90 | 44 / 8 | 0,9 / 0,2 | I | MOFU | [N] /plantillas/libro-ingresos-gastos | P2 |
| escanear facturas | 70 | 7 | 1,22 | T | BOFU | escanea-gastos | P1 |
| gestion de gastos | 70 | 43 | 1,12 | C | MOFU | escanea-gastos | P2 |
| hoja de gastos excel | 70 | 49 | 0,50 | I | TOFU | plantilla | P3 |
| que gastos puedo deducir como autonomo | 70 | 31 | 0,06 | I | TOFU | /guias/gastos-deducibles-autonomos | P1 |
| escanear tickets | 50 | 8 | 1,40 | T | BOFU | escanea-gastos | P1 |
| guardar tickets | 40 | 10 | 0 | I | MOFU | escanea-gastos (FAQ) | P2 |
| dietas autonomos | 30 | 8 | 0,04 | I | TOFU | /guias/gastos-deducibles-autonomos | P2 |
| un ticket es una factura / ticket o factura | 30 / 30 | 8 / 9 | 0 | I | MOFU | /guias/factura-simplificada | P2 |
| app para escanear tickets / facturas | 10 / 10 | 10 / 13 | 0,6 / 0,9 | T | BOFU | escanea-gastos | P2 |
| digitalizar tickets | 10 | 6 | 0 | T | BOFU | escanea-gastos | P2 |
| control de gastos empresa | 10 | 16 | 2,59 | C | MOFU | escanea-gastos | P3 |
| contabilidad autonomos excel | 50 | 13 | 0,36 | I | MOFU | plantilla | P3 |

### C15 · Cobros, morosidad y recordatorios de pago
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| monitorio / proceso monitorio | 2.900 / 1.800 | 79 / 75 | 0,02 | I | TOFU | — (legal) | P3 |
| morosidad | 590 | 33 | 1,21 | I | TOFU | [N] /guias/ley-morosidad-plazos-pago | P2 |
| ley de morosidad | 590 | 17 | 0 | I | TOFU | ídem | P1 |
| gestion de cobros | 320 | 8 | 1,71 | C | MOFU | cobros (H1/H2) + guía | **P1** |
| reclamar factura impagada | 90 | 8 | 1,56 | I | MOFU | [N] /guias/reclamar-factura-impagada | P1 |
| burofax reclamacion deuda | 90 | 5 | 0,53 | I | MOFU | ídem | P3 |
| facturas impagadas / factura impagada | 70 / 70 | 12 / 13 | 1,56 | I | MOFU | ídem | P1 |
| como reclamar una factura impagada | 70 | 8 | 0,17 | I | MOFU | ídem | P1 |
| recordatorio de pago | 40 | 10 | 0 | C | MOFU | cobros + [N] /plantillas/recordatorio-pago (email) | P1 |
| gestion de impagados | 40 | 15 | 0 | C | MOFU | cobros | P2 |
| carta reclamacion deuda | 30 | 5 | 0 | I | MOFU | plantilla | P2 |
| como cobrar facturas impagadas | 20 | 15 | 1,44 | I | MOFU | guía | P2 |
| carta de reclamacion de pago | 20 | 6 | 0 | I | MOFU | plantilla | P2 |
| plazo legal pago facturas | 10 | 18 | 0 | I | MOFU | /guias/ley-morosidad-plazos-pago | P2 |
| reclamacion de pago / control de cobros | 10 / 10 | 16 / 6 | 0 | C | MOFU | cobros | P3 |
| plantilla control de cobros y pagos | s/d (est. media; Quipu saca 159 visitas) | — | — | I | MOFU | [N] plantilla | P2 |

### C16 · Inventario y control de stock
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| control de stock | 390 | 8 | 2,97 | C | MOFU | gestiona-tu-stock (H1 «Control de stock») + guía | **P1** |
| gestion de stock | 260 | 9 | 3,42 | C | MOFU | gestiona-tu-stock | **P1** |
| gestion de inventario | 260 | 23 | 2,70 | C | MOFU | gestiona-tu-stock | P1 |
| control de inventario | 170 | 24 | 3,42 | C | MOFU | gestiona-tu-stock | P1 |
| plantilla inventario excel | 140 | 48 | 1,18 | I | TOFU | [N] /plantillas/inventario | P2 |
| stock minimo | 110 | 6 | 0 | I | TOFU | [N] /guias/stock-minimo (enlazar a alertas de stock mínimo) | P1 |
| gestion de almacen | 110 | 11 | 1,56 | C | MOFU | gestiona-tu-stock (un solo almacén: decirlo) | P2 |
| control de stock excel | 70 | 37 | 1,16 | I | TOFU | plantilla | P2 |
| software de inventario | 70 | 24 | 4,83 | T | BOFU | gestiona-tu-stock | P1 |
| programa control de stock | 70 | 31 | 3,69 | T | BOFU | gestiona-tu-stock | P1 |
| inventario excel | 70 | 42 | 1,22 | I | TOFU | plantilla | P3 |
| programa de inventario | 50 | 30 | 3,71 | T | BOFU | gestiona-tu-stock | P1 |
| app inventario | 40 | 9 | 2,81 | T | BOFU | gestiona-tu-stock | P2 |
| control de inventario excel | 30 | 44 | 1,41 | I | TOFU | plantilla | P3 |
| programa de inventario gratis / control de stock gratis | 20 / 20 | 24 / 33 | 1,5 / 1,3 | C | MOFU | gestiona-tu-stock | P3 |
| programa de stock / programa de almacen / software de stock | 10 / 10 / 10 | 21 / 17 / 22 | 5,71 / 2,26 / 0 | T | BOFU | gestiona-tu-stock | P2 |

### C17 · Facturas recurrentes y automatización
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| facturas recurrentes | 50 | 9 | 2,55 | T | BOFU | [N] /facturas-recurrentes | **P1** |
| factura recurrente | 50 | 8 | 2,55 | T | BOFU | ídem | P1 |
| facturación recurrente | 50 | 7 | 2,55 | T | BOFU | ídem | P1 |
| cobros recurrentes | 10 | 8 | 7,15 | T | BOFU | ídem | P2 |
| facturas periodicas | 0 | 8 | 0 | T | BOFU | ídem | P2 |
| facturacion automatica / facturas automaticas | s/d (est. baja-media) | — | — | T | BOFU | ídem | P2 |
| factura recurrente que es | s/d | — | — | I | MOFU | ídem (FAQ) | P3 |

> Matiz de producto: las recurrentes se generan como **borrador** y las emite el usuario. Hay que decirlo así (CLAUDE.md).

### C18 · Panel financiero y tesorería
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| tesoreria | 8.000 | 98 | 0,60 | I | TOFU | — | — |
| panel de control | 6.600 | 99 | 0,03 | I | — | — | — |
| cash flow | 3.100 | 82 | 0,13 | I | TOFU | /guias/flujo-de-caja | P3 |
| flujo de caja | 720 | 57 | 0,23 | I | TOFU | [N] /guias/flujo-de-caja | P2 |
| gestion financiera | 590 | 29 | 2,11 | C | MOFU | tu-negocio-bajo-control | P2 |
| flujo de caja que es | 320 | 51 | 0,02 | I | TOFU | /guias/flujo-de-caja | P3 |
| control financiero | 260 | 7 | 2,60 | C | MOFU | tu-negocio-bajo-control | P1 |
| dashboard financiero | 110 | 6 | 1,37 | C | MOFU | tu-negocio-bajo-control | P1 |
| cuadro de mando financiero | 50 | 6 | 0 | C | MOFU | tu-negocio-bajo-control | P1 |
| flujo de caja excel | 50 | 15 | 0,98 | I | TOFU | plantilla | P3 |
| prevision de tesoreria | 30 | 9 | 3,72 | C | MOFU | tu-negocio-bajo-control | P2 |
| kpi financieros | 30 | 20 | 0,18 | I | TOFU | blog | P3 |
| software financiero / software gestion financiera | 30 / 20 | 20 / 21 | 5,99 / 0 | T | BOFU | tu-negocio-bajo-control | P2 |
| gestion financiera pymes | 10 | 21 | 0 | C | MOFU | / («suite financiera») | P2 |

### C19 · Clientes y CRM ligero
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| gestion de clientes | 260 | 8 | 3,68 | C | MOFU | gestiona-clientes | P1 |
| cartera de clientes | 210 | 9 | 2,71 | I | TOFU | gestiona-clientes / guía | P2 |
| crm para autonomos | 50 | 16 | 2,39 | T | BOFU | gestiona-clientes | P2 |
| crm facturacion / facturación crm | 40 / 40 | 9 / 9 | — | T | BOFU | gestiona-clientes (ya rankea en la pos. 51-62) | P1 |
| facturacion de clientes / facturas de clientes | 20 / 20 | 21 / 21 | — | T | BOFU | gestiona-clientes | P2 |
| crm gratis | 10 | 51 | 3,26 | C | MOFU | — | P3 |

### C20 · Autónomos (trámites)
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| alta autonomo | 6.600 | 90 | 4,30 | I | TOFU | — (muy difícil) | P3 |
| darse de alta como autonomo | 3.600 | 92 | 2,17 | I | TOFU | — | P3 |
| cuota autonomos | 3.200 | 88 | 0,33 | I | TOFU | — | P3 |
| tarifa plana autonomos | 1.900 | 0 (dato dudoso) | 0,17 | I | TOFU | blog | P3 |
| asesoria autonomos | 590 | 24 | 1,99 | C | MOFU | — (Facturales no es asesoría; posible página de partners o gestorías) | P3 |
| cuanto paga un autonomo | 480 | 27 | 0,07 | I | TOFU | blog | P3 |
| gestoria online | 440 | 22 | 2,09 | C | MOFU | [N] /gestorias (rol gestoría) | P2 |
| ser autonomo | 210 | 27 | 1,70 | I | TOFU | — | P3 |
| cuota autonomos 2026 | 150 | 18 | 0,12 | I | TOFU | blog | P3 |
| cuanto cuesta ser autonomo | 140 | 41 | 0,14 | I | TOFU | — | P3 |
| como darse de alta como autonomo | 110 | 0 | 2,17 | I | TOFU | — | P3 |
| gestoria autonomos | 20 | 21 | 4,14 | C | MOFU | /gestorias | P3 |

### C21 · Gestorías (rol gestoría)
| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| software para gestorias | 50 | 15 | 5,83 | T | BOFU | [N] /gestorias | P1 |
| programa para gestorias | 20 | 20 | 4,31 | T | BOFU | ídem | P1 |
| software gestoria | 20 | 18 | 3,80 | T | BOFU | ídem | P2 |
| software para asesorias / portal cliente gestoria | s/d (est. baja; CPC alto) | — | — | T | BOFU | ídem | P2 |

### C22 · Sectores (long tail BOFU)
SE Ranking devuelve «s/d» para casi todas las variantes «programa de facturación para [sector]». Uso las variantes «software/programa [sector]» con dato y marco el resto como ESTIMACIÓN.

| Keyword | Vol | KD | CPC | Int. | Emb. | Destino | Prio |
|---|---|---|---|---|---|---|---|
| software para restaurantes / software restaurante | 260 / 210 | 29 / 28 | 3,06 / 2,94 | T | BOFU | — (piden TPV/comandas; mal encaje) | P3 |
| tpv hosteleria | 390 | 14 | 2,49 | T | BOFU | — | — |
| software peluqueria | 210 | 24 | 2,13 | T | BOFU | [N] /sectores/peluquerias (sin prometer agenda o TPV) | P2 |
| software para peluquerías | 140 | 8 | 2,06 | T | BOFU | ídem | P2 |
| programa para peluquerias / programa de peluqueria / programa gestion peluqueria | 70 / 70 / 70 | 8 / 20 / 7 | 2,5-2,7 | T | BOFU | ídem | P2 |
| programa de reformas | 170 | 18 | 0 | T | BOFU | [N] /sectores/reformas-construccion | P1 |
| software construccion / software para constructoras | 70 / 40 | 10 / 9 | 3,51 / 4,87 | T | BOFU | ídem | P1 |
| programa presupuestos obra (ver C7) | 70 | 23 | 2,16 | T | BOFU | ídem | P1 |
| software fisioterapia | 110 | 10 | 1,83 | T | BOFU | [N] /sectores/fisioterapeutas (facturación exenta de IVA sanitaria) | P2 |
| software para fisioterapeutas | 70 | 4 | 1,71 | T | BOFU | ídem | P2 |
| programa gestion clinica fisioterapia | 20 | 4 | 2,80 | T | BOFU | ídem | P3 |
| software para psicologos / software psicologos | 70 / 70 | 22 / 20 | 1,24 / 1,21 | T | BOFU | [N] /sectores/psicologos (exención de IVA) | P2 |
| factura psicologo | 40 | 7 | 1,56 | I | MOFU | ídem | P2 |
| software para abogados | 50 | 9 | 2,45 | T | BOFU | [N] /sectores/abogados (provisión de fondos, suplidos, IRPF 15 %) | P2 |
| software gestion despacho abogados | 30 | 10 | 3,73 | T | BOFU | ídem | P2 |
| factura abogado / programa para abogados | 50 / 20 | 7 / 7 | 0,93 / 2,74 | I/T | MOFU | ídem | P2 |
| programa taller mecanico / software taller mecanico / programa gestion taller mecanico | 70 / 70 / 70 | 22 / 18 / 23 | 2,3-2,4 | T | BOFU | [N] /sectores/talleres (encaja si se usa inventario de recambios) | P2 |
| programa para talleres mecanicos / programa de facturacion para taller mecanico | 30 / 20 | 17 / 21 | 2,28 / 2,75 | T | BOFU | ídem | P2 |
| software para academias / software gestion academias | 30 / 30 | 22 / 16 | 1,81 / 2,10 | T | BOFU | [N] /sectores/academias (facturas recurrentes de cuotas; exención de IVA en enseñanza) | P2 |
| factura clases particulares | 20 | 6 | 0 | I | MOFU | ídem | P3 |
| programa para tiendas | 70 | 11 | 0 | T | BOFU | [N] /sectores/comercio (inventario) | P2 |
| software transporte / programa para transportistas | 50 / 10 | 16 / 14 | 3,67 / 0 | T | BOFU | [N] /sectores/transportistas | P3 |
| software electricistas / programa para electricistas | 30 / 10 | 16 / 7 | 0,97 / 0 | T | BOFU | [N] /sectores/electricistas-fontaneros-instaladores | P2 |
| factura electricista / factura fontanero | 40 / 40 | 6 / 5 | 2,35 / 1,14 | I | MOFU | ídem | P2 |
| app para fontaneros / software instaladores | 10 / 10 | 16 / 6 | 0 | T | BOFU | ídem | P2 |
| software para dentistas | 20 | 12 | 0 | T | BOFU | — | P3 |
| software consultoria / facturacion freelance | 10 / 20 | 8 / 9 | 0 / 1,46 | T | BOFU | [N] /sectores/freelance-consultores-disenadores | P2 |
| «programa de facturación para» fontaneros / electricistas / abogados / psicólogos / fisioterapeutas / diseñadores / consultores / academias / peluquerías / construcción / transportistas / comercio / restaurantes / fotógrafos / traductores / arquitectos / clínicas / carpinterías / pintores | s/d (est. baja, 0-30 c/u; CPC 2-5 €) | — | — | T | BOFU | /sectores/* | P2 en conjunto |

**Cuenta:** unas 330 keywords listadas (algunas filas agrupan 2-4 variantes con el mismo dato), de las cuales unas 290 tienen dato de SE Ranking.

---

## 5. Brechas de contenido (gap analysis)

### 5.1 Keywords donde Holded **y** Quipu están en el top 10 y Facturales no aparece (DATO `getDomainKeywordsComparison` holded∩quipu, filtro «factur», vol ≥ 90, ambos ≤ pos. 10)
Facturales no rankea en ninguna (fuera del top 100), así que todas son brecha.

| Keyword | Vol | KD | CPC | Pos. Holded | Pos. Quipu | URL Holded / Quipu | Página Facturales propuesta |
|---|---|---|---|---|---|---|---|
| direccion de facturacion | 810 | 10 | 0,40 | 1 | 7 | blog/direccion-facturacion | glosario |
| programa de facturacion | 590 | 63 | 5,04 | 1 | 1 | listicle / home | home + listicle |
| factura recapitulativa (+ plural) | 590 | 8 | 0,27 | 1 | 1 | blog | /guias/factura-recapitulativa |
| hacer factura(s) online gratis | 590 | 29-30 | 2,1-2,3 | 6-10 | 1 | crea-tu-factura / generador | /generador-de-facturas |
| creador factura(s) | 590 | 24-33 | 2,8-3,1 | 1 | 1 | ídem | ídem |
| crea facturas | 590 | 38 | 3,12 | 3 | 9 | ídem | ídem |
| que es la factura electronica / facturas electronicas que es | 590 | 36 | 0,1-0,2 | 6 | 1 | blog | /factura-electronica |
| plantilla factura autonomo (y unas 20 variantes «modelo/ejemplo/plantilla factura autónomo») | 480 | 13-34 | 0,5-0,9 | 1-10 | 1-8 | plantilla-factura-autonomo / modelos-y-plantillas-factura-autonomo | /plantillas/factura-autonomo |
| modelo factura excel (y unas 12 variantes Excel) | 480 | 26-40 | 0,9-1,0 | 1-9 | 1-8 | plantillas-facturas-excel / modelos-y-plantillas-de-factura | /plantillas/factura |
| plantilla(s) factura(s) gratis (6 variantes) | 480 | 35 | 1,25 | 9-10 | 1 | ídem | ídem |
| factura con excel | 480 | 27 | 0,93 | 9 | 4 | ídem / blog/es-posible-facturar-con-excel | /blog/facturar-en-excel-verifactu |
| programa facturacion verifactu (+ «facturación», «factura») | 480 ×3 | 20-46 | 2,65 | 1 | 1 | blog/mejores-programas-facturacion-verifactu / blog/mejores-programas-para-verifactu | /programa-verifactu + listicle |
| que es factura proforma | 390 | 9 | 0,01 | 1 | 1 | guias/factura-proforma | /guias/factura-proforma |
| factura(s) de abono | 390 | 8 | 0,06 | 8-10 | 1 | blog | /guias/factura-rectificativa |
| como hacer una factura rectificativa | 390 | 9 | 0,07 | 10 | 4 | blog | ídem |
| puedo facturar sin ser autónomo | 390 | 31 | 0,05 | 8 | 7 | blog | /guias/facturar-sin-ser-autonomo |
| factura(s) excel | 390 | 26-31 | 1,00 | 5-7 | 3-4 | plantillas | /plantillas/factura |
| plantilla(s) factura(s) word gratis | 390 | 32 | 0,89 | 2-3 | 1-2 | blog/modelo-factura-word | /plantillas/factura |
| datos de facturacion | 390 | 18 | 1,09 | 1 | 2 | guias/requisitos-datos-facturas | /guias/datos-obligatorios-factura |
| factura(s) con irpf | 390 | 12 | 0,16 | 1 | 1 | blog | /guias/retencion-irpf-factura |

*(La muestra se cortó en 150 filas ordenadas por volumen, y solo cubre keywords que contienen «factur». Hay más brechas en «presupuesto», «modelo 303», «verifactu», «stock», etc.)*

### 5.2 Keywords comerciales de Quipu que Facturales no tiene (DATO `getDomainKeywordsComparison` getquipu.com − facturales.es, filtro programa/software/app/generador/alternativa, vol ≥ 30)
| Keyword | Vol | KD | CPC | Pos. Quipu | URL Quipu |
|---|---|---|---|---|---|
| programa de facturacion | 590 | 63 | 5,04 | 1 | / |
| programa facturacion verifactu / facturación verifactu / factura verifactu | 480 | 20/46/37 | 2,65 | 1 | blog/mejores-programas-para-verifactu |
| programa de factura / programa facturacion | 370 / 330 | 61 / 62 | 4,05 / 4,50 | 1 | / |
| software de facturacion / softwares de facturacion / software de factura / software facturacion | 320 / 320 / 320 / 260 | 70 / 44 / 59 / 54 | 4,1-5,2 | 1 | / |
| programa verifactu gratis | 320 | 20 | 1,24 | 1 | blog/sistema-verifactu-gratis |
| software verifactu gratis | 260 | 21 | 1,41 | 1 | ídem |
| programa facturación autonomos | 320 | 33 | 2,97 | 1 | /es/autonomos |
| programas facturas autonomos | 260 | 23 | 3,23 | 4 | /es/autonomos |
| programa facturacion autonomos | 260 | 33 | 3,23 | 9 | /es/autonomos |
| programa de facturacion para autonomos | 210 | 43 | 3,16 | 11 | /es/autonomos |
| generador de facturas | 210 | 39 | 2,32 | 1 | /es/generador-facturas-gratis-online |
| programas para hacer presupuestos gratis | 210 | 22 | 1,53 | 10 | blog/programa-para-hacer-presupuestos-online |
| software gestion documental (+ variantes) | 390 | 8-17 | 4,42 | 1 | blog/mejores-programas-gestion-documental (listicle fuera del core) |
| programa para hacer (una) factura(s) gratis | 480 | 24-48 | 1,87 | 15-37 | listicle (Quipu no está en el top 10: **hueco abierto**) |
| software facturacion electronica / software factura electronica | 260 | 33 / 41 | 3,82 | 15-23 | listicle (**hueco abierto**) |

**Conclusión del gap (ESTIMACIÓN):** las brechas se agrupan en cinco paquetes que se pueden construir con 20-25 páginas: (1) plantillas de factura (autónomo, Excel, Word, PDF, proforma, rectificativa, simplificada), (2) guías de tipos y requisitos de factura, (3) generador de facturas y presupuestos, (4) silo VeriFactu comercial (programa VeriFactu, VeriFactu gratis, mejores programas VeriFactu), (5) landing de autónomos y listicle «mejores programas de facturación». Holded y Quipu ocupan 1-2 posiciones de cada SERP; las posiciones 3-10 rotan entre competidores medianos y blogs, así que hay sitio.

---

## 6. Análisis de SERPs (DATO: SERP real Google ES, escritorio, 18/10/2026)

**Features detectadas en las 14 SERPs:** AI Overview 14/14 · PAA 13/14 (no en «modelo 303») · vídeo 14/14 · reseñas (rich snippet) 14/14 · imágenes 5/14. Las SERP features de `getSimilarKeywords` confirman AIO («sge») en prácticamente todo el long tail de «programa de facturación» y «verifactu».

| # | Keyword (vol/KD) | Top 10 orgánico (dominio · tipo) | Tipo de página que gana | Qué haría falta para competir (ESTIMACIÓN) |
|---|---|---|---|---|
| 1 | software de facturacion (320/70) | holded (listicle «12 mejores») · sede.agenciatributaria · contasimple (landing gratis) · banktrack (listicle) · wolterskluwer (guía/landing a3) · sage (landing) · facturascloud (home) · billtonic (listicle) · odoo (landing) · stelorder (listicle) | Mezcla 50/50 de listicles y landings | Listicle propio honesto (incluyéndose con criterios claros y tabla de precios) + home con H1 «Software de facturación» y prueba visual. Enlaces de directorios (Capterra/GetApp/Appvizer) |
| 2 | programa de facturacion gratis (210/7) | contasimple · idesoft (descargable con reseñas) · holded (listicle) · AEAT (app gratuita VERI*FACTU) · conavalsi (listicle) · visionwin · facturascripts · mnprogram · facturadirecta · facturalia (listicle) | Productos con plan gratis + listicles + la app de la AEAT | Sin plan gratuito, competir con listicle «programas de facturación gratis: qué limitan y cuándo compensa pagar» + generador gratis. KD 7 engaña: casi todo el top son productos gratis reales |
| 3 | software verifactu (590/5) | AEAT (SIF y VERI*FACTU) · holded (listicle VeriFactu) · sdelsol · contasimple (reglamento) · wolterskluwer · quipu (listicle) · clavei · cegid · b2brouter (VeriFactu gratis) · clavei | Guías de marca + listicles VeriFactu | Landing `/programa-verifactu` muy específica (modalidad, QR, huella, declaración responsable, qué pasa con Excel) + FAQ con schema. Competencia real media pese al KD 5 |
| 4 | programa facturacion autonomos (260/33) | AEAT (app gratis) · contasimple · holded (listicle) · anfix /autonomos · a3factura/autonomos · billin /programa-facturacion-autonomos · softwaredoit (listicle) · sage · getrenn (blog) · conavalsi | Landings de segmento «/autonomos» de marcas (5 de 10) | Landing `/autonomos` (no existe): IVA/IRPF, 303/130 calculados, precio 4,95 €, prueba 14 días, capturas reales, FAQ |
| 5 | plantilla factura (1.900/88) | canva · excel.cloud.microsoft · invoicehome · adobe express · squareup · holded (plantilla autónomo) · wise · facturae.gob.es · quipu · sage | Galerías de plantillas de gigantes | Cabeza muy difícil. Atacar «plantilla factura autónomo/proforma/rectificativa» (KD 7-25) con descargas reales Excel/Word/PDF |
| 6 | modelo 303 (20.100/95) | AEAT ×2 · wolterskluwer · hacienda.gob.es (PDF) · cuentica · contasimple · declarando · taxdown · bbva · talenom | Organismos + guías de marca. Sin PAA | Cabeza inaccesible a corto plazo. Ir a «plazo modelo 303» (KD 0), «como rellenar» (36), «casillas» (16) con una guía casilla a casilla + calendario |
| 7 | alternativa a holded (90/5) | getrenn (blog) · getapp (directorio) · yofacturo (página «alternativa») · factupro (blog) · opusflow (comparativa) · appvizer · docudocu · facturaz · fin2go · mygestion | **Micro-SaaS y blogs pequeños** | **Quick win**: `/alternativas/holded` con tabla de funciones y precios fechada, a quién conviene Holded y a quién Facturales, migración. Hay unos 60 competidores con página similar, así que importa la calidad (datos verificados, capturas) |
| 8 | mejor programa de facturacion para autonomos (70/28) | holded (listicle) · contasimple · anfix /autonomos · albadelgado (blog) · softwaredoit · a3factura · billin · quipu (listicle) · declarando · stelorder | Listicles de marca + landings | Listicle con metodología (pruebas reales, criterios), sección por perfil (≤5 facturas al mes, con gestoría, con stock…) |
| 9 | factura electronica obligatoria (720/42) | AEAT · caixabank · groupseres · sage · holded · declarando · cegid · wolterskluwer · contasimple · dashdoc | Guías de autoridad (banca, software, AEAT) | Guía actualizada con el calendario del reglamento B2B (fechas por facturación), diferencia con VERI*FACTU (ya existe un post) y tabla «qué tengo que hacer si soy autónomo» |
| 10 | conciliacion bancaria (vol anómalo/8) | wolterskluwer · bbvaspark · anfix · embat · youtube · debitoor · pleo · contasimple · holded · wikipedia | Guías informativas | Guía con ejemplo resuelto + plantilla Excel + enlace a `bancos-conciliacion` (extractos Excel/CSV). KD bajo: alcanzable |
| 11 | generador de facturas (210/39) | invoice-generator.com · flowlu · Zoho (Play) · invoicehome · canva · quipu · billin · holded · contasimple · declarando | Herramientas reales sin registro | Herramienta funcional (no un formulario de captación), rápida, con IVA, IRPF y recargo de equivalencia y descarga PDF |
| 12 | control de stock (390/8) | slimstock · wolterskluwer · agorapos · holded (blog) · squareup · anfix (blog) · billin (landing `/control-de-stock/`) · mecalux · valsur · ar-racking | Guías + alguna landing | Guía «Control de stock para pymes» + `gestiona-tu-stock` optimizada (stock mínimo, alertas, descuento al facturar). Muy alcanzable |
| 13 | gestion de cobros (320/8) | unir · cesce · paycomet · kyocera · cuentica (landing feature) · youtube · gestion5 · pbs · esker · bravocapital | Guías genéricas; solo Cuentica como landing de producto | Página `cobros` con H1/H2 «Gestión de cobros» + guía de recordatorios automáticos y plantillas de email. Muy alcanzable |
| 14 | programa para hacer presupuestos (170/22) | Play Store (app) · contasimple · billin · holded (listicle) · capterra · App Store · flowlu (generador) · sage · quipu (listicle) · reddit | Landings de feature + apps + listicles | `crea-envia-presupuestos` reorientada a «Programa para hacer presupuestos» + generador de presupuestos gratis |

**Patrones (ESTIMACIÓN):**
- La **AEAT** entra en el top 3 de casi todo lo relacionado con VeriFactu y «gratis» por su app gratuita. Toca explicar con honestidad cuándo basta la app de la AEAT y cuándo compensa un software (control de cobros, gastos, 303/130, stock).
- Los **listicles «mejores…» de los propios vendedores** ocupan el #1 de los genéricos BOFU. Facturales necesita el suyo, con metodología transparente.
- Los **directorios** (GetApp, Capterra, Appvizer, softwaredoit, cronomia) aparecen en las SERP comparativas. Darse de alta con reseñas reales es a la vez SEO off-page y presencia en el SERP. Sin testimonios inventados.
- **AI Overview en el 100 % de las SERPs:** hay que estructurar las páginas para que el AIO las cite (respuesta en las primeras 40-60 palabras, tablas, listas, FAQ con schema, datos fechados y fuente oficial enlazada).

---

## 7. Oportunidades priorizadas

### 7.1 Matriz de priorización (ESTIMACIÓN)
Puntuación = intención de contratación (1-5) × alcanzabilidad (KD invertido y SERP real, 1-5) × volumen del cluster (1-3).

| Rank | Oportunidad (página) | Keywords principales (vol / KD) | Volumen del cluster (DATO, suma aprox.) | Por qué |
|---|---|---|---|---|
| 1 | **[N] /programa-verifactu** (landing comercial) | programa facturacion verifactu 480/20 · programa factura verifactu 480/37 · software verifactu 590/5 · programa de facturacion con verifactu 210/28 · verifactu programa 170/35 · programa verifactu 150/37 · verifactu software 140/39 · software de facturación verifactu 50/3 | ~2.700 | Intención BOFU, CPC 2,3-4,4 €, KD bajo-medio, demanda creciente hasta la obligatoriedad (2027) |
| 2 | **[N] /autonomos** (landing de segmento) | programa facturación autonomos 320/33 · programa facturacion autonomos 260/33 · programas facturas autonomos 260/23 · programa facturas autonomos 260/41 · programa de facturacion para autonomos 210/43 · programas de facturacion para autonomos 110/33 · facturacion autonomos 110/23 | ~1.600 | En el SERP ganan landings «/autonomos» (5 de 10). Facturales no tiene ninguna |
| 3 | **[N] /alternativas/{holded,quipu,contasimple,billin,anfix,facturadirecta,stel-order}** + hub | precios holded 480/33 · contasimple opiniones 390/16 · holded opiniones 260/25 · billin precios 260/28 · quipu precios 260/21 · contasimple precios 210/0 · stel order precios 210/13 · alternativa(s) a holded 90+90/5 | ~2.900 | Intención de cambio de proveedor; KD 0-33; SERP con micro-SaaS; precio de Facturales competitivo |
| 4 | **[N] /blog/verifactu-gratis** (app AEAT frente a software) | verifactu gratis 610/17 · programa verifactu gratis 320/20 · software verifactu gratis 260/21 · aplicacion verifactu aeat 320/36 · verifactu descargar 320/17 | ~1.800 | MOFU que convierte bien si explica los límites de la app de la AEAT |
| 5 | **[N] /generador-de-facturas** (+ presupuestos) | hacer factura online gratis 590/29 · creador facturas 590/24 · crear factura 590/33 · hacer factura online 390/6 · factura online gratis 480/31 · crear factura online 260/33 · generador de facturas 210/39 · hacer presupuesto online 140/17 · presupuesto online gratis 110/17 | ~4.500 | Recoge la intención «gratis» con CPC 2-3,6 €; es el activo de enlazado natural |
| 6 | **[N] /blog/mejores-programas-facturacion** (listicle honesto) | mejor programa de facturación 210/32 · mejores programas de facturacion 170/37 · programa de facturacion gratis 210/7 · mejores programas… gratis 90/28 · mejor programa… para autonomos 70/28 | ~1.000 + long tail | Es el formato que gana el #1 en los genéricos |
| 7 | **Optimizar módulos existentes** (`gestiona-tu-stock`, `cobros`, `bancos-conciliacion`, `escanea-gastos`, `tu-negocio-bajo-control`, `gestiona-clientes`) | control de stock 390/8 · gestion de stock 260/9 · gestion de inventario 260/23 · gestion de cobros 320/8 · gestion de clientes 260/8 · control financiero 260/7 · dashboard financiero 110/6 · escanear facturas 70/7 | ~2.300 | KD < 10. Solo hace falta reescribir H1/H2/meta, añadir FAQ y una guía de apoyo |
| 8 | **[N] /facturas-recurrentes** (feature nueva, 17/10/2026) | facturas recurrentes 50/9 · factura recurrente 50/8 · facturación recurrente 50/7 · cobros recurrentes 10/8 (CPC 7,15) | ~160 | Poco volumen, intención máxima, SERP débil |
| 9 | **Guías de tipos de factura** (`/guias/…`) | factura recapitulativa 590/8 · que es factura proforma 390/9 · como hacer una factura rectificativa 390/9 · factura de abono 390/8 · tipos de facturas 320/16 · plantilla factura proforma 210/8 · factura simplificada requisitos 140/16 | ~2.400 | KD < 16; enlaces internos hacia `crea-envia-facturas` |
| 10 | **Plantillas** (`/plantillas/…`) | modelo factura autonomo 480/7 · plantilla factura autonomo 480/25 · ejemplo factura autonomo 480/22 · modelo de factura 910/39 · plantilla factura gratis 480/35 · plantilla albaran 590/8 · presupuesto de obra 320/10 | ~4.000 | Es lo que más tráfico estable da a Quipu y Holded |
| 11 | **Calculadora IVA+IRPF** | calculadora irpf autonomos 590/9 · quitar iva 480/11 · como calcular el iva de una factura 260/15 · calcular irpf factura 170/9 (+ cabezas 14.800-22.400 a largo plazo) | ~1.500 (sin cabezas) | Activo que capta enlaces; Anfix y Contasimple sacan el 10-14 % de su tráfico de aquí |
| 12 | **Guías fiscales de long tail** | iva soportado 760/9 · iva repercutido 660/8 · iva deducible 660/9 · modelo 347 880/18 · modelo 390 370/17 · plazo modelo 303 210/0 · plazo modelo 130 170/0 · modelo 130 como rellenar 170/5 · calendario fiscal 2026→2027 720/26 · gastos deducibles autonomos 320/21 | ~4.500 | TOFU/MOFU con KD bajo; encaja con «impuestos 303/130 calculados» |
| 13 | **Sectores** (`/sectores/…`) | programa de reformas 170/18 · presupuesto reforma 320/19 · software construccion 70/10 · software para peluquerías 140/8 · software fisioterapia 110/10 · software para psicologos 70/22 · software para abogados 50/9 · talleres 70×3 | ~1.500 | Long tail BOFU con CPC 2-5 €; ningún gran competidor lo cubre |
| 14 | **[N] /gestorias** | software para gestorias 50/15 (CPC 5,83) · programa para gestorias 20/20 · gestoria online 440/22 | ~500 | El rol gestoría es un diferencial; CPC muy alto |
| 15 | **Factura electrónica obligatoria** | factura electronica obligatoria 720/42 · que es la factura electronica 590/36 · factura electronica autonomos 390/29 · factura electronica b2b 210/17 | ~2.100 | Mucha demanda informativa ligada a VERI*FACTU (ya hay un post) |

### 7.2 Quick wins (≤ 4-8 semanas, KD ≤ 20 e intención T/C)
1. `gestiona-tu-stock`: H1/H2 «Control de stock y gestión de inventario». FAQ sobre stock mínimo, descuento automático al emitir factura y devolución al anular, y que es un solo almacén. → control de stock 390/8, gestion de stock 260/9, stock minimo 110/6, app inventario 40/9.
2. `cobros`: H1/H2 «Gestión de cobros y recordatorios de pago automáticos» más una plantilla de email de recordatorio. → gestion de cobros 320/8, recordatorio de pago 40/10, reclamar factura impagada 90/8.
3. `tu-negocio-bajo-control`: «Panel de control financiero / dashboard». → control financiero 260/7, dashboard financiero 110/6, cuadro de mando financiero 50/6.
4. `gestiona-clientes`: «Gestión de clientes y CRM con facturación». Ya rankea entre la 51 y la 62. → gestion de clientes 260/8, crm facturacion 40/9.
5. `escanea-gastos`: «Escanear facturas y tickets». → escanear facturas 70/7, escanear tickets 50/8, digitalizar facturas 140/23.
6. Nueva `/facturas-recurrentes`: 160/mes en conjunto, KD 7-9.
7. `/alternativas/holded`, `/alternativas/contasimple`, `/alternativas/quipu` y `/alternativas/billin` (KD 0-28).
8. Guías de factura recapitulativa (590/8), factura proforma (390/9 + plantilla 210/8) y rectificativa/abono (390/9 + 390/8).
9. Guías de plazo modelo 303 (210/0), plazo modelo 130 (170/0), cómo rellenar el 130 (170/5) y modelo 347 (880/18).
10. Guía de qué es la conciliación bancaria con ejemplo y plantilla Excel (480/8).

### 7.3 Arquitectura de URLs recomendada (ESTIMACIÓN; adaptar al sitio estático actual)
```
/                                   → «Programa de facturación y suite financiera»
/autonomos  /pymes  /gestorias      → landings de segmento [N]
/programa-verifactu                 → landing comercial VeriFactu [N]
/facturas-recurrentes               → feature nueva [N]
/{módulos existentes}.html          → reoptimizar (stock, cobros, bancos, gastos, panel, clientes)
/sectores/{reformas-construccion|peluquerias|fisioterapeutas|psicologos|abogados|talleres|academias|comercio|instaladores|freelance}  [N]
/alternativas/  + /alternativas/{holded|quipu|contasimple|billin|anfix|facturadirecta|stel-order}  [N]
/comparativas/holded-vs-quipu       [N] (opcional)
/herramientas/generador-de-facturas  /herramientas/generador-de-presupuestos  /herramientas/calculadora-iva-irpf  [N]
/plantillas/  + factura | factura-autonomo | factura-proforma | presupuesto | albaran | recordatorio-pago | inventario | libro-ingresos-gastos  [N]
/guias/  + como-hacer-una-factura | datos-obligatorios-factura | tipos-de-factura | factura-recapitulativa | factura-rectificativa | factura-simplificada | factura-sin-iva-exenta | numeracion-facturas | retencion-irpf-factura | iva-soportado-repercutido | modelo-303 | modelo-130 | modelo-347 | modelo-390 | modelo-349 | conciliacion-bancaria | gastos-deducibles-autonomos | ley-morosidad-plazos-pago | reclamar-factura-impagada | flujo-de-caja | stock-minimo  [N]
/calendario-fiscal-2027             [N] (publicar en dic-2026; renovar cada año en la misma URL o con redirección)
/blog/ (news-grid.html actual) + verifactu-gratis | verifactu-vs-no-verifactu | facturar-en-excel-verifactu | mejores-programas-facturacion | programas-facturacion-gratis | factura-electronica-obligatoria  [N]
```
Enlazado interno: cada guía o plantilla enlaza a su módulo y a la prueba de 14 días (`app.facturales.es/signup`). Los hubs `/guias/`, `/plantillas/` y `/alternativas/` se enlazan desde el footer (`footer-include.js`) y se añaden a `sitemap.xml`.

### 7.4 Riesgos y reglas de contenido (ESTIMACIÓN, alineado con CLAUDE.md)
- No afirmar «gratis» para el producto (es una prueba de 14 días), ni «sin tarjeta», ni presentación automática de modelos a la AEAT, ni conexión bancaria directa (es «Próximamente»; hoy se importan extractos Excel/CSV), ni testimonios o valoraciones inventadas.
- Las páginas de alternativas deben llevar datos verificables y fechados («precios consultados el dd/mm/aaaa en la web oficial»), un tono justo (cuándo conviene el competidor) y nada que imite la marca ajena.
- «Kit digital verifactu» (480/13): solo si Facturales es solución adherida; si no, se descarta.
- TicketBAI, TPV, WooCommerce o PrestaShop: no trabajar mientras no existan.

---

## 8. Anexo: notas de método
- Volúmenes: media mensual de SE Ranking (base `es`), actualizada a oct-2026. Hay variantes singular/plural y con o sin tilde que comparten cifra porque SE Ranking las agrupa; no deben sumarse como demanda independiente.
- Tráfico de competidores: estimación de SE Ranking por CTR. Útil para ranking relativo, no como visitas reales (Holded probablemente recibe bastante más tráfico real por marca y por otros países).
- SERPs: 14 consultas con `getSerpResults` / `getSerpTaskResults` (tipo standard), escritorio, país ES, idioma es, sin personalización. Las features (AIO, PAA, vídeo, reseñas) salen del campo `SERP_features` de la tarea.
- Archivos en bruto: `[scratchpad de la auditoría, no versionado]/data/` (kw1.json, kw1.tsv, gap_holded_quipu.json, serp1.json, s_autonomos.json, s_plantilla.json, s_fe.json, s_conc.json, s_cobros.json).
