# -*- coding: utf-8 -*-
import re

# Sidebar optimizado con títulos más cortos y enlaces correctos
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
                                                        <a href="verifactu-2027-guia-autonomos-pymes.html">
                                                            <img src="assets/img/home-1/news/01.jpg" alt="VERI*FACTU 2027">
                                                        </a>
                                                    </div>
                                                    <div class="gt-recent-content">
                                                        <h5>
                                                            <a href="verifactu-2027-guia-autonomos-pymes.html">
                                                            VERI*FACTU en 2027: guía para autónomos
                                                            </a>
                                                        </h5>
                                                        <ul>
                                                            <li>
                                                                <i class="fa-solid fa-calendar-days"></i>
                                                                30 Ene, 2026
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="gt-recent-items">
                                                    <div class="gt-recent-thumb">
                                                        <a href="factura-electronica-vs-verifactu.html">
                                                            <img src="assets/img/home-1/news/02.jpg" alt="Factura Electrónica">
                                                        </a>
                                                    </div>
                                                    <div class="gt-recent-content">
                                                        <h5>
                                                            <a href="factura-electronica-vs-verifactu.html">
                                                           Factura electrónica vs VERI*FACTU
                                                            </a>
                                                        </h5>
                                                        <ul>
                                                            <li>
                                                                <i class="fa-solid fa-calendar-days"></i>
                                                                25 Ene, 2026
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="gt-recent-items">
                                                    <div class="gt-recent-thumb">
                                                        <a href="contabilidad-negocio-7-pasos.html">
                                                            <img src="assets/img/home-1/news/03.jpg" alt="Contabilidad">
                                                        </a>
                                                    </div>
                                                    <div class="gt-recent-content">
                                                        <h5>
                                                            <a href="contabilidad-negocio-7-pasos.html">
                                                            Contabilidad para tu negocio en 7 pasos
                                                            </a>
                                                        </h5>
                                                        <ul>
                                                            <li>
                                                                <i class="fa-solid fa-calendar-days"></i>
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

print("Actualizando sidebar con títulos cortos y enlaces correctos...\n")

for page in article_pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar y reemplazar todo el sidebar
        pattern = r'<div class="col-lg-4 col-12">.*?</div>\s*</div>\s*</div>\s*</div>'
        
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, correct_sidebar, content, flags=re.DOTALL)
            
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] {page}")
        else:
            print(f"[INFO] {page} - Patrón no encontrado, intentando patrón alternativo")
            # Patrón alternativo más simple
            pattern2 = r'(<div class="col-lg-4 col-12">).*?(</div>\s*</div>\s*</div>)(?=\s*</div>\s*</div>\s*</section>)'
            if re.search(pattern2, content, re.DOTALL):
                content = re.sub(pattern2, correct_sidebar, content, flags=re.DOTALL)
                with open(page, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"[OK] {page} - Actualizado con patrón alternativo")
        
    except Exception as e:
        print(f"[ERROR] {page}: {e}")

print("\nSidebar actualizado correctamente!")
print("- Titulos acortados para no salirse del recuadro")
print("- Enlaces clickeables en imagenes y titulos")
print("- Todas las categorias y etiquetas redirigen a news-grid.html")
