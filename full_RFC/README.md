# Codex Studio — Full Product Concept RFC

**Author: TechSoft**  
**Document version: 1.1 — complete working review draft, supplied in the uploaded archive**  
**Original preparation date: 2026-10-18**  
**Repository presentation update: 2026-10-20**

This is an independent proposal for review, not an announced OpenAI product, a tested implementation, or a release commitment. “Complete” describes the written chapter/appendix set; it does not mean that feasibility, external decisions, or user-value hypotheses have been validated.

## Read the full draft

- [English edition — 15 chapters and 5 appendices](EN/Codex_Studio_Full_RFC_EN.md)
- [النسخة العربية — 15 فصلًا وخمسة ملاحق](AR/Codex_Studio_Full_RFC_AR.md)
- [Selected community article](../article/Article-EN.md)
- [Original mockup gallery](../gallery.md)

The two editions include the supplied v1.1 additions on project groups, human/agent responsibilities, shared contracts, and gated future extensions. These additions remain in the detailed RFC; they have not been inserted into or used to reorganize the selected community article.

## Reading and source files

Each edition has `chapters/` and `appendices/` folders containing the twenty source documents. The compiled Markdown and HTML editions are generated from those sources. The six original PNG mockups are in `assets/` and are reused by the article and RFC.

HTML reading pages are already included. Open `EN/index.html` or `AR/index.html` locally; the same pages work through GitHub Pages.

## Review records and evidence boundaries

- [Source decisions](review/01-source-decisions.md)
- [Bilingual terminology](review/03-terminology.md)
- [Refined outline](review/04-refined-outline.md)
- [Requirement coverage](review/05-requirement-coverage.md)
- [Supplied review report](review/06-review-report.md)
- [Supplied v1.1 revision record](review/08-revision-1.1.md)
- [Publication reference checks](../publication/REFERENCE-CHECKS.md)
- [Current local-link and image validation](../publication/VALIDATION.json)

The supplied review records describe the earlier documentation package. Their original counts and assertions are historical records, not newly performed product tests. The current publication checks separately cover document links, image preservation, article order, generated HTML, and archive integrity. A new comprehensive technical or empirical audit of all RFC claims has not been performed.

References in Appendix E retain their original access dates. Source snapshots are historical drafting material, clearly marked as such. Brand spelling and local image paths were normalized for publication; the original ZIP remains the unmodified reference archive.

## Editing

Edit the English chapter or appendix and its Arabic counterpart. From the repository root run:

```bash
python -m pip install -r tools/requirements.txt
python tools/build_site.py
python tools/check_links.py
```

The original archive-dependent build tools are not used in this publication repository. No commands here execute the proposed product or change the live GitHub repository.
