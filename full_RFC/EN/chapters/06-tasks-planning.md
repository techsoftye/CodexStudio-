<a id="ch-06"></a>
# 06. Tasks and Development Planning

<a id="s-06-1"></a>
## 06.1 Purpose and creation contract

A Task records intended work independently of how many times an agent attempts it. It belongs to one project, may originate in a conversation, may link several applicable decisions, and may have multiple execution attempts and results. Creating a task does not approve its implementation. A user can create it manually or review an agent-extracted draft from Chat.

New Task opens in the right panel with **Back to Tasks**, preserving the center list. Cancel discards only after the user chooses to discard unsaved edits; Back preserves a recoverable local draft. Save validates the whole record and its links. The saved task appears in the appropriate group; if current filters hide it, show a link and a clear explanation instead of silently changing filters.

<a id="s-06-2"></a>
## 06.2 Form inputs and validation

**Table 06-1 — Canonical creation form**

| Field | Default / allowed input | Validation and effect |
|---|---|---|
| Title | Required nonblank text | Trim surrounding whitespace; reject empty title; render as text |
| Description | Optional | Requirements, constraints and acceptance criteria; preserve formatting safely |
| Priority | Medium; Low / Medium / High | Planning priority, not permission or automatic scheduling |
| Status | Todo; dropdown | Todo / Active / Review / Done / Deferred; completion guard applies even on create |
| Stage | Not set | Project-owned stage or null |
| Section | Not set | Section within selected Stage; changing Stage clears incompatible Section visibly |
| Parent Task | None | Same project, not self or descendant; archived parents unavailable for new links |
| Due Date | No date; Today / Tomorrow / Custom | Store calendar date with project display timezone; no unattended run |
| Selected Skills | Not set | Optional available skill identities; missing or changed selection flagged before execution |
| Task Attachments | None | Upload or select Library reference; validate project access and file availability |

There is no separate Assignee, generic Related To, or Add Sub-task field. A child is created by selecting Parent Task. Task-to-decision, source-message and result relationships arise through contextual actions. They are not extra mandatory creation fields. Input length and attachment limits should follow the selected storage/runtime constraints and be visible before submission; this RFC does not invent limits without a platform choice.

Description is optional at creation. Before execution, the user or agent must clarify a materially ambiguous outcome. Acceptance criteria can remain structured within the description and be versioned with the task; no additional top-level form control is required. A selected skill is a preference for applicable runtime loading, not a guaranteed installed capability. Leaving it unset preserves normal discovery.

<a id="s-06-3"></a>
## 06.3 Independent lifecycle

**Table 06-2 — Task states and allowed transitions**

| Current | Event and guard | Next / record |
|---|---|---|
| Todo | Explicit start; context and permissions valid | Active; execution intent or manual-work event |
| Todo | User postpones | Deferred; reason optional |
| Active | Work submitted for evaluation, including incomplete verification | Review; linked result or manual submission |
| Active | Attempt fails | Remains Active unless user chooses Review or Deferred; failure belongs to attempt |
| Review | Reviewer requests correction | Active; unresolved findings preserved |
| Review | Reviewer accepts against task version and completion policy | Done; completion record with accepted result references |
| Any non-Done state | User deliberately postpones, with active-run handling acknowledged | Deferred; running attempt separately interrupted or explicitly left running |
| Deferred | User resumes planning or work | Todo or Active, explicitly selected |
| Done | New work or invalidated evidence warrants reopening | Todo or Active; previous acceptance remains historical |

The task toolbar provides **All / Todo / Active / Review / Done / Deferred**. All is a list filter, not a task state. A runtime completing a turn may submit a result and propose Review; it cannot approve Done. A task marked Deferred does not imply that an agent stopped. The interface must surface any still-running attempt, and interruption uses the runtime control separately.

Manual work remains possible. A user may mark a task Done without an agent run only through an explicit manual completion record stating actor, reason, task version, evidence or lack of evidence, and any permitted exceptions. It must never fabricate a run or tests. Creating a task already marked Done invokes this same guard. The UI must label unverified manual completion; it cannot present it as verified implementation.

<a id="s-06-4"></a>
## 06.4 Organization and hierarchy

Stage describes a phase; Section groups work within that phase; Parent Task expresses decomposition. Status answers progress. These are independent dimensions. A parent may span stages, and a child does not automatically inherit status, due date, or skills. Parent selection may suggest organization, but the user confirms it.

Selecting a stage filters available sections and the list. Unclassified tasks remain accessible through an explicit unclassified option and All. Renaming a stage changes its label, not its identity. Removing a stage or section requires reassigning or clearing affected task references transactionally; it must not delete tasks. Archived tasks remain referencable from historical results, but are excluded from ordinary planning lists.

A parent can be Done only when its current completion scope addresses unfinished children: complete them, remove an incorrect relationship, or record an explicit accepted deferral with rationale. Child completion never automatically approves the parent. Cycle validation must inspect the full ancestor chain, including concurrent updates.

<a id="s-06-5"></a>
## 06.5 Execution and change management

Starting work captures the task version, criteria and selected context. Editing the task while an attempt runs creates a new version and marks that attempt's context as changed. The user can let it finish under the recorded scope, steer it explicitly, or interrupt and start another attempt. The run's original context manifest remains intact; steering adds a dated amendment.

A retry begins a new attempt with current repository state and fresh authorization checks. Dates and priorities do not authorize it. The task detail exposes attempt history and the specific accepted result, not merely the most recent successful-looking message. Concurrent human edits use an expected-version check; a conflict shows both versions and preserves the unsaved draft.

<a id="s-06-6"></a>
## 06.6 Acceptance criteria

**Table 06-3 — Task requirements**

| ID | Proposed requirement and acceptance test |
|---|---|
| R-06-01 | A task MUST save with only Title; defaults and dropdown values match Table 06-1. |
| R-06-02 | Section/Stage and Parent Task consistency MUST be checked at save. Concurrent edits cannot create an ancestor cycle. |
| R-06-03 | Runtime completion MUST NOT set Done. A failed attempt leaves independently meaningful task state. |
| R-06-04 | Done MUST identify reviewed acceptance or explicit manual completion; missing checks cannot become fictional passes. |
| R-06-05 | Editing task scope MUST preserve the version used by an existing attempt and signal divergence. |
| R-06-06 | Deferral, hierarchy changes and due dates MUST NOT silently start, stop, delete or approve execution. |

See Figure A-02 for the task list and Figure A-03 for the form. Chapter 08 defines evidence and acceptance; Appendix D defines relationships and concurrency invariants.

<a id="s-06-7"></a>
## 06.7 Cross-project work and responsibility

In the group expansion, a Change Set expresses a product outcome through links to project-local tasks. Dependencies such as “publish an agreed API contract before integrating the client” are typed links, not parent-child relationships across projects. Each dependency declares its producer, consumer, required contract/evidence version and satisfaction rule. A pending dependency is a visible dispatch blocker; it does not add a new Task status.

The task detail offers a separate responsibility action after creation. A WorkAssignment identifies the accountable human, proposed executor and reviewer scope, including an expiry when relevant. Accepting an assignment does not expand permissions; dispatch still requires a valid DelegationGrant. Reassignment preserves history and explicitly handles any running attempt rather than transferring its credentials or identity.

**R-06-07 — Project-local tasks and bounded assignments.** A task MUST retain one project owner when linked into a Change Set. Acceptance: assigning a Backend task to a Flutter specialist without Backend authority cannot start a Backend write; changing the assignment does not reattribute an existing attempt.

<!-- related-start -->
**Related sections:** [08. Execution Results and Evidence](../chapters/08-results-evidence.md#ch-08) · [Appendix D. Conceptual Data Model](../appendices/D-conceptual-data-model.md#app-d) · [Appendix A. UI/UX Concept Gallery](../appendices/A-design-gallery.md#app-a)
<!-- related-end -->
