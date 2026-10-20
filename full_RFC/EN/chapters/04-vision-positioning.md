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
**Related sections:** [05. Project-Centric Workspace Architecture and UX](../chapters/05-workspace-ux.md#ch-05) · [12. Product Packaging and Delivery Strategy](../chapters/12-delivery-mvp.md#ch-12)
<!-- related-end -->
