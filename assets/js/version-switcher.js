/*
 * Conmutador v1 / v2 (temporal): alterna entre la landing anterior (v1/) y la actual (v2) en la misma página, para comparar a ojo
 * lo que ha cambiado. Ver «Conmutador v1/v2» en CLAUDE.md.
 *
 *  - v1 = copia congelada de la landing de `add-template` antes de las olas de cambios (carpeta v1/, ver v1/SOURCE.txt).
 *  - v2 = el sitio actual.
 *  - Mantiene la página (index.html ↔ v1/index.html, pricing.html ↔ v1/pricing.html…), la búsqueda y el hash. Si la otra versión no
 *    tiene esa página (el v1 tenía 13 páginas de plantilla que ya no existen), va a su portada.
 *  - No se muestra en facturales.es, donde además v1/ redirige al sitio actual.
 *  - La píldora se arrastra por el asa de la izquierda y recuerda dónde la dejas.
 *
 * Sin dependencias. Se carga igual desde las páginas del v2 (assets/js/…) y del v1 (../assets/js/…): la raíz del sitio se deduce de
 * la URL del propio script, así que funciona también si el sitio cuelga de una subruta.
 */
(function () {
  'use strict';

  if (window.__facturalesVersionSwitcher) return;
  window.__facturalesVersionSwitcher = true;

  if (/^(www\.)?facturales\.es$/i.test(location.hostname)) return;

  var script = document.currentScript;
  if (!script || !script.src) return;

  var POSITION_KEY = 'facturales-compare-position';
  var MARGIN = 4;
  // Páginas que existen en las dos versiones (sin la extensión: el sitio se puede servir con URL limpias).
  var SHARED = ['', 'index', '404', 'contabilidad-negocio-7-pasos', 'crea-envia-facturas', 'crea-envia-presupuestos', 'escanea-gastos',
    'factura-electronica-vs-verifactu', 'factura-personalizada', 'faq', 'gestiona-clientes', 'news-grid', 'pricing',
    'service-details', 'tu-negocio-bajo-control', 'verifactu-2027-guia-autonomos-pymes'];
  var VERSIONS = [
    { id: 'v1', label: 'v1, versión anterior a los cambios' },
    { id: 'v2', label: 'v2, versión con los cambios' }
  ];

  var site = new URL('../../', script.src);
  var v1Site = new URL('v1/', site);
  var here = new URL(location.href);
  var current = here.href.indexOf(v1Site.href) === 0 ? 'v1' : 'v2';
  var rel = here.pathname.slice((current === 'v1' ? v1Site : site).pathname.length);
  var shared = SHARED.indexOf(rel.replace(/\.html$/, '')) !== -1;

  function choose(next) {
    if (next === current) return;
    var base = next === 'v1' ? v1Site : site;
    location.assign(base.href + (shared ? rel + here.search + here.hash : ''));
  }

  var style = document.createElement('style');
  style.id = 'fv-switch-style';
  style.textContent = [
    '.fv-switch{position:fixed;left:12px;bottom:12px;z-index:99999;display:inline-flex;align-items:center;gap:2px;padding:3px 3px 3px 0;',
    'border-radius:999px;background:#111827;box-shadow:0 0 0 1px rgba(255,255,255,.22),0 2px 10px rgba(0,0,0,.35);font:600 12px/1 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;',
    'letter-spacing:.02em;-webkit-text-size-adjust:100%}',
    '.fv-grip{box-sizing:border-box;width:24px;height:32px;padding:7px 6px;cursor:grab;touch-action:none;background-clip:content-box;',
    'background-image:radial-gradient(circle,#9ca3af 1.3px,transparent 1.7px);background-size:6px 6px}',
    '.fv-switch.fv-dragging,.fv-switch.fv-dragging .fv-grip{cursor:grabbing}',
    '.fv-switch button{all:unset;box-sizing:border-box;min-width:44px;height:32px;padding:0 12px;border-radius:999px;display:inline-flex;',
    'align-items:center;justify-content:center;cursor:pointer;color:#d1d5db;text-align:center}',
    '.fv-switch button:hover{color:#fff;background:rgba(255,255,255,.14)}',
    '.fv-switch button[aria-pressed="true"]{background:#fff;color:#111827;cursor:default}',
    '.fv-switch button:focus-visible{outline:2px solid #fff;outline-offset:2px;box-shadow:0 0 0 4px #111827}',
    '@media (max-width:575px){.fv-switch button{height:44px;min-width:48px}.fv-grip{height:44px;padding:13px 6px}}',
    '@media print{.fv-switch{display:none}}'
  ].join('');
  document.head.appendChild(style);

  var root = document.createElement('div');
  root.className = 'fv-switch';
  root.setAttribute('role', 'group');
  root.setAttribute('aria-label', 'Versión de la landing');

  var grip = document.createElement('span');
  grip.className = 'fv-grip';
  grip.setAttribute('aria-hidden', 'true');
  grip.title = 'Arrastra para mover';
  root.appendChild(grip);

  VERSIONS.forEach(function (version) {
    var button = document.createElement('button');
    button.type = 'button';
    button.textContent = version.id;
    button.title = version.label;
    button.setAttribute('aria-label', version.label);
    button.setAttribute('aria-pressed', version.id === current ? 'true' : 'false');
    button.addEventListener('click', function () { choose(version.id); });
    root.appendChild(button);
  });

  document.body.appendChild(root);

  /* Posición: arrastrable y recordada (localStorage puede no estar disponible: nada se rompe sin él). */
  function clamp(value, max) {
    return Math.max(MARGIN, Math.min(value, Math.max(MARGIN, max)));
  }

  function place(left, top) {
    root.style.left = clamp(left, window.innerWidth - root.offsetWidth - MARGIN) + 'px';
    root.style.top = clamp(top, window.innerHeight - root.offsetHeight - MARGIN) + 'px';
    root.style.bottom = 'auto';
  }

  function remember() {
    try {
      var rect = root.getBoundingClientRect();
      localStorage.setItem(POSITION_KEY, JSON.stringify({ left: rect.left, top: rect.top }));
    } catch (error) { /* sin almacenamiento: la posición no se recuerda */ }
  }

  try {
    var saved = JSON.parse(localStorage.getItem(POSITION_KEY) || 'null');
    if (saved && typeof saved.left === 'number' && typeof saved.top === 'number') place(saved.left, saved.top);
  } catch (error) { /* posición guardada ilegible: se queda la de por defecto */ }

  window.addEventListener('resize', function () {
    if (root.style.top) place(root.getBoundingClientRect().left, root.getBoundingClientRect().top);
  });

  grip.addEventListener('pointerdown', function (event) {
    if (event.button !== undefined && event.button !== 0) return;
    var rect = root.getBoundingClientRect();
    var offsetX = event.clientX - rect.left;
    var offsetY = event.clientY - rect.top;
    root.classList.add('fv-dragging');
    grip.setPointerCapture(event.pointerId);

    function move(moveEvent) { place(moveEvent.clientX - offsetX, moveEvent.clientY - offsetY); }
    function stop() {
      grip.removeEventListener('pointermove', move);
      grip.removeEventListener('pointerup', stop);
      grip.removeEventListener('pointercancel', stop);
      root.classList.remove('fv-dragging');
      remember();
    }
    grip.addEventListener('pointermove', move);
    grip.addEventListener('pointerup', stop);
    grip.addEventListener('pointercancel', stop);
    event.preventDefault();
  });
})();
