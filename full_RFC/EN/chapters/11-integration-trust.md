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
**Related sections:** [10. Context, Memory, and Agent Orchestration](../chapters/10-context-orchestration.md#ch-10) · [12. Product Packaging and Delivery Strategy](../chapters/12-delivery-mvp.md#ch-12) · [14. Risks, Trade-offs, and Open Questions](../chapters/14-risks-questions.md#ch-14) · [Appendix D. Conceptual Data Model](../appendices/D-conceptual-data-model.md#app-d) · [Appendix E. References and Evidence](../appendices/E-references-evidence.md#app-e)
<!-- related-end -->
