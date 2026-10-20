'use strict';
(() => {
  const post = JSON.parse(document.getElementById('community-post').textContent);
  const status = document.getElementById('copy-status');
  const source = document.getElementById('post-source');
  const field = document.getElementById('post-markdown');
  async function copy(text, kind) {
    try {
      await navigator.clipboard.writeText(text);
      status.textContent = kind === 'title' ? 'Title copied.' : 'Post body copied with all five public image links.';
    } catch {
      source.open = true;
      field.value = text;
      document.querySelector('label[for="post-markdown"]').textContent = kind === 'title' ? 'Topic title' : 'Post body';
      field.focus();
      field.select();
      status.textContent = 'Clipboard access is unavailable. The text is selected below; press Ctrl+C (or Command+C).';
    }
  }
  for (const [id, key] of [['copy-title', 'title'], ['copy-body', 'body']]) {
    const button = document.getElementById(id);
    button.disabled = false;
    button.addEventListener('click', () => copy(post[key], key));
  }
  source.addEventListener('toggle', () => {
    if (source.open && field.value !== post.title) field.value = post.body;
  });
})();
