> **Historical source exhibit — not the current publication.** Wording reflects an earlier drafting stage; brand spelling and local image links have been normalized for this repository. For the selected publication, read the [current article](../../../article/Article-EN.md).

# Codex Studio

### A Project-Centric Development Workspace

**Document type:** Product Concept & Outline  
**Status:** Discussion draft — awaiting approval and direction  
**Proposal prepared by:** TechSoft  
**Date:** October 17, 2026  
**Intended audience:** OpenAI Product, Engineering, and Developer Experience teams and the developer community  
**Note:** An independent proposal, not an official OpenAI document.

---

## Part One: Concept Summary

### The Idea

**Codex Studio** proposes a **project-centric desktop engineering workspace** that draws on existing Codex capabilities and reorganizes them into a unified, persistent developer experience. The organizing center moves from separate conversation histories to the **project**, linking conversations, tasks, decisions, rules, results, files, and agents.

The idea is **not a new AI model, a rebuild of existing Codex functions from scratch, or merely more tabs**. It is a specialized product-experience concept that reuses existing infrastructure and capabilities wherever possible and adds structured connections, interfaces, and complementary workflows.

### Why This Proposal?

Agents capable of inspecting repositories, implementing changes, and testing them are becoming increasingly important. But long-running project management requires more than resumable conversations: **tasks, approved decisions, project rules, execution results, and sources** must be easy to discover and trace across sessions. The proposal aims to reduce repeated requirements, scattered knowledge, and switching between tools while keeping the developer as the final decision-maker.

### Vision

For **Codex Studio to become a daily engineering partner**: an environment for planning development, directing agents, tracking execution, reviewing outcomes, and returning confidently to project context. The intended level of organization could make it a core development tool, without claiming in advance that it will replace IDEs or deliver proven quantitative gains.

### Product Scope and Positioning

- **Principal proposal:** A specialized developer desktop experience/application named *Codex Studio*.
- **Architectural alternative to evaluate:** A functionally distinct engineering workspace inside the unified desktop app, should that prove more viable given the current product direction.
- **Integration rather than duplication:** Build on Codex, Codex CLI, repositories, Git, Skills, `AGENTS.md`, and IDE integration, verifying current support details when writing the full document.
- **Display scope:** Engineering-workspace tools appear **within project context**, not general conversations.
- **Intended benefit:** Better organization, continuity, oversight, and productivity, not a claim that all these functions are currently unavailable.

### Provisionally Agreed Main Interface

`Chat | Tasks | Decisions | Results | Library | More`

| Tab | Practical role |
|---|---|
| **Chat** | Communicate with Codex within the project, formulate requests and plans, and turn discussion outputs into organized records. |
| **Tasks** | Manage `Todo / Active / Review / Done / Deferred` tasks, project stages and sections, parent tasks, and optional dates. |
| **Decisions** | Document and approve engineering/functional decisions, preserve rationale and supersession history, and link decisions to work. |
| **Results** | Track each execution's results, including changes, tests, evidence, outputs, review actions, and reruns. |
| **Library** | Project and session files through `Project Files / Session Files`, with search, file-type filters, preview, and links to records. |
| **More** | Less-used specialist functions and logs, selected by product need without overloading main navigation. |

**Side context changes by tab:** Chat shows sources and conversation context. Tasks shows **Stages / Sections** and a current-context summary; New Task opens in the right panel as a subview with a Back action. Decisions shows **Project Rules** with traceability to sources such as `AGENTS.md`. Library may show **optional** external sources according to actual integrations and permissions, not as automatically supported capabilities.

### Binding Design Principles During Proposal Development

1. **Project-first:** The project organizes connected conversations, tasks, decisions, and results.
2. **Reuse before rebuild:** Do not present existing Codex functions as new inventions; explain the actual addition precisely.
3. **Practical over decorative:** Lightweight daily-use interfaces, not oversized dashboards for display alone.
4. **Human oversight:** No engineering decision approval or sensitive rule change without a clear review/approval mechanism.
5. **Traceability:** Connect tasks to requests, decisions, execution evidence, and output files.
6. **Context discipline:** Separate project context from long execution logs and retrieve necessary information selectively. Resource savings are **a hypothesis requiring measurement**.
7. **Compatibility:** Preserve current Codex workflows and integrations where possible; do not make the proposal a mandatory replacement for VS Code, Git, or project-management tools.
8. **Evidence-based claims:** Distinguish *Currently Available*, *Proposed*, and *Requires Validation*, using official sources.

### Proposed Publication Outputs — After Approval

- **Executive Brief:** A short English summary for professional outreach.
- **Full Product Concept RFC:** A detailed document with designs, comparisons, references, risks, and validation metrics.
- **OpenAI Community Topic:** A focused English post with selected images and a link to the complete document, without putting every detail in the post itself.

> **Central message:** *Codex Studio is not another layer of project-management features. It is a proposal for a focused, project-centric engineering experience that connects the work developers already do with Codex—planning, decisions, execution, evidence, and persistent project knowledge—into a coherent workspace.*

---

## Part Two: Proposed Table of Contents

### 01. Executive Summary
1. A brief presentation of the idea and problem.
2. Distinctive value compared with the current experience.
3. Intended audience and expected effect.
4. The request addressed to OpenAI.

### 02. Current Product Landscape
1. Codex within OpenAI's ecosystem and desktop app.
2. Existing capabilities: projects, conversations, agents, tools, and skills.
3. Potential overlap with ChatGPT Work, IDEs, and work-organization tools.
4. A matrix: **Existing / Proposed / Requires Validation**.

### 03. Problem Statement
1. Fragmented knowledge across conversations and sessions.
2. Weak structured links between request, decision, execution, and result.
3. Context recovery in long-running projects.
4. Practical scenarios showing the need and its limits.

### 04. Product Vision & Positioning
1. The Project-Centric Engineering Workspace concept.
2. Target user personas and use cases.
3. Codex Studio as a day-to-day engineering partner.
4. Goals and exclusions from product scope.
5. Relationship with existing products and development environments.

### 05. Workspace Architecture & UX
1. The project as the basic unit of organization.
2. General conversations versus project conversations.
3. **Chat / Tasks / Decisions / Results / Library / More**.
4. The right panel that changes with the active tab.
5. Navigation, interface layout, and subviews.
6. Use of earlier reference images and mockups.

### 06. Tasks & Development Planning
1. Manual or conversation-context creation.
2. States: Todo / Active / Review / Done / Deferred.
3. Project **Stages** and **Sections**.
4. **Parent Task** and child-task relationships.
5. Priority, optional date, skills, and attachments.
6. Execution tracking and navigation to results.

### 07. Engineering Decisions & Project Rules
1. Technical and functional decision records.
2. Proposal, approval, and supersession flow.
3. Extracting a decision draft from a conversation for review.
4. **Decision** versus **Project Rule**.
5. Source, scope, and integration with `AGENTS.md`.
6. Detecting conflicts when executing related tasks.

### 08. Execution Results & Evidence
1. Task-execution results and multiple attempts.
2. Result states: Completed / Partial / Failed / Pending Review.
3. Changed files, quality checks, and tests.
4. Evidence, output files, and execution reports.
5. Review Changes, Open Task, and Re-run according to execution permissions.
6. Traceability between run, task, decision, and outputs.

### 09. Project Library & Resources
1. **Project Files** and **Session Files**.
2. Search, sorting, and file-type filtering.
3. Input/generated files, attachments, and documents.
4. Preview, open, and manage file links without unnecessary duplication.
5. Optional external sources according to supported integrations.
6. Library's relationship with tasks and execution results.

### 10. Context, Memory & Agent Orchestration
1. Shared, persistent project memory.
2. Conversation, task, and execution context boundaries.
3. Selective retrieval and provenance records.
4. Compatibility with multi-agent work and current Codex capabilities.
5. Structured task and result handoffs.
6. Approval and developer oversight of sensitive operations.

### 11. Technical Integration & Trust
1. Reuse existing Codex infrastructure wherever possible.
2. Codex CLI, IDE, Git, and Worktree integration.
3. Skills and `AGENTS.md` rules.
4. An initial view of data relationships and project state.
5. Permissions, data protection, synchronization, and recovery.
6. Constraints and assumptions requiring engineering verification.

### 12. Product Packaging & Delivery Strategy
1. Rationale for a specialized Codex Studio engineering experience.
2. **Standalone Desktop Product** versus **Specialized Workspace in Unified Desktop**.
3. Benefits, limits, and maintenance costs of each option.
4. MVP scope without attempting to clone complete project-management systems.
5. An incremental roadmap conditioned on test findings.

### 13. Validation & Expected Value
1. Improvement hypotheses to test.
2. Request/decision/result traceability.
3. Speed of resuming work and recovering context.
4. Effects of organization on rework and tool switching.
5. Measuring resource and context usage where possible.
6. Criteria for confirming or rejecting hypotheses.

### 14. Risks, Trade-offs & Open Questions
1. Duplicated capabilities or added complexity.
2. A standalone desktop product's cost versus platform unification.
3. Stale and conflicting decisions or rules.
4. Memory, synchronization, and external-source complexities.
5. Security, approval, and human-control boundaries.
6. Unresolved product and engineering questions.

### 15. Proposal to OpenAI
1. Proposal summary and intended competitive distinction.
2. A suggested evaluation/test of a Project-Centric Workspace.
3. Decisions for Product, Engineering, and Developer Experience teams to discuss.
4. An invitation for feedback and hypothesis testing.
5. Proposed next steps.

---

## Part Three: Appendices

| Appendix | Content |
|---|---|
| **A — UI/UX Concept Gallery** | Six reference designs, describing interface functions, interactions, and subview states. |
| **B — Existing vs. Proposed Capability Matrix** | A documented comparison of existing capabilities, proposals, and items requiring verification. |
| **C — End-to-End Developer Scenario** | The affiliate marketer page, from conversation to task, decision, execution, tests, and result. |
| **D — Conceptual Data Model** | Relationships between Project, Conversation, Task, Stage, Section, Decision, Rule, Execution Run, Result, and File. |
| **E — References & Evidence** | Official OpenAI documents, supporting engineering sources, and inference limits for each. |

---

## Part Four: Agreed Points and Limits of This Draft

**Provisionally agreed:** The working name *Codex Studio*, project-centric direction, six tabs, contextual right panel, distinct Tasks/Decisions/Results/Library roles, and reuse of available Codex capabilities.

**Still open:** Final application-independence decision, technical implementation, cost and schedule estimates, permitted external integrations, and final claims/references. Name availability and possible conflicts with other projects should also be checked before official publication.

**Next step:** Await comments and instructions before writing proposal chapters or turning it into an English community post.
