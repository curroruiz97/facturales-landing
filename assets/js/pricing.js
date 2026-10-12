/*
 * Facturales: página de precios.
 *  - Conmutador Anual / Mensual (botones con aria-pressed dentro de un grupo).
 *  - Mostrar u ocultar las filas adicionales de la comparativa (botón con aria-expanded).
 */
(function () {
  'use strict';

  var annualBtn = document.getElementById('annualToggle');
  var monthlyBtn = document.getElementById('monthlyToggle');
  var status = document.getElementById('pricingStatus');

  function setPricing(mode) {
    var monthly = mode === 'monthly';
    annualBtn.setAttribute('aria-pressed', monthly ? 'false' : 'true');
    monthlyBtn.setAttribute('aria-pressed', monthly ? 'true' : 'false');
    Array.prototype.forEach.call(document.querySelectorAll('.price-amount'), function (el) {
      el.textContent = monthly ? el.getAttribute('data-monthly') : el.getAttribute('data-annual');
    });
    Array.prototype.forEach.call(document.querySelectorAll('.annual-note'), function (el) { el.hidden = monthly; });
    Array.prototype.forEach.call(document.querySelectorAll('.monthly-note'), function (el) { el.hidden = !monthly; });
    if (status) {
      status.textContent = monthly ? 'Mostrando los precios con facturación mensual.' : 'Mostrando los precios con facturación anual.';
    }
  }

  if (annualBtn && monthlyBtn) {
    annualBtn.addEventListener('click', function () { setPricing('annual'); });
    monthlyBtn.addEventListener('click', function () { setPricing('monthly'); });
  }

  var tableBtn = document.getElementById('tableToggleBtn');
  if (tableBtn) {
    var label = tableBtn.querySelector('.table-toggle-label');
    var icon = tableBtn.querySelector('i');
    tableBtn.addEventListener('click', function () {
      var expanded = tableBtn.getAttribute('aria-expanded') === 'true';
      Array.prototype.forEach.call(document.querySelectorAll('.extra-rows'), function (row) { row.hidden = expanded; });
      tableBtn.setAttribute('aria-expanded', expanded ? 'false' : 'true');
      tableBtn.classList.toggle('expanded', !expanded);
      if (label) { label.textContent = expanded ? 'Mostrar todas las funcionalidades' : 'Ocultar funcionalidades'; }
      if (icon) { icon.className = 'fa-solid ' + (expanded ? 'fa-chevron-down' : 'fa-chevron-up'); }
    });
  }
})();
