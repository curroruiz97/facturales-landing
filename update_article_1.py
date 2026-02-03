# -*- coding: utf-8 -*-
import re

print("Actualizando artículo 1: VERI*FACTU 2027...")

with open('verifactu-2027-guia-autonomos-pymes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Actualizar breadcrumb
content = content.replace(
    '<h1 class="text-white wow fadeInUp" data-wow-delay=".3s">Blog Facturales</h1>',
    '<h1 class="text-white wow fadeInUp" data-wow-delay=".3s">Blog Facturales</h1>'
)
content = content.replace(
    '<li>\n                                    Artículo\n                                </li>',
    '<li>\n                                    VERI*FACTU 2027\n                                </li>'
)

# 2. Actualizar fecha, autor y categoría
content = content.replace('por Facturales', 'por Facturales')
content = re.sub(
    r'<i class="fa-solid fa-calendar-days"></i>\s*\d{1,2}\s+\w+,\s+\d{4}',
    '<i class="fa-solid fa-calendar-days"></i>\n                                                        30 Ene, 2026',
    content,
    count=1
)
content = re.sub(
    r'<i class="fa-solid fa-tag"></i>\s*\w+',
    '<i class="fa-solid fa-tag"></i>\n                                                       VeriFactu',
    content,
    count=1
)

# 3. Actualizar título del artículo
content = re.sub(
    r'<h3>.*?</h3>',
    '<h3>VERI*FACTU en 2027: qué es, a quién afecta y cómo prepararte sin perder tiempo (guía para autónomos y pymes)</h3>',
    content,
    count=1,
    flags=re.DOTALL
)

# 4. Reemplazar contenido del artículo (desde el primer <p> después del <h3> hasta antes de tag-share-wrap)
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

pattern = r'(<h3>.*?</h3>)(.*?)(<div class="row tag-share-wrap)'
content = re.sub(pattern, r'\1' + article_content + r'\3', content, flags=re.DOTALL)

# 5. Actualizar etiquetas
old_tags = '''<div class="tagcloud">                                   
                                                    <a href="news-grid.html">News</a>
                                                    <a href="news-grid.html">business</a>
                                                    <a href="news-grid.html">marketing</a>
                                                </div>'''
new_tags = '''<div class="tagcloud">                                   
                                                    <a href="news-grid.html">verifactu</a>
                                                    <a href="news-grid.html">facturación</a>
                                                    <a href="news-grid.html">autónomos</a>
                                                    <a href="news-grid.html">pymes</a>
                                                    <a href="news-grid.html">AEAT</a>
                                                </div>'''
content = content.replace(old_tags, new_tags)

# 6. Eliminar comentarios
pattern_comments = r'<div class="comments-area">.*?</div>\s*</div>\s*</div>\s*'
content = re.sub(pattern_comments, '', content, flags=re.DOTALL)

pattern_form = r'<div class="comment-form-wrap">.*?</form>\s*</div>\s*'
content = re.sub(pattern_form, '', content, flags=re.DOTALL)

# Actualizar títulos del sidebar
content = content.replace('VERI*FACTU en 2027: guía para autónomos', 'VERI*FACTU en 2027: guía para autónomos')
content = content.replace('Factura electrónica vs VERI*FACTU', 'Factura electrónica vs VERI*FACTU')
content = content.replace('Contabilidad para tu negocio en 7 pasos', 'Contabilidad para tu negocio en 7 pasos')

with open('verifactu-2027-guia-autonomos-pymes.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] Artículo 1 actualizado correctamente")
