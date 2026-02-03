# -*- coding: utf-8 -*-
import re

# Artículo 1: VERI*FACTU 2027
print("Actualizando artículo 1: VERI*FACTU 2027...")

with open('verifactu-2027-guia-autonomos-pymes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Actualizar título del breadcrumb
content = content.replace(
    '<h1 class="text-white wow fadeInUp" data-wow-delay=".3s">News Details</h1>',
    '<h1 class="text-white wow fadeInUp" data-wow-delay=".3s">Blog Facturales</h1>'
)

content = content.replace(
    'News Details',
    'VERI*FACTU 2027'
)

# Actualizar título del artículo
content = content.replace(
    '<h3>Unlocking Business Growth with Innovative Solutions</h3>',
    '<h3>VERI*FACTU en 2027: qué es, a quién afecta y cómo prepararte sin perder tiempo (guía para autónomos y pymes)</h3>'
)

# Actualizar fecha y autor
content = content.replace(
    '18 Dec, 2025',
    '03 Feb, 2026'
)

content = content.replace(
    'By Admin',
    'Por Facturales'
)

# Actualizar categoría
content = content.replace(
    'Corporate',
    'VeriFactu'
)

# Actualizar etiquetas
old_tags = '''<div class="tagcloud">                                   
                                                    <a href="news-details.html">News</a>
                                                    <a href="news-details.html">business</a>
                                                    <a href="news-details.html">marketing</a>
                                                </div>'''

new_tags = '''<div class="tagcloud">                                   
                                                    <a href="news-grid.html">verifactu</a>
                                                    <a href="news-grid.html">facturación</a>
                                                    <a href="news-grid.html">autónomos</a>
                                                    <a href="news-grid.html">pymes</a>
                                                    <a href="news-grid.html">AEAT</a>
                                                </div>'''

content = content.replace(old_tags, new_tags)

# Actualizar contenido del artículo
article_content = '''<p class="mb-3">
                                                    Si has llegado hasta aquí buscando "VERI*FACTU", "Verifactu" o "software antifraude", probablemente te pasa una de estas dos cosas:
                                                </p>
                                                <ol>
                                                    <li>Te suena que "va a ser obligatorio" y no quieres enterarte tarde.</li>
                                                    <li>Ya usas un programa para facturar y temes que no cumpla con lo que pide Hacienda.</li>
                                                </ol>
                                                <p class="mb-3">
                                                    Esta guía es para ti: te explico qué es VERI*FACTU, a quién afecta, qué cambia y cómo prepararte con un checklist práctico para no improvisar en el último momento.
                                                </p>

                                                <h4 class="mt-5 mb-3">Qué es VERI*FACTU (y qué NO es)</h4>
                                                <p class="mb-3">
                                                    VERI*FACTU no es "una factura electrónica" como tal. Es una modalidad dentro del marco que regula cómo deben funcionar los Sistemas Informáticos de Facturación (SIF).
                                                </p>
                                                <p class="mb-3">
                                                    La Agencia Tributaria contempla dos modalidades para cumplir con el reglamento de requisitos de los sistemas de facturación:
                                                </p>
                                                <ul class="mb-3">
                                                    <li>VERI*FACTU (sistemas de emisión de facturas verificables)</li>
                                                    <li>Sistemas de emisión de facturas no verificables</li>
                                                </ul>

                                                <div class="hilight-text mt-4 mb-4">
                                                    <p>La diferencia clave: En VERI*FACTU, el sistema remite online a la AEAT los registros de facturación de las facturas emitidas (de forma continuada y segura). En un sistema no verificable, esos registros no se remiten: se almacenan y el sistema debe garantizar integridad, trazabilidad, conservación, etc.</p>
                                                    <div class="icon">
                                                        <i class="fa-solid fa-quote-right"></i>
                                                    </div>
                                                </div>

                                                <h4 class="mt-5 mb-3">¿A quién afecta VERI*FACTU?</h4>
                                                <p class="mb-3">
                                                    En la práctica, afecta a quienes expiden facturas usando un software de facturación… con matices importantes.
                                                </p>
                                                <p class="mb-3">
                                                    La AEAT lo resume con la "regla de los 4 NO": estarías dentro si utilizas un SIF para emitir facturas y no estás en supuestos de exclusión (por ejemplo, no facturar exclusivamente a mano, no estar en SII, no tener domicilio fiscal en territorios forales, etc.).
                                                </p>

                                                <h4 class="mt-5 mb-3">Fechas clave: ¿cuándo será obligatorio?</h4>
                                                <p class="mb-3">Según los plazos vigentes:</p>
                                                <ul class="mb-3">
                                                    <li><strong>01/01/2027:</strong> entidades que presenten Impuesto sobre Sociedades.</li>
                                                    <li><strong>01/07/2027:</strong> el resto de obligados tributarios.</li>
                                                </ul>

                                                <h4 class="mt-5 mb-3">El detalle que mucha gente pasa por alto: el QR</h4>
                                                <p class="mb-3">
                                                    Las facturas generadas con un SIF deben llevar código QR. Según las FAQs, esto aplica tanto a VERI*FACTU como a sistemas no verificables. El QR ayuda a verificar o remitir información esencial según la modalidad.
                                                </p>

                                                <h4 class="mt-5 mb-3">VERI*FACTU vs no verificable: ¿qué te conviene?</h4>
                                                <p class="mb-3">
                                                    VERI*FACTU puede encajar si quieres automatizar remisión de registros y maximizar trazabilidad.
                                                </p>
                                                <p class="mb-3">
                                                    La modalidad no verificable puede encajar si prefieres no remitir en línea, pero exige medidas adicionales de control y conservación.
                                                </p>

                                                <h4 class="mt-5 mb-3">Checklist de preparación (30-60 minutos)</h4>
                                                <ol>
                                                    <li>Cómo facturas hoy (herramientas y canales).</li>
                                                    <li>Si estás en SII o normativa foral (TicketBAI, etc.).</li>
                                                    <li>Si tu sistema contempla QR/URL y trazabilidad.</li>
                                                    <li>Plan por fechas (enero/julio 2027 según caso).</li>
                                                    <li>Decisión de modalidad (verificable o no).</li>
                                                    <li>Software y proceso: emitir, anular, rectificar, conservar y localizar en segundos.</li>
                                                </ol>

                                                <div class="mt-5 p-4" style="background-color: #FFF0E5; border-left: 4px solid #ec8228; border-radius: 8px;">
                                                    <h5 style="color: #ec8228;">¿Quieres ver cómo centralizar facturación y contabilidad para llegar a 2027 con tranquilidad?</h5>
                                                    <p class="mb-3">Facturales te ayuda a cumplir con VERI*FACTU y gestionar tu contabilidad de forma simple y segura.</p>
                                                    <a href="contact.html" class="theme-btn" style="background: #ec8228;">Solicita una demo gratuita <i class="fa-solid fa-arrow-up-right"></i></a>
                                                </div>'''

# Buscar y reemplazar el contenido del artículo
pattern = r'(<div class="post-content">.*?<h3>.*?</h3>)(.*?)(<div class="row tag-share-wrap)'
replacement = r'\1' + article_content + r'\3'
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('verifactu-2027-guia-autonomos-pymes.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] Articulo 1 actualizado")

# Artículo 2: Factura electrónica vs VERI*FACTU
print("\nActualizando articulo 2: Factura electronica vs VERI*FACTU...")

with open('factura-electronica-vs-verifactu.html', 'r', encoding='utf-8') as f:
    content2 = f.read()

content2 = content2.replace(
    '<h1 class="text-white wow fadeInUp" data-wow-delay=".3s">News Details</h1>',
    '<h1 class="text-white wow fadeInUp" data-wow-delay=".3s">Blog Facturales</h1>'
)

content2 = content2.replace(
    'News Details',
    'Factura Electrónica'
)

content2 = content2.replace(
    '<h3>Unlocking Business Growth with Innovative Solutions</h3>',
    '<h3>Factura electrónica obligatoria vs VERI*FACTU: diferencias reales, plazos y cómo prepararte con un solo sistema</h3>'
)

content2 = content2.replace(
    '18 Dec, 2025',
    '10 Feb, 2026'
)

content2 = content2.replace(
    'By Admin',
    'Por Facturales'
)

content2 = content2.replace(
    'Corporate',
    'Facturación'
)

old_tags2 = '''<div class="tagcloud">                                   
                                                    <a href="news-details.html">News</a>
                                                    <a href="news-details.html">business</a>
                                                    <a href="news-details.html">marketing</a>
                                                </div>'''

new_tags2 = '''<div class="tagcloud">                                   
                                                    <a href="news-grid.html">factura electrónica</a>
                                                    <a href="news-grid.html">verifactu</a>
                                                    <a href="news-grid.html">B2B</a>
                                                    <a href="news-grid.html">digitalización</a>
                                                </div>'''

content2 = content2.replace(old_tags2, new_tags2)

article_content2 = '''<p class="mb-3">
                                                    En España conviven (y a veces se confunden) dos grandes "olas" de cambios en facturación:
                                                </p>
                                                <ul class="mb-3">
                                                    <li><strong>VERI*FACTU / Sistemas Informáticos de Facturación (SIF):</strong> enfoque de integridad y trazabilidad del software.</li>
                                                    <li><strong>Factura electrónica obligatoria B2B:</strong> enfoque de digitalización e intercambio entre empresas y profesionales, con estados y pagos.</li>
                                                </ul>

                                                <h4 class="mt-5 mb-3">Qué es VERI*FACTU (en una frase)</h4>
                                                <p class="mb-3">
                                                    VERI*FACTU es una modalidad de los SIF en la que el sistema remite online a la Agencia Tributaria los registros de facturación.
                                                </p>

                                                <h4 class="mt-5 mb-3">Plazos de adaptación del SIF (referencia práctica)</h4>
                                                <ul class="mb-3">
                                                    <li><strong>01/01/2027:</strong> Impuesto sobre Sociedades.</li>
                                                    <li><strong>01/07/2027:</strong> resto de obligados.</li>
                                                </ul>

                                                <h4 class="mt-5 mb-3">Qué es la factura electrónica obligatoria B2B</h4>
                                                <p class="mb-3">
                                                    La obligación B2B implica expedir, remitir y recibir factura electrónica entre empresarios/profesionales, y proporcionar información sobre estados. Su efectividad depende del desarrollo reglamentario.
                                                </p>

                                                <div class="hilight-text mt-4 mb-4">
                                                    <p>Diferencias que importan: VERI*FACTU regula cómo funciona tu sistema (registro, trazabilidad, QR/URL). Factura electrónica B2B regula el intercambio electrónico y la interoperabilidad, además de estados/pagos.</p>
                                                    <div class="icon">
                                                        <i class="fa-solid fa-quote-right"></i>
                                                    </div>
                                                </div>

                                                <h4 class="mt-5 mb-3">Estrategia recomendada: un solo flujo</h4>
                                                <ol>
                                                    <li>Unifica datos (clientes, impuestos, series, vencimientos).</li>
                                                    <li>Emite desde un sistema central (no desde 3 sitios).</li>
                                                    <li>Registra cambios (anulaciones/rectificativas) con orden.</li>
                                                    <li>Prepara salidas: QR/URL y registro; y factura electrónica B2B cuando sea exigible.</li>
                                                    <li>Conecta contabilidad: margen, IVA, tesorería, cobros y pagos.</li>
                                                </ol>

                                                <div class="mt-5 p-4" style="background-color: #FFF0E5; border-left: 4px solid #ec8228; border-radius: 8px;">
                                                    <h5 style="color: #ec8228;">¿Quieres evitar rehacer procesos y estar preparado para ambas normativas?</h5>
                                                    <p class="mb-3">Elige una herramienta que centralice facturación y contabilidad desde el primer día.</p>
                                                    <a href="contact.html" class="theme-btn" style="background: #ec8228;">Pide una demo de Facturales <i class="fa-solid fa-arrow-up-right"></i></a>
                                                </div>'''

pattern2 = r'(<div class="post-content">.*?<h3>.*?</h3>)(.*?)(<div class="row tag-share-wrap)'
replacement2 = r'\1' + article_content2 + r'\3'
content2 = re.sub(pattern2, replacement2, content2, flags=re.DOTALL)

with open('factura-electronica-vs-verifactu.html', 'w', encoding='utf-8') as f:
    f.write(content2)

print("[OK] Articulo 2 actualizado")

# Artículo 3: Contabilidad en 7 pasos
print("\nActualizando articulo 3: Contabilidad en 7 pasos...")

with open('contabilidad-negocio-7-pasos.html', 'r', encoding='utf-8') as f:
    content3 = f.read()

content3 = content3.replace(
    '<h1 class="text-white wow fadeInUp" data-wow-delay=".3s">News Details</h1>',
    '<h1 class="text-white wow fadeInUp" data-wow-delay=".3s">Blog Facturales</h1>'
)

content3 = content3.replace(
    'News Details',
    'Contabilidad para Negocios'
)

content3 = content3.replace(
    '<h3>Unlocking Business Growth with Innovative Solutions</h3>',
    '<h3>Cómo llevar la contabilidad de tu negocio (sin ser contable): método en 7 pasos + checklist mensual para autónomos y pymes</h3>'
)

content3 = content3.replace(
    '18 Dec, 2025',
    '17 Feb, 2026'
)

content3 = content3.replace(
    'By Admin',
    'Por Facturales'
)

content3 = content3.replace(
    'Corporate',
    'Contabilidad'
)

old_tags3 = '''<div class="tagcloud">                                   
                                                    <a href="news-details.html">News</a>
                                                    <a href="news-details.html">business</a>
                                                    <a href="news-details.html">marketing</a>
                                                </div>'''

new_tags3 = '''<div class="tagcloud">                                   
                                                    <a href="news-grid.html">contabilidad</a>
                                                    <a href="news-grid.html">autónomos</a>
                                                    <a href="news-grid.html">pymes</a>
                                                    <a href="news-grid.html">gestión financiera</a>
                                                </div>'''

content3 = content3.replace(old_tags3, new_tags3)

article_content3 = '''<p class="mb-3">
                                                    Llevar la contabilidad a última hora no es solo estresante: es caro. Caro en tiempo, caro en errores y caro en decisiones.
                                                </p>
                                                <p class="mb-3">
                                                    Este método en 7 pasos te ayuda a mantener el negocio ordenado sin volverte contable.
                                                </p>

                                                <h4 class="mt-5 mb-3">Paso 1) Separa tu dinero personal del negocio</h4>
                                                <p class="mb-3">
                                                    Cuenta bancaria y tarjeta de negocio. Evita mezclas.
                                                </p>

                                                <h4 class="mt-5 mb-3">Paso 2) Define categorías claras</h4>
                                                <p class="mb-3">
                                                    Ingresos, gastos fijos, gastos variables, impuestos, colaboradores. Si dudas cada mes, ajusta categorías.
                                                </p>

                                                <h4 class="mt-5 mb-3">Paso 3) Registra semanalmente</h4>
                                                <p class="mb-3">
                                                    Rutina de 30 minutos: sube facturas emitidas/recibidas, categoriza, revisa cobros/pagos.
                                                </p>

                                                <h4 class="mt-5 mb-3">Paso 4) Digitaliza y guarda con criterio único</h4>
                                                <p class="mb-3">
                                                    Nombre de archivo consistente y justificante asociado.
                                                </p>

                                                <h4 class="mt-5 mb-3">Paso 5) Conciliación bancaria</h4>
                                                <p class="mb-3">
                                                    Verifica que banco y contabilidad coinciden. Evita duplicidades y cobros perdidos.
                                                </p>

                                                <h4 class="mt-5 mb-3">Paso 6) Cierre mensual (mini cierre)</h4>
                                                <p class="mb-3">Checklist:</p>
                                                <ul class="mb-3">
                                                    <li>Facturas emitidas y recibidas OK</li>
                                                    <li>Tickets y gastos pequeños OK</li>
                                                    <li>Conciliación OK</li>
                                                    <li>IVA estimado revisado</li>
                                                    <li>Impuestos próximos apuntados</li>
                                                    <li>Top 5 gastos revisados</li>
                                                    <li>Facturas vencidas en seguimiento</li>
                                                </ul>

                                                <h4 class="mt-5 mb-3">Paso 7) Cuadro de mando mínimo (6 números)</h4>
                                                <p class="mb-3">
                                                    Ventas, gastos, margen bruto, IVA estimado, cobros pendientes, tesorería y previsión 30 días.
                                                </p>

                                                <div class="hilight-text mt-4 mb-4">
                                                    <p>Errores típicos: "Ya lo verá la gestoría", gastos sin método, no controlar cobros y pagos.</p>
                                                    <div class="icon">
                                                        <i class="fa-solid fa-quote-right"></i>
                                                    </div>
                                                </div>

                                                <div class="mt-5 p-4" style="background-color: #FFF0E5; border-left: 4px solid #ec8228; border-radius: 8px;">
                                                    <h5 style="color: #ec8228;">¿Quieres llevar la contabilidad sin complicarte y tenerlo todo listo cada mes?</h5>
                                                    <p class="mb-3">Facturales te permite gestionar facturas, gastos y contabilidad en un solo lugar de forma simple.</p>
                                                    <a href="contact.html" class="theme-btn" style="background: #ec8228;">Empieza con Facturales <i class="fa-solid fa-arrow-up-right"></i></a>
                                                </div>'''

pattern3 = r'(<div class="post-content">.*?<h3>.*?</h3>)(.*?)(<div class="row tag-share-wrap)'
replacement3 = r'\1' + article_content3 + r'\3'
content3 = re.sub(pattern3, replacement3, content3, flags=re.DOTALL)

with open('contabilidad-negocio-7-pasos.html', 'w', encoding='utf-8') as f:
    f.write(content3)

print("[OK] Articulo 3 actualizado")
print("\n[SUCCESS] Todos los articulos han sido actualizados correctamente!")
