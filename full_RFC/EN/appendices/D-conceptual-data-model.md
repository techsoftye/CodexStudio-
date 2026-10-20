<a id="app-d"></a>
# Appendix D. Conceptual Data Model

<a id="s-d-1"></a>
## D.1 Model status and identity

This is a conceptual domain model for Studio, not a physical SQL schema, migration, finalized API or claim about OpenAI storage. Field groups indicate information that must be represented; implementations may normalize or combine records while preserving invariants.

All Studio records have a stable identity, project or group boundary where applicable, schema version, creation metadata and revision. Mutable records use optimistic concurrency. Runtime IDs include host/runtime identity. Dates of events include an unambiguous time basis; a task due date is a calendar date with display timezone and does not imply scheduling.

<a id="s-d-2"></a>
## D.2 Core entities

**Table D-1 — Core entity responsibilities**

| Entity | Essential information | Relations and lifecycle |
|---|---|---|
| Project | Name, root bindings, owner/access context, settings revision | Owns conversations, tasks, stages, sections, decisions, rules and file associations |
| Conversation | Project, title, supported runtime reference, source availability | Contains message references; may originate multiple tasks and decisions |
| Task | Title, description/criteria, priority, status, date, skill selections, revision | One project; optional Stage/Section/Parent; many attempts and applicable decisions |
| Stage | Project, name, ordering, archived state | Has zero or more Sections and Tasks |
| Section | Project, Stage, name, ordering, archived state | Belongs to exactly one Stage; groups Tasks |
| Decision | Question, choice, rationale, scope, status, approved version | Many task links; source references; optional successor |
| DecisionVersion | Immutable wording/scope, sources, approval actor/time when approved | Historical versions retained by manifests and reviews |
| Rule | Guidance reference, authority kind, scope, source version/hash | Repository-backed or explicitly approved Studio source; optional Decision relation |
| ExecutionAttempt | Task/version, intent key, lifecycle, target, runtime refs, predecessor | One context manifest; zero or more turns/events; zero or one logical Result |
| Result | Attempt, outcome, summary, unresolved findings, current version | Versions bind changes/checks/files; many review events |
| FileReference | Source kind, locator, project access context, display name | Has versions and project/session/task/result associations |
| FileVersion | Immutable content identity or explicit external revision, hash when obtainable | Evidence links bind exact version; availability is recorded separately |

An attempt may have no result while queued or unobservable. Once summarized, it owns one logical result with version history. Manual task completion is supported by a CompletionRecord; it does not fabricate an ExecutionAttempt.

<a id="s-d-3"></a>
## D.3 Supporting records

**Table D-2 — Supporting records and why they exist**

| Record | Key information | Consistency role |
|---|---|---|
| TaskVersion | Captured title, description/criteria and relevant task settings | Immutable execution/review subject; current Task points to a revision |
| ResultVersion | Outcome, summary and exact evidence links at one revision | Reviews bind this version; additions create a new version |
| SourceReference | Source type, message/file locator, revision, captured excerpt if needed | Distinguishes native reference from captured fallback |
| TaskDecisionLink | Task, decision, applicability note | Many-to-many reuse without copying decision text |
| ContextManifest | Task version, instruction/decision/file versions, inclusion modes, reasons, omissions, resolver version | Immutable record of supplied context |
| ContextAmendment | Manifest, steering event, changed inputs, time | Preserves original context while describing continuation |
| ExecutionIntent | Action key, target, authorized scope, dispatch/acknowledgement observations | Reconciles uncertain dispatch without blind retry |
| RuntimeEventReference | Host, thread/turn/item/event identifiers where available, raw source, observation time | Attribution and deduplication with explicit gaps |
| CodeSnapshot | Repository identity, base revision, preexisting state, patch/content hashes and exclusions | Exact code basis of evidence |
| CheckRecord | Check name/command, snapshot, environment, status, output, exit status | Passed/Failed/Not Run/Inconclusive remains independent |
| ReviewEvent | Result version, reviewer, judgment, criteria mapping, exceptions | Immutable acceptance subject |
| CompletionRecord | Task version, accepted results or manual evidence, actor, exceptions | Explains Done without inventing execution |
| ApprovalReference | Runtime request, target/action scope, response, actor and validity | Operation consent remains distinct from decision/review |
| FileAssociation | File/version, linked record, usage classification, conversation/project scope | Project/Session views without duplicate bytes |
| AvailabilityRecord | File version, current access condition, reason/time | Historical identity survives lawful content removal |
| AuditEvent | Actor, operation, subject/revision, time and correlation | Inspectable history; not a claim of tamper-proof storage |

<a id="s-d-4"></a>
## D.4 Cardinalities and navigation

**Figure D-1 — Conceptual relationship map**

```text
Project 1 --- * Conversation --- * SourceReference
Project 1 --- * Task
Project 1 --- * Stage 1 --- * Section
Task 0..1 --- Parent Task       (acyclic, same project)
Task * --- * Decision --- * DecisionVersion
Decision 0..1 --- successor Decision
Rule --- authoritative SourceReference
Task 1 --- * ExecutionAttempt 1 --- 1 ContextManifest
ExecutionAttempt 1 --- * RuntimeEventReference
ExecutionAttempt 1 --- 0..1 Result 1 --- * ResultVersion
ResultVersion --- CodeSnapshot / CheckRecord / FileVersion
ResultVersion 1 --- * ReviewEvent
TaskVersion 1 --- * CompletionRecord
FileReference 1 --- * FileVersion --- * FileAssociation
```

Stage and Section links on Task are optional; Section implies its Stage. Conversation ownership is not task ownership: multiple conversations can discuss one task, and a source message can create several tasks. TaskDecisionLink determines applicability; a context manifest pins the decision version actually supplied. A FileAssociation can expose a captured report in both project and session views while retaining one FileVersion.

<a id="s-d-5"></a>
## D.5 Consistency invariants

**Table D-3 — Model invariants**

| ID | Invariant | Enforcement / review link |
|---|---|---|
| INV-01 | Every relation respects project/access boundaries; external references remain explicitly external | Service validation; R-04-01, R-11-07 |
| INV-02 | Parent links are acyclic and same-project | Transactional ancestor validation; R-06-02 |
| INV-03 | Section belongs to selected Stage in the same project | Clear incompatible links on change; R-06-02 |
| INV-04 | Approved decision versions cannot be overwritten; supersession is acyclic and preserves predecessor | Atomic approval transaction; R-07-02 |
| INV-05 | No task state, result outcome, check state or review state is inferred solely from another dimension | Explicit transitions; R-06-03, R-08-01 |
| INV-06 | An accepted review binds an exact result version and task criteria | Append-only review; R-08-05 |
| INV-07 | Checks and diffs bind a recorded code snapshot or disclose the missing binding | Evidence validation; R-08-02, R-08-03 |
| INV-08 | Re-run creates a new attempt; uncertain launch cannot auto-create another dispatch | Intent key and reconciliation; R-08-04, R-11-02 |
| INV-09 | Original context manifests remain immutable; changes use amendments/new attempts | Versioned context; R-10-01, R-10-04 |
| INV-10 | Rule projections cannot become competing authoritative copies | Source-aware edit flow; R-07-03 |
| INV-11 | Removing a file association does not delete its content or erase review history | Separate retention action; R-09-05 |
| INV-12 | Revocation/deletion invalidates future retrieval and caches | Access checks and invalidation; R-09-06, R-10-03 |
| INV-13 | Done requires a CompletionRecord; manual completion does not create false tests or attempts | Completion guard; R-06-04 |
| INV-14 | ApprovalReference cannot substitute for Decision approval or ReviewEvent | Separate operations; R-07-06, R-11-04 |
| INV-15 | Record mutation, revision increment and audit entry commit consistently | Transaction and recovery; R-11-03, R-11-05 |

<a id="s-d-6"></a>
## D.6 Concrete consistency example

In Appendix C, T-103 v1 links D-07. CM-21 pins D-07 v1 and the exact rule/file versions. X-21 owns S-21, whose checks bind K-21-result. S-21 remains Partial and Changes Requested. X-22 owns S-22; accepting S-22 creates a ReviewEvent and a CompletionRecord for T-103. If successor D-08 v1 later replaces D-07, CM-21 and S-22 still explain their historical basis; new work selects the current approved successor.

A later edit to S-22's substantive evidence creates ResultVersion v2. The earlier ReviewEvent still accepts v1, so the UI shows v2 as needing review. This prevents an accepted badge from silently covering changed evidence.

<a id="s-d-7"></a>
## D.7 Deletion, export and deferred concerns

Archive is a visibility decision; deletion is a retention/access decision. References needed to explain accepted work retain lawful metadata and availability tombstones if content must be removed. Referential integrity must not be implemented as blind cascading deletion of evidence. Export preserves IDs, versions, link types and declared omissions.

Physical indexing, encryption technology, blob layout, compression, full-text/vector search and sync algorithms remain implementation choices. They do not excuse undefined domain behavior. The MVP needs correct identity, versioning and recovery before sophisticated retrieval or distributed editing.

<a id="s-d-8"></a>
## D.8 Group and hybrid-team extension

These entities are post-MVP extensions. Project-owned entities above remain valid. A scoped record has exactly one owner scope, Project or Project Group; references to member projects are explicit authorized associations. Decisions and source references may be group-owned; Tasks and ExecutionAttempts remain project-owned. All access is checked against current membership and policy, while historical manifests preserve the versions used.

**Table D-4 — Extension records**

| Entity | Essential information | Relationships and constraint |
|---|---|---|
| ProjectGroup | Name, accountable owner, revision, archive state | Flat group; no nested groups in the first expansion |
| GroupMembership | Group, Project, joining/ending revision and authorized actor | Many-to-many; one active edge per pair; no automatic access inheritance |
| EnvironmentProfile / EnvironmentProfileVersion | Project, host/roots, toolchains, configuration/secret references, validation status | One Project to many profiles; attempts pin immutable profile versions |
| ChangeSet | Group, outcome, coordinator Project, phase, required member tasks | Group 1 to many ChangeSets; tasks retain one owning Project |
| DependencyLink | Producer/consumer task or contract, required version and satisfaction predicate | Scoped graph; cycles require an explicit reviewed plan |
| ContractReference / ProjectAcknowledgment | Producer, authoritative source/version, affected consumer Project, acknowledging actor | One contract version to many consumer acknowledgments; no copied authority |
| IntegrationManifest | ChangeSet, member snapshots, profiles, contract versions, checks and review subject | Immutable; aggregate assessment derives from an exact revision set |
| IntegrationAssessment / IntegrationReview | Assessment version, ChangeSet, exact manifest/result versions, criteria, reviewer and exceptions | Group-owned; immutable review binds one assessment version; agent findings cannot create human acceptance |
| Principal / AgentInstance | Principal kind and identity provider; agent instance/runtime identity and accountable human | Each running agent has a declared credential principal; model name is metadata |
| RoleBinding / PolicyVersion | Principal, scoped role, allowed actions and explicit denies, revision | Deny wins in Studio; provider policy remains independently enforced |
| WorkAssignment | Task, accountable human, executor/reviewer references, revision/validity | Responsibility only; cannot substitute for a grant |
| DelegationGrant | Issuer, subject, parent grant, purpose, scopes, environment, validity and limits | Parent chain acyclic; child authority cannot exceed parent |
| MediaSourceReference | Capture identity, media version/time range, transcript/interpretation, consent/retention | Extends SourceReference; permissions and uncertainty preserved |

**Table D-5 — Additional invariants**

| ID | Invariant | Requirement links |
|---|---|---|
| INV-16 | Group visibility never implies access to member code, secrets or hidden counts | R-04-04, R-05-07 |
| INV-17 | Attempts pin one member Project and profile; shared plans cannot retarget a running attempt | R-10-07 |
| INV-18 | Integrated acceptance binds exact member snapshots and satisfied dependency versions | R-07-07, R-10-08 |
| INV-19 | Assignment does not grant authority; delegation is bounded, attributable and revocable | R-06-07, R-11-09, R-11-11 |
| INV-20 | Agent recommendation is distinct from human acceptance and enforced independence | R-11-10 |
| INV-21 | Media/simulation/provider output preserves origin, modality and execution class | R-09-07, R-11-12, R-11-13 |

GroupMembership removal updates future selection and cache authorization but does not cascade-delete evidence. A Project in several groups can face conflicting shared guidance; it must resolve applicable policy explicitly rather than combine group roles blindly. A first pilot can restrict a Project to one group while retaining the association model; Q-10 decides the supported policy.

A shared team service owns authorization and consistent updates; clients hold cache projections only. Offline changes may remain unapproved drafts, but offline clients cannot mint new authoritative approvals or grants against an unknown current policy. Reconnection checks revision, identity and membership before accepting writes. This requires a new deployment/security design beyond copying the local MVP database.

<!-- related-start -->
**Related sections:** [06. Tasks and Development Planning](../chapters/06-tasks-planning.md#ch-06) · [07. Engineering Decisions and Project Rules](../chapters/07-decisions-rules.md#ch-07) · [08. Execution Results and Evidence](../chapters/08-results-evidence.md#ch-08) · [09. Project Library and Resources](../chapters/09-library-resources.md#ch-09) · [10. Context, Memory, and Agent Orchestration](../chapters/10-context-orchestration.md#ch-10) · [11. Technical Integration and Trust](../chapters/11-integration-trust.md#ch-11)
<!-- related-end -->
