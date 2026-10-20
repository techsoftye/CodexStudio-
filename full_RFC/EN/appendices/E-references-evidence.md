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
| L-01 | [Archive README](../../assets/reference-sources/README-EN.md) | Archive provenance and prior scope | Not a current capability audit |
| L-02 | [Latest editorial decisions](../../assets/reference-sources/latest-editorial-decisions-EN.md) | TechSoft identity, no word cap, principal direction | Historical phase restriction superseded by current commission |
| L-03 | [Phase 02 instructions](../../assets/reference-sources/phase-02-rfc-outline-EN.md) | 15+5 allocation and concept boundaries | Outline-only stop superseded |
| L-04 | [Concept and outline](../../assets/reference-sources/concept-and-outline-EN.md) | Core entities, tabs and appendices | Concept, not implementation proof |
| L-05 | [Reviewed community proposal](../../assets/reference-sources/community-proposal-reviewed.md) | Detailed task/panel/state clarifications | Filename does not prove RFC completion; old byline overridden |
| L-06 | [TechSoft article](../../assets/reference-sources/tech-soft-article-EN.md) | Qualitative motivation and tab explanation | No measured study; earlier ambiguous caption corrected in RFC |
| L-07 | [Extended article](../../assets/reference-sources/extended-article-EN.md) | Conceptual continuity and orchestration discussion | Proposed architecture, not OpenAI internals |
| L-08 | [Short article](../../assets/reference-sources/short-article-EN.md) | Early framing and reference scenario | Historical draft |
| L-09 | [Earlier review](../../assets/reference-sources/earlier-review-EN.md) | Editorial reasoning and historical differences | Old verification claims not reused as current evidence |
| L-10 | [Original Arabic concept](../../assets/reference-sources/concept-original-AR.md) | Original concept vocabulary and 15+5 basis | Older identity/title and stop instruction superseded |
| L-11 | [Image source manifest](../../assets/reference-sources/image-manifest-original.json) | Original image names, dimensions and hashes | Images are illustrations; old internal paths retained in archival copy |

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
**Related sections:** [02. Current Product Landscape and Capability Baseline](../chapters/02-capability-baseline.md#ch-02) · [Appendix B. Existing versus Proposed Capability Matrix](../appendices/B-capability-matrix.md#app-b)
<!-- related-end -->
