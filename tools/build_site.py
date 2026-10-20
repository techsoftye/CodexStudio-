#!/usr/bin/env python3
"""Build the static TechSoft proposal reader from the bundled Markdown sources.

Run from any directory: python tools/build_site.py
No network requests, repository writes, or external processes are performed.
"""
from __future__ import annotations
import html
import json
import os
import re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/techsoftye/CodexStudio-'
SITE = 'https://techsoftye.github.io/CodexStudio-/'
MD = MarkdownIt('commonmark', {'html': True, 'typographer': False}).enable('table').enable('strikethrough')


def relative(target: Path, base: Path) -> str:
    return Path(os.path.relpath(target, base)).as_posix()


def assemble_rfc(lang: str) -> None:
    folder = ROOT / 'full_RFC' / lang
    target = folder / f'Codex_Studio_Full_RFC_{lang}.md'
    old = target.read_text(encoding='utf-8')
    header = old.split('<a id="ch-01"></a>', 1)[0].rstrip()
    # Original drafting dates are retained, not advertised as new empirical verification.
    header = header.replace('**Prepared and verified:**', '**Original drafting date:**')
    header = header.replace('**تاريخ الإعداد والتحقق:**', '**تاريخ إعداد المسودة الأصلية:**')
    parts = sorted((folder / 'chapters').glob('*.md')) + sorted((folder / 'appendices').glob('*.md'))
    if len(parts) != 20:
        raise ValueError(f'{lang}: expected 15 chapters and 5 appendices, got {len(parts)}')
    sources = {p.resolve() for p in parts}
    def rebased(text: str, source: Path) -> str:
        def rewrite(m: re.Match[str]) -> str:
            href = m.group(1)
            if href.startswith(('https:', 'http:', '#', 'mailto:')):
                return m.group(0)
            u = urlsplit(href)
            dest = (source.parent / unquote(u.path)).resolve()
            if dest in sources and u.fragment:
                return '](' + '#' + u.fragment + ')'
            path = relative(dest, target.parent)
            return '](' + path + ('#' + u.fragment if u.fragment else '') + ')'
        return re.sub(r'\]\(([^)\s]+)\)', rewrite, text)
    target.write_text(header + '\n\n' + '\n\n---\n\n'.join(rebased(p.read_text(encoding='utf-8').strip(), p) for p in parts) + '\n', encoding='utf-8')


def output_path(source: Path) -> Path:
    rel = source.relative_to(ROOT).as_posix()
    special = {
        'article/Article-EN.md': 'index.html',
        'article/Article-AR.md': 'ar.html',
        'README.md': 'overview.html',
        'README-AR.md': 'overview-ar.html',
        'full_RFC/README.md': 'full_RFC/index.html',
        'full_RFC/EN/Codex_Studio_Full_RFC_EN.md': 'full_RFC/EN/index.html',
        'full_RFC/AR/Codex_Studio_Full_RFC_AR.md': 'full_RFC/AR/index.html',
    }
    return ROOT / special[rel] if rel in special else source.with_suffix('.html')


def slug(text: str) -> str:
    value = re.sub(r'[^\w\s-]', '', text.lower(), flags=re.UNICODE)
    return re.sub(r'[-\s]+', '-', value).strip('-') or 'section'


def lang_for(source: Path) -> str:
    rel = source.relative_to(ROOT).as_posix()
    if '/AR/' in rel or '-AR.' in rel or 'original-AR' in rel:
        return 'ar'
    return 'en'


def render(source: Path, mapping: dict[Path, Path]) -> None:
    out = mapping[source.resolve()]
    lang = lang_for(source)
    ar = lang == 'ar'
    text = source.read_text(encoding='utf-8')
    doc = BeautifulSoup(MD.render(text), 'html.parser')
    # Rewrite local links relative to the generated page; .md links navigate as HTML.
    for element in doc.find_all(['a', 'img']):
        attr = 'src' if element.name == 'img' else 'href'
        href = element.get(attr)
        if not href or href.startswith('#'):
            continue
        u = urlsplit(href)
        if u.scheme or u.netloc:
            if element.name == 'a':
                element['rel'] = 'noopener noreferrer'
            continue
        dest = (source.parent / unquote(u.path)).resolve()
        if element.name == 'a' and dest in mapping:
            dest = mapping[dest]
        element[attr] = quote(relative(dest, out.parent), safe='/.-_') + ('?' + u.query if u.query else '') + ('#' + u.fragment if u.fragment else '')
    ids = {str(x['id']) for x in doc.find_all(id=True)}
    headings = []
    all_headings = doc.find_all(re.compile(r'^h[1-6]$'))
    for i, h in enumerate(all_headings):
        if not h.get('id'):
            proposed = slug(h.get_text(' ', strip=True))
            ident, n = proposed, 1
            while ident in ids:
                n += 1
                ident = f'{proposed}-{n}'
            h['id'] = ident
            ids.add(ident)
        if i > 0 and int(h.name[1]) <= 3:
            headings.append((int(h.name[1]), str(h['id']), h.get_text(' ', strip=True)))
    title = all_headings[0].get_text(' ', strip=True) if all_headings else source.stem
    toc = ''.join(f'<li class="level-{level}"><a href="#{html.escape(ident)}">{html.escape(label)}</a></li>' for level, ident, label in headings)
    for img in doc.find_all('img'):
        img['loading'] = 'lazy'
        img['decoding'] = 'async'
        img['width'] = '1672'
        img['height'] = '941'
        if img.parent and img.parent.name != 'a':
            a = doc.new_tag('a', href=img['src'])
            a['class'] = 'image-link'
            a['target'] = '_blank'
            a['rel'] = 'noopener'
            a['aria-label'] = 'فتح الصورة بالحجم الأصلي' if ar else 'Open original full-size image'
            img.wrap(a)
    for table in doc.find_all('table'):
        wrapper = doc.new_tag('div', attrs={'class':'table-wrap','tabindex':'0','role':'region','aria-label':'جدول قابل للتمرير' if ar else 'Scrollable table'})
        table.wrap(wrapper)
    nav_items = [
        ('index.html', 'المقال EN' if ar else 'Article EN'),
        ('ar.html', 'المقال AR' if ar else 'Article AR'),
        ('full_RFC/EN/index.html', 'RFC EN'),
        ('full_RFC/AR/index.html', 'RFC AR'),
        ('gallery.html', 'الصور' if ar else 'Mockups'),
        ('overview.html', 'المستودع' if ar else 'Overview'),
    ]
    nav = ''.join(f'<a href="{html.escape(relative(ROOT/path, out.parent))}"'+(' aria-current="page"' if ROOT/path == out else '')+f'>{html.escape(label)}</a>' for path,label in nav_items)
    css = relative(ROOT/'assets/reader.css', out.parent)
    js = relative(ROOT/'assets/reader.js', out.parent)
    src = relative(source, out.parent)
    opposite = None
    source_rel = source.relative_to(ROOT).as_posix()
    if source_rel == 'article/Article-EN.md': opposite = ROOT/'ar.html'
    elif source_rel == 'article/Article-AR.md': opposite = ROOT/'index.html'
    elif '/EN/' in source_rel: opposite = mapping.get((ROOT/source_rel.replace('/EN/','/AR/').replace('_EN.md','_AR.md')).resolve())
    elif '/AR/' in source_rel: opposite = mapping.get((ROOT/source_rel.replace('/AR/','/EN/').replace('_AR.md','_EN.md')).resolve())
    language_link = f'<a href="{html.escape(relative(opposite, out.parent))}" class="button">'+('English' if ar else 'العربية')+'</a>' if opposite else ''
    kicker = 'مقترح مستقل من TechSoft · مسودة للمراجعة' if ar else 'An independent proposal by TechSoft · Review draft'
    label_toc = 'محتويات الصفحة' if ar else 'On this page'
    tools = f'''<div class="toolbar"><button type="button" id="wide-toggle" aria-pressed="false">{'عرض واسع' if ar else 'Wide view'}</button><button type="button" id="theme-toggle">{'المظهر' if ar else 'Theme'}</button><button type="button" id="print-button">{'طباعة' if ar else 'Print'}</button>{language_link}<a class="source-link" href="{html.escape(src)}">Markdown</a></div>'''
    body = str(doc)
    is_article = source_rel.startswith('article/')
    css_class = 'article-page' if is_article else 'reference-page'
    footer = 'تصور للنقاش، وليس منتجًا رسميًا أو تطبيقًا منفذًا. جميع الصور نماذج تصورية.' if ar else 'A concept for discussion, not an announced product or implemented application. All interface images are conceptual mockups.'
    description = 'Codex Studio: a project-centric engineering workspace proposal by TechSoft. Read the selected article and the bilingual Full Product Concept RFC.'
    rendered = f'''<!doctype html>
<html lang="{lang}" dir="{'rtl' if ar else 'ltr'}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{html.escape(description)}"><meta name="author" content="TechSoft"><meta name="color-scheme" content="light dark">
<title>{html.escape(title)} — TechSoft</title>
<link rel="stylesheet" href="{html.escape(css)}"><script defer src="{html.escape(js)}"></script>
</head>
<body class="{css_class}"><a class="skip-link" href="#article">{'تجاوز إلى المحتوى' if ar else 'Skip to content'}</a>
<header class="site-header"><a class="brand" href="{html.escape(relative(ROOT/'index.html',out.parent))}" dir="ltr"><strong>TechSoft</strong><span>Codex Studio</span></a><nav aria-label="{'التنقل الرئيسي' if ar else 'Main navigation'}">{nav}<a href="{REPO}" rel="noopener noreferrer">GitHub</a></nav></header>
<div class="layout"><aside class="toc-panel"><details open><summary>{label_toc}</summary><ol>{toc}</ol></details><div class="toc-note">{'15 فصلًا · 5 ملاحق · EN / AR' if ar else '15 chapters · 5 appendices · EN / AR'}</div></aside>
<main id="article" class="reader"><div class="eyebrow">{kicker}</div>{tools}<article>{body}</article><footer class="article-footer"><strong>TechSoft</strong><p>{footer}</p><a href="#article">{'العودة للأعلى' if ar else 'Back to top'}</a></footer></main></div>
</body></html>'''
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(rendered, encoding='utf-8')


def main() -> None:
    for language in ('EN','AR'):
        assemble_rfc(language)
    # These are already complete copy/paste snippets, not independent reading pages.
    excluded = {'publication/COMMUNITY-POST-EN.md','publication/CLOSING-PARAGRAPH-EN.md'}
    sources = [p for p in sorted(ROOT.rglob('*.md')) if '.git' not in p.parts and p.relative_to(ROOT).as_posix() not in excluded]
    mapping = {p.resolve(): output_path(p) for p in sources}
    for source in sources:
        render(source, mapping)
    manifest = {str(p.relative_to(ROOT)): str(q.relative_to(ROOT)) for p, q in mapping.items()}
    (ROOT/'publication/site-map.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f'Generated {len(mapping)} HTML reading pages; all images and styles are local.')

if __name__ == '__main__':
    main()
