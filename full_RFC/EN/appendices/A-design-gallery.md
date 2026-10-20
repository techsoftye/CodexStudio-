<a id="app-a"></a>
# Appendix A. UI/UX Concept Gallery

<a id="s-a-1"></a>
## A.1 Reading the designs

All six supplied PNGs are reproduced unchanged at 1672 × 941 pixels. They are concept images, not product screenshots or test evidence. Their sample identity, model label, dates, counts, paths and outcomes are illustrative. File hashes and source names are recorded in the asset manifest. No dedicated More screen was supplied; Chapter 05 defines its bounded behavior.

Text decisions govern discrepancies. The notes below distinguish visible content, proposed interaction and correction. The images do not approve every pictured menu, field or provider. For future Word conversion, retain full-width readable images with the numbered captions below; do not crop away controls that the commentary discusses.

<a id="s-a-2"></a>
## A.2 Chat

![Figure A-01: Chat project workspace with sources and task promotion](../../assets/01-chat-project-workspace.png)

**Figure A-01 — Chat within a project.** Source: `01-chat-project-workspace.png`. Related: Chapters 05 and 10; R-05-02, R-10-01.

**Visible:** Project conversations appear on the left, the affiliate-page planning request and response occupy the center, and Sources is selected on the right. The response includes More Details, Add to Tasks and Create Task. Current context and related files appear beneath sources.

**Interaction:** Selecting actionable response items opens editable task drafts with message provenance. More Details continues the explanation. Sources open their identified files; Current Context describes the active project/conversation, not a new permission grant.

**Differences:** The response's suggested implementation steps do not authorize implementation when the user asked only for analysis and a plan. Structure and extra panel controls are visual explorations, not committed MVP features. The old account name and model label do not establish current branding or model availability.

<a id="s-a-3"></a>
## A.3 Tasks list

![Figure A-02: Tasks grouped by status with Stages and Sections](../../assets/02-tasks-stages-sections.png)

**Figure A-02 — Task queue and optional organization.** Source: `02-tasks-stages-sections.png`. Related: Chapter 06; R-06-02, R-06-03.

**Visible:** The list contains Todo, Active, Review, Done and Deferred groups, priorities, optional dates and badges. The right panel provides Stages/Sections and Current context. The toolbar offers New Task and Create from Chat.

**Interaction:** Stage selection narrows sections and list scope. New Task replaces the right working panel. A row opens its task and linked attempts. Selection controls select records; they are not one-click verified-completion approval.

**Differences:** The toolbar lacks Todo although the list includes it; the RFC requires the Todo filter. The sidebar uses time groups unlike the canonical project hierarchy. Avatars and Team members do not add an Assignee field or team-administration MVP. “Affiliate Module” is sample context; fixed stage names and counts are not universal defaults.

<a id="s-a-4"></a>
## A.4 New Task

![Figure A-03: New Task right-panel form](../../assets/03-tasks-new-task-form.png)

**Figure A-03 — New Task subview.** Source: `03-tasks-new-task-form.png`. Related: Chapter 06, Table 06-1; R-06-01, R-06-04.

**Visible:** Back to Tasks, Title, Description, Priority, Status dropdown, Stage, Section, Parent task, Due date, Selected skills, attachments, Cancel and Create Task. The center list remains visible.

**Interaction:** Title is required; default Status is Todo and Priority Medium. Stage/Section, parent, date, skills and attachments are optional. Changing Stage clears incompatible Section; parent cycles are rejected. Save creates work without starting execution. Back preserves the draft; Cancel explicitly discards.

**Differences:** Color treatments alone do not reliably establish a selected priority; textual/default semantics govern. The form does not depict validation, unsaved changes, conflict handling, attachment failure or Done completion guard. Chapter 06 supplies those required states without adding excluded fields.

<a id="s-a-5"></a>
## A.5 Decisions and rules

![Figure A-04: Decisions register and Project Rules](../../assets/04-decisions-project-rules.png)

**Figure A-04 — Choice history and applicable guidance.** Source: `04-decisions-project-rules.png`. Related: Chapter 07; R-07-01 through R-07-06.

**Visible:** All, Proposed, Approved and Superseded filters, search, New Decision, decision rows and a Rules-selected right panel containing Project Rules.

**Interaction:** Opening a decision reveals its scope, rationale, source and history. Approving a replacement retains the superseded record. Rule selection exposes the authoritative source and applicable scope.

**Differences:** The visible rule list lacks source/version detail; that detail is mandatory in the RFC. An Approved badge cannot establish authority to execute. The sample Superseded permissions decision does not authorize relaxing real access controls. Sources/Structure/Context tabs in the panel do not expand the agreed default Rules behavior.

<a id="s-a-6"></a>
## A.6 Results

![Figure A-05: Results and execution evidence](../../assets/05-results-execution-evidence.png)

**Figure A-05 — Attempt outcomes and evidence review.** Source: `05-results-execution-evidence.png`. Related: Chapter 08; R-08-01 through R-08-06.

**Visible:** Outcome and Pending Review filters, result cards with counts and durations, Review Changes/Open Task/Re-run actions, summary and selected-result evidence links.

**Interaction:** Review Changes opens captured evidence; Open Task restores intended work; Re-run creates a new checked execution intent. The side panel follows the selected result.

**Differences:** Pending Review is drawn like an exclusive outcome; the RFC models it independently. The summary omits Partial and its visible buckets must not be used as an additive total. “12/12 tests” and durations are sample artwork, not benchmarks. Partial numerical counts do not establish whether other checks failed, were skipped or were unavailable. “Landing page” in one card does not change the affiliate marketer page scenario into a separately approved marketing-site requirement.

<a id="s-a-7"></a>
## A.7 Library

![Figure A-06: Library project/session files and optional external sources](../../assets/06-library-files-external-sources.png)

**Figure A-06 — File discovery with provenance.** Source: `06-library-files-external-sources.png`. Related: Chapter 09; R-09-01 through R-09-06.

**Visible:** Project Files/Session Files, type filters, search, sort, paths, metadata, file selection, Open/Preview and External Sources. Provider names include Google Drive, Dropbox and OneDrive, alongside URL import and Git synchronization.

**Interaction:** A selected file exposes source, version and availability; project/session associations can refer to the same bytes. Input/Output/Resource classification stays inside Library.

**Differences:** Provider buttons are possible future entry points, not verified Studio integrations. Listed paths, sizes and dates are examples. The drawing does not distinguish live versus captured versions, permission denial or revoked access; the RFC requires those states. Quick topic filters are optional examples and do not replace the primary Project/Session division.

<a id="s-a-8"></a>
## A.8 Version 1.1 extensions absent from the drawings

All six PNGs remain unchanged. Project Group selection, independent environment profiles, cross-project Change Sets, role/grant administration and multimodal confirmation are specified in Sections 04.7, 05.7, 10.7–10.8 and 11.8–11.9, not shown in these inherited images. Existing avatars and team labels do not prove the new permission model. New Task retains its canonical fields. No additional main tab, Prompt Templates or generated mockup is introduced.

A later visual-design pass should depict the group/project/profile target together and test permission-filtered empty states, delegated authority expiry and integration blockers. This is a recommendation for a separately requested design task, not a missing image in this package.

<!-- related-start -->
**Related sections:** [05. Project-Centric Workspace Architecture and UX](../chapters/05-workspace-ux.md#ch-05) · [06. Tasks and Development Planning](../chapters/06-tasks-planning.md#ch-06) · [07. Engineering Decisions and Project Rules](../chapters/07-decisions-rules.md#ch-07) · [08. Execution Results and Evidence](../chapters/08-results-evidence.md#ch-08) · [09. Project Library and Resources](../chapters/09-library-resources.md#ch-09)
<!-- related-end -->
