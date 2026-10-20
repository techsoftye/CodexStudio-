# Codex Studio

## A Project-Centric Engineering Workspace for Agentic Software Development

**An independent product concept by TechSoft.** This repository contains a proposal, not a released application, an official OpenAI announcement, or an implementation commitment.

The proposal connects conversations, tasks, approved decisions, execution evidence, and project resources in a dedicated developer workspace. It builds on existing Codex capabilities instead of proposing a new coding model.

### Start reading

| Document | English | العربية |
|---|---|---|
| Selected community article | [Read the article](article/Article-EN.md) | [قراءة المقال](article/Article-AR.md) |
| Full Product Concept RFC — review draft v1.1 | [15 chapters + 5 appendices](full_RFC/EN/Codex_Studio_Full_RFC_EN.md) | [15 فصلًا + 5 ملاحق](full_RFC/AR/Codex_Studio_Full_RFC_AR.md) |
| Design mockups | [Image gallery](gallery.md) | [معرض التصاميم](gallery.md) |
| Repository and publishing guide | [This README](README.md) | [تعليمات الرفع والنشر](publication/UPLOAD-AR.md) |

The RFC is a substantive working draft for review, not a final implementation specification. Integration feasibility, product decisions, and evaluation results remain open where the document says so.

[Download the repository ZIP](https://github.com/techsoftye/CodexStudio-/archive/refs/heads/main.zip) — available after the first successful push.

### HTML reading site

Open **`index.html`** locally to read the selected English article with its images; **`ar.html`** opens the Arabic version. Navigation includes both full RFC editions, their chapters, and the image gallery. All reading assets are local; no web build service or JavaScript framework is required.

**Expected public site after GitHub Pages is enabled:** [https://techsoftye.github.io/CodexStudio-/](https://techsoftye.github.io/CodexStudio-/)

The site URL is not activated by preparing or unzipping this repository. Push the files, then configure **Settings → Pages → Deploy from a branch → main → /(root) → Save**. Wait for the Pages deployment to finish before sharing the site URL. The Markdown documents on GitHub are readable as soon as the branch has been pushed.

### What is preserved

The community article uses the selected extended draft, preserving its nine sections, six tab explanations, and five inline images in their original order: **Chat → Tasks → Decisions → Results → Library**. The separate New Task form remains in the RFC/gallery rather than being inserted into the article. Image bytes are unchanged.

The publication edits are limited to TechSoft attribution, specific wording corrections, valid image paths, and the closing link to the detailed RFC that is now included. [Review the exact article diff](publication/article-changes.diff).

### Repository layout

```text
index.html / ar.html        Selected article, formatted for reading
article/                   English and Arabic Markdown article sources
full_RFC/EN/               English RFC, 15 chapters and 5 appendices
full_RFC/AR/               Arabic RFC, 15 chapters and 5 appendices
full_RFC/assets/           Six original mockups, shared by all pages
full_RFC/review/           Supplied historical RFC review records
assets/                    Local reader stylesheet and script
publication/               Forum copy, closing paragraph, checks and upload guide
tools/                     Optional local build/validation/publishing tools
```

Historical source exhibits cited by the RFC are retained under `full_RFC/assets/reference-sources/` and labelled as earlier drafting material. They are not alternative current publications. Their bylines and image paths have been normalized; the original uploaded archive remains the unmodified source record.

### Copying to the community

[COMMUNITY-POST-EN.md](publication/COMMUNITY-POST-EN.md) contains the complete corrected forum text with raw GitHub image links. Those image links become available after this repository is pushed to `main`; GitHub Pages is not required for them. The forum may impose its own external-image rules.

If the images are already uploaded in your forum draft, **keep those forum uploads**. Replace only the affected paragraphs, especially the [closing paragraph](publication/CLOSING-PARAGRAPH-EN.md); do not replace working forum image links unnecessarily.

### Local editing and checks

No build step is needed to read or publish the supplied files. To regenerate HTML after editing Markdown:

```bash
python -m pip install -r tools/requirements.txt
python tools/build_site.py
python tools/check_links.py
```

The build assembles the RFC from its chapter and appendix sources before rendering. Edit those sources rather than the compiled RFC alone. These are documentation checks—not tests of the proposed Codex Studio product.

### Feedback

Discuss the proposal in the OpenAI community topic where it is posted, or use this repository's [Issues](https://github.com/techsoftye/CodexStudio-/issues). Private feedback can be sent through the community conversation. No private email address or unpublished community URL is assumed here.

The author spelling is **TechSoft**. Names, metrics, model labels, and dates embedded in the original mockups are illustrative. This repository is documentation; publishing it does not imply that a working Codex Studio application exists.
