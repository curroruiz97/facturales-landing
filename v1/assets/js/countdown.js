// Countdown timer for launch offer
(function() {
    // Set end date: 30 days from first visit (stored in localStorage)
    var storageKey = 'facturales_countdown_end';
    var endTime = localStorage.getItem(storageKey);

    if (!endTime) {
        // 30 days from now
        endTime = new Date().getTime() + 30 * 24 * 60 * 60 * 1000;
        localStorage.setItem(storageKey, endTime);
    } else {
        endTime = parseInt(endTime, 10);
    }

    function updateCountdown() {
        var now = new Date().getTime();
        var diff = endTime - now;

        if (diff <= 0) {
            diff = 0;
        }

        var days = Math.floor(diff / (1000 * 60 * 60 * 24));
        var hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        var secs = Math.floor((diff % (1000 * 60)) / 1000);

        var daysEl = document.getElementById('countdown-days');
        var hoursEl = document.getElementById('countdown-hours');
        var minsEl = document.getElementById('countdown-mins');
        var secsEl = document.getElementById('countdown-secs');

        if (daysEl) daysEl.textContent = days < 10 ? '0' + days : days;
        if (hoursEl) hoursEl.textContent = hours < 10 ? '0' + hours : hours;
        if (minsEl) minsEl.textContent = mins < 10 ? '0' + mins : mins;
        if (secsEl) secsEl.textContent = secs < 10 ? '0' + secs : secs;
    }

    updateCountdown();
    setInterval(updateCountdown, 1000);
})();
