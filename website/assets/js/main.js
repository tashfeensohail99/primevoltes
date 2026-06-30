/* PrimeVolt Energy Systems — site interactions */
(function () {
  'use strict';

  // --- sticky header state ---
  var header = document.querySelector('.site-header');
  function onScroll() {
    if (!header) return;
    if (window.scrollY > 24) header.classList.add('scrolled');
    else header.classList.remove('scrolled');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // --- mobile menu ---
  var toggle = document.querySelector('.menu-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
      header.classList.add('scrolled');
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { links.classList.remove('open'); });
    });
  }

  // --- reveal on scroll ---
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (r) { io.observe(r); });
  } else {
    reveals.forEach(function (r) { r.classList.add('in'); });
  }

  // --- animated counters ---
  function animateCount(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var dec = (el.getAttribute('data-dec') === '1');
    var dur = 1500, start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      var val = target * eased;
      el.textContent = dec ? val.toFixed(1) : Math.round(val).toLocaleString();
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var counters = document.querySelectorAll('[data-count]');
  var prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (counters.length && !prefersReduced && 'IntersectionObserver' in window) {
    counters.forEach(function (c) { c.textContent = '0'; });          // start from zero only when we will animate
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { animateCount(e.target); cio.unobserve(e.target); }
      });
    }, { threshold: 0.6 });
    counters.forEach(function (c) { cio.observe(c); });
  } // else: no JS animation — the real values stay in the HTML as written

  // --- current year ---
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // --- form handler: posts to Web3Forms when an access key is set ---
  function showNote(note, color, msg) {
    if (!note) return;
    note.style.display = 'block';
    note.style.color = color;
    note.textContent = msg;
  }
  document.querySelectorAll('form[data-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = form.querySelector('.form-result');
      var keyInput = form.querySelector('input[name="access_key"]');
      var key = keyInput ? keyInput.value.trim() : '';
      // Not configured yet → friendly placeholder behaviour (no errors before go-live)
      if (!key || key.indexOf('REPLACE_WITH') === 0) {
        showNote(note, '#5B7185', 'Form is ready — add your free Web3Forms access key (see README) to start receiving messages at info@primevoltes.ca.');
        form.reset();
        return;
      }
      var btn = form.querySelector('button[type="submit"]');
      var original = btn ? btn.innerHTML : '';
      if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }
      fetch('https://api.web3forms.com/submit', {
        method: 'POST', headers: { 'Accept': 'application/json' }, body: new FormData(form)
      })
        .then(function (r) { return r.json(); })
        .then(function (json) {
          if (json.success) {
            showNote(note, '#10B981', 'Thank you — your message has been sent. We\'ll be in touch within one business day.');
            form.reset();
          } else {
            showNote(note, '#DC2626', 'Sorry, something went wrong. Please email info@primevoltes.ca.');
          }
        })
        .catch(function () { showNote(note, '#DC2626', 'Network error. Please email info@primevoltes.ca.'); })
        .finally(function () { if (btn) { btn.disabled = false; btn.innerHTML = original; } });
    });
  });
})();
