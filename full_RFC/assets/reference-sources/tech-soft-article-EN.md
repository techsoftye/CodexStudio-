> **Historical source exhibit — not the current publication.** Wording reflects an earlier drafting stage; brand spelling and local image links have been normalized for this repository. For the selected publication, read the [current article](../../../article/Article-EN.md).

# Codex Studio — A Project-Centric Development Workspace

*An integrated engineering environment for agentic software development.*

**A product proposal by TechSoft**

*Independent concept for discussion, not an announced OpenAI product. The images are design mockups; their names, dates, model labels, and metrics are illustrative.*

**Why not give developers one integrated environment for the work we already do with Codex?**

Much of the foundation is already there. OpenAI documents project-organized conversations, parallel agents, worktrees, change review, skills, and automations.[1] The question is not whether those capabilities exist. It is how naturally they connect when a developer is responsible for a project that continues beyond a single conversation.

In my ongoing development work at TechSoft, the pieces often feel scattered: a requirement in one chat, an architectural decision in another, instructions in repository documents, and implementation evidence in a particular run. I can find individual pieces, but I still have to reconstruct how they fit together.

When I return to a feature, I want to answer three questions quickly: **What are we trying to achieve? What have we agreed? What has actually been verified?**

That is the motivation behind **Codex Studio**: a dedicated desktop development workspace that builds on Codex, makes the project the center of the experience, and connects planning, execution, decisions, results, and resources. Not a replacement model. Not just a new tab bar. A more complete environment for the engineering work around the agent.

## In this proposal

1. Why a dedicated developer environment?
2. A guided tour: Chat, Tasks, Decisions, Results, Library, and More.
3. One feature, from discussion to reviewed results.
4. The engineering behind the interface.
5. What I would like OpenAI to explore.

## 1. Why a dedicated developer environment?

OpenAI's desktop documentation describes Chat and Work alongside a separate Codex view.[2] My proposal acknowledges that direction while asking whether sustained software development deserves its own more specialized product experience.

A developer working across analysis, design, implementation, and testing needs more than a place to issue instructions. They need to keep requirements, approved choices, unfinished work, and evidence connected as the project evolves.

**My preferred direction is a dedicated Codex Studio desktop product.** It would give engineering-specific workflows room to develop without continually adding specialist controls to the general ChatGPT experience. The argument is specialization and clarity—not an unsupported claim that today's application is slow or oversized.

A distinct product can still share Codex's underlying infrastructure. It should also work alongside existing editors, repositories, and issue trackers. An integrated environment does not have to replace every tool; it should make the transitions between them more useful.

## 2. A guided tour of the workspace

The layout follows one consistent pattern: projects and conversations on the left, the active work area in the center, and relevant context on the right. Account identity stays visible; the working content of the right panel changes with the selected tab.

**Chat · Tasks · Decisions · Results · Library · More**

These are project views, not six separate applications. Switching tabs should preserve the selected project and provide a route back to the same task, decision, or result. Ordinary conversations should remain ordinary conversations; structured records become useful when the work needs them.

### Chat — Turn a useful conversation into continuing work

Chat remains the starting point for describing a feature, investigating existing code, discussing alternatives, and directing Codex. The concept keeps the familiar conversation while making its useful outputs easier to carry forward.

In the example below, I ask for an affiliate marketer page. The response organizes the proposed work into a plan, data review, UI sections, implementation steps, and expected output. Instead of copying that response into a separate tracker, I would have three clear actions:

**More Details** expands the proposal before I commit to it. **Add to Tasks** turns selected actionable items into editable task drafts. **Create Task** opens the task form, with relevant conversation content available to prefill it. The originating message stays linked rather than being duplicated as another transcript.

The right panel shows the sources and files relevant to the discussion, together with the current project context. It helps me see what the conversation is based on without making me leave it.

The important boundary is that a suggested plan is still a suggestion. Creating task drafts should not silently authorize implementation or approve an architectural choice.

> **[IMAGE 01 — INSERT HERE: 01-chat-project-workspace.png]**

*Figure 01 — Chat remains conversational, while useful plans can become linked tasks and the supporting project sources remain accessible.*

### Tasks — Know what needs attention and organize it without ceremony

Tasks provides a persistent view of the project's work rather than a checklist buried in a response. The center groups tasks by **Todo, Active, Review, Done, and Deferred**, with priorities and dates visible where relevant. Filters and grouping let the developer focus on the work that matters now.

**Review and Done are deliberately different.** An agent may finish its attempt while the developer still needs to inspect the changes. Deferred means intentionally postponed, not necessarily failed.

The right panel introduces two organizational dimensions:

**Stages** represent phases such as Analysis, Design, Development, Testing, and Review. **Sections** group work within a stage—for example, Dashboard Components within Design. Neither is a task status, and neither forces a particular module structure on the codebase. A task can remain unclassified until that organization becomes useful.

A selected stage or section should narrow the work being viewed, not open a disconnected list. Each task should retain its originating request, applicable decisions, and execution results, so the developer can move from planning to evidence without searching for the connection again.

> **[IMAGE 02 — INSERT HERE: 02-tasks-stages-sections.png]**

*Figure 02 — Tasks grouped by execution status, with optional project stages and sections in the contextual right panel.*

#### Creating a task without leaving the work

**New Task** opens a form in the right panel while the task list remains visible. **Back to Tasks** restores the panel's previous role. Tasks can be created manually or from a conversation.

The form in the concept contains:

| Field | Purpose |
|---|---|
| **Title and Description** | Identify the work and describe the expected outcome. |
| **Priority and Status** | Express urgency and progress without confusing the two. |
| **Stage and Section** | Optionally place the task within the project's work structure; both start unset. |
| **Parent Task** | Optionally connect a smaller task to a larger piece of work. |
| **Due Date** | Leave it unset, or choose Today, Tomorrow, or a custom date. |
| **Selected Skills** | Optionally identify the skills relevant to this task. |
| **Task Attachments** | Attach supporting specifications, examples, or design references. |

Skills already exist in Codex.[1] The proposed addition is their explicit association with an individual task—not a new skill mechanism. Similarly, selecting a due date would not by itself schedule an unattended run.

The developer should be able to create a simple task quickly and add structure later. No mandatory assignee or elaborate hierarchy is needed to begin.

> **[IMAGE 03 — INSERT HERE: 03-tasks-new-task-form.png]**

*Figure 03 — The New Task subview keeps the work list visible and makes classification, parent relationships, dates, skills, and attachments optional.*

### Decisions — Preserve what was approved, not everything that was said

Discussions contain alternatives. A project needs to know which alternative became the accepted direction.

Decisions would hold technical and functional choices with their rationale, source, scope, and state: **Proposed, Approved, or Superseded**. The developer could use **New Decision** directly or capture a consequential choice from a conversation as a draft for review.

The example includes decisions to reuse an existing affiliate API contract and the platform's commission service. These are not merely notes: they explain which implementation paths should remain consistent across subsequent tasks.

An agent-created entry starts as Proposed. Approval belongs to the developer. When a choice changes, the previous decision should remain traceable and point to its replacement rather than being silently rewritten.

#### Why the right panel contains Project Rules

A **decision** records a choice and why it was made. A **rule** expresses guidance that applies to future work. “Reuse the existing commission service” explains an implementation choice; “Do not change API response structures without approval” governs later changes.

The right panel therefore shows **Project Rules** while the center remains a decision register. Rules should identify their source and scope, including links to existing `AGENTS.md` guidance where applicable—not create an untraceable competing instruction set. Promoting a decision into a rule should also be explicit.

The benefit is practical: the next implementation should start from the current approved direction, not whichever recommendation is easiest to retrieve from an old chat.

> **[IMAGE 04 — INSERT HERE: 04-decisions-project-rules.png]**

*Figure 04 — Decisions retain their approval state and rationale, while project rules remain visible as a distinct form of guidance.*

### Results — Inspect what happened, with the evidence attached

Tasks describes intended work. Results describes what a particular execution attempt produced. One task can have several results: an initial implementation, a failed check, a correction, and a later reviewed outcome.

The concept provides filters for **Completed, Failed, Partial, and Pending Review**. Each result card summarizes the operation and can show changed-file counts, test outcomes, execution time, and links to its task. Search and grouping help locate the relevant attempt.

For implementation, I would keep **execution outcome and review status separate**, even when a combined filter makes navigation convenient. A run can finish successfully and still await human review. “Completed” must not become shorthand for “the feature has been accepted.”

The right panel gives an overview of results and the selected run's details: code changes, test logs, generated reports, and a route back to the original task or project.

**Review Changes** opens the evidence for inspection. **Open Task** restores the purpose and acceptance context. **Re-run** starts a new attempt under the applicable permissions and current repository state; it must not erase the previous attempt.

Test reporting must reflect what actually happened. Passed, failed, partially executed, and not run are meaningfully different. A confident closing message is useful as a summary, but it is not a substitute for the underlying test output.

> **[IMAGE 05 — INSERT HERE: 05-results-execution-evidence.png]**

*Figure 05 — Results connects each execution attempt to its changes, test evidence, review actions, and originating task.*

### Library — Find the working material without reconstructing its history

A project contains more than source code. Specifications, screenshots, spreadsheets, reports, diagrams, and generated files all contribute to development. Library would make these materials discoverable within the same workspace.

**Project Files** surfaces material associated with the project as a whole. **Session Files** focuses on attachments and outputs associated with particular sessions; it is not a raw session-log viewer.

The concept includes **All, Docs, Code, Images, Data, and Archives** filters, search, sorting, and file selection. The list shows names, paths, modification dates, sizes, and types. Selecting a file exposes its location and metadata on the right, with **Open** and **Preview** actions. Quick filters help narrow the material by topics such as API, UI, Analytics, Docs, Design, or Data.

Inputs, outputs, and resources would remain classifications within Library—not additional main tabs. A file referenced by both a task and a result should still have one authoritative location wherever possible. Links should preserve its source or relevant revision rather than quietly producing competing copies.

#### External sources, in the same place

The mockup also explores connections to **Google Drive, Dropbox, and OneDrive**, plus **Import from URL** and **Sync from Git repository**. These are proposed integration entry points, not a statement that every pictured connection is currently available in Codex.

Their useful role is to bring authorized material into view with its source intact. Connecting a service should make its access scope clear; merely displaying a file or URL must not grant the agent unrestricted access.

**Results answers what the run produced. Library helps locate the actual material.** They complement each other without becoming two storage systems for the same files.

> **[IMAGE 06 — INSERT HERE: 06-library-files-external-sources.png]**

*Figure 06 — Project and session files share searchable navigation, with file details, preview actions, and proposed external sources in the right panel.*

### More — Keep specialist controls available without crowding daily work

More gives lower-frequency functions a predictable home: project configuration, detailed execution history, diagnostics, and settings for supported extensions or integrations as the product develops.

It should complement the other tabs, not become a second task manager or a miscellaneous feature warehouse. Results would remain the place to review an outcome; More could expose the deeper operational events needed to investigate a problem. Settings could manage a connection, while Library remains the place to use its files.

Critical failures and approvals should stay visible where work is happening, not disappear behind More. Detailed logs should concern observable commands, events, approvals, and outputs—not imply access to private model reasoning.

*The supplied mockups show More in the main navigation; its dedicated screen is not yet included in this concept set.*

## 3. One feature, from discussion to reviewed results

*The following illustrates how the proposed workspace would connect the screens above.*

Consider the affiliate marketer page used throughout the mockups. In **Chat**, the developer asks Codex to inspect the existing implementation and prepare a plan. Selected steps become **Tasks**: review the APIs, build the page components, and validate commission data.

Before implementation, the developer records two approved **Decisions**: reuse the existing API contract and use the current commission service. Those choices become linked context for the relevant tasks, while broader Project Rules preserve the existing design system and authorization boundaries.

Codex then works through its execution tools. **Results** records each attempt against the task, with its changes and actual test output. A failing check leads to another attempt; it does not disappear behind the latest success message. The developer reviews the evidence before accepting the task as Done.

**Library** provides access to the associated specifications, diagrams, generated reports, and referenced files. On returning later, the developer can start from the remaining task and reach its decisions and latest reviewed result without assembling the story again.

That continuity is what the tabs are meant to deliver. A quick edit should still be a quick edit; a long-running feature should not have to behave like one isolated conversation after another.

## 4. The engineering behind the interface

The UI would only be useful if the relationships underneath it were reliable.

**Connected records, not duplicated histories.** Conversations, tasks, decisions, runs, results, and file references need stable links within the correct project. Several attempts may belong to one task, and several tasks may share a decision. Parallel work should retain each run's branch or worktree context where available, so results are not attributed to the wrong code state.

**Relevant context, not everything ever remembered.** Before work begins, Studio should assemble the task, applicable rules, current approved decisions, relevant files, and the previous result needed to continue. The developer should be able to inspect those sources. Superseded choices and unrelated logs should not silently become new instructions. OpenAI's guidance on skills and `AGENTS.md` similarly emphasizes task-relevant material rather than indiscriminate document loading.[3]

**Reuse execution, add the missing project relationships.** OpenAI's App Server engineering description covers persistent threads, execution events, and approval requests.[4] That provides a basis worth evaluating. Studio's proposed responsibility is to associate that activity with the project's tasks, decisions, evidence, and resources—not assume those relationships already exist or bypass the runtime's controls.

**Keep authority explicit.** Recording a decision is not granting permission to deploy or change a database. The developer's approvals, project boundaries, and authorized data access must remain intact.

A visible project state should help both the human and the agent. It should not require the human to maintain a second documentation system just to keep the first one coherent.

## 5. What I would like OpenAI to explore

I would start by making one complete workflow dependable: **conversation → task → relevant decision → execution → reviewed result → linked files**. That is more valuable than launching a large set of disconnected management features.

My preference remains a dedicated developer product, with shared Codex infrastructure wherever practical. Separate distribution introduces maintenance and integration costs; those should be evaluated, but they do not remove the need for a focused engineering experience.

The value should be tested through real project work: how quickly a developer resumes a feature, finds its current approved constraints, verifies an agent's output, and identifies the next action. Better continuity may reduce repeated explanation and rework; any productivity or context-cost improvement would need measurement.

**Does this integrated workspace address a real gap in your Codex workflow—and which connection would make the greatest difference first?** I would welcome perspectives from developers and the Codex product, engineering, and developer-experience teams.

I am also preparing a more detailed **Product Concept RFC** covering interactions, technical relationships, integration boundaries, and implementation trade-offs. Interested readers are welcome to contact me privately to discuss the proposal or request the fuller material when it is ready.

**The idea is to build on the capabilities already available and give developers a coherent environment in which to use them—from the first discussion to the next release.**

**TechSoft**

---

### Official references

[1] OpenAI — [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/).

[2] OpenAI Help Center — [Moving to the new ChatGPT desktop app](https://help.openai.com/en/articles/20001276-moving-to-the-new-chatgpt-desktop-app).

[3] OpenAI Developers — [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).

[4] OpenAI — [Unlocking the Codex harness: how we built the App Server](https://openai.com/index/unlocking-the-codex-harness/).
