/*
 * Facturales: comportamiento común de todas las páginas (JavaScript propio, sin dependencias).
 *
 *  - Cabecera: clase "sticky" al hacer scroll y submenú de Servicios accesible por teclado.
 *  - Panel de navegación móvil: botón con aria-expanded, foco atrapado, Escape, fondo inerte.
 *  - Botón "Volver arriba" y punto del cursor (solo con puntero fino y sin movimiento reducido).
 *  - Revelado de elementos (WOW, .text-anims) respetando prefers-reduced-motion.
 *
 * Lo específico de la home (animaciones GSAP y carrusel) está en home.js.
 */
(function () {
  'use strict';

  var doc = document;
  var root = doc.documentElement;
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function $(sel, ctx) { return (ctx || doc).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || doc).querySelectorAll(sel)); }

  /* ------------------------------------------------------------------
     Cabecera pegajosa y botón "Volver arriba"
  ------------------------------------------------------------------ */
  var header = $('#header-sticky');
  var backTop = $('#back-top');
  var ticking = false;

  function onScroll() {
    if (ticking) { return; }
    ticking = true;
    window.requestAnimationFrame(function () {
      var y = window.pageYOffset || root.scrollTop;
      if (header) { header.classList.toggle('sticky', y > 250); }
      if (backTop) { backTop.classList.toggle('show', y > window.innerHeight); }
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (backTop) {
    backTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  }

  /* ------------------------------------------------------------------
     Submenú de Servicios (escritorio): ratón y teclado
  ------------------------------------------------------------------ */
  $$('.main-menu li.has-dropdown').forEach(function (li) {
    var link = $('a[aria-haspopup]', li);
    if (!link) { return; }
    function setOpen(open) { link.setAttribute('aria-expanded', open ? 'true' : 'false'); }

    li.addEventListener('mouseenter', function () { li.classList.remove('submenu-dismissed'); setOpen(true); });
    li.addEventListener('mouseleave', function () { li.classList.remove('submenu-dismissed'); setOpen(false); });
    li.addEventListener('focusin', function () { if (!li.classList.contains('submenu-dismissed')) { setOpen(true); } });
    li.addEventListener('focusout', function (e) {
      if (!li.contains(e.relatedTarget)) { li.classList.remove('submenu-dismissed'); setOpen(false); }
    });
    li.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && link.getAttribute('aria-expanded') === 'true') {
        li.classList.add('submenu-dismissed');
        setOpen(false);
        link.focus();
      }
    });
  });

  /* ------------------------------------------------------------------
     Panel de navegación móvil
  ------------------------------------------------------------------ */
  var panel = $('#mobile-nav');
  var toggle = $('.sidebar__toggle');
  var overlay = $('.offcanvas__overlay');
  var closeBtn = panel ? $('.offcanvas__close', panel) : null;
  var lastFocus = null;
  var backgroundEls = [];

  function focusables() {
    return $$('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])', panel).filter(function (el) {
      return el.offsetParent !== null && !el.closest('[hidden]');
    });
  }

  function setBackground(inert) {
    backgroundEls.forEach(function (el) {
      if (inert) { el.setAttribute('aria-hidden', 'true'); } else { el.removeAttribute('aria-hidden'); }
      el.inert = inert;
    });
  }

  function openMenu() {
    if (!panel || panel.classList.contains('info-open')) { return; }
    lastFocus = doc.activeElement;
    backgroundEls = Array.prototype.filter.call(doc.body.children, function (el) {
      return el !== panel.parentNode && el !== overlay && el.tagName !== 'SCRIPT' && el.tagName !== 'LINK' && el.tagName !== 'STYLE';
    });
    panel.inert = false;
    panel.removeAttribute('inert');
    panel.setAttribute('aria-hidden', 'false');
    panel.classList.add('info-open');
    if (overlay) { overlay.classList.add('overlay-open'); }
    if (toggle) { toggle.setAttribute('aria-expanded', 'true'); }
    root.classList.add('offcanvas-open');
    setBackground(true);
    // Foco en el botón de cerrar (si el navegador aún no lo ve visible, en el propio panel)
    if (closeBtn) { closeBtn.focus(); }
    if (!closeBtn || doc.activeElement !== closeBtn) { panel.focus({ preventScroll: true }); }
  }

  function closeMenu(restoreFocus) {
    if (!panel || !panel.classList.contains('info-open')) { return; }
    panel.classList.remove('info-open');
    if (overlay) { overlay.classList.remove('overlay-open'); }
    if (toggle) { toggle.setAttribute('aria-expanded', 'false'); }
    root.classList.remove('offcanvas-open');
    setBackground(false);
    panel.setAttribute('aria-hidden', 'true');
    panel.inert = true;
    panel.setAttribute('inert', '');
    if (restoreFocus !== false) { (lastFocus && lastFocus.focus ? lastFocus : toggle).focus(); }
  }

  if (panel && toggle) {
    toggle.addEventListener('click', openMenu);
    if (closeBtn) { closeBtn.addEventListener('click', function () { closeMenu(true); }); }
    if (overlay) { overlay.addEventListener('click', function () { closeMenu(true); }); }

    doc.addEventListener('keydown', function (e) {
      if (!panel.classList.contains('info-open')) { return; }
      if (e.key === 'Escape') { e.preventDefault(); closeMenu(true); return; }
      if (e.key !== 'Tab') { return; }
      var items = focusables();
      if (!items.length) { return; }
      var first = items[0];
      var last = items[items.length - 1];
      if (e.shiftKey && (doc.activeElement === first || !panel.contains(doc.activeElement))) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && (doc.activeElement === last || !panel.contains(doc.activeElement))) { e.preventDefault(); first.focus(); }
    });

    // Al pasar a escritorio el panel deja de tener sentido
    if (window.matchMedia) {
      var desktop = window.matchMedia('(min-width: 1200px)');
      var onChange = function (e) { if (e.matches) { closeMenu(false); } };
      if (desktop.addEventListener) { desktop.addEventListener('change', onChange); } else if (desktop.addListener) { desktop.addListener(onChange); }
    }
    // Al volver con el botón "atrás" el panel puede restaurarse abierto
    window.addEventListener('pageshow', function (e) { if (e.persisted) { closeMenu(false); } });
  }

  // Submenú de Servicios dentro del panel móvil
  $$('.mobile-sub-toggle').forEach(function (btn) {
    var list = doc.getElementById(btn.getAttribute('aria-controls'));
    if (!list) { return; }
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', open ? 'false' : 'true');
      btn.setAttribute('aria-label', open ? 'Mostrar los servicios' : 'Ocultar los servicios');
      list.hidden = open;
    });
  });

  /* ------------------------------------------------------------------
     Cursor decorativo: solo con puntero fino, pantalla ancha y sin movimiento reducido
  ------------------------------------------------------------------ */
  var cursorInner = $('.cursor-inner');
  var cursorOuter = $('.cursor-outer');
  if (cursorInner && cursorOuter && !reduceMotion && window.matchMedia &&
      window.matchMedia('(min-width: 1200px) and (pointer: fine)').matches) {
    var shown = false;
    window.addEventListener('mousemove', function (e) {
      if (!shown) {
        // El punto aparece al mover el ratón (antes se veía fijo en la esquina)
        shown = true;
        cursorInner.style.visibility = 'visible';
        cursorOuter.style.visibility = 'visible';
      }
      var t = 'translate(' + e.clientX + 'px, ' + e.clientY + 'px)';
      cursorOuter.style.transform = t;
      cursorInner.style.transform = t;
    }, { passive: true });
    doc.body.addEventListener('mouseover', function (e) {
      var hover = !!(e.target.closest && e.target.closest('a, button'));
      cursorInner.classList.toggle('cursor-hover', hover);
      cursorOuter.classList.toggle('cursor-hover', hover);
    });
  }

  /* ------------------------------------------------------------------
     Revelado al hacer scroll
  ------------------------------------------------------------------ */
  var textAnims = $$('.text-anims');
  if (textAnims.length) {
    if (reduceMotion || !('IntersectionObserver' in window)) {
      textAnims.forEach(function (el) { el.classList.add('show'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) { entry.target.classList.add('show'); io.unobserve(entry.target); }
        });
      }, { threshold: 0.5 });
      textAnims.forEach(function (el) { io.observe(el); });
    }
  }

  // WOW (animate.css): con movimiento reducido los elementos se quedan visibles y quietos
  if (!reduceMotion && typeof window.WOW === 'function') { new window.WOW().init(); }

  // Los reveals de la home (home.js) se han preparado, o no hacen falta: se apaga el respaldo CSS
  // (ver "reveal-fallback" en main.css).
  if (!$('.tz-itm-anim, .text-anim, .tp_fade_anim')) { root.classList.add('reveal-ready'); }
})();
