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
**Related sections:** [Appendix B. Existing versus Proposed Capability Matrix](../appendices/B-capability-matrix.md#app-b) · [Appendix E. References and Evidence](../appendices/E-references-evidence.md#app-e)
<!-- related-end -->
