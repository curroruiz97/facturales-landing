(function() {
  // Raíz del sitio, deducida de la URL de este mismo script (assets/js/header-include.js).
  // Los enlaces y las imágenes de la cabecera se escriben relativos a la raíz, de modo que
  // el menú funciona también desde rutas anidadas (p. ej. la página 404).
  var root = '';
  try { root = new URL('../../', document.currentScript.src).href; } catch (e) { root = ''; }

  var html = `
        <!-- Offcanvas Area Start -->
        <div class="fix-area">
            <div class="offcanvas__info">
                <div class="offcanvas__wrapper">
                    <div class="offcanvas__content">
                        <div class="offcanvas__top d-flex justify-content-between align-items-center">
                            <div class="offcanvas__logo">
                                <a href="index.html">
                                    <img src="assets/img/logo/logo-color.svg" alt="Facturales">
                                </a>
                            </div>
                            <div class="offcanvas__close">
                                <button>
                                    <i class="fas fa-times"></i>
                                </button>
                            </div>
                        </div>
                        <div class="mobile-menu fix"></div>
                        <div class="offcanvas__buttons">
                            <a href="https://app.facturales.es/signin" class="offcanvas__btn offcanvas__btn--outline">
                                <i class="fa-solid fa-right-to-bracket"></i> Iniciar sesión
                            </a>
                            <a href="https://app.facturales.es/signup" class="offcanvas__btn offcanvas__btn--primary">
                                Prueba 14 días <i class="fa-solid fa-arrow-up-right"></i>
                            </a>
                        </div>
                        <div class="offcanvas__contact">
                            <ul>
                                <li class="d-flex align-items-center">
                                    <div class="offcanvas__contact-icon">
                                        <i class="fal fa-envelope"></i>
                                    </div>
                                    <div class="offcanvas__contact-text">
                                        <a href="mailto:info@facturales.es">info@facturales.es</a>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="offcanvas__overlay"></div>

        <!-- Header Section Start -->
        <header id="header-sticky" class="header-1">
            <div class="container-fluid">
                <div class="mega-menu-wrapper">
                    <div class="header-main">
                        <div class="header-left">
                            <div class="logo">
                            <a href="index.html" class="header-logo">
                                <img src="assets/img/logo/logo-white.svg" alt="Facturales">
                            </a>
                            <a href="index.html" class="header-logo-2">
                                <img src="assets/img/logo/logo-color.svg" alt="Facturales">
                            </a>
                        </div>
                        </div>
                        <div class="mean__menu-wrapper">
                                <div class="main-menu">
                                    <nav id="mobile-menu">
                                        <ul>
                                            <li>
                                                <a href="index.html">
                                                    Inicio
                                                </a>
                                            </li>
                                                <li class="has-dropdown">
                                                    <a href="service-details.html">Servicios</a>
                                                  
                                                    <ul class="submenu has-homemenu">
                                                      <li>
                                                        <div class="homemenu-items">

                                                          <a href="tu-negocio-bajo-control.html" class="homemenu">
                                                            <div class="homemenu-icon">
                                                              <i class="fa-solid fa-chart-line"></i>
                                                            </div>
                                                            <div class="homemenu-content">
                                                              <h4 class="homemenu-title">Tu negocio bajo control</h4>
                                                              <p class="homemenu-desc">Panel completo de gestión empresarial</p>
                                                            </div>
                                                          </a>
                                                  
                                                          <a href="crea-envia-facturas.html" class="homemenu">
                                                            <div class="homemenu-icon">
                                                              <i class="fa-solid fa-file-invoice"></i>
                                                            </div>
                                                            <div class="homemenu-content">
                                                              <h4 class="homemenu-title">Crea y envía facturas</h4>
                                                              <p class="homemenu-desc">Facturación rápida y profesional</p>
                                                            </div>
                                                          </a>
                                                  
                                                          <a href="crea-envia-presupuestos.html" class="homemenu">
                                                            <div class="homemenu-icon">
                                                              <i class="fa-solid fa-file-invoice-dollar"></i>
                                                            </div>
                                                            <div class="homemenu-content">
                                                              <h4 class="homemenu-title">Crea y envía presupuestos</h4>
                                                              <p class="homemenu-desc">Presupuestos personalizados al instante</p>
                                                            </div>
                                                          </a>
                                                  
                                                          <a href="escanea-gastos.html" class="homemenu">
                                                            <div class="homemenu-icon">
                                                              <i class="fa-solid fa-receipt"></i>
                                                            </div>
                                                            <div class="homemenu-content">
                                                              <h4 class="homemenu-title">Escanea gastos</h4>
                                                              <p class="homemenu-desc">Digitaliza tickets y facturas recibidas</p>
                                                            </div>
                                                          </a>
                                                  
                                                          <a href="gestiona-clientes.html" class="homemenu">
                                                            <div class="homemenu-icon">
                                                              <i class="fa-solid fa-users"></i>
                                                            </div>
                                                            <div class="homemenu-content">
                                                              <h4 class="homemenu-title">Gestiona clientes</h4>
                                                              <p class="homemenu-desc">Clientes y proveedores en un solo lugar</p>
                                                            </div>
                                                          </a>
                                                  
                                                          <a href="factura-personalizada.html" class="homemenu">
                                                            <div class="homemenu-icon">
                                                              <i class="fa-solid fa-palette"></i>
                                                            </div>
                                                            <div class="homemenu-content">
                                                              <h4 class="homemenu-title">Personaliza tus facturas</h4>
                                                              <p class="homemenu-desc">Diseña facturas con tu marca</p>
                                                            </div>
                                                          </a>
                                                  
                                                  
                                                        </div>
                                                      </li>
                                                    </ul>
                                                  </li>
                                             <li>
                                                <a href="news-grid.html">Blog</a>
                                                </li>
                                                     
                                                  
                                             <li>
                                                <a href="faq.html">
                                                    Preguntas frecuentes
                                                </a>
                                            </li>
                                           <li class="menu-item-highlighted">
                                                <a href="pricing.html">
                                                    Precios
                                                </a>
                                            </li>
                                        </ul>
                                    </nav>
                                </div>
                            </div> 
                          <div class="header-right d-flex justify-content-end align-items-center">
                            <div class="header-btn">
                                <div class="header-login">
                                    <a href="https://app.facturales.es/signin">Iniciar sesión</a>
                                </div>
                                <div class="header-button">
                                    <a href="https://app.facturales.es/signup" class="theme-btn">
                                       Prueba 14 días <i class="fa-solid fa-arrow-up-right"></i>
                                    </a>
                                </div>
                            </div>
                            <div class="header__hamburger d-xl-none my-auto">
                                <div class="sidebar__toggle">
                                    <span class="hamburger-line"></span>
                                    <span class="hamburger-line"></span>
                                    <span class="hamburger-line"></span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>`;

  document.write(html.replace(/(href|src)="(?!https?:|mailto:|tel:|#)([^"]+)"/g, '$1="' + root + '$2"'));
})();
