#!/usr/bin/env python3
"""Validate the generated local documentation. Does not check/publish remote URLs."""
from __future__ import annotations
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
MD = MarkdownIt('commonmark', {'html': True}).enable('table').enable('strikethrough')
REPORT = ROOT/'publication/VALIDATION.json'

def run() -> int:
    if not REPORT.exists():
        REPORT.write_text('{}\n',encoding='utf-8')
    errors, external = [], set()
    id_cache = {}
    count = {'html_files':0,'markdown_files':0,'local_links':0,'image_references':0,'fragment_checks':0}
    def parsed(file: Path) -> BeautifulSoup:
        text = file.read_text(encoding='utf-8')
        if file.suffix == '.md': text = MD.render(text)
        return BeautifulSoup(text, 'html.parser')
    def ids_in(file: Path) -> set[str]:
        if file not in id_cache:
            d = parsed(file)
            ids = {str(e['id']) for e in d.find_all(id=True)}
            if file.suffix == '.md':
                for h in d.find_all(re.compile(r'^h[1-6]$')):
                    value = re.sub(r'[^\w\s-]', '', h.get_text(' ',strip=True).lower(), flags=re.UNICODE)
                    value = re.sub(r'[-\s]+','-',value).strip('-') or 'section'
                    ident,n=value,0
                    while ident in ids:
                        n+=1;ident=f'{value}-{n}'
                    ids.add(ident)
            id_cache[file]=ids
        return id_cache[file]
    for file in sorted(list(ROOT.rglob('*.html'))+list(ROOT.rglob('*.md'))):
        if '.git' in file.parts: continue
        count['html_files' if file.suffix=='.html' else 'markdown_files']+=1
        d=parsed(file)
        rel=file.relative_to(ROOT).as_posix()
        if file.suffix=='.html':
            repeated=[i for i,c in Counter(str(e['id']) for e in d.find_all(id=True)).items() if c>1]
            for ident in repeated: errors.append({'file':rel,'error':'duplicate_id','target':ident})
        for tag in d.find_all(['a','img','link','script']):
            attr='src' if tag.name in ('img','script') else 'href'
            href=tag.get(attr)
            if not href: continue
            u=urlsplit(str(href))
            if u.scheme in ('http','https') or u.netloc:
                external.add(str(href));continue
            if u.scheme:
                if u.scheme not in ('mailto','tel','data'):
                    errors.append({'file':rel,'error':'unsupported_local_scheme','target':str(href)})
                continue
            dest=(file.parent/unquote(u.path)).resolve() if u.path else file.resolve()
            try:dest.relative_to(ROOT)
            except ValueError:
                errors.append({'file':rel,'error':'escapes_repository','target':str(href)});continue
            if dest.is_dir():dest=dest/'index.html'
            count['local_links']+=1
            if tag.name=='img':count['image_references']+=1
            if not dest.is_file():
                errors.append({'file':rel,'error':'missing_file','target':str(href)});continue
            if u.fragment and dest.suffix in ('.html','.md'):
                count['fragment_checks']+=1
                if unquote(u.fragment) not in ids_in(dest):
                    errors.append({'file':rel,'error':'missing_fragment','target':str(href)})
    source=(ROOT/'article/Article-EN.md').read_text(encoding='utf-8')
    article_doc=BeautifulSoup(MD.render(source),'html.parser')
    sequence=[Path(urlsplit(img['src']).path).name for img in article_doc.find_all('img')]
    expected=['01-chat-project-workspace.png','02-tasks-stages-sections.png','04-decisions-project-rules.png','05-results-execution-evidence.png','06-library-files-external-sources.png']
    if sequence!=expected:errors.append({'error':'article_image_order_changed','actual':sequence})
    sections=re.findall(r'^## (\d{2})\.',source,flags=re.M)
    if sections != [f'{i:02}' for i in range(1,10)]:errors.append({'error':'article_section_order_changed','actual':sections})
    if 'YemenCoder' in source or 'Tech Soft' in source:errors.append({'error':'incorrect_author_in_article'})
    if 'Anyone interested' in source and 'is welcome  Anyone' in source:errors.append({'error':'duplicate_closing_text'})
    manifest=json.loads((ROOT/'publication/image-integrity.json').read_text())
    verified=[]
    for item in manifest['images']:
        file=ROOT/item['file']
        digest=hashlib.sha256(file.read_bytes()).hexdigest()
        match=digest==item['source_sha256']
        verified.append({'file':item['file'],'sha256':digest,'matches_supplied_image':match})
        if not match:errors.append({'error':'image_changed','file':item['file']})
    rfc_counts={}
    for lang in ['EN','AR']:
        folder=ROOT/'full_RFC'/lang
        chapters=list((folder/'chapters').glob('*.md'));appendices=list((folder/'appendices').glob('*.md'))
        rfc_counts[lang]={'chapters':len(chapters),'appendices':len(appendices)}
        if len(chapters)!=15 or len(appendices)!=5:errors.append({'error':'invalid_rfc_document_count','language':lang})
    data={
        'checked_at_utc':datetime.now(timezone.utc).isoformat(),
        'scope':'Local Markdown/HTML targets, anchors, article section/image order, and supplied image hashes. External server availability and product feasibility are not tested by this script.',
        'passed':not errors,'counts':count,'rfc':rfc_counts,'article_sections':sections,'article_image_order':sequence,
        'image_integrity':verified,'errors':errors,
        'external_urls_referenced_not_tested_here':sorted(external),
        'publication_state':'Prepared locally. No git push or GitHub Pages deployment is performed by this script.'
    }
    REPORT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':not errors,'counts':count,'errors':errors},ensure_ascii=False,indent=2))
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(run())
