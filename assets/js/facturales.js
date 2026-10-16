/* Facturales · comportamiento de la landing (sin dependencias).
   - Cabecera: estado al hacer scroll, menú «Producto» y menú móvil accesibles (teclado, aria-expanded, foco).
   - Precios: conmutador mensual/anual.
   - Contacto: compone un correo con los datos del formulario (no hay servidor de formularios).
   Respeta prefers-reduced-motion (las transiciones viven en CSS y se anulan allí). */
(function () {
  "use strict";

  var header = document.getElementById("fx-header");
  var cuerpo = document.body;

  /* ---------- Cabecera al hacer scroll ---------- */
  function alScroll() {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 8);
  }
  alScroll();
  window.addEventListener("scroll", alScroll, { passive: true });

  /* ---------- Menú «Producto» (escritorio) ---------- */
  var prodBtn = document.getElementById("fx-producto-btn");
  var mega = document.getElementById("fx-mega");

  function abrirMega(abrir, enfocar) {
    if (!prodBtn || !mega) return;
    prodBtn.setAttribute("aria-expanded", abrir ? "true" : "false");
    mega.classList.toggle("is-open", abrir);
    if (abrir && enfocar) {
      var primero = mega.querySelector("a");
      if (primero) primero.focus();
    }
  }
  if (prodBtn && mega) {
    prodBtn.addEventListener("click", function () {
      abrirMega(prodBtn.getAttribute("aria-expanded") !== "true", false);
    });
    prodBtn.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown") { e.preventDefault(); abrirMega(true, true); }
    });
    mega.addEventListener("keydown", function (e) {
      var items = Array.prototype.slice.call(mega.querySelectorAll("a"));
      var i = items.indexOf(document.activeElement);
      if (e.key === "Escape") { abrirMega(false); prodBtn.focus(); }
      else if (e.key === "ArrowDown" && i > -1) { e.preventDefault(); items[(i + 1) % items.length].focus(); }
      else if (e.key === "ArrowUp" && i > -1) { e.preventDefault(); items[(i - 1 + items.length) % items.length].focus(); }
    });
    var item = prodBtn.parentNode;
    item.addEventListener("focusout", function (e) {
      if (e.relatedTarget && !item.contains(e.relatedTarget)) abrirMega(false);
    });
    document.addEventListener("click", function (e) {
      if (!item.contains(e.target)) abrirMega(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && prodBtn.getAttribute("aria-expanded") === "true") { abrirMega(false); prodBtn.focus(); }
    });
  }

  /* ---------- Menú móvil ---------- */
  var menuBtn = document.getElementById("fx-menu-btn");
  var movil = document.getElementById("fx-movilnav");

  function enfocables() {
    var sel = 'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])';
    var lista = [];
    if (header) lista = lista.concat(Array.prototype.slice.call(header.querySelectorAll(sel)));
    if (movil) lista = lista.concat(Array.prototype.slice.call(movil.querySelectorAll(sel)));
    return lista.filter(function (el) { return el.offsetParent !== null || el === menuBtn; });
  }
  function abrirMovil(abrir) {
    if (!menuBtn || !movil) return;
    menuBtn.setAttribute("aria-expanded", abrir ? "true" : "false");
    menuBtn.setAttribute("aria-label", abrir ? "Cerrar menú" : "Abrir menú");
    movil.hidden = !abrir;
    cuerpo.classList.toggle("fx-bloqueo", abrir);
    if (header) header.classList.toggle("is-open", abrir);
    if (abrir) {
      var primero = movil.querySelector("a");
      if (primero) primero.focus();
    }
  }
  if (menuBtn && movil) {
    menuBtn.addEventListener("click", function () {
      var abierto = menuBtn.getAttribute("aria-expanded") === "true";
      abrirMovil(!abierto);
      if (abierto) menuBtn.focus();
    });
    document.addEventListener("keydown", function (e) {
      if (menuBtn.getAttribute("aria-expanded") !== "true") return;
      if (e.key === "Escape") { abrirMovil(false); menuBtn.focus(); return; }
      if (e.key === "Tab") {
        var lista = enfocables();
        if (!lista.length) return;
        var primero = lista[0], ultimo = lista[lista.length - 1];
        if (e.shiftKey && document.activeElement === primero) { e.preventDefault(); ultimo.focus(); }
        else if (!e.shiftKey && document.activeElement === ultimo) { e.preventDefault(); primero.focus(); }
      }
    });
    movil.addEventListener("click", function (e) {
      if (e.target.closest && e.target.closest("a")) abrirMovil(false);
    });
    var mq = window.matchMedia("(min-width: 1080px)");
    var alCambiar = function () { if (mq.matches) abrirMovil(false); };
    if (mq.addEventListener) mq.addEventListener("change", alCambiar); else if (mq.addListener) mq.addListener(alCambiar);
  }

  /* ---------- Año del pie ---------- */
  var anio = document.querySelectorAll("[data-fx-anio]");
  for (var a = 0; a < anio.length; a++) anio[a].textContent = String(new Date().getFullYear());

  /* ---------- Precios: mensual / anual ---------- */
  var conmutador = document.querySelector("[data-fx-periodo]");
  if (conmutador) {
    var botonesPeriodo = conmutador.querySelectorAll("button[data-periodo]");
    var aplicar = function (periodo) {
      for (var b = 0; b < botonesPeriodo.length; b++) {
        botonesPeriodo[b].setAttribute("aria-pressed", botonesPeriodo[b].getAttribute("data-periodo") === periodo ? "true" : "false");
      }
      var precios = document.querySelectorAll("[data-mensual][data-anual]");
      for (var p = 0; p < precios.length; p++) precios[p].textContent = precios[p].getAttribute(periodo === "anual" ? "data-anual" : "data-mensual");
      var notas = document.querySelectorAll("[data-nota-mensual][data-nota-anual]");
      for (var n = 0; n < notas.length; n++) notas[n].textContent = notas[n].getAttribute(periodo === "anual" ? "data-nota-anual" : "data-nota-mensual");
      try { localStorage.setItem("fx-periodo", periodo); } catch (e) {}
    };
    for (var c = 0; c < botonesPeriodo.length; c++) {
      botonesPeriodo[c].addEventListener("click", function () { aplicar(this.getAttribute("data-periodo")); });
    }
    var guardado = null;
    try { guardado = localStorage.getItem("fx-periodo"); } catch (e) {}
    if (guardado === "mensual" || guardado === "anual") aplicar(guardado);
  }

  /* ---------- Contacto: compone el correo ---------- */
  var form = document.getElementById("fx-contacto");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var estado = document.getElementById("fx-contacto-estado");
      var campos = ["nombre", "email", "mensaje"];
      var valido = true;
      for (var i = 0; i < campos.length; i++) {
        var el = form.elements[campos[i]];
        var ok = el && el.value.trim() !== "" && (el.type !== "email" || /.+@.+\..+/.test(el.value));
        el.setAttribute("aria-invalid", ok ? "false" : "true");
        if (!ok && valido) { el.focus(); valido = false; }
      }
      var privacidad = form.elements["privacidad"];
      if (valido && privacidad && !privacidad.checked) { privacidad.focus(); valido = false; }
      if (!valido) { estado.textContent = "Revisa los campos marcados: nombre, correo y mensaje son obligatorios, y debes aceptar la política de privacidad."; return; }
      var destino = form.elements["motivo"].value === "soporte" ? "soporte@facturales.es" : "info@facturales.es";
      var asunto = "[Web] " + (form.elements["motivo"].options[form.elements["motivo"].selectedIndex].text) + " · " + form.elements["nombre"].value.trim();
      var texto = form.elements["mensaje"].value.trim() + "\n\n— " + form.elements["nombre"].value.trim() + " (" + form.elements["email"].value.trim() + ")" + (form.elements["empresa"].value.trim() ? "\n" + form.elements["empresa"].value.trim() : "");
      window.location.href = "mailto:" + destino + "?subject=" + encodeURIComponent(asunto) + "&body=" + encodeURIComponent(texto);
      estado.textContent = "Hemos abierto tu programa de correo con el mensaje preparado. Si no se abre, escríbenos directamente a " + destino + ".";
    });
  }
})();
