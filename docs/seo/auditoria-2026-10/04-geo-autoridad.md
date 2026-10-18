# 04 · GEO, autoridad de dominio y digital PR — Facturales (facturales.es)

Fecha del análisis: 18/10/2026 · Mercado: España · Autor: análisis automatizado (Claude) sobre SE Ranking API, búsquedas web, sitio en producción y repositorios `/home/user/facturales-landing` y `/home/user/facturales/src`.

Convención del documento:
- **[DATO]** = comprobado, con fuente o URL.
- **[HIPÓTESIS]** = inferencia razonable que no se ha podido verificar.
- **[RECOMENDACIÓN]** = acción propuesta.

No se ha modificado ningún archivo de los repositorios.

---

## 0. Resumen ejecutivo

1. **[DATO] Para los buscadores y los LLM, Facturales es hoy prácticamente invisible.** SE Ranking le atribuye **1 dominio referente** (avenuemedia.io, empresa del mismo grupo), 1 backlink con el anchor «Visitar» y un Domain InLink Rank de **6**. En cambio, Holded tiene **5.567** dominios referentes y DIR **82**; Quipu, **3.271** y 74; Billin, **2.462** y 71; Anfix, **2.258** y 69; Contasimple, **1.861** y 73.
2. **[DATO] En búsqueda con IA, la cuota de voz es 0.** Medido en el leaderboard de SE Ranking (ES, con ChatGPT, Perplexity, Gemini, AI Overviews y AI Mode), Facturales tiene `link_presence = 0` y `brand_presence` sin datos. Sage (25 %), Holded (20 %) y Quipu (14 %) dominan.
3. **[DATO] Los LLM no citan a medios de referencia: citan comparativas escritas por los propios fabricantes** (holded.com/blog, getquipu.com/blog, billin.net/blog, stelorder.com/blog, factorial.es) **y por un puñado de terceros pequeños** (getrenn.com, factupro.es, cronomia.com, softwaredoit.es, banktrack.com, conavalsi.com, revolucionatupyme.com, facturalia.info). Esto significa que un actor pequeño **sí puede entrar en las respuestas** si publica páginas comparativas y factuales de calidad y aparece en las listas de terceros.
4. **[DATO] Hay una noticia regulatoria que reordena el tablero.** El 05/10/2026 el Ministerio de Hacienda anunció la *previsión* de aplazar las obligaciones pendientes del RD 1007/2023 (VERI\*FACTU) **hasta octubre de 2028**, para alinearlas con la factura electrónica B2B de empresas con hasta 8 M€ de facturación ([nota del Ministerio](https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf)). La AEAT aún muestra las fechas del RDL 15/2025 (01/01/2027 y 01/07/2027) ([nota AEAT](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html)). La guía de Facturales (`verifactu-2027-guia-autonomos-pymes.html`) sigue hablando de 2027 sin mencionar el aplazamiento. **Es la mayor oportunidad de citación a corto plazo**: ser la fuente más clara, con fecha y actualizada.
5. **[DATO] Faltan señales de entidad:**
   - el Organization schema no tiene `sameAs`, `legalName`, `address` ni `vatID`;
   - la landing no muestra en ningún sitio la razón social (AVENUE DIGITAL GROUP, S.L.);
   - no hay perfiles sociales en el pie;
   - el aviso legal vive en una SPA (`app.facturales.es/aviso-legal`) que, sin JavaScript, sirve un cascarón vacío de 6 KB;
   - **la cabecera y el pie se inyectan con `document.write`**, así que los crawlers de IA que no ejecutan JS no ven la navegación ni el pie;
   - no se han encontrado fichas en Capterra, G2, GetApp, Trustpilot, LinkedIn, Crunchbase, Wikidata, App Store ni Google Play.
6. **[DATO] Hay problemas en los textos legales que afectan a la autoridad y al cumplimiento:**
   - El aviso legal **prohíbe los enlaces profundos** («Se prohíben expresamente enlaces profundos… deberán recabar la autorización expresa y por escrito»). Contradice cualquier estrategia de enlaces.
   - La «declaración» de cumplimiento cita la Ley 11/2021, pero no tiene el contenido que exigen la Orden HAC/1177/2024 y la AEAT.
   - Hay una errata, «app.factuales.es».
   - El fuero es Madrid, pero el domicilio está en Valladolid.

**Prioridades a 90 días:**
- (a) Base técnica de entidad: HTML estático para cabecera y pie, aviso legal en HTML estático, schema completo, `llms.txt`, robots para bots de IA, Bing + IndexNow.
- (b) Página de declaración responsable VERI\*FACTU pública y por versión, y página «Facturales en datos».
- (c) Guía VERI\*FACTU actualizada con el aplazamiento a 2028 y comparativas propias («alternativas a Holded», «programa de facturación gratis vs AEAT»).
- (d) Fichas en Capterra/GetApp/G2, App Store/Play, LinkedIn y Wikidata, y alta en las comparativas de terceros que ya citan los LLM.
- (e) Un activo enlazable: herramienta gratuita y estudio de datos.

---

## 1. Perfil de autoridad (backlinks) frente a la competencia

### 1.1 Métricas principales — [DATO] SE Ranking `getBacklinksSummary`, modo `domain`, 18/10/2026

| Dominio | Backlinks | Dominios referentes | Dofollow RD | Domain InLink Rank | .edu RD | .gov RD | Top anchor por RD |
|---|---:|---:|---:|---:|---:|---:|---|
| **facturales.es** | **1** | **1** | 1 | **6** | 0 | 0 | «Visitar» |
| holded.com | 161.845 | 5.567 | 3.414 | 82 | 28 | 4 | «Holded» (884 RD) |
| getquipu.com | 15.790 | 3.271 | 1.467 | 74 | 31 | 10 | spam Telegram (361) / «Quipu» (314) |
| billin.net | 7.468 | 2.462 | 1.291 | 71 | 20 | 6 | «billin.net» (874) |
| anfix.com | 12.897 | 2.258 | 1.247 | 69 | 11 | 1 | «Anfix» (212) |
| contasimple.com | 389.456 | 1.861 | 1.218 | 73 | 0 | 0 | spam Telegram (193) / «contasimple» (188) |
| quipu.app | 52 | 32 | 7 | 6 | 0 | 0 | (dominio ajeno a Quipu España) |

- [DATO] El único dominio referente de Facturales es **avenuemedia.io** (DIR 43, visto por primera vez el 25/03/2026). Según Sortlist es la agencia Avenue Media de Valladolid, previsiblemente del mismo grupo que el titular AVENUE DIGITAL GROUP, S.L. Es un enlace corporativo legítimo, pero no aporta autoridad independiente.
- [DATO] Los cinco competidores reciben cientos de dominios de spam (anchors tipo «TELEGRAM @SEO_ANOMALY…», directorios «*ranks.com», acortadores). Es ruido o negative SEO habitual que Google ignora. **No es un modelo que imitar** y explica parte del volumen bruto.
- [DATO] Contasimple tiene 389 k backlinks, pero solo 1.861 dominios: son enlaces *sitewide* con anchors comerciales («mejores programas de facturación» 100.713, «factura electrónica obligatoria» 100.722). Su mayor dominio por volumen es **infoautonomos.com (3.993 enlaces)**, lo que refleja un acuerdo comercial o editorial con Infoautónomos.
- [DATO] Los activos que más enlaces captan para los competidores son **plantillas y glosarios**:
  - Holded: `/blog/plantilla-presupuesto` (220 RD) y `/plantillas-de-almacenes-e-inventarios` (205 RD);
  - Quipu: `/blog/plantilla-presupuesto-descargar/` (214 RD);
  - Billin: `/glosario/definicion-fiador/` (323 RD), además de otras entradas de su glosario.

### 1.2 Tipos de enlaces que tienen los competidores — [DATO] dominios referentes con mayor DIR (1.500 por competidor)

| Tipo | Ejemplos reales (quién enlaza a quién) |
|---|---|
| **Medios económicos nacionales** | cincodias.elpais.com (los 5), elpais.com (Holded, Anfix), expansion.com (Holded), forbes.es (Anfix, Holded), europapress.es (Billin, Holded), huffingtonpost.es, libertaddigital.com, elconfidencialdigital.com (los 5), economiadigital.es, theobjective.com, elindependiente.com |
| **Medios para autónomos y pymes** | emprendedores.es (los 5), autonomosyemprendedor.es (4), pymesyautonomos.com (4), cepymenews.es (los 5), infoautonomos.com (Holded, Anfix, Contasimple), elreferente.es (4), ticpymes.es, directivosygerentes.es, ecommerce-news.es, rrhhdigital.com (los 5), economiadehoy.es |
| **Prensa regional (notas de prensa / contenido patrocinado)** | diariodesevilla.es, europasur.es, elprogreso.es, diariodepontevedra.es, salamancartvaldia.es, galiciapress.es, castillayleoneconomica.es (Holded, Anfix — relevante para una empresa de Valladolid), cantabriaeconomica.com |
| **Cámaras de comercio** | Portales «TIC Negocios» de las cámaras: ticnegocios.camaralicante.com (30 enlaces a Holded), camaramurcia.es, camarazaragoza.com, camaranavarra.com, camaramalaga.com; serviciosempresariales.camaramadrid.es (Holded, Quipu, Contasimple) |
| **Asociaciones de autónomos y empresariales** | ceat.org.es (Anfix), uptaemprende.es (Anfix, Contasimple), masempresas.cea.es y club emprendedores de CEA (Anfix 18, Quipu), clubemprendedoresmalaga.es (Anfix, Billin), aedn.es |
| **Programas públicos de digitalización** | oficinaacelerapymecuenca.itecam.com (Holded, Quipu) — red de Oficinas Acelera Pyme de Red.es |
| **Universidades / educación** | blogs.salleurl.edu (Billin, Holded), iebschool.com, crehana.com, guiaemprendimientodigital.coiico.es (colegio de ingenieros, Anfix y Quipu); además, muchos .edu latinoamericanos de spam |
| **Partners / integraciones / ecosistema** | apps.shopify.com y shopify.com, qonto.com, signaturit.com, fintonic.com, generali.es, edenred.es, xolo.io, raiolanetworks.com, dinahosting.com, ionos.es (los 5), blogempresas.masmovil.es (los 5), blog.masorange.es, blogempresas.yoigo.com, dayonecaixabank.es, hubspot.es, intercom.help |
| **Directorios y comparadores de software** | softwaredoit.es (Billin, Quipu), comparasoft.es (Anfix 29, Billin 17, Contasimple 21), microdata.es, radarsaas.es, startupxplore.com, startups-espanolas.es, getlatka.com, crunchbase.com (Anfix), theorg.com, growjo.com, webcatalog.io, appadvice.com |
| **Tiendas de apps** | apps.apple.com (Holded, Quipu, Billin, Anfix) |
| **Wikipedia** | es.wikipedia.org (Holded, Quipu, Billin) |
| **Gestorías y asesorías** | lgsasesores.es, techma.bakertilly.es, danielgrifol.es, justanswer.es, foros.plangeneralcontable.com (los 5) |
| **Competidores que enlazan a competidores** | stelorder.com (enlaza a Anfix, Billin, Contasimple y Quipu en sus comparativas), billin.net (enlaza a Contasimple, Holded y Quipu), factorial.es → Quipu, teamsystem.es → Billin y Quipu |

### 1.3 Link gap: dominios que enlazan a ≥2 competidores y no a Facturales — [DATO]

Método: intersección de los 1.500 dominios referentes con mayor DIR de cada competidor (SE Ranking). Se encontraron **1.374 dominios** que enlazan a ≥2 competidores; Facturales no tiene ninguno. La lista bruta está en `[scratchpad de la auditoría, no versionado]/linkgap_raw.tsv`. Aquí van solo los relevantes y alcanzables, sin spam:

| Dominio | Nº competidores | DIR | Tipo |
|---|---:|---:|---|
| cincodias.elpais.com | 5 | 96 | Medio económico |
| emprendedores.es | 5 | 85 | Medio pymes |
| cepymenews.es | 5 | 78 | Medio pymes |
| elconfidencialdigital.com | 5 | 85 | Medio |
| rrhhdigital.com | 5 | 83 | Medio B2B |
| ionos.es | 5 | 89 | Blog de hosting (guías para autónomos) |
| blogempresas.masmovil.es | 5 | 80 | Blog de telco para pymes |
| foros.plangeneralcontable.com | 5 | 61 | Comunidad contable |
| todoexpertos.com | 5 | 72 | Q&A |
| autonomosyemprendedor.es | 4 | 82 | Medio autónomos |
| elreferente.es | 4 | 80 | Directorio y medio de startups |
| pymesyautonomos.com | 4 | 74 | Medio (Webedia) |
| que.es | 4 | 85 | Medio |
| directivosygerentes.es | 4 | 75 | Medio |
| economiadehoy.es | 4 | 74 | Medio |
| ecommerce-news.es | 4 | 78 | Medio |
| blog.masorange.es | 4 | 72 | Blog de telco |
| apps.apple.com | 4 | 100 | Ficha de app |
| startupxplore.com | 4 | 82 | Directorio de startups |
| rankia.com | 4 | 79 | Comunidad financiera |
| wwwhatsnew.com | 4 | 84 | Medio tech (publicó «Apps para autónomos en España 2026») |
| marketing4ecommerce.net | 4 | 86 | Medio |
| microdata.es, radarsaas.es, facturaz.es, guiafiscal.es, calculafiscal.es, autonomofactura.com, billeo.es | 4 | 12–51 | Nicho de facturación y fiscalidad |
| infoautonomos.com | 3 | 75 | Referente para autónomos |
| serviciosempresariales.camaramadrid.es | 3 | 76 | Cámara de comercio |
| ticpymes.es | 3 | 70 | Medio |
| serautonomo.net | 3 | 53 | Medio autónomos |
| comparasoft.es | 3 | 6 | Comparador (muchos enlaces) |
| es.wikipedia.org | 3 | 100 | Enciclopedia (requiere notoriedad) |
| apps.shopify.com | 3 | 100 | Marketplace de integraciones |
| softwaredoit.es | 2 | 71 | Comparador (citado por ChatGPT) |
| masempresas.cea.es | 2 | 72 | Confederación de Empresarios de Andalucía |
| castillayleoneconomica.es | 2 | 62 | Medio regional (CyL) |
| uptaemprende.es | 2 | 23 | UPTA |
| startups-espanolas.es | 2 | 45 | Directorio |
| certificadoelectronico.es | 2 | 45 | Nicho fiscal |
| crearmiempresa.es | 2 | 50 | Nicho emprendimiento |

[HIPÓTESIS] El análisis cubre solo los 1.500 dominios con mayor DIR de cada competidor, así que no detecta fichas *nofollow* o redirigidas como Capterra/GetApp, que existen pero no aparecen en la muestra.

---

## 2. Visibilidad en búsquedas con IA

### 2.1 Leaderboard IA España — [DATO] SE Ranking `getAiSearchLeaderboard`, source = es, 5 motores, datos de octubre de 2026

| # | Marca (dominio) | Share of voice | Brand presence (prompts) | Link presence (citas) |
|---:|---|---:|---:|---:|
| 1 | Sage (sage.com) | 25,4 % | 7.590 | 27.572 |
| 2 | Holded | 20,3 % | 4.923 | 28.105 |
| 3 | Quipu (getquipu.com) | 14,4 % | 2.564 | 25.021 |
| 4 | Anfix | 12,0 % | 3.100 | 15.509 |
| 5 | Billin | 9,1 % | 916 | 19.573 |
| 6 | Factorial | 8,0 % | 3.985 | 123 |
| 7 | STEL Order | 5,5 % | 554 | 11.784 |
| 8 | Contasimple | 3,6 % | 833 | 5.118 |
| 9 | FacturaDirecta | 1,5 % | 446 | 1.561 |
| 10 | Invoice Ninja | 0,3 % | 133 | 128 |
| 11 | **Facturales** | **0 %** | sin datos | **0** |

Por motor, Holded consigue 24.656 citas en AI Overviews, 1.332 en Perplexity, 401 en ChatGPT y 459 en Gemini. Facturales tiene `no_data` en todos los motores.

### 2.2 Qué responden los LLM a los prompts objetivo — [DATO] respuestas y fuentes guardadas por SE Ranking (ES, octubre de 2026)

| Prompt (motor) | Marcas citadas en la respuesta | Fuentes (URLs) citadas |
|---|---|---|
| «mejor programa de facturacion para autonomos» (Perplexity) | Contasimple, Billin, FacturaDirecta, Quipu, Holded, Alegra, Anfix, Cuéntica | factorial.es/blog/top-programas-facturacion-empresas, stelorder.com/blog/programas-facturacion-autonomos, **banktrack.com/blog/software-facturacion-espana**, **gocardless.com/es/guias/…/5-mejores-programas-de-facturacion…**, getquipu.com/blog/mejores-10-programas…, **revolucionatupyme.com/los-mejores-programas-de-facturacion**, holded.com/es/blog/programa-facturacion-autonomos, billin.net/blog/mejores-programas-facturacion |
| «mejores programas de facturacion» (Perplexity) | FacturaDirecta, Billin, Quipu, Anfix, Sage 50, Holded, Contasimple, a3factura | banktrack.com, factorial.es, billin.net, stelorder.com, getquipu.com, **softwaredoit.es/software-de-facturacion**, holded.com ×2, YouTube, **cronomia.com/software-facturacion** |
| «mejor programa facturacion autonomos» (Perplexity) | Quipu, Holded, Billin, Contasimple, a3factura | getquipu.com, softwaredoit.es, holded.com ×2, revolucionatupyme.com, **softwarepara.net/facturacion-autonomos**, YouTube ×3 |
| «software verifactu» (AI Overviews/AI Mode) | Holded, Billin/Factusol (TeamSystem), Anfix, Quipu, FacturaDirecta, Sage; además, la app gratuita de la AEAT | sede.agenciatributaria.gob.es, contasimple.com/reglamento-verifactu, wolterskluwer.com, sdelsol.com, **holded.com/es/blog/mejores-programas-facturacion-verifactu**, teamsystem.es/magazine/mejores-programas-verifactu, b2brouter.net, cegid.com, clavei.es, YouTube |
| «programa facturacion verifactu» (AIO) | App gratuita de la AEAT, Holded, FacturaDirecta, Factusol/Quipu, Anfix/Billin | AEAT (noticia de la app gratuita, 13/10/2025), holded.com, getquipu.com/blog/mejores-programas-para-verifactu, sdelsol.com, facturadirecta.com/verifactu |
| «alternativa(s) a holded» (AIO) | Anfix, Quipu, Zoho Books, Sage Active, Contasimple | **getrenn.com/es/blog/alternativas-holded**, **factupro.es/blog/alternativas-holded-autonomos**, **cronomia.com/software/holded/alternativas** |
| «mejor programa de facturación gratis» (AIO) | Contasimple, app de la AEAT, Facturi (MN Program), Visionwin | contasimple.com, **getrenn.com/es/blog/programa-de-facturacion-gratis**, mnprogram.com, visionwin.com, holded.com, **conavalsi.com**, **facturalia.info/comparativa-…-verifactu** |
| «software facturacion gratis» (AIO) | FacturaScripts, Mgest Lite, Jasmin, Visionwin | juncotic.com, holded.com, urbantecno.com |
| «verifactu holded» (AIO) | Holded | holded.com (incluye **«Holded, colaborador social de la AEAT para Verifactu»**), help.holded.com, YouTube |

Conclusiones:
- **[DATO]** En AI Overviews/AI Mode, el blog de Holded «12 mejores programas de facturación 2026» aparece como fuente en casi todas las respuestas sobre programas gratuitos.
- **[DATO]** Dos SaaS jóvenes y pequeños, **getrenn.com (renn)** y **factupro.es**, salen citados en «alternativas a Holded» y «programa de facturación gratis» con páginas comparativas en tablas. Es la prueba de que el formato funciona aunque el dominio tenga poca autoridad.
- **[DATO]** Holded aprovecha su condición de **colaborador social de la AEAT** como argumento citable en VERI\*FACTU.
- **[DATO]** Las respuestas informativas («cómo anular una factura», «qué es una factura REBU») citan la AEAT, el BOE, facturae.gob.es y los blogs de Holded, Quipu, Billin y STEL Order. Si Facturales tiene guías de calidad con fuentes oficiales, puede competir ahí.
- **[DATO]** En las respuestas recogidas no aparecen Xataka, Genbeta, Infoautónomos, El Economista ni Capterra para estos prompts. Las fuentes dominantes son blogs de fabricantes y comparativas pequeñas, más YouTube.

### 2.3 Comparativas «mejores programas de facturación 2026» que existen — [DATO] búsqueda web del 18/10/2026

| URL | Tipo | Marcas que incluye (resumen) | ¿Acepta altas? |
|---|---|---|---|
| holded.com/es/blog/los-mejores-programas-de-facturacion | Fabricante | Holded, Mgest, Factusol, SeniorFactu, Jasmin, Visionwin, Odoo, Contasol… | No (competidor) |
| billin.net/blog/mejores-programas-facturacion | Fabricante (TeamSystem) | 10 programas | No |
| billin.net/blog/mejores-programas-verifactu | Fabricante | 7 programas | No |
| getquipu.com/blog/mejores-programas-para-verifactu | Fabricante | 6 | No |
| teamsystem.es/magazine/mejores-programas-facturacion y /mejores-programas-verifactu | Fabricante | 6 | No |
| stelorder.com/blog/los-10-mejores-programas-de-facturacion… / mejores-programas-verifactu / mejores-aplicaciones-para-hacer-facturas | Fabricante | Anfix, Billin, Contasimple, Quipu… | No |
| factorial.es/blog/top-programas-facturacion-empresas | Fabricante (RR. HH.) | 10 | Posible vía partnership |
| economia3.com/2026/08/25/…mejor-programa-de-facturacion-para-autonomos-en-2026 | Medio regional (Redacción E3) | Holded, Quipu, Billin, Contasimple, Anfix (sin patrocinio declarado) | Contacto editorial |
| rankiabusiness.com/mejores-programas-facturacion | Medio / comunidad | varios | Contacto editorial |
| youasesoria.com/mejores-programas-facturacion-autonomos | **Asesoría** | varios | **Sí: tipo partner** |
| contamoney.com/blog/mejores-programas-de-facturacion-contabilidad | Fabricante | — | No |
| billtonic.com/mejores-programas-de-facturacion-en-2026 | Fabricante | — | No |
| softwaredoit.es/software-de-facturacion (+ /aplicaciones-de-facturacion.html, /software-facturacion-para-autonomos.html) | **Comparador citado por ChatGPT** | varios | **Sí (alta de software)** |
| cronomia.com/software-facturacion y /software/holded/alternativas | **Comparador citado por ChatGPT y AIO** | varios | **Sí** |
| banktrack.com/blog/software-facturacion-espana | Fintech (citada ×2) | varios | Contacto / partnership |
| gocardless.com/es/guias/consejos/5-mejores-programas-de-facturacion… | Pagos (citada) | 5 | Vía integración |
| revolucionatupyme.com/los-mejores-programas-de-facturacion | Blog | — | Contacto |
| softwarepara.net/facturacion-autonomos | Comparador | — | Sí |
| conversoriaecnae.es/herramientas/comparativas/mejores-programas-facturacion-autonomos | Comparador | Quipu, … | Contacto |
| wwwhatsnew.com «Apps para autónomos en España 2026» | Medio tech | Holded, Billin, Quaderno… | Contacto editorial |
| getrenn.com/es/blog/… (gratis, alternativas a Holded, mejor app) | Fabricante pequeño | renn, Contasimple, AEAT, Zoho, Sage… | No, pero sirve de referencia de formato |
| factupro.es/blog/alternativas-holded-autonomos | Fabricante pequeño | 5 | No |
| conavalsi.com/blog/programas-de-facturacion-gratis… | Fintech | — | Contacto |
| facturalia.info/comparativa-mejores-programas-de-facturacion-gratuitos-verifactu | Fabricante | — | No |
| declarando.es/factura-electronica/programas-facturacion-electronica | Asesoría online | — | Contacto |

**[DATO] Facturales no aparece en ninguna de estas listas.**

---

## 3. Señales de entidad (repositorio + web)

### 3.1 Auditoría — [DATO] salvo que se indique otra cosa

| Señal | Estado | Evidencia |
|---|---|---|
| Organization schema | Mínimo: `name`, `url`, `logo` (rombo SVG), `email`. **Sin `sameAs`, `legalName`, `address`, `vatID`, `foundingDate`, `founder` ni `contactPoint`** | `index.html` (JSON-LD 1 de 3) |
| SoftwareApplication | Existe, con `offers` (6.45/11.95/23.95 EUR). Sin `priceValidUntil`, `aggregateRating` (correcto: no hay reseñas reales), `featureList`, `screenshot`, `softwareVersion`, `publisher` ni indicación de IVA | `index.html` |
| FAQPage | Sí, en index, pricing y faq | — |
| Article | 3 artículos con `author` = **Organization «Facturales»**; sin `dateModified` ni autor persona | blog |
| about.html | Texto de propósito y valores; **no dice quién está detrás** (ni razón social, ni NIF, ni domicilio, ni equipo, ni año de fundación); sin schema `AboutPage` | `about.html` |
| Titular legal | **AVENUE DIGITAL GROUP, S.L., NIF B-70829601**, RM Valladolid, tomo 1646, folio 78, hoja VA-34519, domicilio en Calle Plaza Mayor 23, 1A, 47001 Valladolid, info@facturales.es | `/home/user/facturales/src/app/pages/legal/LegalContent.tsx` (líneas 7, 193, 231–236) |
| Aviso legal visible para crawlers | **No.** `app.facturales.es/aviso-legal` devuelve un shell SPA de 6 KB sin el texto; `curl` no encuentra «Avenue» en el HTML | curl 18/10/2026 |
| NAP en la landing | **Ausente.** Ni dirección, ni teléfono, ni razón social en páginas o pie | grep del repo |
| Coherencia legal | Errata «app.factuales.es»; fuero «Juzgados de Madrid» con domicilio en Valladolid; la cláusula 12 dice «Uso responsable de TS FACTURALES»; textos sin tildes | LegalContent.tsx |
| **Cláusula anti-enlaces** | «Se prohíben expresamente enlaces profundos (deep link)… deberán recabar la autorización expresa y por escrito» | LegalContent.tsx l.27 |
| Declaración responsable SIF | Solo hay un párrafo sobre la Ley 11/2021 dentro de las condiciones legales. No identifica producto, versión, componentes, modalidad (VERI\*FACTU / no VERI\*FACTU), fecha ni lugar, que es lo que exigen el RD 1007/2023, la Orden HAC/1177/2024 y la FAQ de la AEAT | LegalContent.tsx l.192–194; [FAQ AEAT](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/certificacion-sistemas-informaticos-declaracion-responsable.html) |
| Cabecera y pie | **Inyectados con `document.write`** desde `assets/js/header-include.js` y `footer-include.js`, sin `<noscript>`. Los bots que no ejecutan JS (en general GPTBot, ClaudeBot, PerplexityBot, CCBot) no ven los enlaces del pie (Empresa, Legal, Ayuda) | `footer-include.js` |
| Perfiles sociales | Ninguno en el pie ni en el schema | `footer-include.js` |
| App Store / Google Play | **No se encontraron fichas públicas** «Facturales», y la landing no enlaza a ninguna tienda | WebSearch + grep (0 enlaces apps.apple/play.google) |
| Capterra / G2 / GetApp / Software Advice / Trustpilot | **No se encontraron fichas** | WebSearch «Facturales opiniones Capterra OR Trustpilot OR G2» |
| LinkedIn / Crunchbase / Wikidata | **No se encontraron** | WebSearch |
| Google Business Profile | No verificable desde aquí. [HIPÓTESIS] No existe. Para un SaaS sin atención presencial es opcional, pero ayuda a consolidar la entidad (categoría «Empresa de software» y domicilio social real) |
| Indexación | Una búsqueda web con `"facturales.es"` no devuelve ninguna página del sitio. [HIPÓTESIS] Hay poca o ninguna indexación en Bing, el índice que usan ChatGPT search y Copilot |
| robots.txt | `User-agent: * / Allow: / / Disallow: /partials/`; sin reglas para bots de IA (implícitamente permitidos) | live + repo |
| llms.txt | **404** | curl |
| 404 en producción | Devuelve la página genérica de Plesk «Server Error» con `lang="en"`, no `404.html` | curl `/llms.txt` |
| Producción frente a repositorio | La meta description en producción («Facturación con VERI\*FACTU, conciliación bancaria…») no coincide con la del repo (la del repo habla de stock, recurrentes y recordatorios). [HIPÓTESIS] El repo tiene cambios sin desplegar | curl frente a `index.html` |
| Servidor | nginx + Plesk (`x-powered-by: PleskLin`) | cabeceras |

### 3.2 VERI\*FACTU: certificación, registros y listados — [DATO]

- **No existe homologación ni certificación de la AEAT.** El productor se «auto-certifica» con una **declaración responsable** y no hay registro previo de los SIF. Debe formar parte del propio producto (opción «Ayuda» o «Acerca de», accesible desde cualquier punto), ser accesible también fuera de él (por ejemplo, en Internet, en formato gratuito y muy extendido) y estar disponible en el momento de la adquisición. **Hace falta una declaración por cada versión**, y la AEAT recomienda mantenerlas publicadas, incluidas las de versiones retiradas. No se exige firma electrónica. Fuente: [AEAT FAQ — declaración responsable](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/certificacion-sistemas-informaticos-declaracion-responsable.html). La AEAT publica ejemplos ([EjemplosDeclaracionResponsable V0.5.1](https://www3.agenciatributaria.gob.es/static_files/Sede/Tema/IVA/Verifactu/EjemplosDeclaracionResponsable(V0.5.1).pdf)).
- **La AEAT no publica una lista de software válido** (TeamSystem lo confirma: [teamsystem.es](https://teamsystem.es/magazine/software-homologado-verifactu/)). Cualquier página que hable de software «homologado» es engañosa. **Esto es un ángulo de contenido y de PR**: explicar el error y publicar la declaración propia.
- **Colaboración social (el único «listado» legítimo cercano):** los desarrolladores de software pueden firmar con la AEAT un **acuerdo de colaboración social** para remitir registros de facturación en representación de sus clientes (contacto: comunicacion.sepri@correo.aeat.es). La representación se acredita con los modelos de la Resolución de 18/12/2024. Fuente: [AEAT FAQ — colaboración social](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/colaboracion-social.html). Holded explota esta condición en contenido citado por AI Overviews.
- **Calendario:**
  - Vigente: RDL 15/2025 → sujetos al Impuesto sobre Sociedades antes del 01/01/2027; resto antes del 01/07/2027 ([AEAT](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html)).
  - **Previsión del 05/10/2026: aplazamiento hasta octubre de 2028**, alineado con la factura electrónica obligatoria para empresarios con facturación ≤ 8 M€. Se mantienen en términos «sustancialmente equivalentes» los requisitos de integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad ([nota del Ministerio de Hacienda](https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf)). **Aún no está aprobado** a fecha de este informe.
- Otros listados legítimos donde aparecer: el **catálogo de Agentes Digitalizadores de Kit Digital (Red.es / Acelera Pyme)**, cuya inscripción, según Red.es, está abierta durante todo el programa. [HIPÓTESIS] Falta verificar si en 2026 hay convocatoria activa para el segmento de software de facturación. También los portales **TIC Negocios de las Cámaras de Comercio** (proveedores evaluados por la cámara) y los **marketplaces de integraciones** de pasarelas o bancos (Stripe Partner Directory si aplica, GoCardless, Qonto).

---

## 4. Estrategia GEO

### 4.1 Base técnica (bloqueante) — [RECOMENDACIÓN]

1. **Cabecera y pie en HTML estático**, sin `document.write`. Como no hay sistema de build, sirven un pequeño script de pre-publicación (Node/Python) que incruste `partials/` en cada `.html`, o un SSI de nginx (`ssi on;` con `<!--# include file="partials/footer.html" -->`). Así el contenido del pie y la navegación llegan a los bots de IA y a Bing.
2. **Aviso legal, privacidad y condiciones en HTML estático** en `facturales.es/legal/aviso-legal.html` (o prerenderizados en la app), con `rel=canonical` y enlace desde el pie. Eliminar la cláusula de enlaces profundos y sustituirla por: «Se permite enlazar a cualquier página de este sitio siempre que no se induzca a error sobre la relación con Facturales».
3. **404 real**: `error_page 404 /404.html;` en nginx/Plesk.
4. **Desplegar** el estado actual del repo (producción va por detrás).
5. **Bing Webmaster Tools**: verificar e importar desde Google Search Console, enviar el sitemap y revisar «AI Performance»/Copilot si está disponible. ChatGPT search, Copilot y DuckDuckGo se apoyan en el índice de Bing.
6. **IndexNow**:
   - Generar una clave y publicarla en `https://facturales.es/<clave>.txt`.
   - En cada despliegue, ejecutar: `curl -X POST https://api.indexnow.org/indexnow -H 'Content-Type: application/json' -d '{"host":"facturales.es","key":"<clave>","keyLocation":"https://facturales.es/<clave>.txt","urlList":[...URLs cambiadas...]}'`.
   - Añadir el `lastmod` real por URL en `sitemap.xml`; hoy todas tienen la misma fecha.

### 4.2 Política de robots para bots de IA — [RECOMENDACIÓN]

Recomendación: **permitir todos los bots de búsqueda y recuperación, y también los de entrenamiento**. En un sitio de marketing de una marca desconocida, ser incluido en datos de entrenamiento y en índices de IA es beneficioso: hay poco que proteger y mucho reconocimiento de marca que ganar.

Propuesta exacta de `robots.txt`:

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
User-agent: Bingbot
Allow: /
User-agent: Googlebot
Allow: /
User-agent: Applebot
Allow: /

# Entrenamiento de modelos (decisión de marca: permitido)
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

Ventajas e inconvenientes:

| Bot | Para qué sirve | Si se bloquea |
|---|---|---|
| OAI-SearchBot / ChatGPT-User | Resultados y citas de ChatGPT search; visitas puntuales a petición del usuario | Desapareces de las citas de ChatGPT. **No bloquear** |
| GPTBot | Entrenamiento de OpenAI | No afecta a las citas, pero reduce el conocimiento «de memoria» del modelo sobre la marca |
| Claude-SearchBot / Claude-User / ClaudeBot | Búsqueda, fetch a petición y entrenamiento de Anthropic | Igual que en OpenAI |
| PerplexityBot / Perplexity-User | Índice y fetch de Perplexity | Perplexity es el motor que más cita (Holded tiene 1.332 citas). **No bloquear** |
| Google-Extended | Entrenamiento/grounding de Gemini (apps Gemini y Vertex). **No controla AI Overviews ni AI Mode**: esos dependen de Googlebot | Bloquearlo apenas protege nada y reduce la presencia en Gemini |
| Applebot-Extended | Entrenamiento de Apple Intelligence | Bajo impacto |
| Bingbot | Bing, Copilot y la base de ChatGPT search | Bloquearlo sería catastrófico |
| CCBot | Common Crawl, que alimenta a muchos LLM | Bajo coste permitirlo |

El inconveniente es que el contenido propio (guías) puede reutilizarse sin clic. En una marca sin notoriedad, la mención con enlace vale más que el clic perdido. La app (`app.facturales.es`) debe seguir con `noindex` en rutas privadas; eso se gestiona en su propio robots.

### 4.3 `llms.txt` — [RECOMENDACIÓN] contenido exacto propuesto

Publicar en `https://facturales.es/llms.txt` (texto plano en Markdown). Antes de publicarlo, **validar cada cifra con la app y con `src/services/plans/plans-config.service.ts`**.

```markdown
# Facturales

> Facturales es un software en la nube de facturación y gestión financiera para autónomos y pymes en España. Reúne facturas y presupuestos con VERI*FACTU, facturas recurrentes, inventario, cobros con recordatorios automáticos, conciliación bancaria por extractos, gastos con justificantes e impuestos trimestrales (modelos 303 y 130). Funciona en navegador (app.facturales.es) y en iOS y Android con la misma cuenta. Datos alojados en la Unión Europea. Lo desarrolla AVENUE DIGITAL GROUP, S.L. (NIF B-70829601, Valladolid, España).

Datos verificados a 18/10/2026. Precios sin IVA.

## Hechos clave
- Qué es: suite financiera para autónomos y pymes en España (facturación + inventario + cobros + bancos + gastos + impuestos).
- Para quién: autónomos (persona física) y pymes que facturan en España.
- Precios (€/mes + IVA, pago mensual / pago anual): Starter 6,45 / 4,95 · Pro 11,95 / 8,95 · Ilimitado 23,95 / 17,95. Prueba de 14 días. Sin permanencia. Descuento por pago anual: hasta −25 %.
- VERI*FACTU: cada factura emitida genera su registro de facturación con huella encadenada y código QR de cotejo. Declaración responsable del productor: https://facturales.es/verifactu-declaracion-responsable.html
- Inventario (desde 17/10/2026): stock por producto, alertas de stock mínimo, movimientos, descuento automático al emitir factura y devolución al anularla. Un solo almacén.
- Facturas recurrentes: se generan como borrador en cada periodo; el usuario las emite.
- Recordatorios de cobro automáticos: calendario configurable, enviados por email desde el servidor.
- Bancos: importación de extractos en Excel/CSV y conciliación. La conexión bancaria directa está «Próximamente» (vía agregador bancario regulado).
- Impuestos: cálculo de los modelos 303 (IVA) y 130 (IRPF pago fraccionado). Facturales no presenta automáticamente los modelos ante la AEAT.
- Formatos: PDF, Facturae.
- Bancos, Cobros, Gastos y Gráficas están en despliegue gradual.

## Limitaciones conocidas
- No hay conexión bancaria directa todavía (solo extractos).
- Inventario con un único almacén.
- No hay plan gratuito permanente; hay prueba de 14 días.
- No hay presentación telemática automática de impuestos.

## Páginas de referencia
- [Facturales en datos (ficha oficial)](https://facturales.es/facturales-en-datos.html): hechos, precios con fecha, funciones y limitaciones.
- [Precios](https://facturales.es/pricing.html)
- [Todas las funciones](https://facturales.es/funciones.html)
- [Preguntas frecuentes](https://facturales.es/faq.html)
- [Guía VERI*FACTU (calendario actualizado)](https://facturales.es/verifactu-2027-guia-autonomos-pymes.html)
- [Factura electrónica vs VERI*FACTU](https://facturales.es/factura-electronica-vs-verifactu.html)
- [Sobre Facturales y datos de empresa](https://facturales.es/about.html)
- [Aviso legal](https://facturales.es/legal/aviso-legal.html)

## Módulos
- [Facturación](https://facturales.es/crea-envia-facturas.html)
- [Presupuestos](https://facturales.es/crea-envia-presupuestos.html)
- [Inventario](https://facturales.es/gestiona-tu-stock.html)
- [Cobros](https://facturales.es/cobros.html)
- [Bancos y conciliación](https://facturales.es/bancos-conciliacion.html)
- [Gastos y justificantes](https://facturales.es/escanea-gastos.html)
- [Impuestos 303 y 130](https://facturales.es/impuestos.html)
- [Panel y gráficas](https://facturales.es/tu-negocio-bajo-control.html)
- [Clientes](https://facturales.es/gestiona-clientes.html)

## Contacto
- General: info@facturales.es · Soporte: soporte@facturales.es
- Registro: https://app.facturales.es/signup · Acceso: https://app.facturales.es/signin

## Optional
- [Blog](https://facturales.es/news-grid.html)
- [Contabilidad en 7 pasos](https://facturales.es/contabilidad-negocio-7-pasos.html)
```

**`llms-full.txt`**: es la concatenación, en Markdown limpio (sin navegación), del contenido de *Facturales en datos*, Precios, FAQ completa, la guía VERI\*FACTU y la declaración responsable. Se regenera en cada despliegue con un script (HTML → Markdown con `pandoc` o `turndown`), con la cabecera «Generado el AAAA-MM-DD a partir de facturales.es». [HIPÓTESIS] El impacto directo de `llms.txt` en las citas es todavía bajo: ningún gran motor ha confirmado que lo use para posicionar. Su coste es mínimo y sirve a agentes y herramientas (IDE, Perplexity fetch).

### 4.4 Páginas «fuente de verdad» — [RECOMENDACIÓN]

1. **`/facturales-en-datos.html`** («Facturales en datos», ficha oficial). Estructura:
   - Párrafo inicial de 40–60 palabras: «Facturales es un software en la nube de facturación y gestión financiera para autónomos y pymes en España, desarrollado por AVENUE DIGITAL GROUP, S.L. (Valladolid). Incluye facturación con VERI\*FACTU, inventario, recurrentes, recordatorios de cobro, conciliación por extractos, gastos e impuestos 303/130. Precios desde 4,95 €/mes + IVA (anual).»
   - Tabla «Ficha técnica»: titular, NIF, domicilio, año de lanzamiento, plataformas, alojamiento UE (indicando proveedor y región si se puede publicar), pagos gestionados con Stripe, idiomas, formatos (PDF, Facturae), modalidad VERI\*FACTU, versión actual del SIF.
   - Tabla de precios **con fecha** («Precios vigentes a 18/10/2026, sin IVA») y límites por plan.
   - Tabla «Qué hace / qué no hace (limitaciones)».
   - Registro de cambios (changelog) con fechas: «17/10/2026: inventario, recurrentes, recordatorios».
   - Enlaces a fuentes oficiales (RD 1007/2023, Orden HAC/1177/2024, nota de Hacienda del 05/10/2026).
   - Bloque «Cómo citar»: «Facturales (facturales.es), software de facturación de AVENUE DIGITAL GROUP, S.L.».
   - Schema `WebPage` + `SoftwareApplication` + `Organization`.
2. **`/verifactu-declaracion-responsable.html`**: declaración responsable por versión siguiendo los ejemplos de la AEAT (nombre del SIF, versión, componentes, si funciona exclusivamente como VERI\*FACTU, productor con NIF y domicilio, fecha y lugar), más el histórico de versiones. Debe aparecer también en la app (Ayuda › Acerca de). Además de ser una obligación legal, **es contenido muy citable** («¿Facturales cumple VERI\*FACTU?»).
3. **Guía VERI\*FACTU actualizada**: cambiar el H1 y la URL canónica a un término atemporal (por ejemplo, `/verifactu-guia.html`, con 301 desde la URL de 2027). Incluir un bloque «Última actualización: 18/10/2026» y la tabla de calendario «vigente (RDL 15/2025) vs previsto (nota de Hacienda del 05/10/2026: octubre de 2028)», con fuentes enlazadas, `dateModified` y una sección «Qué no cambia» (integridad, inalterabilidad…). Debe ir acompañada de una nota de prensa (ver §5).
4. **Comparativas propias** (el formato que hoy citan los LLM): «Alternativas a Holded para autónomos (2026)», «Programa de facturación gratis vs app gratuita de la AEAT vs Facturales», «Facturales vs Quipu», «Facturales vs Billin», «Facturales vs Contasimple». Reglas:
   - tabla comparativa al principio;
   - criterios explícitos;
   - precios de terceros con fecha y enlace a su página oficial;
   - reconocer cuándo otro programa encaja mejor;
   - sin claims inventados;
   - revisión trimestral.
5. **Glosario** (`/glosario/…`) con `DefinedTerm`: huella/hash, registro de facturación, SIF, factura rectificativa, REBU, Facturae, FACe, modelo 303, modelo 130, recargo de equivalencia, conciliación bancaria… El glosario de Billin es su mayor captador de enlaces (definicion-fiador: 323 RD).

### 4.5 Formato citable (para todas las páginas) — [RECOMENDACIÓN]

- Responder a la pregunta en las **primeras 40–60 palabras**, con una frase autocontenida que pueda citarse sin el resto.
- **Un dato por frase, con fecha y fuente** («Según el RD 1007/2023, art. X…»). Enlazar a BOE y AEAT.
- **Tablas HTML reales** (no imágenes) para comparativas, calendarios y precios.
- Encabezados en forma de pregunta (H2/H3) y FAQ al final, con `FAQPage`.
- «Última actualización» visible y `dateModified`.
- Autor persona con credenciales (ver Person) y, si es posible, revisión de un asesor fiscal colegiado («Revisado por …, asesor fiscal, n.º colegiado …»).
- Evitar contenido detrás de pestañas o acordeones que solo se cargan con JS. Los `<details>` nativos sí son legibles.

### 4.6 Schema propuesto — [RECOMENDACIÓN]

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://facturales.es/#org",
      "name": "Facturales",
      "legalName": "AVENUE DIGITAL GROUP, S.L.",
      "vatID": "ESB70829601",
      "taxID": "B70829601",
      "url": "https://facturales.es/",
      "logo": "https://facturales.es/assets/img/logo/logo-color.webp",
      "email": "info@facturales.es",
      "address": {"@type": "PostalAddress", "streetAddress": "Plaza Mayor 23, 1A", "postalCode": "47001", "addressLocality": "Valladolid", "addressRegion": "Castilla y León", "addressCountry": "ES"},
      "contactPoint": [{"@type": "ContactPoint", "contactType": "customer support", "email": "soporte@facturales.es", "availableLanguage": "es"}],
      "areaServed": "ES",
      "sameAs": [
        "https://www.linkedin.com/company/<facturales>",
        "https://www.wikidata.org/wiki/<Qid>",
        "https://apps.apple.com/es/app/<id>",
        "https://play.google.com/store/apps/details?id=<id>",
        "https://www.capterra.es/software/<id>/facturales",
        "https://www.g2.com/products/facturales",
        "https://www.crunchbase.com/organization/facturales",
        "https://www.youtube.com/@facturales"
      ]
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://facturales.es/#app",
      "name": "Facturales",
      "applicationCategory": "BusinessApplication",
      "applicationSubCategory": "Software de facturación",
      "operatingSystem": "Web, iOS, Android",
      "publisher": {"@id": "https://facturales.es/#org"},
      "featureList": ["Facturación con VERI*FACTU", "Facturae", "Facturas recurrentes", "Inventario", "Recordatorios de cobro automáticos", "Conciliación bancaria por extractos", "Gastos con justificantes", "Modelos 303 y 130"],
      "offers": [
        {"@type": "Offer", "name": "Starter (mensual)", "price": "6.45", "priceCurrency": "EUR", "priceValidUntil": "2027-03-31", "valueAddedTaxIncluded": false, "url": "https://facturales.es/pricing.html"}
      ]
    }
  ]
}
```

- Solo se debe incluir en `sameAs` un perfil **cuando exista**.
- **Nunca** añadir `aggregateRating` sin reseñas reales y verificables en la propia página.
- Artículos: `Article`/`BlogPosting` con `author` de tipo `Person` (`name`, `jobTitle`, `url` a una página de autor `/autores/…`, `sameAs` a LinkedIn), `reviewedBy`, `dateModified`, `citation` (URLs de BOE y AEAT) y `about` (`DefinedTerm` VERI\*FACTU).
- Páginas de autor con schema `Person` y `ProfilePage`. El candidato natural es el responsable de producto o fundador; si se puede, sumar un asesor fiscal externo como revisor.
- Glosario: `DefinedTermSet` + `DefinedTerm`.
- Guías paso a paso: `HowTo`. Google ya no muestra resultados enriquecidos HowTo, pero el marcado sigue aportando estructura semántica a los LLM.
- `BreadcrumbList` en todas las páginas y `AboutPage` en about.html.

### 4.7 Seguimiento de menciones en IA (método reproducible) — [RECOMENDACIÓN]

**Set de prompts (30)**: 10 de categoría, 10 de VERI\*FACTU/normativa, 5 de comparación y 5 de marca. Ejemplos:
- «mejor programa de facturación para autónomos en España»
- «software verifactu para autónomos»
- «alternativa a Holded barata»
- «programa de facturación gratis»
- «app para hacer facturas desde el móvil»
- «programa de facturación con control de stock»
- «programa para facturas recurrentes»
- «recordatorios de cobro automáticos facturas»
- «cuándo es obligatorio verifactu»
- «verifactu aplazamiento 2028»
- «qué es la declaración responsable verifactu»
- «Facturales opiniones»
- «qué es Facturales»
- «Facturales vs Quipu»
- …

**Cadencia**: mensual. Motores: ChatGPT (search activado), Perplexity, Gemini, Google AI Overviews/AI Mode y Copilot. Siempre en sesión anónima o limpia, con ubicación España e idioma español.

**Registro** (hoja compartida):
- fecha, motor, prompt;
- ¿menciona Facturales? (sí/no) y posición en la lista;
- ¿cita una URL de facturales.es? ¿cuál?;
- competidores mencionados;
- URLs de las fuentes citadas;
- exactitud de lo que dice de Facturales (correcto / incorrecto / desactualizado).

**Herramientas**:
- **SE Ranking**: el proyecto ya tiene las API AI Search. Conviene crear un proyecto SEV o LLM tracking con el set de prompts y la marca «Facturales» con alias («facturales.es»).
- Alternativas: Peec AI, Otterly, Profound o Ahrefs Brand Radar.
- **Bing Webmaster Tools** (informes de Copilot, si están disponibles) y **GA4** con segmento de referrers `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com` y parámetros `utm_source=chatgpt.com`.

---

## 5. Autoridad y digital PR (sin técnicas penalizables)

### 5.1 Activos enlazables — [RECOMENDACIÓN]

1. **Guía y tracker «Calendario VERI\*FACTU y factura electrónica»**, actualizado con cada cambio normativo y con historial de versiones («VERI\*FACTU: de 2026 a 2028 — cronología de aplazamientos»). Es una noticia viva que medios y gestorías enlazan.
2. **Herramientas gratuitas** (sin registro, en HTML estático):
   - Generador de facturas PDF gratis con los campos obligatorios e IVA/IRPF. Advertir que no es un SIF VERI\*FACTU, para no inducir a error.
   - Calculadora de IVA e IRPF por factura y calculadora del modelo 130.
   - Validador de NIF/CIF/NIE con el algoritmo público de dígito de control; no requiere datos de la AEAT.
   - Validador del código QR VERI\*FACTU que decodifica la URL de cotejo, comprueba el formato y enlaza a la sede de la AEAT. No debe simular la verificación oficial.
   - Calculadora de días de retraso e intereses de demora (Ley 3/2004).
   - Plantillas de factura y presupuesto en Excel/Word: son el mayor captador de enlaces de Holded y Quipu.
3. **Estudio de datos propios: «Barómetro de plazos de cobro de autónomos y pymes»**, con datos agregados y anonimizados de la app (días medios de cobro, porcentaje de facturas vencidas, efecto de los recordatorios). **Solo si es legal**:
   - Base jurídica: revisar si las condiciones y la política de privacidad permiten estadística agregada. Como encargado del tratamiento de los datos de terceros, Facturales **no puede usar los datos de clientes de sus usuarios para fines propios** sin base legal, así que haría falta como mínimo anonimización irreversible, agregación con k-anonimato (por ejemplo, ≥ 50 cuentas por celda) y actualización de la política.
   - Mientras tanto, la alternativa es una **encuesta propia** (≥ 400 respuestas, ficha técnica publicada) a autónomos sobre morosidad y VERI\*FACTU, en colaboración con una asociación (UPTA, ATA o CEAT) para aportar muestra y difusión.
   - Ficha metodológica pública y descarga de los datos en CSV.
   - [HIPÓTESIS] Con el volumen actual de usuarios puede que la muestra no sea suficiente; en ese caso, empezar con la encuesta.
4. **Página de prensa** `/prensa.html`: datos de empresa, logos oficiales, capturas reales «con datos de ejemplo», portavoz con bio y foto, notas de prensa con fecha.

### 5.2 Programa de partners para gestorías y asesorías — [RECOMENDACIÓN]

- Acceso de asesor/gestor a las cuentas de los clientes (si la app lo permite; si no, exportaciones para la gestoría), condiciones para despachos y página `/partners-gestorias.html` con un directorio público de gestorías partner. Cada partner recibe una ficha enlazable y enlaza de vuelta con su «sello partner» (enlace editorial legítimo, no recíproco masivo).
- Contenido co-firmado con asesores fiscales colegiados (E-E-A-T): revisión de guías y webinars VERI\*FACTU.

### 5.3 Reseñas reales (proceso) — [RECOMENDACIÓN]

- Email automático entre 30 y 45 días después de la activación (≥ 5 facturas emitidas), con enlace directo a Capterra/GetApp, G2, Google Play/App Store o Trustpilot, rotando la plataforma.
- **Prohibido**: incentivos condicionados a una reseña positiva, reseñas de empleados o del grupo, o comprarlas (Directiva Ómnibus, Ley General para la Defensa de los Consumidores y Usuarios y políticas de las plataformas).
- Capterra/Gartner permite incentivos neutrales mediante sus propios programas. Responder todas las reseñas, también las negativas.
- No marcar `aggregateRating` en la web hasta que haya reseñas propias verificables.

### 5.4 Lista de 52 objetivos de enlace/mención

Dificultad: B = baja, M = media, A = alta. Prioridad: P1 = 0–3 meses, P2 = 3–6, P3 = 6–12.

| # | Objetivo | Tipo | Dificultad | Táctica | Prioridad |
|---:|---|---|:-:|---|:-:|
| 1 | Capterra España (Gartner) | Directorio de reseñas | B | Ficha de vendedor gratuita, capturas y campaña de reseñas reales | P1 |
| 2 | GetApp / Software Advice | Directorio (Gartner) | B | Se sincroniza con Capterra | P1 |
| 3 | G2 | Directorio de reseñas | B | Ficha gratuita y reseñas | P1 |
| 4 | Trustpilot | Reseñas | B | Perfil verificado e invitaciones automáticas posteriores a la compra (con cuidado con sus normas) | P2 |
| 5 | App Store (ES) | Ficha de app | B | Publicar o optimizar la ficha; enlazar la web y la política de privacidad; enlazar la ficha desde la landing | P1 |
| 6 | Google Play | Ficha de app | B | Ídem | P1 |
| 7 | LinkedIn Company Page | Perfil de entidad | B | Página con web, sede y sector; fundador vinculado | P1 |
| 8 | Wikidata | Entidad | M | Item «Facturales» (instancia de: software; desarrollador: AVENUE DIGITAL GROUP, S.L.; web oficial; país). Requiere referencias: registro mercantil y una mención independiente en prensa | P2 |
| 9 | Crunchbase | Directorio de empresas | B | Perfil gratuito | P1 |
| 10 | Product Hunt | Lanzamiento | M | Lanzamiento del inventario o de la herramienta gratuita, en inglés y español | P2 |
| 11 | softwaredoit.es | Comparador (citado por ChatGPT) | B–M | Alta de software y solicitud de inclusión en «software de facturación para autónomos» | P1 |
| 12 | cronomia.com | Comparador (citado por ChatGPT y AIO) | B–M | Alta y solicitud para «alternativas a Holded» | P1 |
| 13 | comparasoft.es | Comparador | B | Alta | P1 |
| 14 | softwarepara.net | Comparador | B | Contacto | P1 |
| 15 | conversoriaecnae.es | Comparador | B | Contacto con datos y precios con fecha | P2 |
| 16 | banktrack.com/blog | Fintech (citada) | M | Proponer inclusión; partnership de conciliación cuando llegue la conexión bancaria | P2 |
| 17 | gocardless.com/es/guias | Pagos (citada) | M | Vía integración o partnership, si se integra | P3 |
| 18 | revolucionatupyme.com | Blog (citado) | B–M | Pitch con ficha y acceso de prueba | P1 |
| 19 | economia3.com | Medio regional | M | Pitch: «nueva alternativa española con VERI\*FACTU e inventario» | P2 |
| 20 | rankiabusiness.com / rankia.com | Medio / comunidad | M | Pitch y respuestas expertas en el foro (sin spam) | P2 |
| 21 | youasesoria.com | Asesoría (lista «mejores programas») | M | Partnership con gestorías | P2 |
| 22 | declarando.es | Asesoría online | M | Pitch / partnership | P3 |
| 23 | wwwhatsnew.com | Medio tech | M | Pitch para la actualización de «Apps para autónomos 2026» | P2 |
| 24 | Infoautónomos | Referente para autónomos | A | Artículo invitado de un experto en VERI\*FACTU; patrocinio de la guía; ojo: tiene vínculo comercial con Contasimple | P3 |
| 25 | autonomosyemprendedor.es | Medio autónomos | M | Nota de prensa sobre el aplazamiento de VERI\*FACTU con el análisis de Facturales y su portavoz | P1 |
| 26 | emprendedores.es | Medio pymes | M–A | Datos propios (barómetro o encuesta) y portavoz experto | P2 |
| 27 | pymesyautonomos.com (Webedia) | Medio | M | Pitch de datos o herramienta | P2 |
| 28 | cepymenews.es | Medio pymes | M | Nota de prensa y tribuna | P1 |
| 29 | Cinco Días (El País) | Medio económico | A | Datos del barómetro de cobros; reacción experta a cambios normativos | P3 |
| 30 | El Economista (Autónomos / Pymes) | Medio | A | Ídem | P3 |
| 31 | Expansión (Pymes / Emprendedores) | Medio | A | Ídem | P3 |
| 32 | Xataka / Genbeta | Medio tech | A | Herramienta gratuita (validador de QR VERI\*FACTU) como gancho | P3 |
| 33 | castillayleoneconomica.es | Medio regional CyL | B–M | Ángulo local: «startup vallisoletana» | P1 |
| 34 | El Norte de Castilla / Diario de Valladolid | Prensa local | M | Historia de empresa local, empleo, lanzamiento | P2 |
| 35 | Cámara de Comercio de Valladolid | Cámara | M | Alta como proveedor tecnológico, jornadas VERI\*FACTU | P1 |
| 36 | Portales TIC Negocios (Cámaras de Madrid, Alicante, Murcia, Zaragoza…) | Cámaras | M | Solicitar evaluación como proveedor (Holded ya está) | P2 |
| 37 | UPTA (uptaemprende.es) | Asociación de autónomos | M | Convenio de ventajas para socios y webinar VERI\*FACTU | P2 |
| 38 | ATA (Federación Nacional de Asociaciones de Trabajadores Autónomos) | Asociación | A | Convenio y encuesta conjunta | P3 |
| 39 | CEAT (ceat.org.es) | Asociación | M | Convenio (Anfix ya está) | P2 |
| 40 | CEA / Club de Emprendedores (Andalucía), CECALE (CyL) | Confederaciones | M | Catálogo de ventajas para socios | P2 |
| 41 | Colegios de gestores administrativos / asesores fiscales (por ejemplo, Colegio de Gestores de Valladolid, AEDAF, REAF-CGE) | Colegios profesionales | A | Acuerdo de formación y patrocinio de jornadas VERI\*FACTU | P3 |
| 42 | Red.es — catálogo de Agentes Digitalizadores (Kit Digital / Acelera Pyme) | Programa público | M | Adhesión si hay convocatoria activa (verificar) | P2 |
| 43 | Oficinas Acelera Pyme (cámaras e itecam) | Programa público | M | Recursos o webinars VERI\*FACTU | P3 |
| 44 | AEAT — acuerdo de colaboración social | Institucional | M–A | Solicitarlo si Facturales va a remitir registros en nombre de clientes (VERI\*FACTU). No es un enlace, pero sí una mención legítima y citable | P2 |
| 45 | ENISA / ICEX / ICE Castilla y León | Financiación pública | A | Solo si se pide financiación; las fichas de empresas financiadas a veces enlazan | P3 |
| 46 | elreferente.es / startupxplore.com / startups-espanolas.es | Directorios de startups | B | Alta gratuita | P1 |
| 47 | Stripe (directorio de partners), Qonto, Shopify App Store | Marketplaces de integraciones | M–A | Construir la integración y su ficha (Qonto y Shopify enlazan a Holded, Billin y Quipu) | P3 |
| 48 | Universidades (Universidad de Valladolid, Lanzadera UVa, escuelas de negocio) | Educación | M | Licencias gratuitas para emprendedores universitarios, talleres de facturación | P3 |
| 49 | Podcasts (por ejemplo, programas sobre autónomos y emprendimiento en iVoox/Spotify) | Audio | M | Portavoz experto en VERI\*FACTU y morosidad | P2 |
| 50 | Plataformas de periodistas que buscan fuentes (equivalentes españoles de HARO: perfiles de portavoz en servicios de PR, avisos de periodistas en LinkedIn/X con «#periodistas busco fuente», Qwoted/Featured en inglés) | Mención en medios | M | Responder solo con valor experto y datos verificables | P2 |
| 51 | YouTube (canal propio) | Vídeo (citado por AIO) | M | Tutoriales «cómo emitir una factura VERI\*FACTU», «qué es el QR VERI\*FACTU». AIO cita mucho YouTube | P1 |
| 52 | Reddit r/askspain, r/SpainFIRE / foros (plangeneralcontable, bandaancha) | Comunidad | M | Participación transparente con la identidad de la empresa; nada de astroturfing | P3 |

**Qué no hacer** (riesgo de penalización o de reputación):
- comprar enlaces en redes de prensa regional sin marcar `rel="sponsored"`;
- PBN, directorios masivos o intercambios recíprocos;
- reseñas falsas o incentivadas a favor;
- notas de prensa con claims no verificables (clientes, valoraciones, «homologado por Hacienda»);
- añadir «sin tarjeta», «−30 %» o la presentación automática a la AEAT, que contradicen las reglas de marca.

---

## 6. KPIs

| KPI | Línea base (18/10/2026) | Objetivo a 6 meses | Objetivo a 12 meses | Fuente / método |
|---|---|---|---|---|
| Dominios referentes (no del grupo, dofollow) | 0 (1 del grupo) | 40 | 120 | SE Ranking `getBacklinksSummary` (mensual) |
| Domain InLink Rank | 6 | 20 | 30 | SE Ranking |
| RD de medios o instituciones españolas (DIR ≥ 50) | 0 | 8 | 25 | SE Ranking, filtro |
| Cobertura del link gap (dominios de la lista §1.3 conseguidos) | 0 / 40 | 10 | 20 | Hoja de seguimiento |
| Share of voice en IA (leaderboard SE Ranking, 10 competidores) | 0 % | 0,5 % | 2 % | `getAiSearchLeaderboard` |
| Link presence (citas a facturales.es en respuestas IA, ES) | 0 | 25 | 150 | `getAiSearchOverview` / `PromptsByTarget` |
| Brand presence (prompts que mencionan Facturales) | sin datos | 10 | 60 | `getAiSearchOverview` (marca «Facturales») |
| Tasa de mención en el set propio de 30 prompts × 5 motores | 0 / 150 | 10 / 150 | 30 / 150 | Registro manual mensual (§4.7) |
| Exactitud de lo que dicen los LLM sobre Facturales | n/d | ≥ 90 % correcto | ≥ 95 % | Registro manual |
| Inclusión en comparativas de terceros «mejores programas 2026/2027» | 0 | 5 | 12 | Hoja de seguimiento |
| Reseñas verificadas (Capterra + G2 + tiendas) | 0 | 25 | 80 | Plataformas |
| Búsquedas de marca («facturales», «facturales opiniones») | medir | +100 % | +300 % | GSC (consultas de marca), Bing WMT, Google Trends |
| Tráfico de referencia desde IA (chatgpt.com, perplexity.ai, gemini, copilot) | medir | 100 visitas/mes | 500/mes | GA4, segmento de referrer |
| Páginas indexadas en Bing | medir | 100 % del sitemap | 100 % | Bing Webmaster Tools |
| Menciones de marca sin enlace (prensa y web) | 0 | 15 | 50 | Google Alerts, Talkwalker Alerts y búsqueda de menciones de SE Ranking |
| Perfiles de entidad completos (LinkedIn, Wikidata, Crunchbase, tiendas, Capterra, G2) | 0 / 7 | 6 / 7 | 7 / 7 | Checklist con `sameAs` |

---

## 7. Plan de 90 días (orden recomendado)

**Semanas 1–2:**
- cabecera y pie en HTML estático; legales en HTML en facturales.es; quitar la cláusula de enlaces profundos y corregir erratas y fuero;
- 404 real;
- desplegar el repo;
- `robots.txt` y `llms.txt`;
- Organization y SoftwareApplication completos;
- Bing WMT + IndexNow.

**Semanas 2–4:**
- guía VERI\*FACTU con el aplazamiento a 2028 (y nota de prensa a autonomosyemprendedor.es, cepymenews.es y castillayleoneconomica.es);
- página de declaración responsable;
- «Facturales en datos»;
- LinkedIn, Crunchbase, Capterra/GetApp, G2 y fichas de tiendas;
- página de prensa.

**Mes 2:**
- comparativas «Alternativas a Holded» y «Gratis vs AEAT vs Facturales»;
- alta en softwaredoit, cronomia, comparasoft, softwarepara y directorios de startups;
- primera herramienta gratuita (calculadora de IVA/IRPF o validador de NIF);
- inicio del registro mensual de prompts.

**Mes 3:**
- encuesta con una asociación;
- programa de partners para gestorías;
- Cámara de Valladolid y TIC Negocios;
- Wikidata, cuando haya al menos una fuente independiente;
- canal de YouTube con 3 tutoriales;
- primera revisión de KPIs.

---

### Anexo A — Fuentes principales

- SE Ranking API: `getBacklinksSummary`, `getBacklinksRefDomains` (1.500 dominios por competidor con mayor DIR), `getAiSearchLeaderboard`, `getAiSearchPromptsByBrand` (ChatGPT, Perplexity, AI Overviews; ES; datos de 2026-10-01).
- AEAT, página VERI\*FACTU: https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html
- AEAT, FAQ de declaración responsable: https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/certificacion-sistemas-informaticos-declaracion-responsable.html
- AEAT, FAQ de colaboración social: https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/colaboracion-social.html
- AEAT, nota sobre la ampliación de plazos (RDL 15/2025): https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html
- Ministerio de Hacienda, nota del 05/10/2026 (previsión de aplazamiento a octubre de 2028): https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf
- AEAT, ejemplos de declaración responsable: https://www3.agenciatributaria.gob.es/static_files/Sede/Tema/IVA/Verifactu/EjemplosDeclaracionResponsable(V0.5.1).pdf
- TeamSystem, «Software homologado para VeriFactu»: https://teamsystem.es/magazine/software-homologado-verifactu/
- Comparativas: las URLs de §2.2 y §2.3.
- Repositorios: `/home/user/facturales-landing/index.html`, `about.html`, `assets/js/footer-include.js`, `robots.txt`, `sitemap.xml`; `/home/user/facturales/src/app/pages/legal/LegalContent.tsx`.
- Datos brutos del link gap: `[scratchpad de la auditoría, no versionado]/linkgap_raw.tsv`.

### Anexo B — Limitaciones

- Las métricas de SE Ranking son estimaciones del propio índice de SE Ranking y no equivalen a DA (Moz) ni a DR (Ahrefs).
- La muestra del link gap se limita a los 1.500 dominios con mayor DIR por competidor.
- WebSearch tiene sesgo de EE. UU. La ausencia de fichas de Facturales en tiendas y directorios se basa en búsquedas web y debe confirmarse a mano, sobre todo las apps iOS/Android, que según el briefing existen.
- No se ha tenido acceso a Google Search Console, Bing ni GA4.
