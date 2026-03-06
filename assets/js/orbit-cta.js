(function() {
    var container = document.getElementById("facturales-orbit");
    var cta = document.getElementById("facturales-cta");
    if (!container || !cta) return;

    var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

    function updateResponsiveVars() {
        var width = container.clientWidth;
        var uiScale = Math.max(0.62, Math.min(1.18, width / 600));
        var ctaScale = Math.max(0.9, Math.min(1.35, width / 600));
        container.style.setProperty("--ui-scale", uiScale.toFixed(3));
        container.style.setProperty("--cta-scale", ctaScale.toFixed(3));
    }

    var resizeObserver = new ResizeObserver(updateResponsiveVars);
    resizeObserver.observe(container);
    updateResponsiveVars();

    if (!prefersReducedMotion.matches) {
        cta.addEventListener("mousemove", function(e) {
            var rect = cta.getBoundingClientRect();
            var px = (e.clientX - rect.left) / rect.width;
            var py = (e.clientY - rect.top) / rect.height;
            var rx = (0.5 - py) * 10;
            var ry = (px - 0.5) * 14;
            cta.style.setProperty("--rx", rx.toFixed(2) + "deg");
            cta.style.setProperty("--ry", ry.toFixed(2) + "deg");
            cta.style.setProperty("--mx", (px * 100).toFixed(2) + "%");
            cta.style.setProperty("--my", (py * 100).toFixed(2) + "%");
        });

        cta.addEventListener("mouseleave", function() {
            cta.style.setProperty("--rx", "0deg");
            cta.style.setProperty("--ry", "0deg");
            cta.style.setProperty("--mx", "50%");
            cta.style.setProperty("--my", "50%");
        });
    }
})();