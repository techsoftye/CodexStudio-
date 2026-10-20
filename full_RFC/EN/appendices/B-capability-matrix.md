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
**Related sections:** [02. Current Product Landscape and Capability Baseline](../chapters/02-capability-baseline.md#ch-02) · [Appendix E. References and Evidence](../appendices/E-references-evidence.md#app-e)
<!-- related-end -->
