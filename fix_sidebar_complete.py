# -*- coding: utf-8 -*-
import re

# Sidebar correcto en español con artículos reales
correct_sidebar = '''                                <div class="col-lg-4 col-12">
                                    <div class="gt-main-sideber sticky-style">
                                        <div class="gt-single-sideber-widget">
                                            <div class="gt-widget-title">
                                                <h3>Buscar</h3>
                                            </div>
                                            <div class="gt-search-widget">
                                                <form action="news-grid.html" method="get">
                                                    <input type="text" name="search" placeholder="Buscar artículos...">
                                                    <button type="submit"><i class="fa-solid fa-magnifying-glass"></i></button>
                                                </form>
                                            </div>
                                        </div>
                                        <div class="gt-single-sideber-widget">
                                            <div class="gt-widget-title">
                                                <h3>Todas las categorías</h3>
                                            </div>
                                            <ul class="gt-category-list">
                                                <li><a href="news-grid.html">Contabilidad</a><span>(3)</span></li>
                                                <li><a href="news-grid.html">Facturación</a><span>(3)</span></li>
                                                <li><a href="news-grid.html">VeriFactu</a><span>(2)</span></li>
                                                <li><a href="news-grid.html">Autónomos</a><span>(3)</span></li>
                                                <li><a href="news-grid.html">Pymes</a><span>(3)</span></li>
                                                <li><a href="news-grid.html">Gestión</a><span>(2)</span></li>
                                            </ul>
                                        </div>
                                        <div class="gt-single-sideber-widget">
                                            <div class="gt-widget-title">
                                                <h3>Artículos recientes</h3>
                                            </div>
                                            <div class="gt-recent-post-area">
                                                <div class="gt-recent-items">
                                                    <div class="gt-recent-thumb">
                                                        <img src="assets/img/home-1/news/01.jpg" alt="VERI*FACTU 2027">
                                                    </div>
                                                    <div class="gt-recent-content">
                                                        <h5>
                                                            <a href="verifactu-2027-guia-autonomos-pymes.html">
                                                            VERI*FACTU en 2027: qué es, a quién afecta y cómo prepararte
                                                            </a>
                                                        </h5>
                                                        <ul>
                                                            <li>
                                                                30 Ene, 2026
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="gt-recent-items">
                                                    <div class="gt-recent-thumb">
                                                        <img src="assets/img/home-1/news/02.jpg" alt="Factura Electrónica">
                                                    </div>
                                                    <div class="gt-recent-content">
                                                        <h5>
                                                            <a href="factura-electronica-vs-verifactu.html">
                                                           Factura electrónica vs VERI*FACTU: diferencias y plazos
                                                            </a>
                                                        </h5>
                                                        <ul>
                                                            <li>
                                                                25 Ene, 2026
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="gt-recent-items">
                                                    <div class="gt-recent-thumb">
                                                    <img src="assets/img/home-1/news/03.jpg" alt="Contabilidad">
                                                    </div>
                                                    <div class="gt-recent-content">
                                                        <h5>
                                                            <a href="contabilidad-negocio-7-pasos.html">
                                                            Cómo llevar la contabilidad de tu negocio en 7 pasos
                                                            </a>
                                                        </h5>
                                                        <ul>
                                                            <li>
                                                                15 Ene, 2026
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="gt-single-sideber-widget mb-0">
                                            <div class="gt-widget-title">
                                                <h3>Etiquetas</h3>
                                            </div>
                                            <div class="tagcloud">
                                                <a href="news-grid.html">VeriFactu</a>     
                                                <a href="news-grid.html">Facturación</a>
                                                <a href="news-grid.html">Contabilidad</a>
                                                <a href="news-grid.html">Autónomos</a>
                                                <a href="news-grid.html">Pymes</a>
                                                <a href="news-grid.html">AEAT</a>
                                                <a href="news-grid.html">Gestión</a>
                                                <a href="news-grid.html">Software</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>'''

# Páginas de artículos a procesar
article_pages = [
    'verifactu-2027-guia-autonomos-pymes.html',
    'factura-electronica-vs-verifactu.html',
    'contabilidad-negocio-7-pasos.html'
]

print("Reemplazando sidebar con la versión correcta...\n")

for page in article_pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar y reemplazar todo el sidebar desde <div class="col-lg-4 col-12"> hasta su cierre
        pattern = r'<div class="col-lg-4 col-12">.*?</div>\s*</div>\s*</div>'
        
        if re.search(pattern, content, re.DOTALL):
            # Reemplazar con el sidebar correcto
            content = re.sub(pattern, correct_sidebar, content, flags=re.DOTALL)
            
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] {page} - Sidebar reemplazado correctamente")
        else:
            print(f"[INFO] {page} - No se encontró el patrón del sidebar")
        
    except Exception as e:
        print(f"[ERROR] {page}: {e}")

print("\nProceso completado!")
