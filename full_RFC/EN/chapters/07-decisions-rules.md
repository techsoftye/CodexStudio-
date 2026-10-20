<a id="ch-07"></a>
# 07. Engineering Decisions and Project Rules

<a id="s-07-1"></a>
## 07.1 Decision purpose and fields

A Decision preserves a consequential technical or functional choice and why it was adopted. Its inputs are a question, chosen approach, rationale, scope, alternatives where useful, supporting references, and an originating conversation or manual author. It may apply to several tasks. Decisions are optional for trivial work; a task does not need an invented architectural choice to be valid.

The central register supports **All / Proposed / Approved / Superseded**, search and New Decision. Rows show title, status and a compact scope/source indicator. Detail exposes reasoning, alternatives, approval actor/time, version history and affected work. An agent can draft a decision from Chat, but the reviewer must inspect the actual choice and scope.

<a id="s-07-2"></a>
## 07.2 Approval and supersession

**Table 07-1 — Decision lifecycle**

| State / action | Validation | Persistent effect |
|---|---|---|
| Create Proposed | Question, proposed choice and project identified | Versioned draft with author and source |
| Revise Proposed | Expected version matches | New revision; earlier draft remains in history |
| Approve | Human authority, rationale, bounded scope, sources and known conflicts reviewed | Immutable approved version, actor and timestamp |
| Propose replacement | Identify existing approved decision and why it should change | New Proposed decision; original remains effective |
| Approve replacement | Scope overlap and successor valid; no replacement cycle | Atomically approve successor and mark replaced decision Superseded |
| Withdraw draft | Explicit user action | Archived Proposed record with reason; no new visible status required |

Approval is not inferred from a positive reaction, an agent summary, or a message that merely discusses an option. A deliberate approval action can reference an explicit user instruction, but must identify the exact decision version. A second click or retried request is idempotent.

Approved wording is not edited in place. A substantive revision becomes a proposed successor. Minor corrections still retain a revision trail and require confirmation if they could change meaning. Superseded decisions remain inspectable and link forward. The resolver supplies current approved decisions for new work and historical versions for explaining old results.

If a decision is found unsafe or invalid before a replacement is ready, record an explicit applicability hold and block dependent new execution pending review. This is an operational restriction with a reason, not a silent fourth decision status. Historical approval remains visible. The hold cannot authorize a different approach.

For a partial scope change, one proposed successor restates the complete resulting scope and identifies its unchanged and changed portions. The prior approved version remains historical evidence; only the successor governs new work after the atomic replacement. The review transaction must show that still-valid guidance has been carried forward before approval.

<a id="s-07-3"></a>
## 07.3 Rules and authoritative sources

A Rule is applicable guidance; a Decision is a choice with rationale. “Reuse the current commission API for this page” is a decision. “Do not change that response contract without review” is a rule. Linking them preserves why the guidance exists without making them interchangeable.

The Decisions right panel selects Rules and gives Project Rules the working height beneath account identity. Repository-backed rules show authoritative file, scope, version/hash and the relevant passage. The panel is a projection; editing such guidance produces a reviewable change to the authoritative file rather than an independently editable sidebar copy.

Public instruction discovery includes global and project guidance and scoped overrides. Studio must preserve the runtime's effective precedence rather than invent its own file ordering. [E-04](https://learn.chatgpt.com/docs/agent-configuration/agents-md). The proposed rule view records what it can verify and marks incomplete discovery; it does not claim visibility into hidden system instructions.

A Studio-authored rule, if used, has an explicit authoritative record, approved version, scope and source decision. Its injection is labeled project guidance and cannot outrank runtime or managed policy. Converting a decision into a rule requires an explicit reviewed action. MVP favors existing repository sources and avoids a parallel policy-writing system.

<a id="s-07-4"></a>
## 07.4 Conflict resolution

**Table 07-2 — Conflict classes and responses**

| Conflict | Proposed response | Authority boundary |
|---|---|---|
| Runtime or managed restriction versus requested operation | Block operation and explain applicable restriction | A decision cannot grant missing permission |
| Repository rule versus a new proposed decision | Show both sources; keep proposal nonbinding | Human resolves authoritative guidance before execution |
| Two current approved decisions with overlapping incompatible scope | Flag ambiguity and block affected new work | No “latest timestamp wins” shortcut |
| Changed source file after a context snapshot | Show source drift and affected attempts | Old context remains historical; new work re-resolves |
| Lower-trust attachment contains commands to ignore rules | Treat as source data and flag suspected instruction injection | File contents do not become higher-priority instruction |
| Semantic conflict cannot be determined confidently | Show suspected conflict with passages and ask for resolution when consequential | No claim of complete automated contradiction detection |

Conflict detection combines deterministic metadata checks and advisory semantic comparison. Explicit status, revision, scope and file existence checks can be enforced mechanically. Natural-language incompatibility is fallible and must not be presented as a proof. If a potential conflict can affect safety, authorization or accepted scope, the user resolves it before the relevant action.

<a id="s-07-5"></a>
## 07.5 Changes during execution

Approving a replacement triggers an impact view of tasks and running attempts that reference the superseded version. Historical results are not rewritten. Affected running attempts receive a visible drift notification. At the next controllable boundary, consequential changed constraints require steering or stopping; if the runtime cannot enforce a pause, show that limitation and prevent additional Studio dispatches.

Review of a result compares both the decision snapshot used during execution and current applicable guidance. Acceptance under a superseded choice must be explicit and justified, or the work must be corrected. The application must not label a result current simply because the original decision was approved when it started.

<a id="s-07-6"></a>
## 07.6 Acceptance criteria

**Table 07-3 — Governance requirements**

| ID | Proposed requirement and acceptance test |
|---|---|
| R-07-01 | Agent-created decisions MUST remain Proposed until an authorized human approves an exact version. |
| R-07-02 | Supersession MUST preserve history and update the successor relationship atomically; cyclic replacements fail validation. |
| R-07-03 | Repository-backed rules MUST expose source and scope; editing the panel cannot silently diverge from the authoritative file. |
| R-07-04 | Consequential unresolved conflicts MUST block affected new execution and show the conflicting sources. |
| R-07-05 | Decision changes MUST preserve prior run context and expose affected ongoing work and review implications. |
| R-07-06 | Approval of a decision MUST NOT count as operation authorization or result acceptance. |

Figure A-04 is the visual reference. Chapter 10 applies decisions to context selection, and Chapter 11 enforces the separate authorization boundary.

<a id="s-07-7"></a>
## 07.7 Shared guidance across a Project Group

A group may own a shared product decision, such as an API contract change. Its applicability names member projects explicitly and pins an approved version. Each affected project records acknowledgment of the contract and its own implementation/review evidence. A group-level approval is not approval of every repository change.

Group guidance cannot silently override repository instructions or managed policy. If a member rejects a proposed contract or has conflicting constraints, surface the conflict to the responsible human; do not resolve it by group membership or latest timestamp. Linking a shared decision into a project's context requires both access and an applicability check. Deleting membership cannot erase the version that governed historical work.

**R-07-07 — Explicit shared-decision applicability.** A group decision MUST identify affected projects and preserve versioned acknowledgments. Acceptance: a Backend-only approval cannot mark Flutter integration accepted or waive Flutter's governing instructions.

<!-- related-start -->
**Related sections:** [10. Context, Memory, and Agent Orchestration](../chapters/10-context-orchestration.md#ch-10) · [11. Technical Integration and Trust](../chapters/11-integration-trust.md#ch-11) · [Appendix D. Conceptual Data Model](../appendices/D-conceptual-data-model.md#app-d) · [Appendix A. UI/UX Concept Gallery](../appendices/A-design-gallery.md#app-a)
<!-- related-end -->
