/* Local-only reading controls. No network requests or analytics. */
(() => {
  'use strict';
  const ar = document.documentElement.lang === 'ar';
  const storage = {
    get: (key) => { try { return localStorage.getItem(key); } catch (_) { return null; } },
    set: (key, value) => { try { localStorage.setItem(key, value); } catch (_) { /* file:// may deny storage */ } }
  };
  const theme = storage.get('techsoft-codex-theme');
  if (theme === 'dark') document.documentElement.dataset.theme = 'dark';
  const wide = document.getElementById('wide-toggle');
  wide?.addEventListener('click', () => {
    const active = document.body.classList.toggle('wide');
    wide.setAttribute('aria-pressed', String(active));
    wide.textContent = active ? (ar ? 'عرض عادي' : 'Standard view') : (ar ? 'عرض واسع' : 'Wide view');
  });
  document.getElementById('theme-toggle')?.addEventListener('click', () => {
    const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    storage.set('techsoft-codex-theme', next);
  });
  document.getElementById('print-button')?.addEventListener('click', () => window.print());
  const details = document.querySelector('.toc-panel details');
  if (window.matchMedia('(max-width: 820px)').matches && details) details.open = false;
  const tocLinks = Array.from(document.querySelectorAll('.toc-panel a'));
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.find(entry => entry.isIntersecting);
      if (!visible) return;
      tocLinks.forEach(link => link.classList.toggle('active', decodeURIComponent(link.hash.slice(1)) === visible.target.id));
    }, {rootMargin:'-8% 0px -72% 0px'});
    document.querySelectorAll('article h1[id], article h2[id], article h3[id]').forEach(h => observer.observe(h));
  }
})();
