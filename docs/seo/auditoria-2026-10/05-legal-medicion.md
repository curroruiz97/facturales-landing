# 05 — SEO legal/fiscal (YMYL) y plan de medición · Facturales

**Fecha del informe:** 18/10/2026 · **Alcance:** facturales.es (landing estática) + app.facturales.es (repo `/home/user/facturales`). No se ha modificado ningún archivo de repositorio.

**Leyenda de cada afirmación**
- **[DATO]**: comprobado en fuente primaria, con URL y fecha de consulta (18/10/2026 salvo que se indique otra).
- **[DATO-2ª]**: comprobado solo en fuente secundaria fiable. Hay que confirmarlo en fuente primaria antes de publicarlo.
- **[HIPÓTESIS]**: inferencia o previsión, con su razonamiento.
- **[RECOMENDACIÓN]**: acción propuesta.

Estados normativos: **VIGENTE** · **APROBADO, PENDIENTE DE APLICACIÓN** · **PREVISTO / ANUNCIADO** (sin norma en BOE).

---

## 0. Resumen ejecutivo

1. **Cambio de calendario de VERI*FACTU anunciado el 5/10/2026 (PREVISTO).** El Ministerio de Hacienda anunció que las obligaciones pendientes del RD 1007/2023 se aplazan «hasta octubre de 2028», para que coincidan con la factura electrónica B2B de las empresas que facturan menos de 8 M€. **Todavía no hay norma en el BOE.** Los plazos vigentes siguen siendo 1/1/2027 para los contribuyentes del IS y 1/7/2027 para el resto. La web no menciona este anuncio, y la guía se titula «VERI*FACTU en 2027».
2. **La factura electrónica B2B ya tiene reglamento y orden ministerial (APROBADO, PENDIENTE DE APLICACIÓN).**
   - RD 238/2026, de 25 de marzo (BOE 31/03/2026).
   - Orden HAC/1028/2026, de 2 de octubre (BOE 05/10/2026), en vigor desde el 06/10/2026. Con ella empiezan a contar los plazos: unos 12 meses para quienes facturan más de 8 M€ (≈ octubre de 2027) y 24 meses para el resto (≈ octubre de 2028).
   - El artículo `factura-electronica-vs-verifactu.html` sigue diciendo que «su efectividad depende del desarrollo reglamentario». **Está desactualizado.**
3. **Riesgo grave de copy: la web describe un cumplimiento VERI*FACTU que la app todavía no tiene.**
   - El código y la declaración responsable de la app muestran cuatro carencias:
     - **No hay remisión a la AEAT:** los registros se quedan en `estado_envio='pendiente'`.
     - **Faltan el XML conforme a la Orden HAC/1177/2024 y el registro de anulación.**
     - **La declaración responsable no está firmada.** El documento interno pide expresamente no firmarla todavía.
     - **El registro solo se genera si el usuario activa `verifactu_enabled`.**
   - Pese a eso, la web afirma en más de 10 sitios que «cada factura emitida genera su registro VERI*FACTU» y lleva el «QR de cotejo».
   - Además, la app codifica en el QR la URL de cotejo de la modalidad **VERI*FACTU** (`ValidarQR`) y muestra la leyenda «Factura verificable en la sede electrónica de la AEAT». Sin remisión, ese QR no encontrará el registro en la AEAT.
4. **Analítica: no hay nada medido.**
   - La landing no tiene GA4, GTM, Search Console por meta, ni banner de cookies.
   - La app tampoco tiene GA4, eventos de alta ni captura de UTM o referrer en el registro.
   - La política de cookies de la app es una plantilla genérica: declara cookies analíticas y publicitarias que no existen y remite a la «configuración del navegador». Eso no cumple la Guía de cookies de la AEPD (2023).

---

# PARTE A — SEO legal y financiero (YMYL)

## A1. VERI*FACTU / Reglamento de Sistemas Informáticos de Facturación (SIF)

### A1.1 Marco normativo [DATO]

| Norma | Contenido | Estado | Fuente |
|---|---|---|---|
| Ley 58/2003 LGT, art. 29.2.j) (redacción Ley 11/2021) | Obligación de que el software de facturación garantice integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad. Prohíbe el software de «doble uso». | VIGENTE (desde 11/10/2021) | https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html (normativa citada en la página, actualizada a 14/10/2026) |
| LGT art. 201 bis | Infracción por fabricar, comercializar o tener SIF no conformes | VIGENTE | ídem |
| RD 1007/2023, de 5 de diciembre (Reglamento SIF) | Requisitos de los SIF, registros de facturación, modalidades VERI*FACTU y no VERI*FACTU | VIGENTE. Última modificación publicada el 03/12/2025 | https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 |
| Orden HAC/1177/2024, de 17 de octubre | Especificaciones técnicas (registro, huella, QR, XML, servicios web, declaración responsable) | VIGENTE | https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138 |
| RD 254/2025, de 1 de abril (BOE 02/04/2025) | Primer aplazamiento: 1/1/2026 (IS) y 1/7/2026 (resto) | Superado por el RD-ley 15/2025 | https://www.boe.es/buscar/doc.php?id=BOE-A-2025-6600 |
| **RD-ley 15/2025, de 2 de diciembre** (BOE núm. 290, 03/12/2025; en vigor 04/12/2025; convalidado por el Congreso el 11/12/2025 [DATO-2ª]) | Disposición final 1.ª: nueva DF 4.ª del RD 1007/2023 | **VIGENTE** | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-24446 |
| **Nota de prensa del Ministerio de Hacienda, 05/10/2026** | «Aplazamiento de las obligaciones pendientes de aplicación del RD 1007/2023 hasta octubre de 2028», alineado con la factura electrónica de quienes facturan ≤ 8 M€ | **PREVISTO** (no publicado en BOE a 18/10/2026) | https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf (PDF creado el 05/10/2026). La sede AEAT lo recoge como «Previsión de ampliación del plazo» |

**Texto de la nota de Hacienda del 5/10/2026** [DATO]:
- Dice: «proceder al aplazamiento de las obligaciones pendientes de aplicación del Real Decreto 1007/2023 […] hasta octubre de 2028, para hacerlas coincidir con la obligatoriedad de la factura electrónica para empresarios y profesionales cuya facturación anual no supere los 8 millones de euros».
- Anuncia una modificación posterior para «la convergencia de los ámbitos de aplicación y ciertos aspectos técnicos […] teniendo en cuenta los futuros requisitos de reporte digital derivados de ViDA».
- Mantiene «en términos sustancialmente equivalentes» las exigencias de integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad.

**[HIPÓTESIS] Ambigüedades de la nota:**
- No dice expresamente si los contribuyentes del IS con más de 8 M€ también pasan a octubre de 2028. La redacción («las obligaciones pendientes») sugiere un aplazamiento general.
- No indica el vehículo normativo (real decreto o real decreto-ley).
- Hasta que salga en el BOE, la web debe presentarlo como «anunciado».
- Fuentes secundarias del 6 al 13/10/2026 coinciden en que no está publicado: https://www.afiris.es/verifactu-aplazamiento/ y https://www.xn--serviciospeas-skb.com/2026/10/13/anuncian-nuevo-aplazamiento-de-verifactu-hasta-2028-pero-cuidado-que-aun-no-esta-aprobado/

### A1.2 Fechas de obligatoriedad

| Sujeto | Plazo VIGENTE (DF 4.ª RD 1007/2023, redacción RD-ley 15/2025) | PREVISTO (nota 05/10/2026) |
|---|---|---|
| Contribuyentes del IS (art. 3.1.a) | Sistemas adaptados **antes del 1/1/2027** | Octubre de 2028 (pendiente de confirmar también para > 8 M€) |
| Resto de obligados del art. 3.1: autónomos en IRPF, no residentes con EP, entidades en atribución de rentas | Sistemas operativos **antes del 1/7/2027** | Octubre de 2028 |
| Productores y comercializadores de SIF (art. 3.2) | **Nueve meses desde la entrada en vigor de la Orden HAC/1177/2024** (en vigor 18/10/2024), es decir, **29/07/2025**. No se ha aplazado. | El anuncio no lo menciona |
| Servicio de recepción de la AEAT | Mismo plazo de nueve meses (operativo) | — |

Fuente: https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 (DF 4.ª consolidada).
[DATO-2ª] La fecha de 29/07/2025 para productores la citan varias asesorías y la propia AEAT en sus FAQ.

### A1.3 Quién está obligado y quién no

| Supuesto | Situación | Fuente |
|---|---|---|
| IS, IRPF con actividad económica, IRNR con EP y entidades en atribución de rentas que usen un SIF (aunque sea para parte de su actividad) | Obligados | RD 1007/2023, art. 3.1 [DATO] |
| Quienes llevan los libros por **SII** (art. 62.6 RIVA) | **Excluidos** | RD 1007/2023, art. 3.3 [DATO] |
| Facturación íntegramente manual (sin SIF) | No les aplica, porque el reglamento regula sistemas informáticos | art. 1-3 [DATO] |
| Operaciones de las DA 3.ª y 6.ª del RD 1619/2012, operaciones documentadas por EP en el extranjero, y facturación por destinatario o tercero cuando estos lleven SII | Excluidas (art. 4) | [DATO] |
| País Vasco (TicketBAI en Álava, Gipuzkoa y Bizkaia; en Bizkaia, «Batuz/LROE») | Fuera del Reglamento estatal: aplica su normativa foral | [DATO-2ª] Hay que verificarlo en las FAQ de la AEAT y en batuz.eus / ticketbai.eus |
| Navarra | Régimen foral propio, fuera del RD estatal | [DATO-2ª]. [RECOMENDACIÓN] Antes de publicar, verificar si Navarra ha aprobado su propio sistema y en qué fechas |
| Canarias, Ceuta y Melilla | **Sí obligados**: el reglamento es estatal y no depende del IVA; en el registro figura IGIC o IPSI | [DATO-2ª] (FAQ AEAT citada por getquipu.com/blog/verifactu-canarias) |
| Recargo de equivalencia y módulos | **No hay exclusión subjetiva.** Están obligados si expiden facturas (completas o simplificadas) con un SIF. Muchos minoristas en recargo de equivalencia apenas facturan, pero si usan TPV o software para emitir tickets o facturas, ese sistema debe cumplir. | [HIPÓTESIS sólida] Se deduce de los arts. 3 y 4, que no los excluyen. Confirmar con las FAQ de la AEAT y con un asesor |

**Sobre la «regla de los 4 NO»** (`verifactu-2027-guia-autonomos-pymes.html:72`): la usan medios y asesorías, pero no he localizado el documento oficial de la AEAT que la formule. [RECOMENDACIÓN] Citar la fuente concreta (folleto o FAQ de la AEAT) o reformular como «En resumen, estás dentro si…».

### A1.4 Modalidades y requisitos técnicos [DATO]

- **VERI*FACTU** (sistemas de emisión de facturas verificables): el SIF remite automáticamente a la AEAT cada registro de facturación. Con esta modalidad no son obligatorios algunos requisitos, como el registro de eventos y la firma electrónica de los registros.
- **NO VERI*FACTU**: los registros se conservan en el propio sistema con firma electrónica, registro de eventos y obligación de entregarlos a la AEAT si los requiere.
- **Comunes a ambas:**
  - Registro de facturación de alta o anulación, generado de forma simultánea o inmediatamente anterior a la expedición.
  - **Huella (hash SHA-256) encadenada** con el registro anterior.
  - **Código QR obligatorio en todas las facturas, sea cual sea la modalidad.**
  - Identificación del sistema y **declaración responsable del productor** (art. 13 RD 1007/2023; art. 15 Orden HAC/1177/2024), accesible desde el propio sistema.
- **La leyenda «VERI*FACTU» o «Factura verificable en la sede electrónica de la AEAT» solo puede figurar en sistemas que operan en modalidad VERI*FACTU**, es decir, que remiten los registros. Fuente: FAQ AEAT https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes.html (FAQ actualizadas a 21/07/2026, según la página principal).
- **Periodo voluntario** [DATO, AEAT nota RD-ley 15/2025]: hasta las fechas de obligatoriedad se puede dejar de remitir registros con un SIF VERI*FACTU y usar otros SIF.

### A1.5 Sanciones (LGT art. 201 bis) [DATO, Ley 11/2021]

- **Productores y comercializadores:** 150.000 € por cada ejercicio y por cada tipo de sistema no conforme o sin la certificación (declaración responsable) exigida.
- **Usuarios (tenencia de un SIF no conforme o alterado):** 50.000 € por ejercicio.

### A1.6 Lo que hace hoy la app Facturales (repo `/home/user/facturales`) [DATO, código]

| Elemento | Estado | Evidencia |
|---|---|---|
| Modalidad declarada | **VERI*FACTU** (con remisión) | `docs/declaracion-responsable-fabricante.md:28` |
| Declaración responsable | **Borrador, «NO FIRMAR TODAVÍA»**, sin versión de software | `docs/declaracion-responsable-fabricante.md:3-10, 27` |
| Registro de alta con huella SHA-256 encadenada | Hecho | `supabase/functions/emit-invoice-verifactu/index.ts:1-12`, `supabase/migrations/20260602000000_create_verifactu_registros.sql` |
| Generación del registro | **Solo si el usuario activa `verifactu_enabled`** | `src/features/invoices/adapters/invoices.adapter.ts:257-269` |
| Registro de anulación | «Pendiente de despliegue» según la checklist, aunque existe la función `anular-invoice-verifactu` | `docs/declaracion-responsable-fabricante.md:72` |
| XML conforme a la Orden HAC/1177/2024 | **Pendiente** | ídem:73 |
| **Remisión a la AEAT** | **Pendiente**: requiere certificado y alta como colaborador social Tipo 017. Los registros quedan en `estado_envio='pendiente'` | `emit-invoice-verifactu/index.ts:10-11`; migración `...create_verifactu_registros.sql:39` |
| QR | Usa la URL de cotejo **VERI*FACTU** (`/wlpl/TIKE-CONT/ValidarQR`) | `src/domain/rules/fiscal/verifactu-qr.ts:18-21` |
| Leyenda | «Factura verificable en la sede electrónica de la AEAT». En la vista previa nueva se añade el aviso «la validación se activará al completar el alta como colaborador» | `src/features/invoices/pages/VistaPreviaFacturaVg.tsx:200`, `InvoicePreviewPage.tsx:204` |

**Conclusiones:**
- Hoy la app **no** cumple la modalidad VERI*FACTU, porque no remite.
- Tampoco cumple la modalidad NO VERI*FACTU, porque no firma los registros ni tiene registro de eventos.
- Imprimir un QR VERI*FACTU con la leyenda «verificable» sin haber remitido el registro **es contrario a la Orden HAC/1177/2024**: el destinatario que lo escanee no encontrará la factura en la AEAT.
- Para los usuarios aún no es sancionable, porque están en periodo voluntario hasta 2027 (o 2028).
- **Para el productor, el plazo venció el 29/07/2025.** Comercializar el SIF como adaptado sin declaración responsable firmada expone a la sanción del art. 201 bis (150.000 €).
- [RECOMENDACIÓN] Revisión urgente por asesor fiscal o abogado tributario. Hay que decidir entre:
  - (a) completar la remisión y firmar la declaración, o
  - (b) desactivar la leyenda y el QR VERI*FACTU hasta que la remisión funcione, y comunicar el producto como «preparándose para VERI*FACTU».

---

## A2. Factura electrónica B2B obligatoria y ViDA

### A2.1 Normativa española [DATO]

| Norma | Contenido | Estado | Fuente |
|---|---|---|---|
| Ley 18/2022 «Crea y Crece», art. 12, que modifica el art. 2 bis de la Ley 56/2007 | Obligación de expedir, remitir y recibir factura electrónica B2B e informar de los estados | VIGENTE, con aplicación diferida | Preámbulo de la Orden HAC/1028/2026 |
| Ley 7/2024, que añade la DA 21.ª a la Ley 56/2007 | Solución pública de facturación electrónica de la AEAT: gratuita, con funciones de emisión e interconexión, y **repositorio universal obligatorio** | VIGENTE | ídem |
| **RD 238/2026, de 25 de marzo** (BOE 31/03/2026, BOE-A-2026-7295; en vigor a los 20 días) | Reglamento B2B. También modifica el RD 1619/2012 | **APROBADO, PENDIENTE DE APLICACIÓN** | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-7295 · Nota AEAT: https://www3.agenciatributaria.gob.es/static_files/Sede/Actualidad/Novedades/2026/Nota_informativa_RD_Facturacion.pdf · Noticia AEAT del 31/03/2026: https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/marzo/31/facturacion-electronica-obligatoria.html |
| **Orden HAC/1028/2026, de 2 de octubre** (BOE núm. 247, 05/10/2026, BOE-A-2026-20587; **en vigor el 06/10/2026**) | Regula la solución pública. Su entrada en vigor **inicia el cómputo de los plazos** | **VIGENTE** (la orden). Las obligaciones B2B se aplican según el calendario siguiente | https://www.boe.es/buscar/act.php?id=BOE-A-2026-20587 |

**Calendario de aplicación** (DF 4.ª del RD 238/2026 y DF única de la Orden HAC/1028/2026):

| Colectivo | Plazo legal | Fecha estimada [HIPÓTESIS de cómputo: 12 o 24 meses desde el 06/10/2026] |
|---|---|---|
| Volumen de operaciones > 8 M€ en el año anterior | 12 meses desde la entrada en vigor de la orden | **≈ 6 de octubre de 2027**. Durante los primeros 12 meses deben acompañar cada factura con un PDF legible, salvo que el destinatario acepte el formato |
| Resto de empresarios y profesionales | 24 meses | **≈ 6 de octubre de 2028** |
| Obligación de informar de estados para personas físicas y entidades en atribución de rentas ≤ 8 M€ | 12 meses más (unos 36 meses desde la orden) | **≈ octubre de 2029** |
| Plataformas privadas de intercambio | 12 meses | ≈ octubre de 2027 |
| Solución pública de la AEAT disponible | Al menos 2 meses antes de la primera aplicación | ≈ antes de agosto de 2027 |

[RECOMENDACIÓN] Publicar «octubre de 2027» y «octubre de 2028», no el día exacto, hasta que la AEAT publique la fecha concreta en su sede.

**Contenido técnico** [DATO, RD 238/2026 art. 7 y Orden HAC/1028/2026]:
- **Sintaxis admitidas entre plataformas privadas:** UBL, UN/CEFACT CII, EDIFACT y Facturae, todas conforme al modelo semántico **EN 16931**. Las plataformas deben poder transformar entre ellas. Peppol BIS se considera válido porque es UBL.
- **La solución pública trabaja en UBL** (EN 16931).
- **Si no se emite por la solución pública, la plataforma o el sistema del emisor debe remitir «simultáneamente a su emisión una copia electrónica fiel» en UBL a la solución pública** (Orden, art. 4).
- **Estados que debe comunicar el destinatario:** rechazo, fecha de pago efectivo completo y fecha de vencimiento (art. 7). Puede informar además de la recepción de mercancías o servicios. Si no rechaza, la factura se presume aceptada.
- **El emisor puede comunicar** cobro, impago o discrepancias. Todo esto sirve para monitorizar la morosidad (Ley 3/2004).
- **Exclusiones:**
  - Facturas simplificadas (salvo las «cualificadas» del art. 7.2 del RD 1619/2012).
  - Operaciones con consumidores, que no son B2B.
  - Destinatarios no establecidos en España.
  - Mercado eléctrico y de gas organizado, y la compensación de IATA (DA 2.ª).
  - Otras que se excluyan por orden ministerial.
- **Relación con VERI*FACTU:** el RD 238/2026 no menciona VERI*FACTU. La nota de Hacienda del 05/10/2026 anuncia la «convergencia» de ambos regímenes (PREVISTO).

### A2.2 Unión Europea — ViDA [DATO]

- **Directiva (UE) 2025/516 del Consejo, de 11 de marzo de 2025** («IVA en la era digital»; DO de 25/03/2025; en vigor 14/04/2025). Paquete completado con el Reglamento (UE) 2025/517 y el Reglamento de Ejecución 2025/518. Fuente: https://eur-lex.europa.eu/eli/dir/2025/516/oj
- Desde la entrada en vigor, los Estados miembros pueden imponer la factura electrónica nacional sin pedir autorización a la UE.
- **1 de julio de 2030:** factura electrónica estructurada (EN 16931) y **reporte digital casi en tiempo real** obligatorios en las operaciones B2B intracomunitarias. Sustituye a la declaración recapitulativa (modelo 349) para esas operaciones.
- Los sistemas nacionales deberán converger antes de 2035 [DATO-2ª: eumonitor.eu].

---

## A3. Temas fiscales evergreen (estado en octubre de 2026)

| Tema | Estado / dato | Fuente |
|---|---|---|
| **Tipos de IVA** | 21 % general, 10 % reducido, 4 % superreducido (Ley 37/1992, arts. 90-91). IGIC en Canarias (7 % general) e IPSI en Ceuta y Melilla | LIVA (BOE). [RECOMENDACIÓN] Revisar cada enero las medidas temporales de la Ley de PGE o de los RD-ley |
| **Retención de IRPF en facturas de profesionales** | 15 % general. **7 % el año de inicio y los dos siguientes** (hay que comunicarlo al cliente). 7 % también para determinadas actividades (recaudadores, mediadores de seguros, delegados comerciales). 1 % para actividades en módulos del art. 95.6 RIRPF. 19 % en arrendamientos de locales (modelo 115) | LIRPF art. 101.5; RIRPF art. 95. [DATO, normas estables] |
| **Modelo 303** (IVA) | Trimestral: 1-20 de abril, julio y octubre; 4T del 1 al 30 de enero. Mensual para REDEME, grandes empresas o SII | Orden HAC/3625/2003 y sucesivas |
| **Modelo 130 / 131** | Pagos fraccionados del IRPF: 130 en estimación directa, 131 en módulos. Mismos plazos que el 303. **No tienen que presentar el 130 los profesionales con al menos el 70 % de sus ingresos sujetos a retención el año anterior** | RIRPF art. 109 |
| **111 / 115** | Retenciones de trabajo y profesionales (111) y de alquileres (115). Trimestrales: 1-20 del mes siguiente; 4T del 1 al 20 de enero | — |
| **180 / 190** | Resúmenes anuales del 115 y del 111. Del 1 al 31 de enero | — |
| **390** | Resumen anual del IVA. Del 1 al 30 de enero. No lo presentan quienes están exonerados, en la mayoría de los casos de tributación solo en territorio común con 303 trimestral | — |
| **347** | Operaciones con terceros de más de 3.005,06 € al año. En febrero. No lo presentan los obligados al SII | — |
| **349** | Operaciones intracomunitarias. Mensual, o trimestral si las entregas o servicios no superan 50.000 € por trimestre. Lo transformará ViDA desde 2029-2030 | — |
| **036/037** | **El modelo 037 está suprimido desde el 3/02/2025.** Solo existe el 036, que tiene una nueva página de titularidad real. Orden HAC/1526/2024, de 11 de diciembre (BOE 09/01/2025). No hay cambios en 2026 | https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410 · https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2025/enero/9/orden-ministerial-modificacion-declaraciones-censales.html |
| **Requisitos de factura (RD 1619/2012)** | **Completa** (art. 6). **Simplificada** (art. 7): hasta 400 € con IVA, o hasta 3.000 € en sectores del art. 4.2; la «cualificada» lleva NIF y domicilio del destinatario. **Rectificativa** (art. 15), con serie específica. **Recapitulativa** (art. 13), para operaciones de un mes natural con el mismo destinatario. El **RD 238/2026 modifica el RD 1619/2012** para la factura electrónica: hay que revisar el texto consolidado | BOE-A-2012-14696 (consolidado) |
| **Conservación** | 4 años a efectos tributarios (prescripción, art. 66 LGT), y más mientras puedan comprobarse bases o créditos fiscales. **6 años a efectos mercantiles** (art. 30 del Código de Comercio). Digitalizar papel exige un software de digitalización certificada (Orden EHA/962/2007) para poder destruir el original | [DATO, normas estables] |
| **SII** | Obligatorio con volumen de operaciones > 6.010.121,04 €, inscritos en REDEME y grupos de IVA. Voluntario para el resto | RIVA art. 62.6 |
| **Cuota de autónomos 2026** | **Orden PJC/297/2026, de 30 de marzo** (BOE núm. 79, 31/03/2026), con efectos desde el 01/01/2026. **Mantiene las mismas bases y tramos que 2025**: 15 tramos; base mínima de 653,59 € (tramo 1 reducido, ≤ 670 €) a 1.928,10 € (> 6.000 €); base máxima de 5.101,20 €. Tipos: CC 28,30 %, CP 1,30 %, MEI 0,90 % (con cese y FP, en torno al 31,5 % total; [DATO-2ª] para cese y FP) | https://www.boe.es/eli/es/o/2026/03/30/pjc297 (art. 18) |
| **Cuota de autónomos 2027** | **Sin aprobar.** El RD-ley 13/2022 solo fijó la senda 2023-2025, y lo de después depende del diálogo social y de la orden de cotización 2027, que suele publicarse entre enero y marzo | [HIPÓTESIS] No publicar cifras de 2027 hasta que aparezca la orden |

**Calendario fiscal 2027.** Es una [HIPÓTESIS] derivada de las normas de cada modelo y del corrimiento al siguiente día hábil cuando el plazo acaba en sábado o domingo. La AEAT suele publicar el calendario oficial en diciembre.
- 4T 2026: 111/115/123 hasta el **miércoles 20/01/2027**. 303, 390 y 130/131 terminan el 30/01, que es sábado, así que pasan al **lunes 01/02/2027**. 180/190 terminan el 31/01 (domingo) y también pasan al **01/02/2027**.
- 347: 28/02/2027 es domingo, así que pasa al **lunes 01/03/2027**.
- 1T 2027: **martes 20/04/2027**. Con domiciliación, hasta el 15/04.
- Renta 2026: previsiblemente de abril al 30/06/2027.
- 2T: **martes 20/07/2027**.
- 3T: **miércoles 20/10/2027**.

---

## A4. Revisión jurídica de la web (archivo:línea)

Gravedad: **ALTA** (afirmación falsa o con riesgo legal o de consumo), **MEDIA** (desactualizada o incompleta), **BAJA** (matiz).

### A4.1 Afirmaciones sobre el cumplimiento VERI*FACTU de Facturales

| # | Archivo:línea | Texto actual | Problema | Corrección propuesta |
|---|---|---|---|---|
| 1 | `faq.html:28` (JSON-LD) y `faq.html:47`; `index.html:30` (JSON-LD) y `index.html:240` | «Cada factura emitida genera su registro de facturación con huella encadenada y lleva el código QR de cotejo.» | **ALTA.** (a) Solo ocurre si el usuario activa VERI*FACTU (`verifactu_enabled`). (b) Sin remisión a la AEAT, el «QR de cotejo» no permite cotejar nada, y la leyenda «verificable» induce a error. (c) La pregunta «¿Cómo cumple / ¿Cumple con VERI*FACTU?» da a entender un cumplimiento pleno que la declaración responsable sin firmar contradice. En YMYL, y como publicidad (Ley 3/1991 de competencia desleal, arts. 5 y 7), es una práctica engañosa | «¿Está Facturales preparado para VERI*FACTU? Facturales ya genera, al emitir cada factura (con VERI*FACTU activado en Ajustes), su registro de facturación con huella encadenada y su código QR. Estamos completando la remisión de registros a la AEAT antes de que la obligación sea exigible (hoy, 1/1/2027 para sociedades y 1/7/2027 para el resto; Hacienda ha anunciado su aplazamiento a octubre de 2028).» Cuando la remisión funcione en producción y la declaración esté firmada, volver a la redacción afirmativa y enlazar la declaración responsable |
| 2 | `verifactu-2027-guia-autonomos-pymes.html:102`; `factura-electronica-vs-verifactu.html:76`; `contabilidad-negocio-7-pasos.html:94` (bloque CTA) | «Facturales emite facturas con su registro VERI*FACTU y su QR…» | **ALTA.** Igual que el n.º 1, y además va dentro de artículos YMYL que explican que VERI*FACTU implica remitir a la AEAT. El lector deduce que Facturales remite | «Facturales genera el registro de facturación con huella encadenada y el QR de cada factura, y se está preparando para VERI*FACTU…» |
| 3 | `crea-envia-facturas.html:39` | «Facturas correctas a la primera, listas para VERI*FACTU.» | **MEDIA-ALTA.** «Listas» da a entender conformidad | «…preparadas para VERI*FACTU» (y lo mismo que el n.º 1) |
| 4 | `crea-envia-facturas.html:7` (meta), `:59`, `:82` (FAQ); `index.html:62`, `:110`, `:143`; `impuestos.html:50`; `pricing.html:85` («VERI*FACTU (registro y QR) Incluido»); `funciones.html:46`; `about.html:43` («Cumplimiento: … VERI*FACTU») | «Registro VERI*FACTU con QR», «su registro VERI*FACTU», «Cumplimiento … VERI*FACTU» | **MEDIA.** Se puede mantener «registro de facturación con huella y QR», pero no «Cumplimiento VERI*FACTU» mientras no haya remisión ni declaración firmada | Unificar en «Registro de facturación con huella encadenada y QR (VERI*FACTU en preparación)». En `about.html:43`, quitar VERI*FACTU de «Cumplimiento» o añadir «en preparación» |
| 5 | `index.html:7`, `:15` (meta description y OG) | «Factura con VERI*FACTU…» | **MEDIA.** El snippet de Google es una afirmación comercial | «Factura preparada para VERI*FACTU…» |
| 6 | App (fuera de la landing): `src/domain/rules/fiscal/verifactu-qr.ts:18-21`, `VistaPreviaFacturaVg.tsx:200`, `InvoicePreviewPage.tsx:204` | QR con URL `ValidarQR` (VERI*FACTU) y leyenda «Factura verificable…» sin remisión | **ALTA** (producto). Contrario a la Orden HAC/1177/2024 y a la FAQ de la AEAT: la leyenda solo procede en modalidad VERI*FACTU con remisión | No imprimir la leyenda ni la URL VERI*FACTU en facturas reales hasta que `estado_envio` pueda llegar a «aceptado». Revisión por un asesor fiscal |
| 7 | `docs/declaracion-responsable-fabricante.md` | Borrador sin firmar; se declara la modalidad VERI*FACTU | **ALTA** (productor). El plazo de los productores venció el 29/07/2025 | Completar la checklist (XML, anulación, remisión, versión) y firmar. Mientras tanto, no afirmar «cumple» en ningún canal, incluido el Kit Digital |

### A4.2 Artículos del blog

| # | Archivo:línea | Texto | Problema | Corrección + fuente |
|---|---|---|---|---|
| 8 | `verifactu-2027-guia-autonomos-pymes.html:74-78` | «Según los plazos vigentes: 01/01/2027 IS · 01/07/2027 resto» | **MEDIA.** Correcto como vigente, pero **falta el anuncio de aplazamiento a octubre de 2028 (05/10/2026)** y la norma de origen | Añadir una tabla de estado normativo: «VIGENTE: RD-ley 15/2025 (BOE 03/12/2025)…» y «ANUNCIADO, sin publicar en BOE: octubre de 2028 (nota del Ministerio de Hacienda, 05/10/2026)». Enlazar el BOE y la nota |
| 9 | `verifactu-2027-guia-autonomos-pymes.html:6, 39` (title/H1) y slug | «VERI*FACTU en 2027» | **MEDIA (SEO y exactitud).** Si se publica el aplazamiento, el título queda obsoleto | Title: «VERI*FACTU: fechas, a quién afecta y cómo prepararte (actualizado oct. 2026)». **Mantener la URL**, que ya está indexada; cambiar solo title, H1 y el texto |
| 10 | `verifactu-2027-guia-autonomos-pymes.html:72` | «La AEAT lo resume con la "regla de los 4 NO"… (no tener domicilio fiscal en territorios forales)» | **BAJA-MEDIA.** La atribución a la AEAT no tiene enlace. «Domicilio fiscal» simplifica: lo relevante es estar sujeto a la normativa foral (Concierto o Convenio) | Enlazar la fuente oficial o reformular. Añadir «Canarias, Ceuta y Melilla **sí** están incluidas» y «el SII está excluido (art. 3.3 RD 1007/2023)» |
| 11 | `verifactu-2027-guia-autonomos-pymes.html:63-66` | Descripción de las modalidades | Correcta, pero incompleta | Añadir: en NO VERI*FACTU los registros se **firman electrónicamente** y hay **registro de eventos**. La leyenda «VERI*FACTU» solo aparece en la modalidad verificable |
| 12 | `verifactu-2027-guia-autonomos-pymes.html` (ausencia) | No menciona sanciones, productores ni la declaración responsable | **MEDIA** (falta información útil y E-E-A-T) | Sección «Sanciones»: art. 201 bis LGT, 150.000 € al productor y 50.000 € por ejercicio al usuario. Sección «Pide a tu proveedor la declaración responsable» |
| 13 | `verifactu-2027-guia-autonomos-pymes.html:86` | «VERI*FACTU puede encajar si quieres automatizar remisión…» | **BAJA** | Añadir que la AEAT ofrece una **aplicación gratuita VERI*FACTU** para quien emite pocas facturas. Es honesto y aporta valor |
| 14 | `factura-electronica-vs-verifactu.html:63` | «Su efectividad depende del desarrollo reglamentario.» | **ALTA (desactualizado).** El RD 238/2026 está publicado (31/03/2026) y la Orden HAC/1028/2026 está en vigor desde el 06/10/2026 | «Ya tiene reglamento (RD 238/2026) y orden de la solución pública (Orden HAC/1028/2026, BOE 05/10/2026). Será obligatoria ≈ en octubre de 2027 para quienes facturan más de 8 M€ y ≈ en octubre de 2028 para el resto, autónomos incluidos. Las personas físicas tendrán que informar del estado de pago ≈ desde octubre de 2029.» Añadir: formatos (UBL, CII, EDIFACT, Facturae), la solución pública gratuita de la AEAT, la copia fiel en UBL, los estados (rechazo, pago, vencimiento) y que **las facturas simplificadas quedan excluidas** |
| 15 | `factura-electronica-vs-verifactu.html:56-59` | Plazos del SIF | **MEDIA.** Igual que el n.º 8. Ahora además hay que explicar la **convergencia prevista en octubre de 2028** | Tabla comparativa VERI*FACTU / factura electrónica con columnas de estado |
| 16 | `factura-electronica-vs-verifactu.html` (ausencia) | No menciona ViDA | BAJA (oportunidad) | Párrafo sobre la Directiva (UE) 2025/516: factura electrónica intracomunitaria y reporte digital desde el 01/07/2030 |
| 17 | `contabilidad-negocio-7-pasos.html:63-65` | «Digitaliza y guarda con criterio único» | **BAJA.** Puede inducir a destruir papel | Añadir: «Conserva las facturas al menos 4 años (LGT) y los libros y justificantes 6 años (Código de Comercio). Solo puedes destruir el papel si digitalizas con software de digitalización certificada.» |
| 18 | `contabilidad-negocio-7-pasos.html:89` | «Sin categorías claras, pierdes deducciones» | BAJA | Matizar: un gasto es deducible si está vinculado a la actividad, justificado con factura completa y registrado |
| 19 | Las tres entradas: JSON-LD `datePublished` (feb. 2026), sin `dateModified`. Autor «Equipo de Facturales» / Organization. Sitemap con `lastmod` 2026-10-16 | Sin revisor ni fecha de actualización visible | **MEDIA (E-E-A-T y YMYL).** Incoherencia entre la fecha visible y el `lastmod` | Implementar el protocolo de la sección A5: `dateModified`, `reviewedBy` (Person con credenciales), bloque «Última revisión» |

### A4.3 Páginas de producto

| # | Archivo:línea | Texto | Evaluación |
|---|---|---|---|
| 20 | `impuestos.html:28,63`; `faq.html:59` | «No. Facturales calcula las cifras para que tú o tu gestoría presentéis los modelos…» | **Correcto** y alineado con la política de no afirmar presentación automática. Mantener |
| 21 | `impuestos.html:50` | «Modelo 130: Estimación del pago fraccionado del IRPF» | BAJA. Añadir «(estimación directa; no aplica a módulos —131— ni, en general, a profesionales con ≥ 70 % de ingresos retenidos)» |
| 22 | `impuestos.html:28,64`; `faq.html:49` | «IVA peninsular y de Baleares, IGIC canario e IPSI…» | Correcto |
| 23 | `faq.html:48` | «Una factura emitida… solo se corrige con una factura rectificativa» | Correcto (art. 15 RD 1619/2012). Se puede añadir «o se anula si la operación no existió (registro de anulación)» |
| 24 | `faq.html:50` | «Puedes descargar cualquier factura en Facturae 3.2.2, el formato que admite la Administración a través de FACe.» | Correcto para B2G. **Riesgo de malentendido en B2B:** descargar un Facturae **no** cumplirá por sí solo la obligación B2B del RD 238/2026, que exige intercambio por plataforma o solución pública, copia fiel en UBL y estados. Añadir: «Para la factura electrónica obligatoria entre empresas (≈ 2027-2028) iremos informando de cómo se integrará Facturales» |
| 25 | `pricing.html:28` (JSON-LD) | Precios sin IVA, Stripe, prueba | Sin problemas legales fiscales |

---

## A5. Protocolo editorial YMYL (fiscal)

### A5.1 Flujo
1. **Redacción.** Equipo de contenidos, con fuentes primarias obligatorias (BOE, sede AEAT, DGT/consultas vinculantes, EUR-Lex, diputaciones forales).
2. **Ficha de fuentes** por artículo: norma, artículo, URL del BOE consolidado y fecha de consulta.
3. **Revisión técnica por un asesor fiscal colegiado** (Colegio de Economistas / REAF, AEDAF, o gestor administrativo colegiado). Debe estar identificado con nombre, número de colegiado y perfil enlazado (página `/equipo/nombre` con Person schema). Revisa la exactitud, los estados normativos y los disclaimers.
4. **Revisión de copy de producto.** Cualquier mención a funciones de Facturales se contrasta con el estado real del producto (checklist del repo de la app). Regla: **nunca afirmar remisión a la AEAT ni «cumple VERI*FACTU» hasta que exista la declaración responsable firmada.**
5. **Publicación** con bloque de revisión, `dateModified`, `reviewedBy` y la tabla de estado normativo.

### A5.2 Bloque «Última revisión» (componente reutilizable `fx-revision`)
```
Última revisión: 18 de octubre de 2026 · Revisado por: [Nombre Apellido], asesor fiscal colegiado n.º XXXX ([Colegio])
Fuentes oficiales: RD 1007/2023 (BOE consolidado) · RD-ley 15/2025 · Nota del Ministerio de Hacienda de 05/10/2026 · FAQ VERI*FACTU de la AEAT
Próxima revisión prevista: enero de 2027 o antes si hay cambios en el BOE.
```
JSON-LD: `Article` con `dateModified`, `author` (Person u Organization), `reviewedBy` (Person con `hasCredential` y `memberOf`), `citation` (URLs del BOE), `about`. También puede usarse `WebPage` con `lastReviewed`.

### A5.3 Tabla de «estado normativo» (componente reutilizable `fx-estado-norma`)
| Obligación | Estado | Fecha | Norma | Fuente |
|---|---|---|---|---|
| VERI*FACTU (sociedades) | 🟢 Vigente | Antes del 1/1/2027 | RD 1007/2023, DF 4.ª (RD-ley 15/2025) | BOE |
| VERI*FACTU (autónomos y resto) | 🟢 Vigente | Antes del 1/7/2027 | ídem | BOE |
| Aplazamiento a octubre de 2028 | 🟡 Anunciado, sin norma | Oct. 2028 | Nota del Ministerio de Hacienda, 05/10/2026 | hacienda.gob.es |
| Factura electrónica B2B > 8 M€ | 🔵 Aprobado, pendiente de aplicación | ≈ oct. 2027 | RD 238/2026 + Orden HAC/1028/2026 | BOE |
| Factura electrónica B2B, resto | 🔵 Aprobado, pendiente de aplicación | ≈ oct. 2028 | ídem | BOE |
| ViDA intracomunitario | 🔵 Aprobado (UE) | 1/7/2030 | Directiva (UE) 2025/516 | EUR-Lex |

(En la web, sustituir los emojis por badges `fx-badge` con texto, por accesibilidad.)

### A5.4 Cadencia
- **Cada semana:** revisar alertas (BOE, AEAT). Si hay cambio, actualizar en menos de 72 h las páginas afectadas: artículos, FAQ, JSON-LD de index, faq y crea-envia-facturas.
- **Cada mes:** comprobar fechas y enlaces y verificar el estado del producto frente al copy.
- **Cada trimestre:** revisión completa por el asesor de todos los artículos fiscales y renovación de `dateModified` solo si hay cambios reales (no cambiar fechas sin cambios).
- **Calendario fijo:** enero (orden de cotización de autónomos, PGE, cambios de tipos, calendario del contribuyente), marzo y abril (campaña de renta), octubre (anteproyecto de PGE).

### A5.5 Monitorización de cambios normativos
- **Mi BOE** (https://www.boe.es/mi_boe/): alertas por texto («1007/2023», «238/2026», «facturación electrónica», «sistemas informáticos de facturación», «cotización»), por departamento (Ministerio de Hacienda) y por sección I (Disposiciones generales).
- **RSS del BOE:** https://www.boe.es/rss/ (sumario diario, sección I).
- **Sede de la AEAT:** página de VERI*FACTU (https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html; vigilar la fecha «Página actualizada») y «Todas las noticias». Monitorizar con un cambio de página (Visualping o un script diff) si no hay RSS, y suscribirse al RSS de novedades de la AEAT si está disponible.
- **Portal de desarrolladores de la AEAT** (especificaciones técnicas, WSDL y XSD de VERI*FACTU y de la solución pública).
- **Notas de prensa** del Ministerio de Hacienda (hacienda.gob.es → Gabinete → Notas de prensa) y referencias del Consejo de Ministros (lamoncloa.gob.es).
- **Foral:** batuz.eus, ticketbai.eus y la Hacienda Foral de Navarra.
- **UE:** taxation-customs.ec.europa.eu (ViDA).
- **Responsable:** una persona del equipo con un SLA de lectura diaria. Registrar cada cambio en un changelog interno (fecha, norma, páginas afectadas).

### A5.6 Disclaimers
- **Pie de artículo fiscal:** «Este contenido es informativo y está actualizado a la fecha indicada. No constituye asesoramiento fiscal ni jurídico. La normativa cambia: consulta el BOE y la sede de la AEAT o a tu asesor antes de tomar decisiones.»
- **Cuando haya normas anunciadas:** «Las fechas marcadas como "anunciadas" no tienen todavía rango normativo. Actualizaremos este artículo cuando se publiquen en el BOE.»
- **En las páginas de producto sobre impuestos:** «Facturales calcula importes orientativos a partir de tus registros. No presenta declaraciones ante la AEAT.» Ya se dice en la FAQ: mantenerlo.
- **No usar** «homologado por Hacienda». La AEAT no homologa ni certifica software: el productor emite una declaración responsable.

---

# PARTE B — Medición

## B6. Estado actual de la analítica [DATO, grep 18/10/2026]

**Landing (`/home/user/facturales-landing`)**
- **Sin** gtag, GTM, GA4, Plausible, Umami, Matomo, Clarity, Hotjar ni píxeles (búsqueda de `gtag|googletagmanager|GTM-|G-XXXX|plausible|umami|matomo|clarity|hotjar|fbq` en `*.html` y `*.js`: 0 resultados en las páginas reales).
- **Sin** `google-site-verification` ni `msvalidate.01`. Si GSC está verificado, sería por DNS (no se puede comprobar desde el repo).
- **Sin** banner de cookies ni gestor de consentimiento.
- `assets/js/footer-include.js:5` enlaza la política de cookies a `https://app.facturales.es/politica-de-cookies`. Hoy no hace falta banner en la landing porque no se instalan cookies no exentas, pero hará falta en cuanto se añada GA4.
- `assets/js/facturales.js` (233 líneas): solo comportamiento de UI (menú, focus trap, conmutador de precios y formulario de contacto por mailto en la l. 136). No contiene eventos.
- Los CTA apuntan a `https://app.facturales.es/signup` (index.html ×5, pricing ×4, módulos ×2) sin UTM ni parámetros de plan o ubicación.
- `robots.txt` correcto y `sitemap.xml` con 20 URL (sin IndexNow).

**App (`/home/user/facturales`)**
- **Sin** GA4, GTM, PostHog, Mixpanel, Amplitude, Vercel Analytics ni Sentry en `index.html`, `src`, `package.json` o `vercel.json`.
- La CSP de `vercel.json:8-12` no permite `googletagmanager.com` ni `google-analytics.com`: habría que añadirlos (o usar server-side tagging o un proxy de primera parte).
- **Registro:** `src/services/auth/auth.service.ts:99-104` llama a `supabase.auth.signUp` con `options.data` = metadatos de `buildSignUpMetadata()` (`src/app/pages/domain/acceso.ts:99-107`), que solo incluye `first_name`, `last_name` y `full_name`. **No captura `utm_*`, `document.referrer`, `gclid` ni la landing page.** No hay ninguna tabla de atribución entre las migraciones.
- **Pago:** Stripe (`supabase/functions/create-checkout-session`, `stripe-webhook`) y RevenueCat en móvil (`revenuecat-webhook`). Es el punto ideal para enviar `purchase` desde el servidor (GA4 Measurement Protocol).
- **Política de cookies:** `src/app/pages/legal/LegalContent.tsx:459-500`. Es una plantilla genérica que declara cookies «analíticas», «de personalización» y «publicitarias» que no existen. No las enumera (nombre, proveedor, finalidad, duración), remite a la configuración del navegador y no ofrece un panel para retirar el consentimiento. **No cumple la Guía de cookies de la AEPD (2023)** y contradice el uso real (Supabase auth usa localStorage, Stripe y el captcha de Cloudflare Turnstile).

## B7. Plan de medición

### B7.1 Google Search Console
1. **Propiedad de dominio `facturales.es`** verificada por DNS (TXT). Cubre `facturales.es`, `www.` y `app.`, y http/https.
2. **Propiedades de prefijo adicionales:**
   - `https://facturales.es/`: datos más limpios para la landing y la API.
   - `https://app.facturales.es/`: vigilar que no se indexen pantallas privadas. Solo deberían indexarse las legales y signup/signin si interesa.
   - En el futuro, `https://facturales.es/blog/` si se migra a carpeta.
3. **Sitemaps:** enviar `https://facturales.es/sitemap.xml`. Mantener `lastmod` real (hoy pone 2026-10-16/17 en todas las URL; actualizarlo solo cuando cambie el contenido).
4. **Informes que revisar:**
   - Rendimiento: consultas y páginas, con filtro de marca (regex `facturales|factura les`) frente al resto.
   - Indexación de páginas: «Rastreada: actualmente sin indexar» y «Descubierta: sin indexar».
   - Core Web Vitals.
   - HTTPS.
   - Mejoras: FAQ, Artículo y breadcrumbs. Aviso: Google limitó los rich results de FAQ a webs gubernamentales y sanitarias desde 2023, así que el JSON-LD de FAQ no dará snippet pero no perjudica.
   - Enlaces.
   - Inspección de URL tras cada publicación.
5. Vincular GSC con GA4 y con Looker Studio (conector nativo y exportación masiva a BigQuery si se quiere histórico de más de 16 meses).

### B7.2 Bing Webmaster Tools + IndexNow
- Importar la propiedad desde GSC y enviar el sitemap. Bing alimenta Copilot y parte de ChatGPT Search, lo que importa para las menciones en IA.
- **IndexNow:**
  - Generar la clave y publicar `https://facturales.es/<clave>.txt`.
  - En cada despliegue, enviar un POST a `https://api.indexnow.org/indexnow` con las URL cambiadas. Un script en CI o en la acción de despliegue sirve, porque el sitio es estático.
  - Google no usa IndexNow: para Google basta con el sitemap y la inspección manual.

### B7.3 GA4 con cross-domain y Consent Mode v2
- **Un solo flujo web GA4** para `facturales.es` y `app.facturales.es`. Al ser subdominios del mismo dominio raíz, la cookie `_ga` con `cookie_domain: 'auto'` ya se comparte en `.facturales.es`.
- Configurar igualmente en Admin → Flujos → Configurar dominios: `facturales.es` y `app.facturales.es`.
- Añadir `stripe.com` / `checkout.stripe.com` a la **lista de referencias no deseadas**.
- **Implementación:** GTM (contenedor web único) en la landing (inyectado en `header-include.js` o como snippet en el `<head>` de cada página) y en `index.html` de la app. Actualizar la CSP (`script-src`/`connect-src`: `https://www.googletagmanager.com https://*.google-analytics.com https://*.analytics.google.com`) o servir GTM desde un dominio propio (server-side GTM en `sgtm.facturales.es`).
- **Consent Mode v2:**
  - Por defecto, `ad_storage`, `analytics_storage`, `ad_user_data` y `ad_personalization` = `denied`, con `wait_for_update: 500`.
  - Actualizar a `granted` según la elección del usuario.
  - **Modo avanzado** (pings sin cookies y modelado de conversiones) frente a **básico** (no carga nada hasta el consentimiento). Recomiendo el básico para empezar: es el más defendible ante la AEPD, aunque se pierde modelado.
- **CMP:** banner propio ligero o CMP certificada por Google (obligatorio si se usan Google Ads en el EEE; por ejemplo Cookiebot, CookieYes o Didomi). Requisitos AEPD (Guía sobre el uso de las cookies, actualización de julio de 2023, adaptada a las directrices 03/2022 del EDPB, de cumplimiento obligatorio desde el 11/01/2024; https://www.aepd.es/guias/guia-cookies.pdf):
  - **Botón «Rechazar» en la primera capa, al mismo nivel y con la misma prominencia que «Aceptar».**
  - Sin casillas premarcadas.
  - El scroll o la navegación no valen como consentimiento.
  - Panel de configuración por finalidad.
  - Retirar el consentimiento debe ser tan fácil como darlo: enlace «Configurar cookies» permanente en el footer (`footer-include.js`).
  - Conservar la elección como máximo 24 meses.
  - Política de cookies con tabla (nombre, titular, finalidad, duración).
- **El consentimiento debe compartirse entre la landing y la app.** Guardarlo en una cookie de primera parte con `domain=.facturales.es` para no mostrar el banner dos veces.

### B7.4 Alternativa sin cookies

| Opción | Pros | Contras |
|---|---|---|
| **Plausible** (UE, alojado en Alemania) o **Umami** (autoalojable) | Sin cookies ni identificadores persistentes, así que la AEPD lo considera exento o de bajo riesgo si solo se hace medición agregada propia. Sin banner. Ligero (< 1 KB). Eventos personalizados y objetivos | Sin modelo de usuario cross-session, atribución pobre en un ciclo largo (visita → registro días después), sin integración con Google Ads, embudo limitado |
| **Matomo** sin cookies (configuración de la AEPD/CNIL) | Más potente; puede quedar exento si se configura según la CNIL | Alojamiento y mantenimiento |
| **GA4 + Consent Mode** | Integración con GSC y Ads, embudos y exploraciones | Con banner se pierde un 30-60 % de los datos [HIPÓTESIS] por rechazos |

**[RECOMENDACIÓN] Modelo híbrido:**
- **Plausible o Umami sin cookies** como fuente de verdad del tráfico agregado en la landing (100 % de visitas).
- **GA4 con consentimiento** para el embudo detallado.
- **Atribución propia en Supabase** (first-touch guardado en el registro, que no depende de cookies de terceros: se lee de la URL y del referrer, y la base jurídica es el interés legítimo o la ejecución del contrato, documentado en la política de privacidad).
- Las métricas de negocio (registros, activación, MRR) **siempre desde la base de datos**, nunca desde GA4.

### B7.5 Eventos y conversiones (nombres exactos)

| Evento | Dónde | Parámetros | Conversión clave |
|---|---|---|---|
| `page_view` (automático) | Landing y app | `page_location`, `page_title`, `content_group` (`home`, `modulo`, `blog_verifactu`, `blog_efactura`, `blog_gestion`, `precios`, `legal`) | — |
| `cta_click` | Landing (`facturales.js`, delegación en `a[href*="app.facturales.es/signup"]`, `[data-cta]`) | `cta_id` (p. ej. `hero_primary`), `cta_location` (`header`, `hero`, `pricing_card`, `article_inline`, `article_end`, `footer`, `mobile_menu`), `cta_text`, `plan` (`starter`, `pro`, `ilimitado`), `billing_period` (`monthly`, `annual`), `page_type` | Sí (micro) |
| `pricing_toggle` | Landing (`facturales.js:115`, función `aplicar`) | `billing_period` | No |
| `contact_submit` | Landing (`facturales.js:136`) | `form_id` = `contacto` | Sí (micro) |
| `faq_open` | Landing (`<details>` toggle) | `faq_question` (texto corto), `page_type` | No |
| `lead_magnet_download` | Landing (futuras guías o plantillas) | `asset_id`, `asset_type` (`pdf`, `xlsx`), `topic` (`verifactu`, `efactura`, `calendario_fiscal`) | Sí |
| `tool_use` | Landing (futuras calculadoras: cuota de autónomos, IVA, retención) | `tool_id`, `tool_step` (`start`, `result`), `tool_value_band` | Sí (micro) |
| `outbound_click` | Landing (enlaces a BOE o AEAT) | `link_domain` | No |
| `signup_start` | App, al montar `/signup` | `method` = `email`, `plan_hint`, `source` (desde utm o referrer) | No |
| `sign_up` (evento recomendado de GA4) | App, tras el éxito de `authService.signUp` (`src/app/pages/hooks/use-acceso.ts:135-138`) y, para fiabilidad, desde el servidor | `method` = `email`, `user_id` (hash del UUID de Supabase, nunca el email), `plan_hint` | **Sí (principal)** |
| `email_confirmed` | App `/confirm-email` | — | No |
| `trial_start` | Servidor: `create-checkout-session` / `stripe-webhook` (`customer.subscription.created` con `status=trialing`) o cuando se asigna el plan de prueba | `plan`, `billing_period`, `trial_days` = 14 | Sí |
| `activation_first_invoice` | Servidor o app al emitir la **primera** factura (en `invoices.adapter.ts`, emisión) | `days_since_signup`, `has_verifactu_enabled` | **Sí (activación)** |
| `activation_milestone` | App | `milestone` (`first_client`, `first_bank_import`, `first_expense_ocr`, `first_quote`) | No |
| `purchase` | **Servidor:** `supabase/functions/stripe-webhook` en `invoice.paid` (primer pago y renovaciones, con `transaction_id` = id de la factura de Stripe) vía **Measurement Protocol** con el `client_id` guardado | `transaction_id`, `value` (sin IVA), `currency` = `EUR`, `items[{item_id: plan, item_variant: billing_period}]`, `subscription_type` (`new`, `renewal`, `upgrade`) | **Sí** |
| `subscription_cancel` | Servidor (`cancel-subscription`, webhook) | `plan`, `tenure_days` | No |

- **User-ID** con el hash del UUID para unir dispositivos.
- **Dimensiones personalizadas:** `cta_location`, `plan`, `content_group`, `first_touch_channel` (ámbito de usuario).

### B7.6 Atribución de registros orgánicos (first-touch en Supabase)

1. **Landing** (`assets/js/facturales.js`, bloque nuevo):
   - En la primera visita, guardar en una cookie de primera parte `fx_ft` (`domain=.facturales.es`, 90 días):
     - `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`
     - `gclid` / `msclkid`
     - `document.referrer` (solo el dominio)
     - `landing_page`
     - `ts`
   - Es una cookie técnica o de análisis propia. [HIPÓTESIS] Si solo sirve para atribuir la conversión del propio servicio y no se cruza con terceros, la AEPD la admite como analítica propia de bajo riesgo, pero conviene condicionarla al consentimiento o justificarla por escrito.
   - Al hacer clic en el CTA, añadir a la URL de signup `?ft=<base64>` y `&cta=<location>&plan=<plan>` como respaldo cross-subdominio.
2. **App:**
   - Al cargar `/signup`, leer `fx_ft`, la query y el `document.referrer` actual. Si no hay first-touch, crearlo (tráfico directo a la app).
   - Pasar en `buildSignUpMetadata()` (`src/app/pages/domain/acceso.ts:99`) un objeto `acquisition: {ft_source, ft_medium, ft_campaign, ft_referrer_domain, ft_landing_page, ft_ts, lt_* (last-touch), signup_cta, signup_plan_hint}`.
   - Se guarda en `auth.users.raw_user_meta_data` automáticamente.
3. **Base de datos:**
   - Migración nueva `supabase/migrations/2026xxxx_user_acquisition.sql`: tabla `public.user_acquisition (user_id uuid pk references auth.users, ft_* text, lt_* text, ga_client_id text, created_at)`, con RLS solo de lectura para el propio usuario y el rol admin.
   - Trigger `on auth.users insert` que copie desde `raw_user_meta_data->'acquisition'`.
   - Guardar también `ga_client_id` (leído de `_ga`) para el Measurement Protocol.
4. **Clasificación de canal** (vista SQL `v_signup_channel`):
   - `organic_search` si el referrer es google, bing, duckduckgo o ecosia y no hay utm.
   - `ai_assistant` si el referrer es chatgpt.com, perplexity.ai, copilot.microsoft.com o gemini.google.com.
   - `paid` si hay gclid o utm_medium=cpc.
   - `referral`, `direct`, `email` y `social` para el resto.
5. **Panel de administración:** la app ya tiene `src/features/admin`. Añadir un widget de registros, activación y pago por canal y por landing page.

### B7.7 Dashboards (Looker Studio)
1. **SEO orgánico** (fuente: GSC):
   - Clics, impresiones, CTR y posición por **cluster**, con un campo calculado CASE por patrón de URL o query: `verifactu`, `factura electrónica`, `facturación general` (programa de facturas, autónomos), `impuestos/modelos`, `módulos de producto`, `marca`.
   - Tabla de páginas con su variación frente a 28 días.
   - **Marca frente a no marca** (regex).
   - **CTR por query** con posición entre 1 y 10, para detectar títulos que mejorar.
   - Distribución de posiciones por cluster (1-3, 4-10, 11-20, 21-50).
2. **Embudo orgánico → registro → pago:**
   - Fuentes: GA4 y Supabase (conector PostgreSQL de solo lectura o exportación diaria a BigQuery o Google Sheets).
   - Pasos: sesiones orgánicas en la landing (Plausible o GA4) → `cta_click` → `signup_start` → `sign_up` (BD) → `activation_first_invoice` (BD) → `trial` → primer `purchase` (BD/Stripe) → MRR por canal first-touch.
3. **Contenido YMYL:**
   - Fecha de última revisión por artículo, días desde la revisión y alertas de páginas con más de 90 días sin revisar.
4. **Técnico:** CWV (informe CrUX o PageSpeed API), páginas indexadas y sin indexar (exportación de GSC).

### B7.8 Cadencia de revisión
- **Cada semana (30 min):**
  - GSC: picos o caídas, nuevas queries y errores de indexación.
  - Registros por canal.
  - Alertas normativas.
  - Rankings del proyecto SE Ranking (keywords prioritarias).
- **Cada mes:**
  - Informe de clusters, CTR y títulos.
  - Embudo completo.
  - Enlaces conseguidos.
  - Menciones en IA.
  - Contenidos que actualizar.
- **Cada trimestre:**
  - Revisión de los OKR de la sección B8.
  - Auditoría técnica.
  - Revisión YMYL completa con el asesor.
  - Recalibrar previsiones.

### B7.9 Rankings y menciones en IA
- **SE Ranking:** proyecto `facturales.es` con Google España (escritorio y móvil, idioma es) y Bing.
  - Grupos de keywords por cluster:
    - VERI*FACTU: «verifactu», «verifactu autónomos», «verifactu fechas», «verifactu 2028», «software verifactu».
    - Factura electrónica: «factura electrónica obligatoria», «factura electrónica autónomos 2028», «solución pública facturación electrónica».
    - Facturación: «programa de facturación autónomos», «programa facturas gratis», «facturación online».
    - Modelos: «modelo 303», «modelo 130», «calendario fiscal 2027», «cuota autónomos 2027».
    - Marca.
  - Competidores: Holded, Quipu, Billin, Contasimple, Factorial/Facturadirecta, Anfix, Cuentica, Sage.
  - Auditoría de sitio mensual.
- **Menciones en IA:**
  - Módulo AI Search de SE Ranking (prompts como «mejor programa de facturación para autónomos con verifactu», «qué es verifactu y cuándo es obligatorio») en ChatGPT, Perplexity, Gemini y AI Overviews.
  - Complementar con el seguimiento manual mensual de unos 20 prompts y con el canal `ai_assistant` en la atribución propia.
  - KPI: % de prompts con mención o enlace a facturales.es.

### B7.10 Tareas concretas por archivo

**Landing**
1. `assets/js/header-include.js`:
   - Cargar el consentimiento por defecto (Consent Mode v2 `denied`) y después GTM o Plausible.
   - Alternativa preferible: snippet estático en el `<head>` de cada página antes de `header-include.js`. Aviso: `document.write` no debe insertar scripts asíncronos.
2. `assets/js/footer-include.js:5`: añadir el enlace «Configurar cookies» (`button`, que abre el panel de la CMP). Mantener el enlace a la política.
3. `assets/js/facturales.js`:
   - Nuevo módulo `fxMedicion` con `dataLayer.push` para `cta_click` (delegación de clics), `pricing_toggle` (en `aplicar`, l. 115), `contact_submit` (l. 136), `faq_open` y `outbound_click`.
   - Captura del first-touch (`fx_ft`) y decoración de los enlaces a app.facturales.es con `ft`, `cta` y `plan`.
4. Todos los HTML de CTA: añadir `data-cta-location` y `data-plan` a los enlaces de signup (index ×5, pricing ×4, módulos ×2, artículos ×1).
5. Raíz: `<clave-indexnow>.txt` y un script de envío en el despliegue. Meta de verificación de Bing si no se importa desde GSC.
6. `sitemap.xml`: `lastmod` real por página.
7. Artículos: bloque `fx-revision`, tabla de estado normativo y `dateModified` y `reviewedBy` en el JSON-LD.

**App**
1. `index.html` + `vercel.json` (CSP): GTM o gtag y los dominios de Google en `script-src`, `connect-src` e `img-src`.
2. `src/app/pages/domain/acceso.ts:99` (`buildSignUpMetadata`): añadir `acquisition`.
3. `src/app/pages/hooks/use-acceso.ts:135-138`: `dataLayer.push({event:'sign_up', method:'email'})` tras el éxito, y `signup_start` al montar la página.
4. `supabase/migrations/…_user_acquisition.sql`: tabla, trigger y vista de canal.
5. `supabase/functions/stripe-webhook`: Measurement Protocol `purchase`, `trial_start` y `subscription_cancel` con `client_id` y `user_id`. Guardar `measurement_id` y `api_secret` como secretos.
6. `src/features/invoices/adapters/invoices.adapter.ts` (emisión): marcar la primera emisión con `activation_first_invoice`. Mejor desde el servidor, con un trigger SQL que inserte en una tabla `eventos_producto`.
7. `src/app/pages/legal/LegalContent.tsx:459-500`: reescribir la política de cookies con la tabla real (Supabase en localStorage, Stripe, Cloudflare Turnstile, GA4 si se activa, `fx_ft`, cookie de consentimiento), las bases jurídicas, cómo retirar el consentimiento y la fecha de actualización.
8. Banner o CMP compartido entre la landing y la app (cookie `.facturales.es`).

## B8. Objetivos SMART y KPIs

**Hipótesis de partida:**
- Dominio nuevo, autoridad muy baja (DR/DA < 10), unas 20 URL indexables y 3 artículos.
- Nicho muy competido, con SERP dominadas por Holded, Quipu, Billin, la AEAT, medios y asesorías.
- Picos de demanda alrededor de VERI*FACTU y de la factura electrónica (octubre de 2026 y de nuevo antes de 2027-2028).
- Publicación de 4 a 8 piezas al mes y campaña de enlaces activa.
- Sin presupuesto de pago.
- **Las previsiones son rangos orientativos con mucha incertidumbre.**

### B8.1 Métricas verificables (dependen de la ejecución)

| Plazo | Objetivo |
|---|---|
| **30 días** (~17/11/2026) | GSC (dominio y prefijo), Bing e IndexNow operativos. GA4 o Plausible, CMP y eventos `cta_click`, `sign_up` y `purchase` en producción. Tabla `user_acquisition` desplegada. **Corregidas las 7 incidencias ALTA de la sección A4.** ≥ 90 % de las URL del sitemap indexadas. Al menos 4 piezas nuevas o actualizadas (VERI*FACTU con la previsión de 2028; factura electrónica con el RD 238/2026; calendario fiscal 2027; cuota de autónomos). CWV «bueno» en ≥ 90 % de URL (LCP < 2,5 s, INP < 200 ms, CLS < 0,1) |
| **60 días** | 10-12 piezas publicadas. Bloque de revisión con asesor colegiado en el 100 % de los artículos fiscales. 5-10 dominios de referencia nuevos de calidad (directorios SaaS, asociaciones de autónomos, colaboraciones con gestorías, guest posts) |
| **90 días** | 16-20 piezas. 10-20 dominios de referencia. 1 lead magnet (calendario fiscal 2027 o checklist VERI*FACTU) y 1 herramienta (calculadora de cuota de autónomos o de retención) publicados. Dashboards de Looker Studio activos |
| **180 días** | 35-45 piezas. 25-40 dominios de referencia. Revisión trimestral YMYL hecha dos veces. 0 afirmaciones legales desactualizadas en la auditoría |
| **365 días** | 70-90 piezas. 50-80 dominios de referencia. Clusters completos: VERI*FACTU, factura electrónica, modelos y calendario, autónomos, gestión |

### B8.2 Métricas de resultado

Las impresiones son medibles, pero dependen de Google; el resto son previsiones (P10-P90 orientativo).

| Plazo | Impresiones GSC/mes (no marca) | Clics orgánicos/mes | Keywords top 10 | Registros orgánicos/mes (first-touch) | Nuevos clientes de pago orgánicos/mes | MRR orgánico acumulado |
|---|---|---|---|---|---|---|
| 30 d | 1.000-5.000 | 20-100 | 0-5 (sobre todo marca y long tail) | 0-5 | 0-1 | 0-15 € |
| 90 d | 5.000-25.000 | 100-600 | 5-25 | 5-25 | 1-4 | 10-60 € |
| 180 d | 20.000-80.000 | 500-2.500 | 20-80 | 20-80 | 3-12 | 50-250 € |
| 365 d | 60.000-250.000 | 2.000-10.000 | 60-250 | 60-300 | 8-40 al mes | 300-1.500 € |

**Hipótesis de conversión:**
- CTR orgánico medio del 1,5-4 % en la fase inicial, con posiciones medias de 15 a 40.
- De visita a registro: 1,5-3 % en páginas de producto y 0,3-1 % en blog.
- De registro a pago: 8-15 % (prueba de 14 días sin tarjeta [a confirmar]).
- ARPU de unos 10 €/mes (mezcla Starter y Pro, con mensual y anual).
- **Riesgo de calendario:** si el aplazamiento a 2028 se publica, la urgencia de búsqueda de «verifactu» bajará en 2027 y subirá otra vez en 2028. La factura electrónica (≈ octubre de 2027/2028) será el nuevo pico. Hay que preparar el contenido 3-6 meses antes.

### B8.3 Objetivos SMART de ejemplo
- **O1 (exactitud YMYL):** antes del 15/11/2026, el 100 % de las afirmaciones fiscales de la web tendrá fuente primaria enlazada y revisión de un asesor colegiado, y 0 afirmaciones de «cumplimiento VERI*FACTU» que no estén respaldadas por la declaración responsable firmada.
- **O2 (medición):** antes del 17/11/2026, el 100 % de los registros tendrá el first-touch guardado en `user_acquisition` y el embudo orgánico → registro → pago será visible en Looker Studio.
- **O3 (visibilidad):** antes del 18/04/2027, 25.000 impresiones no marca al mes en GSC y 20 keywords del cluster VERI*FACTU o factura electrónica en el top 10 de Google España (SE Ranking).
- **O4 (negocio, previsión):** antes del 18/10/2027, 100 registros orgánicos al mes y 10 altas de pago orgánicas al mes, medidos en Supabase.

---

## Anexo — Fuentes consultadas (18/10/2026)
- RD 1007/2023, consolidado: https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840
- RD-ley 15/2025: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-24446
- RD 254/2025: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-6600
- Orden HAC/1177/2024: https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138
- Nota de Hacienda, 05/10/2026: https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf
- Sede AEAT VERI*FACTU (actualizada a 14/10/2026): https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html
- Nota de la AEAT sobre la ampliación de plazos (RD-ley 15/2025): https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html
- RD 238/2026: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-7295 · Noticia AEAT del 31/03/2026: https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/marzo/31/facturacion-electronica-obligatoria.html · Nota AEAT: https://www3.agenciatributaria.gob.es/static_files/Sede/Actualidad/Novedades/2026/Nota_informativa_RD_Facturacion.pdf
- Orden HAC/1028/2026 (BOE 05/10/2026): https://www.boe.es/buscar/act.php?id=BOE-A-2026-20587
- Directiva (UE) 2025/516: https://eur-lex.europa.eu/eli/dir/2025/516/oj
- Orden HAC/1526/2024 (supresión del 037): https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410
- Orden PJC/297/2026 (cotización 2026): https://www.boe.es/eli/es/o/2026/03/30/pjc297
- Guía de cookies de la AEPD: https://www.aepd.es/guias/guia-cookies.pdf
- Fuentes secundarias (solo contexto): afiris.es (06/10/2026), serviciospeñas (13/10/2026), getquipu.com (Canarias), cuatrecasas.com (RD 238/2026).
