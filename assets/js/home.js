/*
 * Facturales: efectos de la home (carrusel de servicios y animaciones GSAP).
 * Se carga solo en index.html, después de gsap, ScrollTrigger, SplitText y Swiper.
 *
 * Con prefers-reduced-motion no se crea ninguna animación de scroll: los titulares y las
 * tarjetas se quedan visibles y quietos.
 */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ------------------------------------------------------------------
     Carrusel de servicios: sin reproducción automática, con teclado y etiquetas
  ------------------------------------------------------------------ */
  if (window.Swiper && document.querySelector('.service-slider')) {
    new window.Swiper('.service-slider', {
      spaceBetween: 30,
      speed: reduceMotion ? 0 : 500,
      watchOverflow: true,
      keyboard: { enabled: true },
      a11y: {
        prevSlideMessage: 'Servicios anteriores',
        nextSlideMessage: 'Servicios siguientes',
        paginationBulletMessage: 'Ir al grupo de servicios {{index}}',
        slideLabelMessage: 'Servicio {{index}} de {{slidesLength}}'
      },
      navigation: { nextEl: '.array-next', prevEl: '.array-prev' },
      pagination: { el: '.dot', clickable: true },
      breakpoints: {
        0: { slidesPerView: 1 },
        575: { slidesPerView: 1 },
        767: { slidesPerView: 2 },
        991: { slidesPerView: 3 },
        1199: { slidesPerView: 4 },
        1399: { slidesPerView: 5 }
      }
    });
  }

  /* ------------------------------------------------------------------
     Animaciones GSAP (solo sin movimiento reducido)
  ------------------------------------------------------------------ */
  if (!reduceMotion && window.gsap && window.ScrollTrigger && window.SplitText) {
    var gsap = window.gsap;
    var ScrollTrigger = window.ScrollTrigger;
    gsap.registerPlugin(ScrollTrigger, window.SplitText);
    gsap.config({ nullTargetWarn: false });

    // SplitText (versión sin opción aria) parte el titular en un <div> por línea, palabra y letra: se expone el texto
    // completo en aria-label (son titulares h2) y se oculta el desglose a las tecnologías de apoyo.
    function splitHeading(element, options) {
      var label = (element.textContent || '').replace(/\s+/g, ' ').trim();
      var split = new window.SplitText(element, options);
      if (label) { element.setAttribute('aria-label', label); }
      Array.prototype.forEach.call(element.children, function (child) { child.setAttribute('aria-hidden', 'true'); });
      return split;
    }

    // Titulares .text-anim: los caracteres entran al llegar a la vista
    document.querySelectorAll('.text-anim').forEach(function (element) {
      var split = splitHeading(element, { type: 'chars, words' });
      ScrollTrigger.create({
        trigger: element,
        start: 'top 85%',
        onEnter: function () {
          gsap.from(split.chars, { duration: 1, delay: 0.1, x: 20, autoAlpha: 0, stagger: 0.03, ease: 'power2.out' });
        }
      });
    });

    // Titulares .tz-itm-title: en táctil entran una vez; en escritorio avanzan con el scroll
    document.querySelectorAll('.tz-itm-title').forEach(function (el) {
      el.split = splitHeading(el, { type: 'lines,words,chars', linesClass: 'split-line' });
      if (el.classList.contains('tz-itm-anim')) {
        gsap.set(el.split.chars, { opacity: 0, x: '-7' });
      }
      if (ScrollTrigger.isTouch === 1) {
        ScrollTrigger.create({
          trigger: el,
          start: 'top 90%',
          onEnter: function () {
            gsap.to(el.split.chars, { x: '0', y: '0', opacity: 1, duration: 0.8, stagger: 0.025, ease: 'power2.out' });
          }
        });
      } else {
        el.anim = gsap.to(el.split.chars, {
          scrollTrigger: { trigger: el, start: 'top 92%', end: 'top 60%', markers: false, scrub: 1 },
          x: '0', y: '0', opacity: 1, duration: 0.7, stagger: 0.2
        });
      }
    });

    // Los paneles de "Lo que puedes hacer" se apilan con pin solo en pantallas de 1200 px o más.
    // ScrollTrigger.matchMedia revierte por sí solo lo creado en cada consulta cuando deja de cumplirse.
    ScrollTrigger.matchMedia({
      '(min-width: 1200px)': function () {
        document.querySelectorAll('.project-panel').forEach(function (section) {
          gsap.to(section, {
            scrollTrigger: {
              trigger: section,
              pin: section,
              scrub: 1,
              start: 'top 10%',
              end: 'bottom 65%',
              endTrigger: '.project-panel-area',
              pinSpacing: false,
              markers: false
            }
          });
        });
      }
    });

    // Tarjetas de noticias: entran desde su lado
    gsap.utils.toArray('.tp_fade_anim').forEach(function (item) {
      var offset = item.getAttribute('data-fade-offset') || 40;
      var direction = item.getAttribute('data-fade-from') || 'bottom';
      gsap.from(item, {
        opacity: 0,
        ease: item.getAttribute('data-ease') || 'power2.out',
        duration: item.getAttribute('data-duration') || 0.75,
        delay: item.getAttribute('data-delay') || 0.15,
        x: direction === 'left' ? -offset : (direction === 'right' ? offset : 0),
        y: direction === 'top' ? -offset : (direction === 'bottom' ? offset : 0),
        scrollTrigger: { trigger: item, start: 'top 85%', toggleActions: 'play none none reset' }
      });
    });

    ScrollTrigger.refresh();
  }

  // Todo lo que oculta contenido hasta animarse ya está preparado (o no hace falta):
  // se apaga el respaldo CSS "reveal-fallback" de main.css.
  root.classList.add('reveal-ready');
})();
