# Codex Studio — A Project-Centric Engineering Workspace for Agentic Software Development

**Full Product Concept RFC — Complete Review Draft, version 1.1**

**Submitted by:** TechSoft  
**Original drafting date:** 2026-10-18  
**Status:** Independent proposal; not an official OpenAI product or release commitment.  
**Language:** English reference edition.

This document contains 15 complete chapters and 5 complete appendices. Normative words describe proposed Studio behavior. Existing capability claims are dated and sourced. Outstanding external decisions are recorded in Chapter 14; they do not represent missing chapter content.

[Terminology and translation conventions](../review/03-terminology.md) · [Review report](../review/06-review-report.md) · [Package README](../README.md)

## Contents

- [01. Executive Summary](#ch-01)
- [02. Current Product Landscape and Capability Baseline](#ch-02)
- [03. Real-World Problem Statement](#ch-03)
- [04. Product Rationale, Vision, and Positioning](#ch-04)
- [05. Project-Centric Workspace Architecture and UX](#ch-05)
- [06. Tasks and Development Planning](#ch-06)
- [07. Engineering Decisions and Project Rules](#ch-07)
- [08. Execution Results and Evidence](#ch-08)
- [09. Project Library and Resources](#ch-09)
- [10. Context, Memory, and Agent Orchestration](#ch-10)
- [11. Technical Integration and Trust](#ch-11)
- [12. Product Packaging and Delivery Strategy](#ch-12)
- [13. Validation and Expected Value](#ch-13)
- [14. Risks, Trade-offs, and Open Questions](#ch-14)
- [15. Proposal to OpenAI and Next Steps](#ch-15)
- [Appendix A. UI/UX Concept Gallery](#app-a)
- [Appendix B. Existing versus Proposed Capability Matrix](#app-b)
- [Appendix C. End-to-End Developer Scenario](#app-c)
- [Appendix D. Conceptual Data Model](#app-d)
- [Appendix E. References and Evidence](#app-e)

<a id="ch-01"></a>
# 01. Executive Summary

<a id="s-01-1"></a>
## 01.1 Proposal and decision sought

TechSoft proposes **Codex Studio — A Project-Centric Engineering Workspace for Agentic Software Development** as a dedicated desktop product for developers. It would reuse supported Codex execution capabilities and provide durable relationships among project conversations, intended work, engineering decisions, applicable rules, execution attempts, reviewed results, and files. This is an independent product concept submitted for engineering review, not an OpenAI announcement or an implementation commitment.

The decision sought is whether to evaluate a narrow, complete workflow: select work from a conversation, preserve its request, approve a consequential choice when necessary, execute under existing controls, inspect revision-specific evidence, and resume later with current guidance. Approval of this RFC would authorize design investigation only if the approving party explicitly says so; it would not authorize deployments or external access.

<a id="s-01-2"></a>
## 01.2 Problem and evidence boundary

The supplied TechSoft drafts describe difficulty reconstructing what was requested, approved, implemented, and verified across ongoing conversations. They are qualitative author observations. The archive contains no usability study, product telemetry, or controlled comparison establishing frequency or magnitude. The affiliate marketer page in Appendix C is an illustrative scenario, not an implemented Studio experiment.

Current tools already support substantial project work. Chapter 02 and Appendix B acknowledge the documented baseline. The hypothesis is that explicit relationships and independent state dimensions can reduce reconstruction and review errors beyond a credible existing setup. That hypothesis can fail: maintaining records may cost more time than it saves, and the existing product may already address some needs adequately.

<a id="s-01-3"></a>
## 01.3 What the product would add

The six views remain **Chat / Tasks / Decisions / Results / Library / More**. They query shared project records. A conversation filter changes visibility without creating private copies of shared tasks. A result links to a specific attempt and code snapshot; its review identifies exactly what a developer accepted. An approved decision retains the version supplied to earlier execution. Library exposes Project Files and Session Files with stable provenance.

The design separates four questions: is the task complete; did an execution attempt end; which checks actually ran; and did a human accept the result? These distinctions are operational requirements throughout the RFC. They prevent an agent's final sentence or a successful command exit from becoming an implicit acceptance record.

<a id="s-01-4"></a>
## 01.4 Product direction and initial scope

A standalone developer desktop product is the primary direction. Specialization provides room for engineering workflows and a coherent identity. It does not establish faster performance, lower memory usage, or cheaper delivery. A specialized workspace in the unified desktop application and an extension-based delivery remain comparison options in Chapter 12.

The proposed MVP is local, single-user, and centered on one project and one primary repository per execution. It includes all six navigation entries with bounded functions, manual and conversation-derived tasks, versioned decisions, repository rule references, execution attribution, evidence review, local Library references, basic context selection, restart recovery, and export. Optional cloud sources, automatic cross-device synchronization, rich team governance, and advanced parallel scheduling are later candidates. Prompt Templates are excluded.

<a id="s-01-5"></a>
## 01.5 Review standard

This is a complete **review draft**, not a release specification or proof of value. MUST, SHOULD, and MAY express proposed requirements: MUST is necessary for the described behavior; SHOULD permits a documented trade-off; MAY is optional. Stable requirement identifiers use `R-CC-NN`; evaluation cases use `V-NN`; unresolved questions use `Q-NN`. English is the reference text; Arabic carries the same meaning and identifiers.

Review should first test the state model and trust boundaries, then integration feasibility, then user value. The most consequential unknowns are runtime recovery guarantees, compatible authentication and distribution, evidence retention policy, and the incremental maintenance cost of independence. Chapter 14 assigns each an impact, owner role, and decision gate. No measured improvement, budget, delivery date, or OpenAI endorsement is claimed.

<a id="s-01-6"></a>
## 01.6 Version 1.1: coordinated projects and accountable teams

The full product concept now explicitly includes an optional Project Group over independently configured Projects, illustrated by MetaStore Backend, Flutter and Next.js. Later gated capabilities include environment profiles, dependency/contract tracking, coordinated Change Sets and combined evidence. A hybrid human/agent team uses scoped roles, separate work assignments, attributable delegation and human acceptance.

The 2026–2036 outlook adds optional voice/visual interaction and specialist robotics or quantum-development adapters where evidence justifies them. These additions preserve the six tabs, canonical task form, independent state dimensions and narrow local MVP. They are specifications for later review, not claims of shipped Studio capabilities or permission to alter the user's repositories. See Sections 02.6, 11.8–11.9 and 12.5–12.6.

<!-- related-start -->
**Related sections:** [02. Current Product Landscape and Capability Baseline](#ch-02) · [04. Product Rationale, Vision, and Positioning](#ch-04) · [12. Product Packaging and Delivery Strategy](#ch-12) · [13. Validation and Expected Value](#ch-13) · [14. Risks, Trade-offs, and Open Questions](#ch-14)
<!-- related-end -->

---

<a id="ch-02"></a>
# 02. Current Product Landscape and Capability Baseline

<a id="s-02-1"></a>
## 02.1 Verification method

The baseline was checked against official documentation on **2026-10-18**. Appendix E identifies final URLs, supported claims, and inference limits; Appendix B maps each capability to Studio's proposed addition. Documentation confirms a public description at the verification date, not universal account availability or a tested integration on this machine. The RFC does not use its own drafts, mockups, or filenames as evidence of shipped behavior.

Three labels are used consistently: **Existing** means supported by an opened official source; **Proposed** means a behavior specified by this RFC; **Requires Validation** means available evidence does not establish the needed behavior or guarantee. A row may contain all three. Failure to find documentation is never treated as proof that a feature is absent.

<a id="s-02-2"></a>
## 02.2 Existing foundations

The desktop documentation presents ChatGPT and Codex choices, with Chat and Work available within ChatGPT. Projects can organize related work; local projects connect work to folders. Work targets broader deliverables and overlaps with files and reviewable outcomes. These are existing foundations, not inventions of Studio. [E-01](https://learn.chatgpt.com/docs/app), [E-02](https://learn.chatgpt.com/docs/projects), [E-11](https://learn.chatgpt.com/docs/get-started-with-work).

Official pages separately document worktrees, code review, and scheduled tasks. Studio must evaluate these workflows before adding competing controls. A due date in a Studio task would remain planning metadata, with no automatic schedule implied. [E-07](https://learn.chatgpt.com/docs/environments/git-worktrees), [E-08](https://learn.chatgpt.com/docs/code-review), [E-09](https://learn.chatgpt.com/docs/automations).

Codex also has local memories, instruction discovery through `AGENTS.md`, skill loading, and subagent workflows. Studio's contribution is the proposed scope, approval, version, and evidence linkage around relevant material. It must not claim to introduce memory, instruction files, or delegation. [E-03](https://learn.chatgpt.com/docs/customization/memories), [E-04](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [E-05](https://learn.chatgpt.com/docs/build-skills), [E-10](https://learn.chatgpt.com/docs/agent-configuration/subagents).

<a id="s-02-3"></a>
## 02.3 Integration baseline

App Server documents a client interface involving threads, turns, items, streamed events, and approvals. Public integration guidance distinguishes App Server, the Codex SDK, and noninteractive execution. These support investigating reuse; they do not establish Studio's proposed entities, recovery contract, or permission to reuse every private desktop component. [E-06](https://learn.chatgpt.com/docs/app-server), [E-12](https://developers.openai.com/blog/codex-as-a-platform).

Chapter 11 proposes an adapter above the supported runtime. Its contract is a Studio design. A connector returning a thread identifier does not establish that Studio may read all historical conversations. A local file path does not establish cross-device access. The adapter must discover actual capabilities and degrade explicitly.

<a id="s-02-4"></a>
## 02.4 Overlap and authority

**Table 02-1 — Product boundary assessment**

| Surface | Existing or external responsibility | Studio proposal | Boundary requiring review |
|---|---|---|---|
| Codex runtime | Agent execution and configured controls | Attribute execution to task and context versions | Available events, interrupted-state reconciliation |
| Current desktop | Project and conversation experience | Connected engineering records across the six views | Duplication and navigation cost |
| ChatGPT Work | General deliverable workflows | Engineering-specific acceptance and code evidence | Shared components versus different product needs |
| IDE and Git workflow | Editing, code state, repository operations | Open exact evidence and current paths distinctly | Safe handoff and dirty-work preservation |
| Existing issue tracker | Team's chosen work authority | Optional reference to an external issue | No bidirectional status sync in MVP |

The table assigns proposed ownership; it is not a claim that external issue trackers lack equivalent concepts. A bounded documentary comparison was added in version 1.1; no comparative product trial or provider contract audit was performed. If a project already uses a tracker, Studio must identify whether a record is Studio-owned or externally referenced. MVP links cannot silently update external status.

<a id="s-02-5"></a>
## 02.5 What remains unverified

The current public baseline does not establish full session migration into an independent Studio, replay of every missed runtime event, an atomic launch spanning Studio and runtime storage, identical APIs across all hosts, or access to private reasoning. It also does not establish permission, support guarantees, licensing terms, or the cost of independent distribution. These are explicit investigation topics, not negative feature claims.

**R-02-01 — Claim traceability.** Every assertion of current capability MUST map to an official source and verification date. Acceptance: a reviewer can follow each Appendix B baseline row to Appendix E; unsupported guarantees remain classified Requires Validation. Proposed behavior must never acquire Existing status because it appears in a convincing mockup.

<a id="s-02-6"></a>
## 02.6 Existing umbrella and team foundations

Codex documents local multi-folder projects, with primary-folder distinctions discussed in Section 10.7. [E-02](https://learn.chatgpt.com/docs/projects). Codex Cloud documents reusable environments containing repositories and tools. [E-17](https://learn.chatgpt.com/docs/cloud). These are existing overlap, not novelty claims for Studio.

Outside Codex, VS Code provides multi-root workspaces; GitLab Groups organize related projects and permissions; dev containers describe reproducible development environments. [E-14](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces), [E-15](https://docs.gitlab.com/user/group/), [E-16](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers). Folder grouping, project governance and environment setup solve different portions of the problem. None alone proves compatibility between a Backend contract and two client revisions.

ChatGPT Teams and Team Tasks document shared work and service-account execution; workspace roles and workload identity federation document distinct access boundaries. [E-19](https://learn.chatgpt.com/docs/enterprise/teams), [E-18](https://learn.chatgpt.com/docs/enterprise/roles-and-workspace-permissions), [E-20](https://developers.openai.com/api/docs/guides/workload-identity-federation/federation-rules). These support the feasibility investigation for governed human/agent work, but do not verify the exact Studio role matrix or uniform availability in every account.

The proposed addition is the explicit connection among independently configured Projects, versioned contracts, accountable delegation and combined acceptance evidence. Whether that connection should be built, integrated or omitted remains a comparative product question. Existing investment is a need indicator, not measured demand for another desktop product.

<!-- related-start -->
**Related sections:** [Appendix B. Existing versus Proposed Capability Matrix](#app-b) · [Appendix E. References and Evidence](#app-e)
<!-- related-end -->

---

<a id="ch-03"></a>
# 03. Real-World Problem Statement

<a id="s-03-1"></a>
## 03.1 Available observation

The starting evidence is TechSoft's supplied account of recurring planning, implementation, review, and resumption in ongoing software projects. It describes scattered requirements, decisions and outputs. It does not include time measurements, interview transcripts, or an incident dataset. The proposal therefore treats the problem as plausible and concrete, with prevalence and commercial significance still unmeasured.

The relevant unit is a feature continued across sessions. A developer can locate a conversation yet still need to establish whether a suggestion was adopted, whether a later correction superseded it, and whether the evidence refers to the current code. That reconstruction is distinct from simply retrieving text.

<a id="s-03-2"></a>
## 03.2 Problem register

**Table 03-1 — Observations, interpretations, and falsifiable consequences**

| ID | Qualitative observation in supplied drafts | Interpretation to test | Observable failure in an evaluation |
|---|---|---|---|
| P-01 | Alternatives and accepted choices share discussion history | Approval is expensive to recover | Participant selects a superseded or unapproved choice |
| P-02 | A closing response may leave verification unfinished | Task progress is conflated with agent progress | Participant calls a feature Done while a required check is Not Run |
| P-03 | Diffs, logs, and summaries require manual association | Evidence identity is difficult to assess | Participant uses a passing check from a different revision |
| P-04 | Relevant constraints must be restated on resumption | Context recovery requires avoidable work | Participant omits a known applicable constraint or repeats its explanation |
| P-05 | Organization itself requires upkeep | A structured product may add burden | More maintenance time than recovery time saved |

These are evaluation failure definitions, not claims that such failures occurred at measured rates. Their proposed remedies belong in Chapters 05–11; Chapter 13 specifies how to compare them fairly.

<a id="s-03-3"></a>
## 03.3 Existing workarounds

A developer can keep repository decision records, issue descriptions, checklists, Git history, and links to relevant conversations. This is a credible baseline. It offers explicit review and portable knowledge; the effort lies in keeping relationships and freshness current. A skilled team may already maintain these well enough that Studio adds little value.

Another workaround is to keep a feature in one long conversation. It can preserve detail but does not by itself specify independent task acceptance, versioned decisions, or the relationship between a test and a code snapshot. This statement is a distinction in the conceptual model, not a diagnosis of undisclosed Codex storage.

Studio should therefore reduce bookkeeping by capturing provenance when actions occur. It must not require a developer to rewrite every useful message, manually duplicate source files, or categorize every question before receiving help. If reliable automatic attribution is unavailable, the interface should expose the limitation rather than conceal manual maintenance.

<a id="s-03-4"></a>
## 03.4 Scenario and scope

Appendix C uses the affiliate marketer page already present in the mockups. The illustrative request is to inspect the existing application and plan the page; implementation requires a subsequent instruction. The example considers commission summaries, referral activity, and payout information without establishing a real endpoint, schema, balance, or financial result.

The scenario is useful because it has a consequential reuse decision, interface work, evidence review, and a later return to unfinished verification. It does not justify adding financial logic to Studio. The host application remains responsible for domain data and authorization.

<a id="s-03-5"></a>
## 03.5 Evidence needed before investment

Recruit participants who actually return to software work after an interruption, including developers with organized repository documentation. Observe current practice before introducing Studio terminology. Ask them to retrieve an approved constraint, explain an incomplete result, and identify the next safe action. Record errors and maintenance effort as well as speed.

**R-03-01 — Honest problem evidence.** The evaluation MUST separate self-reported friction from observed task errors and measured time. Acceptance: the study dataset identifies its evidence type and does not report the illustrative scenario or mockup values as participant results. If participants already recover state reliably and quickly, reduce or reject the corresponding product claim.

<!-- related-start -->
**Related sections:** [Appendix C. End-to-End Developer Scenario](#app-c) · [13. Validation and Expected Value](#ch-13)
<!-- related-end -->

---

<a id="ch-04"></a>
# 04. Product Rationale, Vision, and Positioning

<a id="s-04-1"></a>
## 04.1 Why a dedicated product

The principal proposal is a specialized desktop workspace whose daily language is software work: requirements, changes, constraints, checks, review, and continuation. Product independence would allow those workflows to develop coherently and make their ownership visible. The project remains the durable organizing unit while conversations remain an efficient way to direct an agent.

Independence has a cost: distribution, security updates, account experience, accessibility, support, data migration, and integration compatibility must all be maintained. A shared engine does not eliminate those costs. Chapter 12 compares packaging options without treating a separate executable as proof of value.

<a id="s-04-2"></a>
## 04.2 Target users and jobs

**Table 04-1 — Priority users and expected jobs**

| User context | Job Studio should support | Observable value |
|---|---|---|
| Individual developer maintaining a feature over several sessions | Recover the current task, choice and outstanding check | Correct next action without reconstructing all discussion |
| Engineer reviewing agent changes | Compare requested scope with revision-specific evidence | Identify unsupported completion claims |
| Maintainer of an established repository | Preserve applicable conventions while work moves between conversations | Relevant guidance stays traceable to its source |
| Later team pilot | Hand work to another authorized engineer | Clear attribution without pretending shared approval policy already exists |

The MVP serves the first three contexts with one local human owner. A team can review exported documents, but shared concurrent editing, delegated approval roles, and organization-wide policy administration are not implied by that review. Those require additional product and security decisions.

<a id="s-04-3"></a>
## 04.3 Goals

The core goal is an inspectable chain from intent to evidence. A user can answer what is wanted, why a consequential choice was approved, what an attempt changed, which checks support it, and what remains unresolved. The system should preserve those answers across restarts and changing working trees.

The second goal is low-friction adoption. The developer can continue using the repository and IDE, leave task organization unset, and ask questions without creating records. Structure is added at meaningful transitions. The third goal is bounded agent context: select relevant material while preserving required guidance and showing what could not be retrieved.

<a id="s-04-4"></a>
## 04.4 Exclusions and product discipline

Studio does not propose a new model or replacement agent harness, a general IDE, a universal file manager, a financial ledger, a full enterprise project-management suite, or a hidden-reasoning viewer. Prompt Templates, a separate Execution main tab, and extra task creation fields such as Assignee, generic Related To, or Add Sub-task remain excluded.

The More tab has a bounded operational role, defined in Chapter 05. It is not a commitment to add whatever tools later fit in a menu. Optional integration examples in images do not enlarge the MVP. Product requirements in this RFC are proposals for review; they do not change existing account settings, authorize new providers, or execute code.

<a id="s-04-5"></a>
## 04.5 Principles with operational consequences

**R-04-01 — Project continuity.** All structured records MUST carry their owning Project identity, or explicit Group identity for group-owned coordination records, and cross-project access MUST be checked even when a link is known. Acceptance: opening a record from a different project cannot silently change the active execution target or reveal inaccessible content.

**R-04-02 — Optional structure.** A title-only task and an ordinary conversation MUST remain valid entry points. Acceptance: a user can ask a question without a task, and create a task without Stage, Section, Parent Task, Due Date, Skills, or attachments.

**R-04-03 — Reuse with accountability.** Studio SHOULD use a supported Codex integration while owning its own record consistency and review semantics. Acceptance: the architecture review identifies which component owns every persistent record and failure response; no private OpenAI service or undocumented database is assumed.

<a id="s-04-6"></a>
## 04.6 Differentiation to validate

The proposed distinction is the combination of navigable provenance, independent lifecycle dimensions, current approved guidance, and durable evidence references. None alone proves novelty or demand. Review should compare the complete workflow against an organized current setup and against an integrated workspace alternative. A strong result would be correct, faster continuation with manageable administrative cost; a weak result would be another interface that users must keep synchronized by hand.

<a id="s-04-7"></a>
## 04.7 Project Groups and hybrid teams

A **Project Group** is an optional product-level umbrella over independently configured Projects. In the user's MetaStore example, Backend, Flutter and Next.js belong to the same product while retaining their repositories, dependencies, execution environments, instructions and release responsibilities. This example uses the user's description; no repository inspection or environment diagnosis was performed.

A Group is not a merged filesystem, mandatory monorepo, shared credential pool or runtime environment. A Project remains the ownership boundary for tasks and attempts. Group-owned coordination records carry group identity and explicit member-project links. Membership in the umbrella does not itself grant access to every member. Independent projects continue to work without a Group.

The full concept includes a hybrid team: humans define responsibility and approve consequential outcomes; agents execute or review within explicit delegated scopes. A named specialist, model or skill is a capability label, not an authorization identity. The agent instance, credential principal and accountable human must be distinguishable. A team assignment is recorded outside the canonical New Task form; the excluded Assignee field is not reintroduced.

The user need is plausible because existing products already invest in multi-folder workspaces, project groups and reusable environments, but this is evidence of a recognized coordination problem rather than proof that Studio will solve it economically. Chapter 02 acknowledges that overlap; Chapters 05, 10 and 11 specify the additional behavior, and Chapter 13 tests its incremental value.

**R-04-04 — Explicit umbrella boundary.** A Project Group MUST preserve member-project identity, environment selection and authorization. Acceptance: adding Backend and Flutter to one group neither changes their working directories nor grants either participant new repository access. Group coordination records identify their own scope rather than masquerading as project records.

<!-- related-start -->
**Related sections:** [05. Project-Centric Workspace Architecture and UX](#ch-05) · [12. Product Packaging and Delivery Strategy](#ch-12)
<!-- related-end -->

---

<a id="ch-05"></a>
# 05. Project-Centric Workspace Architecture and UX

<a id="s-05-1"></a>
## 05.1 Workspace identity and navigation

The workspace exists to make project state navigable without forcing every exchange into a task. Its inputs are the active project, optional conversation, selected tab, record selection, and view filters. The user selects the project explicitly; the agent may suggest related records but cannot change the execution target merely by presenting a link.

The left side organizes projects and their conversations. The center contains exactly **Chat / Tasks / Decisions / Results / Library / More**. The right panel keeps account identity and changes its working content with the selected view. A project header exposes the active repository or folder and conversation filter when present. A general conversation has no implicit project records; attaching it to a project requires an explicit choice and a permission check.

Navigation state is separate from domain state. Remember the last tab, filters, selection and scroll position per project locally. Returning from a linked result restores the task's previous position. A result opened through a task carries a return path, not a duplicate task screen. Switching projects invalidates selections that belong to the prior project. It does not move records or retarget an active run.

<a id="s-05-2"></a>
## 05.2 Chat behavior and record promotion

Chat supports discussion, inspection, planning, and instructions to execute within existing permissions. A user can keep a small edit entirely conversational. Creating structured work is optional. The three referenced actions have distinct effects:

**Table 05-1 — Chat actions and saved effects**

| Action | User and agent behavior | Saved effect / error behavior |
|---|---|---|
| More Details | User requests elaboration; agent explains the selected proposal | Continues discussion; no approval or task state change |
| Add to Tasks | Agent suggests actionable items; user selects and edits drafts | Save selected items atomically with message references; failed save retains drafts |
| Create Task | User opens a single editable draft, optionally prefilled | Same validation as Chapter 06; no execution on save |
| Capture decision | User requests extraction of a consequential choice | Proposed decision with source reference, never automatic approval |

A source reference identifies conversation, message and, where supported, the selected passage or message revision. If the underlying surface cannot supply a stable message identity, capture an explicitly labeled excerpt with capture time and provenance limitation. Do not manufacture a runtime message ID. Repeating a save after a timeout uses the same action key so it cannot create duplicate tasks.

Chat's right panel defaults to Sources and shows relevant conversation context below. Rules may be reachable as a secondary option; Sources must not display rule content when selected. Selecting a source shows whether it is a live file, captured artifact, or unavailable reference. A quoted document remains information; its instructions do not become approved project policy.

<a id="s-05-3"></a>
## 05.3 Right-panel contracts

**Table 05-2 — Contextual panel behavior**

| Tab | Default content | Selection / subview | Return behavior |
|---|---|---|---|
| Chat | Sources; compact conversation context | File/source detail | Return to source list without moving the chat |
| Tasks | Stages / Sections; compact Current Context | New Task replaces working panel content; account identity remains | Back to Tasks restores prior stage/section filter |
| Decisions | Rules selected; Project Rules uses available height | Rule provenance or authoritative source | Return to rules without resetting decision selection |
| Results | Selected result and evidence links; compact overview | Check, change or artifact detail | Return to same attempt and review state |
| Library | Selected file details; optional supported External Sources | Preview or authorized source selection | Restore Project Files / Session Files scope |
| More | Configuration or diagnostic detail appropriate to selection | Detail only for bounded functions | Restore originating view and project |

Tasks' Current Context shows active project, relevant conversation and selected organization when known. “Affiliate Module” in the image is example content; Studio must not assume that every project uses modules. With no selected result or file, show a neutral selection prompt rather than stale details from another record.

<a id="s-05-4"></a>
## 05.4 More and operational visibility

More contains project configuration, observable execution history and diagnostics in the MVP. Configuration includes project bindings and local evidence/export settings; it does not create a new permission engine. Diagnostics shows adapter connectivity, version compatibility, unresolved dispatch/recovery items, and sanitized event references. Detailed history is reachable from a result and retains attempt identity.

Entering More is read-only. Changing a binding or retention setting requires an explicit save with its impact shown. An invalid folder, unsupported adapter or failed export must produce an actionable error and retain the prior valid setting. Export produces a local package only. No operation is triggered by merely expanding diagnostic history.

Critical approvals, storage failures and interrupted attempts remain visible beside the affected task or conversation even when More is closed. Logs concern available commands, tool events, approvals and outputs; private model reasoning is outside scope. No separate More mockup exists and none is invented.

<a id="s-05-5"></a>
## 05.5 Interaction states and accessibility

Each list distinguishes loading, empty project, no filter matches, unavailable source, access denied, stale data and save conflict. An empty filtered list offers Clear filters; it does not invite duplicate project creation. Pending writes show saving and confirmed states. A failed write leaves a recoverable draft and does not claim success.

The desktop layout must adapt when the right panel cannot coexist with the center: use a dismissible pane or full-width subview while preserving navigation and focused control. Keyboard operation must reach tabs, lists, forms, evidence and Back actions. Focus returns to the invoking control. Status uses text plus visual cues, not color alone. Loading and validation are announced to assistive technology. English and Arabic layouts must preserve readable paths, code, timestamps and identifiers; these technical strings remain left-to-right within an RTL layout. No claim of accessibility conformance is made before implementation testing.

<a id="s-05-6"></a>
## 05.6 Acceptance criteria

**Table 05-3 — Workspace requirements**

| ID | Proposed requirement and acceptance test |
|---|---|
| R-05-01 | Switching tabs MUST preserve project identity. Start a run, switch projects, and confirm the run remains bound to its original project. |
| R-05-02 | Task promotion MUST be editable and nonexecuting. Save selected items twice after a simulated timeout; one logical save produces one set of tasks. |
| R-05-03 | Panels MUST follow Table 05-2. Opening and closing New Task restores the previous task filter and keyboard focus. |
| R-05-04 | Navigation MUST distinguish inaccessible, missing and filtered records without showing another record's content. |
| R-05-05 | Every primary action MUST be keyboard accessible and understandable without color; verify English and Arabic at enlarged text sizes. |
| R-05-06 | More MUST expose diagnostics without starting work; blocking approvals must also remain visible at their source. |

Figures A-01 through A-06 illustrate the inherited shell. Appendix A records their deviations. Chapters 06–09 own the individual record interactions; Chapter 11 owns persistence and permission enforcement.

<a id="s-05-7"></a>
## 05.7 Group navigation and environment visibility

The group expansion adds a selector above the existing project navigation, not a seventh main tab. Opening MetaStore shows its authorized member projects and a permission-filtered overview. Chat / Tasks / Decisions / Results / Library / More remain unchanged. A group-level conversation may plan work, but mutating execution requires selection of a concrete Project and Environment Profile. Every launch confirmation identifies both; group selection alone is insufficient.

Tasks and Results can show a grouped read view labeled by originating project. Counts only include accessible records and must not disclose hidden project names, amounts or result summaries. Each item opens its owning project with a return path. Group planning creates a Change Set linking project-local tasks; it does not make one task simultaneously owned by three projects. Cross-project Parent Task links remain invalid.

More holds group membership, dependency and environment-profile configuration for authorized administrators. Member project selection restores that project's contextual right panel. A group overview has no selected project panel; it shows an explicit selection prompt. Existing six drawings remain the single-project references; the proposed group selector and access controls are textual specifications, not depicted controls.

Creating a group requires a name and authorized project references. Adding a member validates the owner and records membership revision. Removing or archiving a member retains historical links, prevents new group dispatch to it, and flags affected Change Sets; it neither deletes the project nor stops an active process silently. Duplicate membership is rejected. Concurrent edits compare revision. An unavailable project displays an access-appropriate unavailable state.

**R-05-07 — Group navigation without implicit execution.** Group views MUST retain originating project labels and permission-filtered counts. Acceptance: switch between Backend and Flutter, then launch; only the explicitly confirmed project/profile is targeted, and inaccessible records do not leak through search, counts or previews.

<!-- related-start -->
**Related sections:** [06. Tasks and Development Planning](#ch-06) · [07. Engineering Decisions and Project Rules](#ch-07) · [08. Execution Results and Evidence](#ch-08) · [09. Project Library and Resources](#ch-09) · [Appendix A. UI/UX Concept Gallery](#app-a)
<!-- related-end -->

---

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
**Related sections:** [08. Execution Results and Evidence](#ch-08) · [Appendix D. Conceptual Data Model](#app-d) · [Appendix A. UI/UX Concept Gallery](#app-a)
<!-- related-end -->

---

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
**Related sections:** [10. Context, Memory, and Agent Orchestration](#ch-10) · [11. Technical Integration and Trust](#ch-11) · [Appendix D. Conceptual Data Model](#app-d) · [Appendix A. UI/UX Concept Gallery](#app-a)
<!-- related-end -->

---

<a id="ch-08"></a>
# 08. Execution Results and Evidence

<a id="s-08-1"></a>
## 08.1 Purpose and independent state dimensions

Results answers what happened during an execution attempt and what evidence supports the reported outcome. A Task describes intended work; an Execution Attempt records runtime activity; a Result summarizes that attempt; a Check records verification; a Review records human acceptance. A File is supporting material, not the result itself.

**Table 08-1 — State dimensions**

| Dimension | Proposed values | Meaning |
|---|---|---|
| Task | Todo / Active / Review / Done / Deferred | Planning and accepted completion |
| Attempt lifecycle | Queued / Starting / Running / WaitingApproval / Interrupted / Finished / Failed / Unknown | Runtime activity, independent of work quality |
| Result outcome | Completed / Partial / Failed; unset while undetermined | Reported achievement against captured task scope |
| Check | Passed / Failed / Not Run / Inconclusive | Evidence from a specific check on a specific snapshot |
| Result review | Pending Review / Accepted / Changes Requested | Human judgment of an exact result version |

Unknown means runtime state cannot currently be established; it is not success or confirmed failure. Interrupted means interruption is confirmed. Finished means execution ended normally, not that the task passed. An unavailable test environment yields Not Run, while a test that ran but produced insufficient usable evidence is Inconclusive. A suite with mixed results is represented by individual checks or an explicitly partial suite, never a misleading single pass.

The preserved quick filters are **All / Completed / Partial / Failed / Pending Review**. Pending Review selects a separate review dimension and may overlap all outcomes. An unknown or unfinished attempt remains discoverable from All with outcome unset. Any summary counts must state their dimensions and must not add overlapping buckets into a total.

<a id="s-08-2"></a>
## 08.2 Result contents and evidence capture

A result identifies project, task and task version, attempt, relevant runtime references, execution environment, start/end observations where known, context manifest, work summary, changed files, check records, unresolved findings and linked artifacts. Outcome is an attributed assessment, not a direct reading of an agent's confidence.

The code identity must include a commit or equivalent immutable base and the actual change snapshot. For dirty working trees, capture the preexisting state and resulting patch or artifact hashes. A branch name alone is insufficient. Untracked and binary files need explicit inclusion or exclusion. If safe capture is unavailable, label evidence incomplete and prevent a verified-completion claim.

A changed-file count derives from the captured change set. Test counts derive from a parser or tool output with a known source. If the tool emits only exit status, display that fact rather than inventing test totals. A command record includes command description, working directory, environment identifier, relevant tool version when available, timestamps, exit status and accessible output reference. Secrets must be redacted without concealing that redaction occurred.

**Table 08-2 — Evidence identity and limits**

| Evidence | Minimum binding | Limit displayed |
|---|---|---|
| Diff | Base revision plus captured patch and included file set | Preexisting changes, untracked exclusions or unsupported binaries |
| Test report | Command/check ID, snapshot, environment, observation time | Failed / Not Run / Inconclusive checks; parser limitations |
| Screenshot or generated report | File version/hash, origin and capture context | Illustration versus runtime observation |
| Agent summary | Authoring attempt and supporting references | Reported interpretation; not independent test evidence |
| External check link | Provider identity, external record and revision if available | Unavailable content or unverifiable current access |

<a id="s-08-3"></a>
## 08.3 Review workflow

The user selects a result; the right panel shows that result and its evidence links. **Review Changes** opens the captured change set by default, clearly distinguishing it from the current checkout. **Open Task** returns to intended scope and criteria. **Re-run** opens a new execution intent after current context, side effects, repository and authorization are checked.

Review proceeds against the captured task version and acceptance criteria. The reviewer can accept, request changes, or leave the result pending. A request for changes records specific findings and moves the task to Active only through the corresponding task transition. An Accepted result remains an immutable historical judgment even when later code changes make it inapplicable to the current tree.

Task completion can cite several accepted results if no single attempt covers the full scope. The completion record must identify which result or manual evidence supports each criterion. A latest-run shortcut is insufficient. Accepting an inspection-only result may close an analysis task; it cannot establish implementation completion for a different task.

<a id="s-08-4"></a>
## 08.4 Missing verification and exceptions

A required Not Run, Failed or Inconclusive check blocks **verified completion**. If the responsible human intentionally accepts a narrower outcome or waives a criterion within their authority, record the exception, reason, actor, affected criterion and follow-up. The result and task visibly retain “accepted with verification exception”; no missing check becomes Passed.

Mandatory policy requirements cannot be waived through a Studio button. If a release check is required by repository or organization policy, the result may be accepted for limited development review, but cannot claim release readiness. Closing a task and granting permission to deploy are separate operations.

When a check is rerun after code changes, it belongs to the new snapshot and usually a new attempt. If additional evidence is attached without changing the code, create a new result version; existing acceptance remains bound to the old version until reviewed again. Corrections to summaries cannot mutate underlying command output.

<a id="s-08-5"></a>
## 08.5 Retry, interruption and recovery

Re-run is not command replay. It creates a new attempt linked to its predecessor and includes unresolved findings and current guidance. Before repeating an operation with external side effects, establish whether the earlier operation occurred. An uncertain dispatch or timeout must be reconciled before another start.

An interrupted attempt retains partial changes and available evidence. The user can inspect, continue where supported, or start a correction. Studio never silently resets a worktree. A crash before result finalization produces an incomplete record that can be reconciled from available runtime events; refreshing Results cannot execute work.

<a id="s-08-6"></a>
## 08.6 Acceptance criteria

**Table 08-3 — Evidence requirements**

| ID | Proposed requirement and acceptance test |
|---|---|
| R-08-01 | All five state dimensions MUST remain independent. A Finished attempt with a Not Run required check stays unverified and Pending Review. |
| R-08-02 | Review Changes MUST open the recorded snapshot or explain its unavailability; it cannot substitute today's file. |
| R-08-03 | Counts and check states MUST be evidence-derived. A successful build cannot populate unrelated acceptance checks as Passed. |
| R-08-04 | Re-run MUST create a new attributable attempt and preserve earlier evidence; unknown side effects require reconciliation. |
| R-08-05 | Acceptance MUST bind actor, exact result version and task criteria; exceptions remain visible and cannot bypass enforced policy. |
| R-08-06 | Additional evidence or corrected summaries MUST preserve review history and require renewed acceptance when its subject changes. |

Figure A-05 contains illustrative counts only. Chapter 11 defines event ingestion and recovery; Appendix C demonstrates the distinctions in a continuous example.

<a id="s-08-7"></a>
## 08.7 Attempt transition contract

**Table 08-4 — Execution-attempt transitions**

| From | Trigger | To and guard |
|---|---|---|
| Queued | Explicit dispatch after context and permission validation | Starting; durable intent exists |
| Starting | Runtime acknowledges active work | Running; runtime identity persisted |
| Starting | Explicit launch rejection | Failed; preserve rejection and any known side effects |
| Starting or Running | Connection lost or acknowledgement ambiguous | Unknown; retain last confirmed observation |
| Running | Runtime requests operation consent | WaitingApproval; request identity and scope visible |
| WaitingApproval | Valid consent and runtime continuation | Running; never infer continuation from the UI click alone |
| WaitingApproval | Denial, expiry or cancellation | Follow observed runtime outcome: Running with denied action, Interrupted or Failed; no invented terminal state |
| Running | Normal terminal event | Finished; result outcome and review remain separate |
| Running | Confirmed runtime failure or interruption | Failed or Interrupted; preserve partial evidence |
| Unknown | Supported reconciliation finds current/terminal state | Corresponding observed state; no automatic new dispatch |
| Interrupted | Explicit supported continuation | Running with context amendment, or a new linked attempt if continuity cannot be established |
| Finished or Failed | User requests Re-run | New Queued attempt; original remains terminal |

**R-08-07 — Observable transitions.** Attempt state MUST follow confirmed runtime events or an explicitly uncertain observation. Lost connectivity cannot establish Finished, and a rejected approval cannot be translated into an assumed cancellation without runtime evidence.

<a id="s-08-8"></a>
## 08.8 Group integration evidence

Each member task retains its own results and acceptance history. The Change Set's integration assessment references these results and an immutable Integration Manifest; it is not a File and cannot be represented by a count of green task badges. Record missing platforms, stale contracts and failed member checks explicitly.

Acceptance of a group outcome requires an authorized human judgment on the combined evidence. A member's accepted result remains historical if later contract drift invalidates compatibility; the integration assessment becomes stale and needs renewed evidence/review. Accepting integration does not grant deployment authority. Sections 10.8 and D.8 define the coordination relationships; V-14/V-15 specify the partial-failure cases.

<!-- related-start -->
**Related sections:** [06. Tasks and Development Planning](#ch-06) · [09. Project Library and Resources](#ch-09) · [11. Technical Integration and Trust](#ch-11) · [Appendix C. End-to-End Developer Scenario](#app-c) · [Appendix D. Conceptual Data Model](#app-d) · [Appendix A. UI/UX Concept Gallery](#app-a)
<!-- related-end -->

---

<a id="ch-09"></a>
# 09. Project Library and Resources

<a id="s-09-1"></a>
## 09.1 Purpose, views and classifications

Library provides access to the material used or produced in project work while preserving origin and version. Its primary views are **Project Files / Session Files**. Project Files contains project-associated references, selected repository paths and maintained artifacts. Session Files contains attachments and generated outputs associated with an identified conversation. It is not a browser for all raw runtime session logs.

A single file version may appear in both views through associations. Inputs, Outputs and Resources are classifications within Library. A generated report can be an Output and a document; when reused by another task it may also be that task's Input. Classification belongs to the relationship or usage, not an exclusive permanent label on the bytes.

Type filters remain **All / Docs / Code / Images / Data / Archives**. Search matches visible metadata and, only when explicitly supported and authorized, indexed content. Sorting uses named fields such as modified time or filename. Optional list/grid presentation must not change selection or permissions. No mandatory cloud connection is required.

<a id="s-09-2"></a>
## 09.2 File identity and provenance

**Table 09-1 — Reference kinds**

| Kind | Identity and version | Expected behavior |
|---|---|---|
| Live repository file | Project root binding plus relative path; current revision/hash when read | Opening live source shows current content, with a live indicator |
| Uploaded attachment | Stable artifact identity, original name, content hash and capture time | Immutable captured version; replacement creates a new version |
| Generated artifact | Attempt/conversation origin, file identity and hash | Linked from Results; cannot be mistaken for a measured test if illustrative |
| External reference | Provider/account scope, external ID, version when available | Availability depends on authorization; cache behavior is explicit |
| Historical evidence file | Exact recorded version/hash and evidence relation | Opening never silently resolves to a newer same-named file |

A filename is a label, not identity. Two sessions can contain different files with the same name. The list must show enough source/session information to distinguish them. Deduplicating identical bytes is optional storage optimization within an authorized boundary; it must not leak that another project possesses a file.

<a id="s-09-3"></a>
## 09.3 Ingest, selection and preview

Users can upload a file, select an existing authorized reference, or associate a generated output with the project. An agent may propose that association; it does not automatically expose every generated or personal file to future tasks. Import stages are selected, validating, available, or failed. Validation checks safe path resolution, content type, size limits provided by implementation, readable content where required, and permissions.

The right panel shows selected-file metadata, location, origin, availability, linked work and **Open / Preview** actions. Preview should use a safe renderer appropriate to type. Unsupported formats offer an explicit open/download route without executing embedded content. Archives are listed without automatically extracting them. An invalid path, denied access, corrupt file or unsupported preview yields a specific message while preserving the reference.

Removing an association from a task or session does not delete the underlying file. Deleting an owned artifact is a separate action showing affected evidence links and retention implications. Live repository deletion should remain an explicit file operation under runtime permissions, not a side effect of clearing a Library row.

<a id="s-09-4"></a>
## 09.4 Availability and lifecycle

Availability is independent of classification: Available, Missing, Access Denied, Offline, or Version Unavailable. An external reference may remain a visible historical record after revocation while its content becomes inaccessible. The UI should not infer that cached bytes are authorized for continued use merely because they exist.

Moving a repository root changes the binding only after identity and containment are checked. If the same relative path resolves to different bytes, historical links remain attached to their recorded version. Results' evidence retention rules take priority over convenience cleanup. If policy requires removal, leave a tombstone stating what is no longer available and why; do not retain prohibited content under the guise of auditability.

Search indexing respects project access and deletion. A deleted or revoked document must not remain retrievable through a stale index. Index rebuilds are derivable operations and cannot alter authoritative records or approval state.

<a id="s-09-5"></a>
## 09.5 Optional external sources

The inherited mockup names Google Drive, Dropbox, OneDrive, Import from URL and Sync from Git repository. Those are design examples. This RFC does not verify their compatibility with a standalone Studio or promise them in the MVP. Provider authorization, scopes, revocation, revision access, rate limits and retention must be evaluated individually.

A future connection flow must identify provider account, chosen resource scope, project association and intended agent access. Connecting an account does not grant all projects its entire contents. A URL import is content retrieval, not permission to execute instructions inside the page. “Sync from Git repository” must not imply an automatic pull, branch change or overwrite when viewing Library. These behaviors require separate approved integration design.

<a id="s-09-6"></a>
## 09.6 Acceptance criteria

**Table 09-2 — Library requirements**

| ID | Proposed requirement and acceptance test |
|---|---|
| R-09-01 | Project Files and Session Files MUST remain primary views; Input/Output/Resource and type filters do not replace them. |
| R-09-02 | A file shared by project and session associations MUST retain one logical identity and distinguish revisions. |
| R-09-03 | Live and historical references MUST open their stated versions; a missing historical artifact cannot fall back silently to the live path. |
| R-09-04 | Preview and import MUST validate access and safe handling; malformed files cannot trigger executable content. |
| R-09-05 | Removing an association MUST NOT delete bytes; deleting retained evidence requires an explicit policy-aware action and availability record. |
| R-09-06 | External access MUST be scoped and revocable; unavailable providers remain unavailable rather than suggesting a working integration. |

Figure A-06 illustrates navigation. Chapter 08 owns interpretation of evidence; Chapter 11 owns storage, containment, retention and export.

<a id="s-09-7"></a>
## 09.7 Shared contracts and multimodal evidence

A group-shared reference is a permission-checked FileAssociation exposed within a member's Project Files; it is not a third primary Library division. Session attachments remain Session Files, and Input/Output/Resource remain usage classifications. Shared API contracts retain producer project, immutable version/hash, consumer associations and availability. Membership changes invalidate access and cached previews.

Optional voice/video interaction produces consented SourceReferences: transcript or frame/time range, origin, capture time, model interpretation and retention choice. An interpretation is separate from the captured media. Screen images can contain secrets; scope the capture, redact exports and preserve an explicit omission marker. Audio/video collection is off unless the user invokes it and the selected integration supports it. A transcript cannot authorize a repository write merely by quoting “approved.”

**R-09-07 — Shared and multimodal provenance.** Shared contracts and media-derived context MUST retain source/version and access scope. Acceptance: revocation removes future retrieval, an uncertain transcript stays uncertain, and a visual claim links to the captured frame or declares its absence.

<!-- related-start -->
**Related sections:** [08. Execution Results and Evidence](#ch-08) · [11. Technical Integration and Trust](#ch-11) · [Appendix D. Conceptual Data Model](#app-d) · [Appendix A. UI/UX Concept Gallery](#app-a)
<!-- related-end -->

---

<a id="ch-10"></a>
# 10. Context, Memory, and Agent Orchestration

<a id="s-10-1"></a>
## 10.1 Persistent knowledge and trust

Persistent project knowledge is the set of linked, versioned records that survive a conversation. It includes tasks, approved decisions, rule source references, accepted outcomes, unresolved findings and file associations. It is not an ever-growing transcript injected into every prompt. Summaries are derived aids; their citations and freshness must remain inspectable.

Existing Codex memories provide a recall mechanism with separate controls. They do not replace required checked-in guidance. [E-03](https://learn.chatgpt.com/docs/customization/memories). Studio proposes to consult such recall only through supported access and to distinguish remembered information from authoritative project records. A remembered suggestion cannot become an Approved decision by retrieval alone.

The active execution context has four scopes: project binding, conversation intent, task version, and attempt snapshot. Project records can be shared by several conversations, but authorization still applies at retrieval. Cross-project search is outside the MVP. Selecting a new conversation changes the visible context, not the identity of an already-running attempt.

<a id="s-10-2"></a>
## 10.2 Selective context assembly

The proposed resolver takes project and task identity, current execution target, explicit user instruction, known touched paths, selected skills, relevant file references, and unresolved findings. It produces a manifest plus selected content/references. It is an application component, not a claimed description of OpenAI's internal prompt assembly.

**Table 10-1 — Proposed resolver sequence**

| Step | Action | Failure or limit |
|---|---|---|
| 1. Establish boundary | Resolve authorized project/root, task version, runtime capabilities and current instruction sources | Missing binding or denied access blocks dispatch |
| 2. Load required guidance | Preserve runtime-discovered mandatory instructions and managed constraints | Unknown effective guidance is marked; consequential ambiguity blocks work |
| 3. Select approved context | Find current in-scope decisions and explicit task links | Superseded/held/conflicting records cannot be silently selected as governing |
| 4. Add necessary material | Include relevant files, selected skill references, accepted prior result and open findings | Missing required source blocks; optional missing source is disclosed |
| 5. Budget and summarize | Reserve space for required material; summarize optional history with provenance | If required context does not fit, narrow scope or stop; never silently truncate it |
| 6. Freeze manifest | Record IDs, versions, hashes, source scopes, inclusion reasons, exclusions and resolver version | Store before dispatch; failed persistence blocks launch |
| 7. Revalidate | Check critical versions and permissions immediately before starting | Drift rebuilds context or requests a decision |

The manifest records supplied material, not proof that a model obeyed it. It must distinguish fully included content, excerpt, summary, reference-only and unavailable material. Token estimates, when available, are estimates labeled by method. The interface must not claim token savings from hiding a panel.

<a id="s-10-3"></a>
## 10.3 Selection rules and conflict boundaries

Explicit task links are strong relevance signals, but not proof of current applicability. A linked decision may be superseded, out of scope or on hold. Scope and status checks precede semantic similarity. Approved guidance is preferred over an unapproved suggestion for governing behavior; this is project-record selection, not a replacement for the runtime's higher-level instruction hierarchy.

The user can inspect selected sources and remove optional material. Required instructions cannot be deselected merely to fit a context budget. Untrusted attachments and external pages stay in a data category; they cannot grant access, change policy, approve decisions or instruct the resolver to ignore authoritative sources.

Staleness is checked through source revisions and hashes rather than arbitrary age alone. An old unchanged contract may remain valid; a recently modified contract may invalidate a result. When paths expand during execution, applicable guidance may also change. Studio should resolve the additional scope before dispatching a new action or steering at a supported boundary. If the runtime supplies no such visibility, disclose the limitation and constrain the prototype workflow.

<a id="s-10-4"></a>
## 10.4 Cache, memory and invalidation

Cache keys include project identity, permissions, task version, source versions and resolver version. A changed decision, source file, permission scope or task criterion invalidates dependent selections. Cached summaries retain links to source records and are never authoritative replacements. A cache miss may increase latency; it must not trigger broad unauthorized scanning.

Deletion and revocation invalidate indexes and cached material. Local memory contribution remains controlled by the runtime/account mechanism; storing a Studio task does not implicitly enable global memory sharing. The MVP needs only explicit links and bounded retrieval. Vector indexing or learned relevance ranking is an optional later optimization that must outperform this simpler baseline.

<a id="s-10-5"></a>
## 10.5 Execution coordination and handoff

Studio submits work to Codex and attributes returned activity. Existing subagent workflows are documented, but Studio's coordination records are proposed. [E-10](https://learn.chatgpt.com/docs/agent-configuration/subagents). MVP serializes mutating attempts for a given execution target. Read-only review can run separately only when its source snapshot and permissions are clear.

Later parallel work requires declared scope, target repository/worktree, task/attempt identifiers, context manifests and contribution lineage. Worktrees isolate file changes but cannot prove that independently produced changes are semantically compatible. A combined change requires its own integration attempt, snapshot, checks and review.

A handoff contains intended outcome, current task version, applicable decision versions, rule source references, code snapshot, accepted prior evidence, unresolved findings, permitted next action and missing information. It excludes credentials and unnecessary transcripts. The receiving agent acknowledges the available target and context; an unavailable artifact is surfaced before relying on it.

Coordination cannot create new authority. A parent agent's delegation does not authorize a provider connection or production write. A worker may propose a result or decision, but only the responsible human can approve the decision or accept the result under the applicable policy.

<a id="s-10-6"></a>
## 10.6 Interruptions, drift and acceptance

A connection failure freezes the local observed state as uncertain until reconciliation. Do not treat absence of streamed events as proof of idleness. A rule change mid-run appends an impact event; it never rewrites the original manifest. A supported continuation can append a steering amendment and retain prior content identity. A new attempt begins if a clean, separately attributable retry is required.

**Table 10-2 — Context requirements**

| ID | Proposed requirement and acceptance test |
|---|---|
| R-10-01 | Every dispatched attempt MUST have a persisted manifest identifying task, source versions and inclusion modes. |
| R-10-02 | Context budgeting MUST preserve required guidance; an oversized required set blocks or narrows scope visibly. |
| R-10-03 | Superseded, held or inaccessible material MUST NOT silently govern new work; test stale links and revoked access. |
| R-10-04 | Changes during execution MUST produce drift or steering records without modifying the original manifest. |
| R-10-05 | Concurrent contributions MUST retain separate lineage; integration success requires evidence for the combined snapshot. |
| R-10-06 | Retrieved content MUST NOT elevate its authority; an injected instruction in a file cannot approve or grant access. |

Chapter 11 specifies durable dispatch and recovery. Appendix D supplies manifest and handoff relationships. Chapter 13 measures correctness and overhead, including context omissions.

<a id="s-10-7"></a>
## 10.7 Independent environment profiles

Each Project may define several versioned Environment Profiles. A profile describes an execution target; it does not contain credentials or instantiate an environment merely by being viewed. Record host/platform, repository roots, working directory, toolchain constraints, supported setup/check commands, configuration references, secret references, network policy reference and required test targets. Store secrets in the authorized provider/credential service.

**Table 10-3 — MetaStore profile illustration**

| Project | Profile requirements to discover | Evidence boundary |
|---|---|---|
| Backend | PHP/dependency runtime, database fixture, queue/service dependencies, API contract revision | Backend checks apply to their recorded service/data fixture |
| Flutter | Flutter/Dart toolchain, platform target, emulator/device availability, API endpoint configuration | Analysis/unit checks, Android tests and iOS tests remain separate |
| Next.js | Node/package manager versions, build/runtime configuration, Backend endpoint and browser fixture | Build success does not establish browser or cross-client behavior |

These are profile categories, not facts discovered about the user's installed versions. Windows-local, container, remote and cloud profiles may coexist. A Linux container does not establish an iOS-capable host; platform/device evidence requires the appropriate target. Referencing a dev container is optional and cannot erase native-platform constraints.

Profile lifecycle is Draft → Ready after bounded validation; changed toolchains/configuration produce Stale; inaccessible targets produce Unavailable. Validation itself runs only when authorized. Dispatch pins the exact profile version and records observed environment identity. Failure keeps the selected target visible; no silent fallback to another host or production endpoint. A new profile version cannot rewrite old evidence.

Codex uses the primary folder for default Git and instruction discovery; secondary folders do not automatically supply their own project guidance. [E-02](https://learn.chatgpt.com/docs/projects). The proposed adapter must explicitly establish member-specific guidance at supported boundaries or split work into separate attempts. Adding every folder to one prompt is insufficient.

**R-10-07 — Environment identity.** Every group-coordinated attempt MUST pin one Project, Environment Profile version and observed target. Acceptance: an unavailable Flutter target blocks its dependent check and never redirects it to the Backend environment.

<a id="s-10-8"></a>
## 10.8 Cross-project Change Sets and recovery

A Change Set links an outcome, member tasks, dependency edges, contract versions, contributions and an Integration Manifest. It contains no single shared mutable checkout. The coordinator proposes an ordered plan; required producers must supply reviewed contract artifacts before consumers rely on them. Dependency cycles require an explicitly reviewed batch or a revised plan; the scheduler cannot resolve them by guessing.

The Integration Manifest pins each repository revision/dirty-state capture, API/schema contract version, environment profile and relevant CheckRecord. Tests against separately moving branches do not prove one compatible product state. An integration attempt belongs to an explicitly selected coordinator Project and integration profile, with read/access grants for required member evidence; its manifest carries all referenced snapshots.

Change Set phases are Planned / Executing / Awaiting Integration / Awaiting Review / Accepted / Held. This coordination lifecycle is separate from Task and Attempt states. Accepted requires a versioned IntegrationAssessment of the combined revision set and an immutable IntegrationReview by an authorized human; changing the assessment requires a new review. Permitted exceptions remain explicit and never imply verified completion. Any member failure or changed contract marks affected downstream edges unsatisfied and makes the integration assessment stale. Other unaffected work may continue within its grants.

There is no distributed atomic Git commit across repositories. If Backend succeeds while Flutter fails, preserve both outcomes and hold group acceptance. Recovery may implement a compatible intermediate contract, revert an owned change with authorization, or create a corrective attempt. Never reset unrelated changes or replay unknown side effects. Retrying a consumer uses a new attempt and a new manifest when inputs changed.

**R-10-08 — Combined compatibility.** Group acceptance MUST bind an Integration Manifest across the required member revisions. Acceptance: Backend passing and Flutter Not Run cannot produce a verified integrated result; a subsequent contract change invalidates only the dependent assessment and preserves history.

<!-- related-start -->
**Related sections:** [07. Engineering Decisions and Project Rules](#ch-07) · [11. Technical Integration and Trust](#ch-11) · [13. Validation and Expected Value](#ch-13) · [Appendix D. Conceptual Data Model](#app-d)
<!-- related-end -->

---

<a id="ch-11"></a>
# 11. Technical Integration and Trust

<a id="s-11-1"></a>
## 11.1 Architecture and ownership

This chapter proposes a conceptual architecture for Studio. It does not select a framework, database engine, OpenAI internal service, or private schema. The engineering question is whether a small project-record layer can reliably connect supported execution with reviewable evidence.

**Table 11-1 — Component responsibilities**

| Component | Owns | Does not own |
|---|---|---|
| Desktop shell | Navigation, forms, accessible views, user intent | Runtime policy enforcement |
| Project service | Tasks, decisions, relationships, reviews, versions | Git truth or external tracker authority |
| Context resolver | Scoped selection and immutable manifests | Hidden runtime prompts or model compliance |
| Execution adapter | Capability negotiation, dispatch mapping, event normalization | New agent loop or policy bypass |
| Evidence service | Captured snapshots, check records, artifact references | Unsupported claims of test coverage |
| Local durable store | Atomic record updates, audit events, schema versions | Provider credentials in exported data |
| Source adapters | Authorized reads and version metadata | Automatic access to every connected account |
| Codex runtime | Supported execution and configured controls | Studio's task acceptance semantics |

**Figure 11-1 — Proposed integration boundaries (text diagram)**

```text
Developer -> Desktop shell -> Project service <-> Local durable store
                                  |
                           Context resolver
                                  |
                           Execution adapter <-> Codex runtime -> Tools
                                  |
                           Evidence service <-> Git / artifacts
```

Arrows indicate interaction, not a shared transaction. Source adapters feed authorized references into the resolver and evidence service. The runtime remains the execution boundary; Studio's service enforces its own record operations and project isolation.

<a id="s-11-2"></a>
## 11.2 Adapter contract and runtime mapping

The candidate integration is a local supported App Server client. Its public documentation supplies thread/turn/item concepts and version-specific schema generation. The documentation also marks WebSocket transport experimental and unsupported for production; transport suitability must be evaluated rather than assumed. [E-06](https://learn.chatgpt.com/docs/app-server). SDK or noninteractive execution remains an alternative for bounded jobs. [E-12](https://developers.openai.com/blog/codex-as-a-platform).

A conceptual adapter offers: identify runtime/version/capabilities; establish authorized conversation reference; submit a turn; observe events; respond to an exact approval request; interrupt; query current state where supported; and read available evidence references. These are Studio operations mapped to verified public APIs during a future spike, not invented OpenAI endpoint names.

One Studio conversation may reference a runtime thread; one task may span several conversations and attempts; one attempt may contain multiple turns. Every runtime reference includes host/runtime identity to avoid collisions across machines. The adapter preserves raw event references and records normalization version. Unsupported fields are absent with a reason, not guessed.

<a id="s-11-3"></a>
## 11.3 Durable launch and event processing

Before dispatch, commit an execution intent containing an action key, project/task/version, target snapshot, context manifest, actor and authorized scope. Set the attempt Starting, then call the runtime. On acknowledgement, store runtime IDs and transition to the observed state. There is no assumed distributed atomic commit between the local store and runtime.

If the process crashes after dispatch but before acknowledgement, the intent remains uncertain. On restart, query supported runtime state or inspect a known correlation reference. If the adapter cannot determine whether execution started, mark Unknown and require explicit reconciliation. Do not automatically resubmit. Studio's action key prevents duplicate local submissions; it cannot promise exactly-once remote side effects without a runtime guarantee.

Persist events before updating projections. Deduplicate by reliable runtime event identity where available. If no such identity exists, use an adapter-specific conservative scheme and retain uncertain duplicates for inspection; hashing identical text alone can incorrectly merge legitimate repeated events. Out-of-order events must not move a terminal attempt back to Running without an explicit continuation. Event gaps mark evidence incomplete.

A result is finalized from observed execution and captured evidence, then submitted for review. Finalization is idempotent per attempt and result version. Later evidence creates a revision. The audit record captures actor, operation, subject version, time, source and correlation ID. A local audit trail is useful but is not tamper-proof certification against a user controlling the machine.

<a id="s-11-4"></a>
## 11.4 Storage, consistency and migration

The local-first MVP requires transactional metadata and immutable evidence blobs or equivalent durable files. Large logs stay outside hot record queries, referenced by identity and retention policy. Source links are preferred to wholesale repository duplication; exact evidence capture is deliberate and scoped.

Updates use optimistic concurrency: compare expected revision, validate relationships and permissions, then commit record changes and audit event together. A conflict returns the current revision and preserves the user's draft. Approved decision versions, context manifests, recorded evidence and accepted review subjects are immutable. Current-view projections are rebuildable.

Storage schema version is explicit. Before an application upgrade changes records, take a recoverable local backup, validate free space, and migrate transactionally or in resumable stages with a journal. An interrupted migration must resume or restore a known compatible backup. An older application opening a newer schema becomes read-only or refuses with recovery guidance; it must not downgrade silently.

Export includes readable records, stable IDs, relationship manifests and authorized evidence with hashes. It excludes credentials and unauthorized external bytes. Import, if implemented later, validates schema, identities, permissions and collisions; this RFC's MVP guarantees export and backup recovery, not arbitrary third-party import.

<a id="s-11-5"></a>
## 11.5 Permissions, approval and data protection

**Table 11-2 — Separate authority decisions**

| Operation | Authority required | Evidence recorded |
|---|---|---|
| Approve engineering choice | Responsible human for the project | Decision version, scope, actor and time |
| Run an operation | Current runtime and managed policy plus user-authorized task scope | Exact approval/request reference where applicable |
| Accept a result | Responsible reviewer | Result/task versions, criteria and exceptions |
| Access external material | Provider grant and project access | Provider identity, scope and revocation state |
| Change repository rule | Authorized file edit and review | Source diff/revision; never only a sidebar change |

Sandbox and approval mechanisms are distinct documented controls. [E-13](https://learn.chatgpt.com/docs/agent-approvals-security). Studio must neither suppress an approval request nor manufacture consent from a decision badge. An approval response is bound to its runtime request, target and current state. A stale request cannot be replayed after cancellation, expiry or material change; lack of an interactive response leaves the action pending or denied according to runtime behavior.

Threats include cross-project ID guessing, symlink/path escape, malicious source instructions, unsafe previews, credential leakage in logs, stale approval replay, and deceptive evidence. Enforce project authorization at each service operation, canonicalize file targets within permitted roots, sandbox previews, separate data from instructions, and redact secrets before indexing/export. Secret references belong in appropriate credential storage; the record store holds only safe identifiers.

Local storage protection, encryption at rest and retention duration depend on platform and organizational requirements. They are pre-pilot decisions, not assumed product properties. User deletion may require removing evidence; preserve a lawful tombstone and availability status, not prohibited bytes. Export and backup must disclose what is omitted.

<a id="s-11-6"></a>
## 11.6 Failure and recovery contract

**Table 11-3 — Failure handling**

| Failure | Required user-visible state | Recovery action / forbidden shortcut |
|---|---|---|
| Runtime disconnect while running | Unknown observation with last confirmed event | Reconcile; never assume success or relaunch |
| Disk full before intent commit | Launch blocked; draft retained | Free space or choose approved storage; do not dispatch first |
| Disk failure during execution | Evidence persistence degraded; active operation visible | Request safe interruption where supported, reconcile and recover; never claim durable evidence |
| Credential expiry or revoked source | Access denied / unavailable | Reauthorize explicitly or proceed only without optional material |
| Dirty working tree or moved root | Target mismatch and captured preexisting changes | Confirm target or isolate; no reset/clean |
| Partial event stream | Incomplete result evidence | Query supported state, retain gaps, request review |
| Artifact deleted by policy | Version unavailable with tombstone | Historical acceptance remains, current verification limited |
| Concurrent record edit | Version conflict | Review and merge intentionally; no silent last-write-wins for approvals |
| App/schema incompatibility | Read-only or blocked adapter | Export/restore or compatible update; no undocumented state scraping |

MVP storage is local and single-writer by project service, even if several windows are open. Cross-device sync is deferred. A later sync design needs identity mapping, conflict resolution, encrypted transport, deletion propagation and explicit authority for approved records; copying the local database is not an acceptable synchronization design.

<a id="s-11-7"></a>
## 11.7 Integration acceptance gates

**Table 11-4 — Technical requirements**

| ID | Proposed requirement and acceptance test |
|---|---|
| R-11-01 | Every persistent entity and external reference MUST have a declared owner and project boundary. |
| R-11-02 | An uncertain launch MUST NOT auto-retry; inject crashes before/after acknowledgement and prove no second dispatch occurs without reconciliation. |
| R-11-03 | Duplicate/out-of-order events MUST preserve consistent state and auditable gaps; verify against a pinned adapter contract. |
| R-11-04 | Approval, operation permission and result acceptance MUST remain separate; stale approval replay is rejected. |
| R-11-05 | Storage upgrades and evidence retention MUST have tested failure recovery and explicit availability semantics. |
| R-11-06 | Export MUST preserve authorized relationships and hashes while excluding secrets and disallowed content. |
| R-11-07 | Cross-project access and path escape MUST fail at the service boundary, not merely be hidden in the UI. |
| R-11-08 | Unsupported runtime capabilities MUST disable or degrade the dependent workflow explicitly; no private database dependence. |

These gates are proposed tests for a future prototype. No adapter, application code, migration, or product test has been executed as part of writing this RFC.

<a id="s-11-8"></a>
## 11.8 Hybrid team roles and effective permissions

The team expansion adds authenticated Principal records, scoped RoleBindings, WorkAssignments and time-bounded DelegationGrants. A Principal is a human or a service identity; an AgentInstance is an execution actor operating through a declared principal and accountable human. Model names and skill files are never principals. Shared editing requires an authoritative service and identity integration; the local single-owner store is not a secure shared authorization server.

**Table 11-5 — Proposed role/action matrix for the team expansion**

| Role | Read and propose | Execute/change | Engineering acceptance | Access administration / release |
|---|---|---|---|---|
| Group administrator — human | Authorized group metadata | Group configuration | No implicit decision/result authority | Manage scoped bindings; no implicit release right |
| Technical lead — human | Authorized contracts and plans | Only separately granted repository actions | Approve in-scope decisions; integration acceptance if granted | No implicit membership or production control |
| Project maintainer — human | Own authorized project and linked contracts | Scoped development work | Submit evidence; final acceptance only if separately granted | No inherited cross-project or production right |
| Reviewer — human | Assigned evidence and required source snapshots | Read-only review by default | Accept/request changes within granted review scope | No implicit execution or release right |
| Release operator — human | Authorized accepted release evidence | Separately approved deployment target | Release gate responsibility, not retroactive test approval | Deployment through provider controls; outside MVP |
| Coordinator agent | Authorized plans and status | Delegate only a subset of its explicit grant | Propose decisions and integration assessment | Cannot grant roles or approve release |
| Specialist agent | Authorized task and required source scope | Scoped changes/checks with valid grant | Submit Result; cannot approve own or another Result | No role administration or release authority |
| Review agent | Authorized captured evidence | Advisory/read-only review | Findings and recommendation only | No human acceptance or privilege elevation |

Role labels are examples for the proposed product, not existing Codex roles. A responsibility matrix answers who owns work; authorization answers which action may execute on which resource and environment. One person may hold multiple roles, but a configured independent-review policy requires a different authenticated principal from the author. Merely running another model or creating a second agent is not independence.

Effective access requires every applicable layer to permit the action: organizational policy, scoped role, current delegated grant, runtime sandbox, repository/provider access and environment constraints. Within Studio's own policy, explicit deny wins; provider-specific permission aggregation remains the provider's rule. Group membership does not create a blanket repository grant. Existing OpenAI documentation separates these control layers; it does not establish this Studio matrix. [E-18](https://learn.chatgpt.com/docs/enterprise/roles-and-workspace-permissions).

A grant records issuer, subject, accountable human, project/group scope, resource/action allowlist, environment, purpose, validity, policy revision and optional cost/run ceiling. Delegation can only narrow the issuer's effective authority. Validate at dispatch, source retrieval and supported consequential-action boundaries. Revocation blocks new actions and invalidates cached access; interruption of already-running operations depends on runtime/provider capabilities. Record any residual credential lifetime and reconcile outstanding effects rather than promising instantaneous revocation. Public federation controls illustrate bounded service identity, not guaranteed Studio compatibility. [E-20](https://developers.openai.com/api/docs/guides/workload-identity-federation/federation-rules).

**R-11-09 — Identity and least privilege.** Every delegated execution MUST identify its agent instance, authenticated principal, accountable human and grant. Acceptance: a coordinator cannot grant a child access the coordinator lacks.

**R-11-10 — Separate assignment and acceptance.** Assignment MUST NOT grant access or bypass independent review. Acceptance: a review agent's favorable assessment cannot produce human Accepted status; the same author principal fails a configured independent-review gate.

**R-11-11 — Revocation and audit.** Expired/revoked grants MUST prevent new authorized actions, with an explicit limitation for already-issued credentials and ongoing work. Audit actor, principal, delegator, policy/grant revision, target and decision outcome without storing secrets.

<a id="s-11-9"></a>
## 11.9 Voice, visual interaction and specialist execution boundaries

A voice or visual interface feeds the same task/decision/action pipeline. It must display a reviewable interpretation, project/profile target and action scope. Low-confidence transcription, ambiguous references such as “deploy that,” speaker ambiguity or an outdated screen capture require clarification before consequential action. Voice identity alone is not authentication. Supported explicit confirmation by an authenticated user is bound to the exact action; a recorded voice clip or embedded instruction is not reusable consent.

Robotics development can later use simulation, logs and device-specific evidence adapters. Studio remains a development workspace; it is not a certified real-time controller or physical safety system. A simulation pass cannot establish safe physical operation. Hardware tests require a separately approved environment and responsible operator.

Quantum development can later expose a simulator or provider job adapter through ordinary project/profile/result concepts. Record circuit/program version, compilation settings, backend identity, simulator-versus-hardware designation, job ID, shots where applicable, cost authorization and result provenance. A queued or timed-out provider job follows Unknown/reconciliation rules; do not resubmit a possibly charged job blindly. Compiling an algorithm is not evidence of practical quantum advantage.

**R-11-12 — Modality-independent authority.** Voice/image inputs MUST obey the same scoped permissions and exact-action confirmation as text. Acceptance: an instruction visible in an image, uncertain transcript or replayed approval cannot authorize a write.

**R-11-13 — Specialist evidence boundaries.** Domain adapters MUST distinguish simulation, physical-device execution and quantum-provider execution. Acceptance: a simulator report cannot be labeled hardware validation, and provider cost or actuation is never authorized by a research request alone.

<!-- related-start -->
**Related sections:** [10. Context, Memory, and Agent Orchestration](#ch-10) · [12. Product Packaging and Delivery Strategy](#ch-12) · [14. Risks, Trade-offs, and Open Questions](#ch-14) · [Appendix D. Conceptual Data Model](#app-d) · [Appendix E. References and Evidence](#app-e)
<!-- related-end -->

---

<a id="ch-12"></a>
# 12. Product Packaging and Delivery Strategy

<a id="s-12-1"></a>
## 12.1 Delivery alternatives

The primary direction remains a standalone Codex Studio desktop product with shared Codex capability where supported. Evaluation must separate user-facing product independence from how much implementation can be shared. A separate binary may share runtime components; an integrated workspace may still require substantial new state and recovery logic.

**Table 12-1 — Packaging trade-offs**

| Option | Advantages to test | Costs and constraints | Appropriate decision condition |
|---|---|---|---|
| Standalone desktop product — primary | Focused engineering navigation, distinct onboarding and release priorities | Installer/update chain, authentication, compatibility, support, accessibility and data migration ownership | Connected workflow value justifies incremental lifecycle cost |
| Specialized workspace inside unified desktop | Shared distribution, account and common UI infrastructure may reduce duplication | Navigation complexity, release coupling, shared-state boundaries and competing product priorities | Comparable workflow value with materially lower total maintenance |
| Extension or companion around current tools | Small integration surface may test demand quickly | Limited navigation/event hooks, split state, inconsistent recovery and extra user bookkeeping | Adequate for validation without pretending to deliver the full product |
| Continue current workflow | No new product maintenance | Relationships maintained through current tools and documentation | Measured incremental benefit does not justify Studio |

No cost ranking is asserted without investigation. Shared infrastructure can also impose coupling costs, and an extension can become expensive if it relies on unstable interfaces.

<a id="s-12-2"></a>
## 12.2 MVP boundary

**Table 12-2 — MVP / Later / Excluded**

| Area | MVP | Later, conditional on evidence | Excluded from this concept |
|---|---|---|---|
| Project scope | Local single-user project; one primary repo per attempt | Project Groups with independent environments, then hybrid-team authority | Replacing all work-management systems |
| Navigation | Six tabs and contextual panels | Refined layouts based on study findings | Seventh Execution tab |
| Tasks | Canonical form, lifecycle, provenance, optional organization | External tracker mapping after authority design | Assignee, generic Related To, Add Sub-task creation fields |
| Decisions/rules | Proposed/Approved/Superseded; version history; source-backed rules | Rich shared approval workflows | Automatic agent approval |
| Results | Attempt mapping, checks, captured evidence, review and retry | Provider check integrations | Private reasoning exposure |
| Library | Local references, attachments, outputs, Project/Session views | Selected cloud sources after scoped authorization | Universal automatic account ingestion |
| Context | Explicit links and bounded selection with manifest | Advanced ranking and parallel coordination | Unbounded history injection |
| Operations | Recovery, backup, export and diagnostics | Cross-device sync after conflict/security design | Silent background execution from due dates |
| Reuse | One validated runtime adapter | Additional supported hosts/integrations | Rebuilding the Codex agent engine |
| Prompts | Existing conversational interaction | No committed expansion | Prompt Templates |

A complete vertical workflow is the MVP acceptance unit. A shell with six empty tabs is not an MVP. Conversely, advanced connectors are not prerequisites for testing local continuity and review.

<a id="s-12-3"></a>
## 12.3 Staged delivery gates

**Table 12-3 — Conditional roadmap**

| Stage | Deliverable | Exit evidence | Stop or revise condition |
|---|---|---|---|
| G0 — Design and feasibility | Reviewed state model; supported integration inventory; privacy/retention decisions | Q-01 to Q-04 resolved sufficiently for a bounded prototype | Required runtime control unavailable without unsafe dependence |
| G1 — Local vertical prototype | Chat-to-task-to-attempt-to-reviewed-result chain; local Library; recovery | MVP-scoped requirements pass, including crash and stale-evidence cases | Duplicated dispatch or unreliable evidence attribution |
| G2 — Comparative value pilot | Counterbalanced workflow study from Chapter 13 | Correctness guardrails and actionable time/effort results | Faster navigation with worse constraint or review accuracy |
| G3 — Packaging assessment | Standalone versus integrated lifecycle cost and support plan | Account/update/migration/accessibility ownership agreed | Incremental maintenance exceeds justified value |
| G4 — Limited expansion | One evidence-backed addition at a time | Integration-specific security, recovery and value checks | Scope grows without improved user outcomes |

No durations, staffing figures or budgets are estimated here. G0 requires engineering input from the eventual implementer; the document does not assume authority over OpenAI's internal roadmap or teams.

<a id="s-12-4"></a>
## 12.4 Maintenance and adoption

Maintenance accounting must include adapter schema changes, runtime regressions, platform packaging, authentication compatibility, state migrations, evidence storage, connector permissions, localization, accessibility and incident handling. Measure the work needed to track a runtime update and restore a backup; do not count only initial UI development.

Adoption starts by opening a repository and creating useful work without importing an entire backlog. Existing code and instructions remain authoritative. A tracker issue can be linked without an automatic status mirror. Exportability provides an exit route if Studio is not retained. Historical records must remain readable after a pilot is stopped.

**R-12-01 — Complete narrow delivery.** G1 MUST demonstrate one end-to-end workflow including failure and recovery, with every MVP cell in Table 12-2 represented. An attractive mockup or isolated successful run is insufficient.

**R-12-02 — Evidence-gated expansion.** New integration, synchronization or parallel coordination scope MUST identify the validated user need, authority model and maintenance owner before implementation approval.

<a id="s-12-5"></a>
## 12.5 Expansion sequence and requirement applicability

Version 1.1 makes Project Groups and hybrid teams explicit parts of the full concept. The local MVP remains the first complete learning unit. Requirements introduced for group/team/modality/domain behavior apply when that expansion is implemented; they are not hidden prerequisites for G1. Every release review must declare its implemented scope and corresponding requirements.

**Table 12-4 — Expansion gates after the local workflow**

| Expansion | Delivered behavior | Required gate | Intentionally not inferred |
|---|---|---|---|
| Group visibility | Authorized member links, independent profiles, shared contract references | R-04-04, R-05-07, R-09-07, R-10-07; V-13 | Shared filesystem, credentials or automatic launch |
| Coordinated product change | Project-local tasks, dependency graph, Change Sets and combined evidence | R-06-07, R-07-07, R-10-08; V-14/V-15 | Atomic changes or releases across repositories |
| Hybrid-team pilot | Authenticated roles, grants, accountable humans and independent review | R-11-09 through R-11-11; V-16; authoritative shared service and Q-05/Q-11 | Permission from skill names or assignment |
| Multimodal workflow | Opt-in voice/visual context, reviewable interpretation and provenance | R-09-07, R-11-12; V-17; Q-12 | Permission from an overheard voice or screen text |
| Domain adapters | One justified robotics/simulation or quantum workflow | R-11-13; V-18; provider/platform feasibility | A new robot engine, quantum hardware, or certified controller |

Group visibility may be evaluated before shared-team editing. Dependency-aware coordination may precede broad parallel execution. No release date or simultaneous delivery of all expansions is promised. Additional costs include environment drift, contract testing, identity administration, service hosting, permission-filtered search, incident response and connector compatibility.

<a id="s-12-6"></a>
## 12.6 Ten-year technology horizon: indicators and product consequences

The horizon below is a 2026–2036 research outlook, not a Studio delivery schedule. “Strong direction” means several concrete technical foundations exist; it does not quantify adoption or guarantee commercial benefit. New languages may emerge, but no source supports choosing one future universal language now.

**Table 12-5 — Evidence-backed horizon**

| Direction and present evidence | Assessment | Consequence for Studio |
|---|---|---|
| Real-time voice and visual interaction; E-21 | Strong direction; capabilities already documented | Optional modalities on the same authority/evidence pipeline, with text fallback |
| Vision-language-action models and local robotic inference; E-22 | Active technical direction; general reliability still needs testing | Extensible simulation/device evidence; no automatic physical actuation |
| Rust robotics bindings; Mojo hardware-oriented language work; E-25/E-26 | Concrete ecosystem activity; future dominance unproven | Language/toolchain-neutral project profiles rather than a fixed language bet |
| Lingua Franca coordination and Scenic environment modeling; E-23/E-24 | Research-backed specialist abstractions | Support timing, simulation and verification artifacts through optional adapters |
| Q#, OpenQASM/Qiskit and Qrisp/Jasp; E-27/E-28/E-29 | Quantum programming tools already exist | Preserve simulator/hardware provenance and hybrid job records |
| Error-corrected quantum systems on IBM's roadmap; E-30 | Conditional engineering targets, not achieved benefits or guaranteed dates | Defer provider commitments until practical workflow, entitlement and cost evidence exist |
| Project groups, reusable environments and governed service identities; E-14–E-20 | Existing foundations indicate a coordination need | Prioritize measurable multi-project continuity and accountable delegation |

C/C++ and Python remain relevant foundations; a language-neutral workspace can also accommodate Rust, Dart, TypeScript, emerging languages and quantum DSLs without claiming equivalent tooling maturity. Domain plugins must disclose unsupported debugging, testing and event capabilities. Existing infrastructure should be integrated where useful; a new language or model is not itself a reason to enlarge Studio.

**R-12-03 — Evidence-bounded roadmap.** Every horizon item MUST distinguish an existing capability, proposed Studio support and an uncertain forecast. Acceptance: no vendor target date becomes a Studio commitment, and no optional robotics/quantum adapter becomes an MVP dependency.

<!-- related-start -->
**Related sections:** [04. Product Rationale, Vision, and Positioning](#ch-04) · [11. Technical Integration and Trust](#ch-11) · [13. Validation and Expected Value](#ch-13) · [14. Risks, Trade-offs, and Open Questions](#ch-14)
<!-- related-end -->

---

<a id="ch-13"></a>
# 13. Validation and Expected Value

<a id="s-13-1"></a>
## 13.1 Hypotheses and study design

The proposal predicts better continuity and review, not proven productivity gains. The evaluation must compare Studio with a credible current workflow: current Codex, the participant's IDE/Git tools, repository instructions, and an organized tracker or notes. Preserve equivalent source material, task scope, runtime/model configuration where possible, and access permissions.

Use a counterbalanced within-participant study with matched tasks: half encounter Studio first and half the baseline first. Avoid asking the same person to solve the identical task twice; remembered answers would bias resumption and decision retrieval. Include an interrupted multi-session feature and a simple edit to detect administrative overhead. Use the affiliate scenario as one candidate, alongside a different repository/domain to reduce scenario-specific advantage.

Recruit developers who routinely return to ongoing work, with varied experience and existing organization habits. Determine sample size after an exploratory pilot estimates variability and the minimum effect worth acting on. Do not claim statistical power from an arbitrary participant count. Preregister the final primary measures, exclusions and decision thresholds before the confirmatory study.

<a id="s-13-2"></a>
## 13.2 Operational metrics

**Table 13-1 — Hypothesis and measurement matrix**

| ID | Hypothesis / measure | Operational definition | Judgment criterion |
|---|---|---|---|
| H-01 | Faster correct resumption | Time from opening assigned project to stating and beginning the correct next authorized action | Paired time improvement with no correctness degradation; minimum worthwhile difference set before confirmatory study |
| H-02 | Better decision retrieval | Correct current applicable decision selected / all retrieval trials | Accuracy at least baseline; superseded-choice errors separately reported |
| H-03 | Better evidence traceability | Correct task → attempt → snapshot → check chain / all trace trials; completion time | Improve trace completion or time without wrong-revision evidence use |
| H-04 | Better review judgment | Detection of seeded missing/failed checks; false acceptance rate | No false verified-completion acceptance in safety-critical seeded cases |
| H-05 | Lower repetition and rework | Repeated constraint explanations; corrections caused by missed approved constraints | Reduced events without increasing omitted constraints |
| H-06 | Manageable administrative cost | Time creating/correcting records, resolving links and organizing material | Recovery/review benefit exceeds measured maintenance burden for target work |
| H-07 | Efficient context | Supplied tokens/bytes and total execution cost where observable, including resolver overhead | Compare total cost alongside correctness; no savings claim if cost is unavailable or scope differs |

Time metrics include failed attempts and timeouts. Record “unable to complete” as an outcome rather than dropping it. Report medians, distributions, paired differences and uncertainty; do not convert small samples into precise population claims. Tool-switch counts are meaningful only when the switch interrupts the work; fewer switches with worse evidence access is not success.

<a id="s-13-3"></a>
## 13.3 Instrumentation and evidence

Collect minimal consented interaction events: anonymous participant/session ID, condition, task fixture version, record navigation, dispatch/review timestamps, source availability, task outcome and observer-coded errors. Record code snapshots and seeded issues for scoring; avoid collecting private source contents or secrets unnecessarily. Separate task time from external outages and explain both.

An independent rubric defines correct next action, governing decision, required checks and acceptable evidence. Ideally a reviewer unaware of the interface condition scores the participant's final answer and acceptance choice. Preserve disagreement and adjudication rather than silently adjusting a score to fit the hypothesis.

Baseline configuration and Studio overhead must be documented. If model, runtime, repository or task difficulty differs, stratify or limit inference. For cost, distinguish model usage from local indexing, storage, human maintenance and support costs. If a provider does not expose tokens or billing for the tested path, report that metric unavailable.

<a id="s-13-4"></a>
## 13.4 Functional and adversarial validation cases

**Table 13-2 — Proposed verification cases**

| ID | Fixture / action | Expected observation | Requirements covered |
|---|---|---|---|
| V-01 | Save title-only task; switch panels and return | Defaults valid; draft/filter/focus preserved | R-04-02, R-05-03, R-06-01 |
| V-02 | Repeat save after timeout; concurrently reparent tasks | No duplicate logical save; no cycle | R-05-02, R-06-02 |
| V-03 | Agent proposes a decision and finishes a run | Decision stays Proposed; task not automatically Done | R-06-03, R-07-01 |
| V-04 | Approve replacement during an active attempt | Old manifest retained; drift and impacted work visible | R-07-02, R-07-05, R-10-04 |
| V-05 | Required integration check unavailable; build succeeds | Not Run remains visible; verified completion blocked | R-08-01, R-08-03, R-08-05 |
| V-06 | Change working tree after evidence capture | Historical diff still exact; current mismatch identified | R-08-02, R-09-03 |
| V-07 | Crash around dispatch; duplicate/out-of-order events | No blind redispatch; Unknown or reconciled state | R-11-02, R-11-03 |
| V-08 | Revoked external source, malicious attachment and escaped path | Access blocked; no instruction or permission promotion | R-09-04, R-10-06, R-11-07 |
| V-09 | Required context exceeds budget or sources conflict | No silent truncation; affected work blocked | R-07-04, R-10-02 |
| V-10 | Disk full, interrupted upgrade and backup restore | Clear failure; recoverable records and evidence availability | R-11-05, R-11-06 |
| V-11 | English/Arabic, keyboard-only and enlarged text | Same functions, readable identifiers and controlled focus | R-05-05 |
| V-12 | Two isolated contributions combined | Integration checks bind combined snapshot | R-10-05 |

The cases specify future product tests. They have not been executed by preparing this document.

<a id="s-13-5"></a>
## 13.5 Decision rules and stopping

Adopt zero-tolerance design gates for cross-project disclosure, unauthorized action, duplicated uncertain side effects, lost approved history, and false claims that missing checks passed. A single reproduced instance blocks further expansion until corrected and retested. Zero observed incidents in a pilot does not prove zero risk.

For value, move forward only if primary measures show an actionable improvement under preregistered thresholds and administrative burden remains acceptable. If accuracy improves but time worsens, report the trade-off and target the users for whom reliability matters. If the integrated alternative delivers comparable outcomes with lower maintenance, reconsider standalone packaging while preserving the core workflow findings.

**R-13-01 — Measurable evaluation.** Each reported benefit MUST include its metric definition, baseline, sample, uncertainty and limitations. No mockup counts or hypothetical scenario outcomes may be entered as observed data.

**R-13-02 — Correctness guardrails.** Any rollout recommendation MUST satisfy the safety gates and report negative or inconclusive findings, not only favorable speed metrics.

<a id="s-13-6"></a>
## 13.6 Group and hybrid-team validation

Extend the study only after the corresponding expansion gate. Compare against a deliberately organized baseline using current multi-folder/repository tools, separate environment configuration and existing access controls. Do not compare Studio with an artificially disorganized team. Use synthetic MetaStore-like Backend/Flutter/Next.js fixtures; this RFC contains no results from the user's actual repositories.

**Table 13-3 — Additional measurable hypotheses**

| ID | Measure | Collection and success condition |
|---|---|---|
| H-08 | Correct cross-project impact identification | Correctly identified required consumers and stale contracts / seeded cases; improve accuracy or time without disclosing inaccessible data |
| H-09 | Environment-selection errors and recovery time | Wrong-target starts / launch trials, plus time to recover after profile drift; no unauthorized target accepted |
| H-10 | Delegation and review integrity | Unauthorized attempts prevented, permitted work falsely blocked, and handoff time; no authority escalation or false independent review |
| H-11 | Multimodal usefulness | Correct interpreted tasks, clarification rate, action-confirmation errors and total time versus text; benefit must exceed correction overhead |

**Table 13-4 — Expansion acceptance cases**

| ID | Fixture / action | Expected observation | Requirements |
|---|---|---|---|
| V-13 | Add three projects; revoke one; switch selected environment | Independent profiles; no hidden names/counts; no wrong-target dispatch | R-04-04, R-05-07, R-09-07, R-10-07 |
| V-14 | Change an API contract after one client passes | Impacted consumer evidence becomes stale; combined acceptance blocked | R-07-07, R-10-08 |
| V-15 | Backend passes, Flutter fails, Next.js dependency waits | Separate project-local tasks and attempts; corrective plan without reset or blind replay | R-06-07, R-10-08 |
| V-16 | Assign out-of-scope work; delegate wider access; revoke a grant; same-author review | Assignment grants nothing; elevation rejected; new actions blocked; independent-review policy enforced | R-11-09, R-11-10, R-11-11 |
| V-17 | Ambiguous spoken target; approval text in screenshot; revoked media | Reviewable interpretation and scoped confirmation; no source-to-permission promotion | R-09-07, R-11-12 |
| V-18 | Simulation marked hardware; quantum job times out after submission | Mislabel rejected; uncertain job reconciled before charged resubmission | R-11-13, R-12-03 |

These are proposed cases, not executed experiments. Measure environment setup, coordination and policy maintenance alongside task speed. A larger group overview that increases wrong-environment actions fails even if navigation is faster.

<!-- related-start -->
**Related sections:** [03. Real-World Problem Statement](#ch-03) · [12. Product Packaging and Delivery Strategy](#ch-12) · [14. Risks, Trade-offs, and Open Questions](#ch-14) · [Appendix C. End-to-End Developer Scenario](#app-c)
<!-- related-end -->

---

<a id="ch-14"></a>
# 14. Risks, Trade-offs, and Open Questions

<a id="s-14-1"></a>
## 14.1 Risk register

Severity below is a design assessment, not a measured probability. Owners are proposed responsibility roles, not named OpenAI teams or commitments.

**Table 14-1 — Material risks**

| Risk | Consequence / severity | Mitigation and evidence required | Residual uncertainty |
|---|---|---|---|
| RISK-01: Duplicate organization | More bookkeeping and abandonment; high | Narrow workflow, optional structure, H-06 maintenance measurement | User habits and existing tools vary |
| RISK-02: Runtime drift | Broken attribution or controls; high | Versioned adapter, contract tests, explicit unsupported state | Public interface stability and support |
| RISK-03: Stale guidance | Wrong implementation under obsolete decision; high | Versioned context, supersession impact, V-04/V-09 | Semantic conflict detection remains fallible |
| RISK-04: Misleading completion | Unverified work accepted as ready; high | Independent states and criterion-based review, V-05 | Humans can still accept exceptions unwisely |
| RISK-05: Lost/incorrect evidence | Review cannot be reproduced; high | Snapshot hashes, retention, backup restore, V-06/V-10 | Storage cost and policy constraints |
| RISK-06: Permission confusion | Unauthorized action or data disclosure; critical | Separate authority records, exact approvals, V-08 | Runtime/provider enforcement differences |
| RISK-07: Standalone lifecycle cost | Product maintenance exceeds value; high | G3 assessment including support and updates | No cost estimate available yet |
| RISK-08: Synchronization conflicts | Approved state silently overwritten; high | Defer sync; design conflict protocol before expansion | Multi-device identity and deletion semantics |
| RISK-09: Overspecialized UX | Small tasks become slow or inaccessible; medium | Quick chat, title-only tasks, bilingual keyboard tests | Layout needs real user testing |
| RISK-10: Overstated evidence | Unsupported novelty or endorsement claims; high | Dated claim register and bounded baseline | Documentation changes after verification |

<a id="s-14-2"></a>
## 14.2 External decisions required

**Table 14-2 — Open decision register**

| ID | Decision and owner role | Impact / alternatives | Gate and proposed interim position |
|---|---|---|---|
| Q-01 | Supported runtime adapter and transport — integration engineering | Local App Server, SDK or bounded noninteractive execution; differing lifecycle visibility | Before G1; use only validated public contract, no private database scraping |
| Q-02 | Authentication, entitlement, distribution and naming — product/platform/legal owners | Independent app, integrated workspace or constrained companion | Before external pilot/distribution; no entitlement or trademark availability assumed |
| Q-03 | Retention, encryption, backup and deletion policy — security/data owner | Managed artifact retention versus minimal local references; different auditability/cost | Before pilot with real data; use non-sensitive fixtures meanwhile |
| Q-04 | Recovery and event guarantees — runtime integration owner | Reconcile supported state or require manual resolution of Unknown | Before unattended or side-effecting prototype work; no blind retry |
| Q-05 | Completion exceptions and team authority — product/security owner | Single local owner, required peer review, or managed roles | MVP single owner; team expansion blocked until policy defined |
| Q-06 | Standalone maintenance viability — product/engineering owner | Continue primary direction or adopt integrated delivery after comparison | G3; no schedule/cost promise |
| Q-07 | External sources and tracker authority — integration/product owner | Reference-only links, scoped read integration, or later bidirectional sync | After local value pilot; links only in MVP |
| Q-08 | Study thresholds and sample — research owner | Minimum useful improvement and correctness margin based on pilot variability | Before confirmatory study; no invented success threshold or result |
| Q-09 | Target operating systems and accessibility acceptance — desktop owner | Limited first platform versus simultaneous parity | Before implementation plan; bilingual content does not prove platform parity |

These questions do not leave unwritten RFC chapters. They mark decisions that require authority, engineering evidence or user data outside document preparation. Each has a bounded interim behavior so an implementation review can proceed without guessing.

<a id="s-14-3"></a>
## 14.3 Rejected shortcuts

A last-message-wins rule would be easy to implement but would conflate discussion with authority. A universal context dump would avoid selection logic but would increase stale/conflicting material. A latest-branch evidence link would simplify storage but lose the state actually reviewed. Automatic retry after a timeout would improve apparent responsiveness but risk duplicated side effects. None is acceptable in the proposed core workflow.

<a id="s-14-4"></a>
## 14.4 Reassessment triggers

Reopen the concept if existing product capabilities substantially change, if a supported integration cannot preserve approval semantics, if users consistently avoid record upkeep, or if standalone distribution cannot be maintained responsibly. A complete RFC is an input to that decision, not a reason to proceed despite contrary evidence.

**R-14-01 — Explicit unresolved decisions.** Every unresolved high-impact dependency MUST have an owner role, consequence, alternatives and gate. An implementation plan must not treat an interim position as external approval.

<a id="s-14-5"></a>
## 14.5 Expansion risks and external decisions

**Table 14-3 — Additional risks**

| Risk | Consequence | Mitigation and remaining evidence |
|---|---|---|
| RISK-11: Wrong environment or stale contract | Valid local change breaks a consumer or targets production | Profile pinning, dependency versions, combined manifest; V-13–V-15 |
| RISK-12: Assignment confused with authority | Agent or human gains unintended access; self-approval appears independent | Separate principals/grants, deny enforcement, revocation and review policy; V-16 |
| RISK-13: Roadmap exceeds evidence | Trend-driven scope growth, unsafe device action or unjustified provider cost | Optional adapters, explicit modality consent and scope gates; V-17/V-18 |

**Table 14-4 — Expansion decisions**

| ID | Decision and owner | Alternatives / impact | Gate and interim position |
|---|---|---|---|
| Q-10 | Group membership and contract authority — product/architecture owners | One or multiple groups per Project; shared contracts or external authoritative registry | Before group prototype; use explicit flat membership and versioned references, no inherited code access |
| Q-11 | Team identity, shared service and enforcement — security/platform owners | Existing identity provider and policy service versus dedicated managed backend | Before shared editing; local owner model remains; no self-issued agent privileges |
| Q-12 | Modality retention and specialist-provider scope — privacy/domain owners | Ephemeral media versus retained excerpts; simulation versus separately approved hardware/provider jobs | Before each adapter pilot; opt-in capture and no implied actuation/spend |

The proposed matrix answers the design question at review level; the actual organization must approve bindings, independent-review policy and provider enforcement. Q-05 remains open for that adoption decision. No future technology forecast resolves Q-01/Q-02 or licenses unsupported integration.

<!-- related-start -->
**Related sections:** [11. Technical Integration and Trust](#ch-11) · [12. Product Packaging and Delivery Strategy](#ch-12) · [13. Validation and Expected Value](#ch-13) · [Appendix E. References and Evidence](#app-e)
<!-- related-end -->

---

<a id="ch-15"></a>
# 15. Proposal to OpenAI and Next Steps

<a id="s-15-1"></a>
## 15.1 Review request

TechSoft asks OpenAI's relevant product, engineering and developer-experience reviewers to evaluate whether a dedicated project-centric engineering workspace would add sufficient value to justify its implementation and continued maintenance. The request concerns the connected workflow and its trustworthy state, with standalone desktop delivery as the primary direction.

The supporting material is this complete review draft, six inherited designs, a documented public capability baseline, an illustrative developer scenario, a conceptual data model, and a measurable validation plan. It does not include a working Studio prototype, verified market demand, performance gains, or an agreed partnership.

<a id="s-15-2"></a>
## 15.2 Decisions requested from reviewers

**Table 15-1 — Review questions and expected outputs**

| Review area | Question | Useful output |
|---|---|---|
| Product | Does the linked workflow solve a meaningful continuing-work problem beyond current tools? | Priority users, strongest/weakest use cases, overlap corrections |
| Engineering | Can supported interfaces provide required lifecycle, approval and evidence semantics? | Feasibility findings for Q-01/Q-04 and adapter constraints |
| Developer experience | Are the six views and optional structure understandable in daily work? | Interaction objections, terminology corrections and test participants |
| Security and platform | Are the proposed authority and retention boundaries enforceable? | Conditions for a non-sensitive prototype and later real-data pilot |
| Delivery | Does standalone identity justify lifecycle costs relative to integration? | Comparative ownership and cost assessment, without assumed commitment |

Reviewers may reject individual additions while retaining the underlying continuity problem. Feedback should identify the affected requirement or question ID, the evidence behind the objection, and a concrete alternative where available.

<a id="s-15-3"></a>
## 15.3 Proposed next steps after review

First, reconcile factual corrections and product-scope decisions in a versioned RFC revision. Preserve the English/Arabic equivalence and change log. Second, if separately authorized, perform a bounded integration feasibility spike against the chosen runtime/version using non-sensitive fixtures. Third, build the narrow vertical prototype only after authority and recovery gates are agreed. Fourth, run the comparative study and decide whether to continue, integrate differently, or stop.

None of these later activities is authorized by the act of packaging this document. Publication, GitHub upload, outreach, provider connections, and product execution require their own instruction. The package is prepared for private engineering review and later professional Word conversion.

<a id="s-15-4"></a>
## 15.4 Completion and acceptance of this document

The documentation deliverable is complete when all fifteen chapters and five appendices exist in both languages, source claims are bounded, images and links resolve, requirements and examples align, and the review report identifies remaining external decisions. That standard is separate from product approval or release readiness.

**R-15-01 — Reviewable proposal.** A reviewer MUST be able to trace a proposed behavior to its requirement, related model invariant, validation case where applicable, and supporting source or explicit design status. A favorable presentation alone is not a basis for implementation approval.

The immediate next decision is whether the concept merits G0 feasibility review under the boundaries in Chapters 11–14. No answer from OpenAI or other reviewers is presumed.

<!-- related-start -->
**Related sections:** [11. Technical Integration and Trust](#ch-11) · [12. Product Packaging and Delivery Strategy](#ch-12) · [13. Validation and Expected Value](#ch-13) · [14. Risks, Trade-offs, and Open Questions](#ch-14)
<!-- related-end -->

---

<a id="app-a"></a>
# Appendix A. UI/UX Concept Gallery

<a id="s-a-1"></a>
## A.1 Reading the designs

All six supplied PNGs are reproduced unchanged at 1672 × 941 pixels. They are concept images, not product screenshots or test evidence. Their sample identity, model label, dates, counts, paths and outcomes are illustrative. File hashes and source names are recorded in the asset manifest. No dedicated More screen was supplied; Chapter 05 defines its bounded behavior.

Text decisions govern discrepancies. The notes below distinguish visible content, proposed interaction and correction. The images do not approve every pictured menu, field or provider. For future Word conversion, retain full-width readable images with the numbered captions below; do not crop away controls that the commentary discusses.

<a id="s-a-2"></a>
## A.2 Chat

![Figure A-01: Chat project workspace with sources and task promotion](../assets/01-chat-project-workspace.png)

**Figure A-01 — Chat within a project.** Source: `01-chat-project-workspace.png`. Related: Chapters 05 and 10; R-05-02, R-10-01.

**Visible:** Project conversations appear on the left, the affiliate-page planning request and response occupy the center, and Sources is selected on the right. The response includes More Details, Add to Tasks and Create Task. Current context and related files appear beneath sources.

**Interaction:** Selecting actionable response items opens editable task drafts with message provenance. More Details continues the explanation. Sources open their identified files; Current Context describes the active project/conversation, not a new permission grant.

**Differences:** The response's suggested implementation steps do not authorize implementation when the user asked only for analysis and a plan. Structure and extra panel controls are visual explorations, not committed MVP features. The old account name and model label do not establish current branding or model availability.

<a id="s-a-3"></a>
## A.3 Tasks list

![Figure A-02: Tasks grouped by status with Stages and Sections](../assets/02-tasks-stages-sections.png)

**Figure A-02 — Task queue and optional organization.** Source: `02-tasks-stages-sections.png`. Related: Chapter 06; R-06-02, R-06-03.

**Visible:** The list contains Todo, Active, Review, Done and Deferred groups, priorities, optional dates and badges. The right panel provides Stages/Sections and Current context. The toolbar offers New Task and Create from Chat.

**Interaction:** Stage selection narrows sections and list scope. New Task replaces the right working panel. A row opens its task and linked attempts. Selection controls select records; they are not one-click verified-completion approval.

**Differences:** The toolbar lacks Todo although the list includes it; the RFC requires the Todo filter. The sidebar uses time groups unlike the canonical project hierarchy. Avatars and Team members do not add an Assignee field or team-administration MVP. “Affiliate Module” is sample context; fixed stage names and counts are not universal defaults.

<a id="s-a-4"></a>
## A.4 New Task

![Figure A-03: New Task right-panel form](../assets/03-tasks-new-task-form.png)

**Figure A-03 — New Task subview.** Source: `03-tasks-new-task-form.png`. Related: Chapter 06, Table 06-1; R-06-01, R-06-04.

**Visible:** Back to Tasks, Title, Description, Priority, Status dropdown, Stage, Section, Parent task, Due date, Selected skills, attachments, Cancel and Create Task. The center list remains visible.

**Interaction:** Title is required; default Status is Todo and Priority Medium. Stage/Section, parent, date, skills and attachments are optional. Changing Stage clears incompatible Section; parent cycles are rejected. Save creates work without starting execution. Back preserves the draft; Cancel explicitly discards.

**Differences:** Color treatments alone do not reliably establish a selected priority; textual/default semantics govern. The form does not depict validation, unsaved changes, conflict handling, attachment failure or Done completion guard. Chapter 06 supplies those required states without adding excluded fields.

<a id="s-a-5"></a>
## A.5 Decisions and rules

![Figure A-04: Decisions register and Project Rules](../assets/04-decisions-project-rules.png)

**Figure A-04 — Choice history and applicable guidance.** Source: `04-decisions-project-rules.png`. Related: Chapter 07; R-07-01 through R-07-06.

**Visible:** All, Proposed, Approved and Superseded filters, search, New Decision, decision rows and a Rules-selected right panel containing Project Rules.

**Interaction:** Opening a decision reveals its scope, rationale, source and history. Approving a replacement retains the superseded record. Rule selection exposes the authoritative source and applicable scope.

**Differences:** The visible rule list lacks source/version detail; that detail is mandatory in the RFC. An Approved badge cannot establish authority to execute. The sample Superseded permissions decision does not authorize relaxing real access controls. Sources/Structure/Context tabs in the panel do not expand the agreed default Rules behavior.

<a id="s-a-6"></a>
## A.6 Results

![Figure A-05: Results and execution evidence](../assets/05-results-execution-evidence.png)

**Figure A-05 — Attempt outcomes and evidence review.** Source: `05-results-execution-evidence.png`. Related: Chapter 08; R-08-01 through R-08-06.

**Visible:** Outcome and Pending Review filters, result cards with counts and durations, Review Changes/Open Task/Re-run actions, summary and selected-result evidence links.

**Interaction:** Review Changes opens captured evidence; Open Task restores intended work; Re-run creates a new checked execution intent. The side panel follows the selected result.

**Differences:** Pending Review is drawn like an exclusive outcome; the RFC models it independently. The summary omits Partial and its visible buckets must not be used as an additive total. “12/12 tests” and durations are sample artwork, not benchmarks. Partial numerical counts do not establish whether other checks failed, were skipped or were unavailable. “Landing page” in one card does not change the affiliate marketer page scenario into a separately approved marketing-site requirement.

<a id="s-a-7"></a>
## A.7 Library

![Figure A-06: Library project/session files and optional external sources](../assets/06-library-files-external-sources.png)

**Figure A-06 — File discovery with provenance.** Source: `06-library-files-external-sources.png`. Related: Chapter 09; R-09-01 through R-09-06.

**Visible:** Project Files/Session Files, type filters, search, sort, paths, metadata, file selection, Open/Preview and External Sources. Provider names include Google Drive, Dropbox and OneDrive, alongside URL import and Git synchronization.

**Interaction:** A selected file exposes source, version and availability; project/session associations can refer to the same bytes. Input/Output/Resource classification stays inside Library.

**Differences:** Provider buttons are possible future entry points, not verified Studio integrations. Listed paths, sizes and dates are examples. The drawing does not distinguish live versus captured versions, permission denial or revoked access; the RFC requires those states. Quick topic filters are optional examples and do not replace the primary Project/Session division.

<a id="s-a-8"></a>
## A.8 Version 1.1 extensions absent from the drawings

All six PNGs remain unchanged. Project Group selection, independent environment profiles, cross-project Change Sets, role/grant administration and multimodal confirmation are specified in Sections 04.7, 05.7, 10.7–10.8 and 11.8–11.9, not shown in these inherited images. Existing avatars and team labels do not prove the new permission model. New Task retains its canonical fields. No additional main tab, Prompt Templates or generated mockup is introduced.

A later visual-design pass should depict the group/project/profile target together and test permission-filtered empty states, delegated authority expiry and integration blockers. This is a recommendation for a separately requested design task, not a missing image in this package.

<!-- related-start -->
**Related sections:** [05. Project-Centric Workspace Architecture and UX](#ch-05) · [06. Tasks and Development Planning](#ch-06) · [07. Engineering Decisions and Project Rules](#ch-07) · [08. Execution Results and Evidence](#ch-08) · [09. Project Library and Resources](#ch-09)
<!-- related-end -->

---

<a id="app-b"></a>
# Appendix B. Existing versus Proposed Capability Matrix

<a id="s-b-1"></a>
## B.1 Classification and verification

All official sources below were opened on **2026-10-18**. Existing means documented at that date, not independently tested in this task. Proposed identifies this RFC's addition. Requires Validation identifies an unestablished integration or product property. A capability can have an existing foundation and a proposed extension. No row infers absence from missing documentation.

**Table B-1 — Capability, evidence, proposed addition and validation**

| ID / capability | Current baseline and source | Studio addition / chapter | Requires Validation |
|---|---|---|---|
| B-01 Desktop surfaces | Existing: ChatGPT and Codex choices; E-01 | Proposed: dedicated engineering product; 04/12 | Independent distribution and shared-component boundaries |
| B-02 Projects and chats | Existing: project organization and local folder contexts; E-02 | Proposed: shared task/decision/result relationships; 05/D | Import and cross-surface identity mapping |
| B-03 Memory | Existing: local Codex memory mechanism; E-03 | Proposed: approval/version/evidence-aware selection; 10 | Supported access and completeness of provenance |
| B-04 Repository guidance | Existing: AGENTS.md discovery and scoped guidance; E-04 | Proposed: source-backed Rules view and conflict impact; 07 | Effective instruction visibility for selected runtime |
| B-05 Skills | Existing: skill discovery and loading; E-05 | Proposed: optional task selection and version attribution; 06 | Availability and stable identity across hosts |
| B-06 Runtime integration | Existing: App Server client protocol; E-06 | Proposed: task/attempt/result adapter; 11 | Transport support, event gaps and launch reconciliation |
| B-07 Worktrees | Existing: local/worktree workflows; E-07 | Proposed: explicit attempt target and integrated-result lineage; 10/11 | Isolation and handoff guarantees on each target |
| B-08 Review | Existing: code review and diff inspection; E-08 | Proposed: acceptance against task criteria and captured evidence; 08 | Stable snapshots and check provenance across surfaces |
| B-09 Scheduling | Existing: scheduled task workflows; E-09 | Proposed: dates remain planning-only; 06 | Any later scheduling bridge and its permission model |
| B-10 Subagents | Existing: delegated agent workflows; E-10 | Proposed: contribution/handoff attribution; 10 | Detailed event mapping and integrated change verification |
| B-11 ChatGPT Work | Existing: general work producing reviewable deliverables; E-11 | Proposed: specialized software lifecycle; 04 | Shared UX components and actual incremental value |
| B-12 Harness reuse | Existing: public reuse/integration guidance; E-12 | Proposed: Studio owns project state around runtime; 11 | Support, entitlement and maintenance obligations |
| B-13 Execution controls | Existing: sandbox and approval controls; E-13 | Proposed: separate decision/operation/result authority; 11 | Equivalent enforcement under chosen integration |
| B-14 Task lifecycle | Requires Validation: exact Studio lifecycle not established by cited baseline | Proposed: Todo/Active/Review/Done/Deferred; 06 | Current product overlap and migration mapping |
| B-15 Decision register | Requires Validation: exact proposed approval/version model not established | Proposed: Proposed/Approved/Superseded and rule links; 07 | Existing equivalent experiences and review authority |
| B-16 Evidence model | Requires Validation: end-to-end Studio criterion-to-snapshot chain not established | Proposed: separate checks, review and immutable versions; 08/D | Capture completeness and retention cost |
| B-17 Library divisions | Requires Validation: exact Studio Project/Session model not established | Proposed: file associations and usage classifications; 09 | Source identity across runtime and attachments |
| B-18 Cloud connectors | Requires Validation: pictured providers not verified for Studio | Proposed later: scoped sources; 09/12 | Provider-specific APIs, authorization, revocation and versions |
| B-19 Cross-device sync | Requires Validation: Studio record synchronization contract unknown | Proposed later, outside MVP; 11/12 | Conflict, deletion, identity and approval consistency |
| B-20 Productivity/cost | Requires Validation: no Studio measurements | Proposed hypotheses H-01–H-11; 13 | Comparative study and full overhead accounting |

<a id="s-b-2"></a>
## B.2 How to use the matrix

Rows B-14 through B-19 do not claim that the current OpenAI product lacks related features. They identify exact behaviors this proposal needs and for which this bounded review did not establish an equivalent contract. Before implementing an overlapping function, inspect the current supported surface and update the row with dated evidence.

The matrix is not a competitive feature scorecard. It excludes model benchmarks, pricing comparisons and unsupported provider promises. Changes to product documentation after the verification date require a new evidence revision, not silent reinterpretation of historical claims. Appendix E supplies links and source limitations.

<a id="s-b-3"></a>
## B.3 Group, team and future-domain baseline

**Table B-2 — Additional capability classifications**

| ID / capability | Existing foundation | Studio proposal | Requires Validation |
|---|---|---|---|
| B-21 Project umbrella | E-02/E-14/E-15: multi-folder work and related-project grouping | Explicit Project Group with preserved project boundaries; 04/05 | Exact integration, access-filtered views and migration |
| B-22 Independent environments | E-16/E-17: configurable/reusable development environments | Per-Project versioned profiles and target evidence; 10 | Host/platform/device support and reproducibility |
| B-23 Hybrid team governance | E-18/E-19/E-20: roles, shared tasks and bounded service identities | Studio role/action matrix, assignments and grants; 11 | Identity backend, per-action enforcement and review independence |
| B-24 Cross-project acceptance | Exact proposed contract not established by reviewed sources | Change Sets, dependency versions and Integration Manifest; 10/D | Combined tests, partial recovery and authority |
| B-25 Voice and vision | E-21: real-time multimodal interaction | Optional reviewable inputs through existing approval path; 09/11 | Latency, interpretation errors, retention and selected runtime support |
| B-26 Robotics/language evolution | E-22–E-26: model and language/tool ecosystems | Optional simulation/device evidence and neutral profiles; 11/12 | Device safety, actual tool maturity and domain value |
| B-27 Quantum development | E-27–E-29: programming tools; E-30: hardware targets | Optional simulator/provider records; 11/12 | Hardware utility, job guarantees, access and cost; forecast is not delivery |

Existing foundations do not establish all proposed end-to-end semantics. Proposed support does not mean absent support in every current product. This expansion is a dated documentary comparison, not an exhaustive competitor audit or a tested provider integration.

<!-- related-start -->
**Related sections:** [02. Current Product Landscape and Capability Baseline](#ch-02) · [Appendix E. References and Evidence](#app-e)
<!-- related-end -->

---

<a id="app-c"></a>
# Appendix C. End-to-End Developer Scenario

<a id="s-c-1"></a>
## C.1 Scenario assumptions

This is a worked **illustration of proposed Studio behavior**, not a report of actual execution. Names, IDs, revisions and outcomes below are fictional identifiers for tracing relationships. No real affiliate endpoint, database schema, financial balance, measured test count or production operation is asserted.

The developer maintains an existing commerce application and asks for an affiliate marketer page showing commission summaries, referral activity and payout information. The initial request is inspection and planning. The example assumes inspection later finds a reusable API contract and existing UI conventions. If inspection instead finds no suitable contract, the decision and plan must change before implementation.

**Table C-1 — Example record inventory**

| ID | Meaning | Initial relation |
|---|---|---|
| P-AFF | Example project | Owns all records below |
| C-PLAN / M-01 | Planning conversation and request | Source of three tasks |
| T-101 | Inspect existing affiliate contract | Analysis task |
| T-102 | Prepare page components | Design → Dashboard Components |
| T-103 | Connect and verify page | Parent T-102 optional only if decomposition is intended |
| D-07 v1 | Reuse existing contract for the page | Proposed, then explicitly Approved |
| U-01 | Preserve existing authorization and localization guidance | Repository-backed rule reference |
| X-21 / X-22 | First implementation and corrective attempts | Both belong to T-103 |
| S-21 / S-22 | Results of those attempts | Separate evidence and review history |

<a id="s-c-2"></a>
## C.2 Planning and approval

In Chat the developer says: “Inspect the current affiliate implementation and prepare a plan before changing code.” Codex reads authorized sources and identifies assumptions. The response may describe future implementation steps, but those steps remain a plan.

The user selects Add to Tasks and edits T-101–T-103. Each retains M-01. Stage and Section are optional; T-102 is placed in Design → Dashboard Components for illustration. T-101's acceptance criterion is a sourced contract assessment. T-103's illustrative criteria are: use the agreed contract, preserve existing access control, show loading/empty/error states, and obtain relevant implementation and integration evidence. These criteria are scenario assumptions, not discovered facts about the repository.

Suppose inspection confirms a suitable contract. The agent drafts D-07 v1 with rationale: reuse the existing source of commission data and avoid an independent calculation path. The developer reviews scope and approves it. U-01 remains linked to its authoritative repository instruction. Approving D-07 does not authorize a schema change, payout operation or deployment.

<a id="s-c-3"></a>
## C.3 Execution and incomplete verification

The developer then explicitly authorizes implementing T-103 within the inspected scope. Studio checks project/root, task version, source availability and current permissions. It records context manifest CM-21 containing T-103 v1, D-07 v1, U-01's source revision and selected files. X-21 begins with code snapshot K-21-base and preserves preexisting changes.

For the illustration, implementation produces a captured change set K-21-result. A relevant unit check runs and passes; an integration check cannot start because its fixture environment is unavailable. These are hypothetical outcomes, with no fabricated counts.

**Table C-2 — First result without state conflation**

| Dimension | Example value | Interpretation |
|---|---|---|
| Attempt X-21 | Finished | Runtime work ended normally |
| Result S-21 | Partial | Required verification remains incomplete |
| Unit check | Passed on K-21-result | Evidence applies only to recorded scope/snapshot |
| Integration check | Not Run; environment unavailable | No inferred pass |
| Review | Pending Review | Human has not accepted the result |
| Task T-103 | Review | Intended work awaits evaluation |

The reviewer opens Review Changes, inspects K-21-result and the check log, and records Changes Requested because integration evidence is required. T-103 returns to Active. The generated report appears as a Session File Output and can also be associated with Project Files without duplicating bytes.

<a id="s-c-4"></a>
## C.4 Correction and acceptance

After the test environment becomes available, the developer requests a correction and verification attempt. Re-run prepares X-22; it does not replay every command from X-21. The resolver includes the unresolved finding and checks current sources. If code has changed since K-21-result, the new checks bind the new snapshot.

For the example only, X-22 completes the required integration check and produces S-22 with sufficient evidence for the agreed criteria. The reviewer accepts S-22's exact version. T-103 can become Done with a completion record mapping criteria to S-22 and, where still applicable, explicitly referenced evidence from S-21. S-21 remains Partial/Changes Requested in history; later acceptance does not rewrite it.

If the reviewer instead accepts with an authorized verification exception, the exception remains visible. The scenario cannot claim verified completion or release readiness from that exception. A production deployment or payout action would require separate authorization.

<a id="s-c-5"></a>
## C.5 Return in a later session

A later conversation C-RETURN opens the same project. The developer sees the current tasks, D-07, accepted S-22 and any unresolved follow-up. The context resolver selects these records and verifies their source revisions. It does not load all historical discussion by default.

Suppose the contract source has changed. Studio flags drift, retains CM-21 and S-22 as historical evidence, and asks for a scoped investigation before claiming that the accepted implementation remains valid. A new decision may supersede D-07; the prior approval is still explainable. The task is reopened or a new follow-up created according to whether the intended outcome changed.

<a id="s-c-6"></a>
## C.6 Failure branches and review walkthrough

**Table C-3 — Alternate branches**

| Trigger | Required response | Why it matters |
|---|---|---|
| No suitable API found | Keep decision Proposed; revise plan and seek choice | Scenario assumptions cannot force a false source of truth |
| Runtime disconnect after launch | Mark observation Unknown; reconcile X-21 | Avoid duplicate changes or side effects |
| Rule conflicts with proposed implementation | Block affected action and show sources | Decision cannot override higher authority silently |
| Source attachment revoked | Mark unavailable; exclude from new context or stop if required | A cached file is not perpetual authorization |
| User chooses Deferred during execution | Show active attempt and explicit interruption choice | Planning state does not stop a process |
| Historical diff missing | Show Version Unavailable | Today's checkout cannot impersonate reviewed evidence |

A reviewer can walk the example from M-01 to T-103, D-07, CM-21, X-21, S-21, X-22 and S-22, then return through Library to the same evidence. This is the reference narrative for V-03 through V-09. Its purpose is to test semantic consistency before product implementation.

<a id="s-c-7"></a>
## C.7 MetaStore group extension and hybrid handoff

The following extension uses the user's Backend + Flutter + Next.js structure. All record IDs and contract versions remain fictional; no real schema, endpoint, secret or repository state is asserted. G-META contains P-BACK, P-MOBILE and P-WEB, each with its own Environment Profile. The original single-project affiliate narrative remains valid independently.

The human technical lead requests an impact assessment for exposing an affiliate summary consistently to both clients. The coordinator agent can read authorized contract references and propose a Change Set CS-AFF; it has no blanket write access. A Backend specialist receives a grant for P-BACK development paths and fixture checks. Mobile and Web specialists receive separate grants for their own projects. A human reviewer receives evidence access; a review agent can provide findings but cannot accept the result.

Inspection first decides whether an API change is necessary. If the existing contract is sufficient, retain it and create only consumer work; the scenario does not require a gratuitous Backend change. If a change is needed, a proposed group decision identifies affected consumers, compatibility/deprecation options and the authoritative contract version. Approval by the responsible human is followed by consumer acknowledgments, not automatic client acceptance.

For illustration, tasks T-B, T-M and T-W remain in their owning Projects and CS-AFF records their dependencies. Attempts X-B, X-M and X-W pin separate profiles and snapshots. Suppose Backend and Web evidence pass but the required Flutter device is unavailable. The Flutter CheckRecord remains Not Run. CS-AFF stays Awaiting Integration or Held with a stated blocker; no single green Backend result closes the product outcome.

A handoff records the missing target, current contract version, accessible snapshots, permitted next action and grant expiry. When a human or new agent resumes, it revalidates identity, profile and contract rather than reusing expired credentials. If the contract changed, dependent evidence is stale and new checks bind the revised snapshot set.

Only an authorized integration attempt with IM-AFF covering required member revisions, followed by human review, can establish the agreed integrated outcome. Deployment remains a separate action. An optional spoken request such as “resume the mobile check” first resolves P-MOBILE and its profile visibly; it cannot accidentally launch the Backend service or approve production release.

<!-- related-start -->
**Related sections:** [06. Tasks and Development Planning](#ch-06) · [07. Engineering Decisions and Project Rules](#ch-07) · [08. Execution Results and Evidence](#ch-08) · [10. Context, Memory, and Agent Orchestration](#ch-10) · [Appendix D. Conceptual Data Model](#app-d)
<!-- related-end -->

---

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
**Related sections:** [06. Tasks and Development Planning](#ch-06) · [07. Engineering Decisions and Project Rules](#ch-07) · [08. Execution Results and Evidence](#ch-08) · [09. Project Library and Resources](#ch-09) · [10. Context, Memory, and Agent Orchestration](#ch-10) · [11. Technical Integration and Trust](#ch-11)
<!-- related-end -->

---

<a id="app-e"></a>
# Appendix E. References and Evidence

<a id="s-e-1"></a>
## E.1 Evidence policy

Official pages below were opened and read on **2026-10-18**. The date is verification/access date, not necessarily publication date. References describe public behavior at that time; they do not prove availability for every account, platform, version or integration. No installed-runtime test, provider connection test or product prototype was performed.

The register uses short paraphrases. The RFC's state model, consistency rules, workflows and validation design are TechSoft proposals, not claims that OpenAI implements the same architecture. Source absence or failed retrieval cannot establish feature absence.

<a id="s-e-2"></a>
## E.2 Official source register

**Table E-1 — Official references, supported claims and limits**

| ID | Source and final URL | Verified | Supported claim | Inference limit |
|---|---|---|---|---|
| E-01 | [ChatGPT desktop app](https://learn.chatgpt.com/docs/app) | 2026-10-18 | Desktop offers ChatGPT/Codex entry points | No independent Studio endorsement |
| E-02 | [Projects and chats](https://learn.chatgpt.com/docs/projects) | 2026-10-18 | Project organization; local directory context | No proposed record-schema guarantee |
| E-03 | [Memories](https://learn.chatgpt.com/docs/customization/memories) | 2026-10-18 | Local Codex recall and controls | Recall is not decision approval |
| E-04 | [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | 2026-10-18 | Scoped instruction discovery | No complete semantic-conflict detector |
| E-05 | [Build skills](https://learn.chatgpt.com/docs/build-skills) | 2026-10-18 | Skill discovery and instruction loading | No Studio task-selection contract |
| E-06 | [Codex App Server](https://learn.chatgpt.com/docs/app-server) | 2026-10-18 | Public client protocol and lifecycle | No assumed exactly-once dispatch or full missed-event replay |
| E-07 | [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees) | 2026-10-18 | Worktree/local development workflows | Isolation does not prove combined correctness |
| E-08 | [Code review](https://learn.chatgpt.com/docs/code-review) | 2026-10-18 | Review and diff inspection | No Studio acceptance-policy guarantee |
| E-09 | [Scheduled tasks](https://learn.chatgpt.com/docs/automations) | 2026-10-18 | Explicit scheduled workflows | A Studio due date is not a schedule |
| E-10 | [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | 2026-10-18 | Delegated agent workflows | No assumed universal host/event parity |
| E-11 | [Get started with ChatGPT Work](https://learn.chatgpt.com/docs/get-started-with-work) | 2026-10-18 | General reviewable work deliverables | Does not establish Studio's incremental value |
| E-12 | [Codex as a platform](https://developers.openai.com/blog/codex-as-a-platform) | 2026-10-18 | Harness integration/reuse direction | No license, entitlement or support conclusion |
| E-13 | [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security) | 2026-10-18 | Distinct sandbox and approval controls | Studio must validate chosen integration enforcement |

Some earlier developers.openai.com documentation links redirected to learn.chatgpt.com. The final URLs above are used consistently. Markdown variants were not readable through the web retrieval tool because it rejected the content type; HTML pages were opened instead. Initial guessed paths for worktrees, scheduled tasks and the desktop app failed; the correct destinations were resolved through the official documentation navigation. These failures do not support a negative capability claim.

<a id="s-e-3"></a>
## E.3 Local source register

**Table E-2 — Supplied sources and authority**

| ID | Packaged source | What it supports | Limits |
|---|---|---|---|
| L-01 | [Archive README](../assets/reference-sources/README-EN.md) | Archive provenance and prior scope | Not a current capability audit |
| L-02 | [Latest editorial decisions](../assets/reference-sources/latest-editorial-decisions-EN.md) | TechSoft identity, no word cap, principal direction | Historical phase restriction superseded by current commission |
| L-03 | [Phase 02 instructions](../assets/reference-sources/phase-02-rfc-outline-EN.md) | 15+5 allocation and concept boundaries | Outline-only stop superseded |
| L-04 | [Concept and outline](../assets/reference-sources/concept-and-outline-EN.md) | Core entities, tabs and appendices | Concept, not implementation proof |
| L-05 | [Reviewed community proposal](../assets/reference-sources/community-proposal-reviewed.md) | Detailed task/panel/state clarifications | Filename does not prove RFC completion; old byline overridden |
| L-06 | [TechSoft article](../assets/reference-sources/tech-soft-article-EN.md) | Qualitative motivation and tab explanation | No measured study; earlier ambiguous caption corrected in RFC |
| L-07 | [Extended article](../assets/reference-sources/extended-article-EN.md) | Conceptual continuity and orchestration discussion | Proposed architecture, not OpenAI internals |
| L-08 | [Short article](../assets/reference-sources/short-article-EN.md) | Early framing and reference scenario | Historical draft |
| L-09 | [Earlier review](../assets/reference-sources/earlier-review-EN.md) | Editorial reasoning and historical differences | Old verification claims not reused as current evidence |
| L-10 | [Original Arabic concept](../assets/reference-sources/concept-original-AR.md) | Original concept vocabulary and 15+5 basis | Older identity/title and stop instruction superseded |
| L-11 | [Image source manifest](../assets/reference-sources/image-manifest-original.json) | Original image names, dimensions and hashes | Images are illustrations; old internal paths retained in archival copy |

The original RFC authoring commission was the highest-authority instruction for that drafting package: exact title, TechSoft, complete bilingual RFC, preservation, review and ZIP, with no publication or product execution. Its reconciled decisions are recorded in `review/01-source-decisions.md`. The copied references are provenance exhibits, not assembled chapter sources. For this publication repository, brand spelling and local image navigation were normalized; the supplied source ZIP remains the unmodified archival record.

<a id="s-e-4"></a>
## E.4 Unverified claims and required evidence

**Table E-3 — Explicit verification gaps**

| Claim not established | Current status | Evidence needed |
|---|---|---|
| Studio exists as an announced or shipped OpenAI product | Not claimed | Official product announcement, if one ever exists |
| Full migration/synchronization of existing conversations into Studio | Requires Validation | Supported API and identity/permission semantics |
| Complete missed-event replay and exactly-once remote side effects | Requires Validation | Versioned runtime guarantees and fault-injection results |
| Every pictured provider works with standalone Studio | Requires Validation | Provider-specific supported integration and authorization tests |
| Standalone packaging is cheaper/faster/lighter | Unmeasured hypothesis | Comparative lifecycle and resource measurements |
| Studio improves productivity or reduces tokens | Unmeasured hypothesis | Chapter 13 study with credible baseline |
| All hidden internal Codex architecture is known | Not claimed | Outside the public evidence and product scope |
| Product name/distribution entitlement is cleared | Unresolved Q-02 | Relevant owner/legal review before external distribution |

<a id="s-e-5"></a>
## E.5 Reverification procedure

Before implementation or external circulation, re-open the cited official pages, record changes to affected claims, identify the chosen runtime and target platforms, and update Appendix B. Preserve the earlier access date in history. Reviewers should challenge both unsupported novelty and unsupported assumptions of compatibility. Public documentation establishes a starting point for integration investigation; the proposed product still requires engineering and user validation.

<a id="s-e-6"></a>
## E.6 Version 1.1 evidence expansion

The sources below were opened on **2026-10-18**. E-02 was rechecked for current multi-folder behavior. E-14–E-20 support the group/team comparison; E-21–E-30 support the technology horizon. They establish documented foundations, not tested Studio integrations. Primary vendor/project documentation is not independent evidence of future market adoption.

**Table E-4 — Additional official and primary research/project sources**

| ID | Source | Verified | Supported claim | Limit |
|---|---|---|---|---|
| E-14 | [VS Code multi-root workspaces](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces) | 2026-10-18 | Multiple folders and scoped settings | No cross-project approval guarantee |
| E-15 | [GitLab Groups](https://docs.gitlab.com/user/group/) | 2026-10-18 | Related-project groups and access administration | Studio does not copy permission inheritance |
| E-16 | [GitHub dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers) | 2026-10-18 | Configured development toolchains | No universal platform/device parity |
| E-17 | [Codex Cloud](https://learn.chatgpt.com/docs/cloud) | 2026-10-18 | Reusable multi-repository environments | No Studio group schema or entitlement guarantee |
| E-18 | [Roles and workspace permissions](https://learn.chatgpt.com/docs/enterprise/roles-and-workspace-permissions) | 2026-10-18 | Separate workspace/runtime/provider controls | No unified implicit permission grant |
| E-19 | [Teams and Team Tasks](https://learn.chatgpt.com/docs/enterprise/teams) | 2026-10-18 | Shared tasks and service-account context | Not Studio engineering roles or acceptance policy |
| E-20 | [Codex federation rules](https://developers.openai.com/api/docs/guides/workload-identity-federation/federation-rules) | 2026-10-18 | Bounded workload-to-principal mapping | Existing token lifetime can outlast policy edit |
| E-21 | [Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api) | 2026-10-18 | Real-time voice and visual input | No automatic Studio integration or consent |
| E-22 | [Gemini Robotics](https://deepmind.google/models/gemini-robotics/) | 2026-10-18 | Vision-language-action and local model variants | No general physical-safety guarantee |
| E-23 | [Lingua Franca](https://www.lf-lang.org/) | 2026-10-18 | Research-backed coordination and timing | Not a universal replacement language |
| E-24 | [Scenic](https://scenic-lang.org/) | 2026-10-18 | Probabilistic environment modeling and testing | Simulation does not prove deployment safety |
| E-25 | [Mojo roadmap](https://mojolang.org/docs/roadmap/) | 2026-10-18 | Hardware-oriented language development | Roadmap phases are not delivery dates |
| E-26 | [ROS 2 Rust bindings](https://github.com/ros2-rust/ros2_rust) | 2026-10-18 | Rust integration exists | No market-share or dominance conclusion |
| E-27 | [Microsoft Q# overview](https://learn.microsoft.com/en-us/azure/quantum/qsharp-overview) | 2026-10-18 | Quantum programming language | No practical quantum advantage claim |
| E-28 | [OpenQASM 3 and Qiskit](https://quantum.cloud.ibm.com/docs/en/guides/interoperate-qiskit-qasm3) | 2026-10-18 | Quantum program interchange tooling | Some interoperability remains exploratory |
| E-29 | [Qrisp reference](https://qrisp.eu/reference/index.html) | 2026-10-18 | High-level quantum programming and Jasp compilation | Compilation is not hardware execution |
| E-30 | [IBM Quantum roadmap](https://www.ibm.com/roadmaps/quantum/2030/) | 2026-10-18 | Fault-tolerance and scale targets | Vendor objectives may change; not achieved results |

The current user follow-up authorizes extending this RFC with Project Groups, a hybrid human/agent role matrix and the relevant earlier technology outlook. These remain product proposals. No actual MetaStore repository, environment, identity configuration or provider workload was inspected or changed. Availability and integration guarantees require a chosen account/version and an authorized feasibility test.

<!-- related-start -->
**Related sections:** [02. Current Product Landscape and Capability Baseline](#ch-02) · [Appendix B. Existing versus Proposed Capability Matrix](#app-b)
<!-- related-end -->
