(function () {
  // Cabecera común del sitio: barra de prueba, cabecera con menú de escritorio y panel móvil.
  // Se escribe de forma síncrona (document.write) para que esté en el primer pintado y sea idéntica
  // en todas las páginas. El comportamiento (abrir/cerrar el panel, submenús, foco) está en main.js.
  //
  // Raíz del sitio, deducida de la URL de este mismo script (assets/js/header-include.js):
  // los enlaces y las imágenes se escriben relativos a la raíz, de modo que el menú funciona
  // también desde rutas anidadas (p. ej. la página 404).
  var root = '';
  try { root = new URL('../../', document.currentScript.src).href; } catch (e) { root = ''; }

  // Página actual (para marcar el enlace activo con aria-current="page").
  var current = (location.pathname.split('/').pop() || 'index.html');

  var SERVICES = [
    { href: 'tu-negocio-bajo-control.html', icon: 'fa-chart-line', title: 'Tu negocio bajo control', desc: 'Panel completo de gestión empresarial' },
    { href: 'crea-envia-facturas.html', icon: 'fa-file-invoice', title: 'Crea y envía facturas', desc: 'Facturación rápida y profesional' },
    { href: 'crea-envia-presupuestos.html', icon: 'fa-file-invoice-dollar', title: 'Crea y envía presupuestos', desc: 'Presupuestos personalizados al instante' },
    { href: 'escanea-gastos.html', icon: 'fa-receipt', title: 'Escanea gastos', desc: 'Digitaliza tickets y facturas recibidas' },
    { href: 'gestiona-clientes.html', icon: 'fa-users', title: 'Gestiona clientes', desc: 'Clientes y proveedores en un solo lugar' },
    { href: 'factura-personalizada.html', icon: 'fa-palette', title: 'Personaliza tus facturas', desc: 'Diseña facturas con tu marca' }
  ];

  function cur(href) { return href === current ? ' aria-current="page"' : ''; }

  function serviceLinkDesktop(s) {
    return '<a href="' + s.href + '" class="homemenu"' + cur(s.href) + '>' +
      '<div class="homemenu-icon"><i class="fa-solid ' + s.icon + '" aria-hidden="true"></i></div>' +
      '<div class="homemenu-content"><span class="homemenu-title">' + s.title + '</span>' +
      '<p class="homemenu-desc">' + s.desc + '</p></div></a>';
  }

  function serviceLinkMobile(s) {
    return '<li><a href="' + s.href + '"' + cur(s.href) + '>' +
      '<span class="homemenu-icon"><i class="fa-solid ' + s.icon + '" aria-hidden="true"></i></span>' +
      '<span>' + s.title + '</span></a></li>';
  }

  var html = `
        <!-- Barra superior: texto fijo (sin cuenta atrás) -->
        <div class="header-top-section" role="region" aria-label="Prueba de 14 días">
            <div class="container-fluid">
                <div class="header-top-wrapper header-top-promo">
                    <p class="header-top-text"><i class="fa-solid fa-gift" aria-hidden="true"></i> 14 días de prueba gratuita · cancela cuando quieras</p>
                    <a href="https://app.facturales.es/signup" class="header-top-link">Prueba 14 días</a>
                </div>
            </div>
        </div>

        <!-- Panel de navegación móvil (cerrado: inert y oculto; se abre desde main.js) -->
        <div class="fix-area">
            <div class="offcanvas__info" id="mobile-nav" role="dialog" aria-modal="true" aria-label="Menú de navegación" aria-hidden="true" tabindex="-1" inert>
                <div class="offcanvas__wrapper">
                    <div class="offcanvas__content">
                        <div class="offcanvas__top d-flex justify-content-between align-items-center">
                            <div class="offcanvas__logo">
                                <a href="index.html">
                                    <img src="assets/img/logo/logo-color.svg" alt="Facturales" width="172" height="52">
                                </a>
                            </div>
                            <button type="button" class="offcanvas__close" aria-label="Cerrar menú">
                                <i class="fa-solid fa-xmark" aria-hidden="true"></i>
                            </button>
                        </div>
                        <nav class="mobile-menu" aria-label="Menú principal">
                            <ul class="mobile-nav">
                                <li><a href="index.html"${cur('index.html')}>Inicio</a></li>
                                <li class="mobile-has-sub">
                                    <div class="mobile-sub-row">
                                        <a href="service-details.html"${cur('service-details.html')}>Servicios</a>
                                        <button type="button" class="mobile-sub-toggle" aria-expanded="false" aria-controls="mobile-sub-servicios" aria-label="Mostrar los servicios">
                                            <i class="fa-solid fa-plus" aria-hidden="true"></i>
                                        </button>
                                    </div>
                                    <ul class="mobile-sub" id="mobile-sub-servicios" hidden>
                                        ${SERVICES.map(serviceLinkMobile).join('\n                                        ')}
                                    </ul>
                                </li>
                                <li><a href="news-grid.html"${cur('news-grid.html')}>Blog</a></li>
                                <li><a href="faq.html"${cur('faq.html')}>Preguntas frecuentes</a></li>
                                <li><a href="pricing.html"${cur('pricing.html')}>Precios</a></li>
                            </ul>
                        </nav>
                        <div class="offcanvas__buttons">
                            <a href="https://app.facturales.es/signin" class="offcanvas__btn offcanvas__btn--outline">
                                <i class="fa-solid fa-right-to-bracket" aria-hidden="true"></i> Iniciar sesión
                            </a>
                            <a href="https://app.facturales.es/signup" class="offcanvas__btn offcanvas__btn--primary">
                                Prueba 14 días <i class="fa-solid fa-arrow-up-right" aria-hidden="true"></i>
                            </a>
                        </div>
                        <div class="offcanvas__contact">
                            <ul>
                                <li class="d-flex align-items-center">
                                    <div class="offcanvas__contact-icon">
                                        <i class="fa-solid fa-envelope" aria-hidden="true"></i>
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

        <!-- Cabecera -->
        <header id="header-sticky" class="header-1">
            <div class="container-fluid">
                <div class="mega-menu-wrapper">
                    <div class="header-main">
                        <div class="header-left">
                            <div class="logo">
                                <a href="index.html" class="header-logo">
                                    <img src="assets/img/logo/logo-white.svg" alt="Facturales" width="172" height="52">
                                </a>
                                <a href="index.html" class="header-logo-2">
                                    <img src="assets/img/logo/logo-color.svg" alt="Facturales" width="172" height="52">
                                </a>
                            </div>
                        </div>
                        <div class="mean__menu-wrapper">
                            <div class="main-menu">
                                <nav id="main-nav" aria-label="Principal">
                                    <ul>
                                        <li><a href="index.html"${cur('index.html')}>Inicio</a></li>
                                        <li class="has-dropdown">
                                            <a href="service-details.html" aria-haspopup="true" aria-expanded="false"${cur('service-details.html')}>Servicios</a>
                                            <ul class="submenu has-homemenu">
                                                <li>
                                                    <div class="homemenu-items">
                                                        ${SERVICES.map(serviceLinkDesktop).join('\n                                                        ')}
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                        <li><a href="news-grid.html"${cur('news-grid.html')}>Blog</a></li>
                                        <li><a href="faq.html"${cur('faq.html')}>Preguntas frecuentes</a></li>
                                        <li class="menu-item-highlighted"><a href="pricing.html"${cur('pricing.html')}>Precios</a></li>
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
                                        Prueba 14 días <i class="fa-solid fa-arrow-up-right" aria-hidden="true"></i>
                                    </a>
                                </div>
                            </div>
                            <div class="header__hamburger d-xl-none my-auto">
                                <button type="button" class="sidebar__toggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="mobile-nav">
                                    <span class="hamburger-line"></span>
                                    <span class="hamburger-line"></span>
                                    <span class="hamburger-line"></span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>`;

  document.write(html.replace(/(href|src)="(?!https?:|mailto:|tel:|#)([^"]+)"/g, '$1="' + root + '$2"'));
})();
