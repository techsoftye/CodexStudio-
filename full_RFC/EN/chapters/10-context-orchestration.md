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
**Related sections:** [07. Engineering Decisions and Project Rules](../chapters/07-decisions-rules.md#ch-07) · [11. Technical Integration and Trust](../chapters/11-integration-trust.md#ch-11) · [13. Validation and Expected Value](../chapters/13-validation-value.md#ch-13) · [Appendix D. Conceptual Data Model](../appendices/D-conceptual-data-model.md#app-d)
<!-- related-end -->
