> **Historical source exhibit — not the current publication.** Wording reflects an earlier drafting stage; brand spelling and local image links have been normalized for this repository. For the selected publication, read the [current article](../../../article/Article-EN.md).

# Codex Studio — A Project-Centric Engineering Workspace for Agentic Software Development

*An independent product concept by TechSoft. Codex Studio is a working name for this proposal, not an announced OpenAI product.*

**When you return to a software project, finding the conversation is only the beginning. You still need to know which decisions stand, which changes were verified, and what the next agent should do.**

This proposal grows out of how I work with Codex: discussing implementation plans, refining constraints, directing changes, and returning to related conversations as a project develops. The repository holds the code. The conversations preserve the discussion. Keeping the intended work, approved choices, and evidence connected is a separate responsibility.

Codex Studio would give that responsibility a permanent home: a dedicated engineering workspace built around the project, using the agent capabilities Codex already provides.

**Contents**

- **01. The Idea**
- **02. Why a Dedicated Product?**
- **03. The Practical Problem**
- **04. The Engineering Foundation**
- **05. The Workspace Experience**
- **06. One Connected Workflow**
- **07. Expected Value**
- **08. A Practical Product Direction**
- **09. Feedback and Further Details**

## 01. The Idea

I propose **Codex Studio as a specialized desktop product for developers**, organized around ongoing software projects rather than individual exchanges with an agent.

Its purpose is to connect the work around coding: understanding a request, turning it into actionable tasks, preserving important decisions, supervising execution, reviewing evidence, and continuing later. A developer should be able to move from a result to its originating task, the decision that governed it, and the files supporting it without reconstructing those relationships manually.

The main views would be **Chat, Tasks, Decisions, Results, Library, and More**. These are different views of connected project information—not six isolated applications, six automatically loaded contexts, or six mandatory steps for every change.

The product would reuse Codex's capabilities wherever appropriate. It would not require a new coding model, a replacement execution engine, or abandonment of an existing IDE. Its contribution would be a persistent engineering workflow that makes existing capabilities easier to direct and their outcomes easier to trust.

## 02. Why a Dedicated Product?

The proposal must start by acknowledging the current product. OpenAI's [desktop migration guidance](https://help.openai.com/en/articles/20001276-moving-to-the-new-chatgpt-desktop-app) explains that the desktop application brings together Chat, Work, and Codex, while Codex retains its own view and history. The [Codex app announcement](https://openai.com/index/introducing-the-codex-app/) already describes project-organized agent threads, parallel work, worktrees, change review, skills, and automations.

I am not proposing these capabilities as inventions, nor arguing that Codex lacks a developer-focused experience. I am asking whether a deeper, connected engineering workflow deserves a specialized product that can evolve on its own terms.

A general assistant must serve many kinds of work. A development environment must also make room for recurring engineering concerns: comparing implementation against approved constraints, distinguishing execution from acceptance, coordinating parallel changes, and recovering project context across sessions. These concerns deserve consistent interactions rather than a growing collection of unrelated controls.

**The case for a dedicated Studio is specialization, not an unmeasured performance claim.** A separate application is not automatically smaller or faster. The opportunity is to let developer workflows expand without imposing their full complexity on the general desktop experience.

Product independence need not mean a separate engine; developers should retain their repositories and IDE workflows rather than migrate their entire toolchain.

OpenAI could assess a specialized workspace within the unified application as an alternative. My primary proposal remains a dedicated developer product whose sustained workflow value justifies its maintenance and integration costs.

## 03. The Practical Problem

The friction appears in ordinary development work, not only in ambitious multi-agent demonstrations. In the workflow behind this proposal, I prepare plans, refine what an agent may change, review its output, and continue through related conversations. Four questions repeatedly matter.

**What did we actually approve?** A discussion can contain several alternatives and a later correction. Search can retrieve all of them, but future implementation needs to distinguish an explored idea from the choice the developer accepted. Without that distinction, the same architectural question can be reopened unnecessarily.

**What remains to be done?** An agent may finish one attempt while the feature still needs an integration check or a developer decision. Conversely, a deliberately deferred task is not a failed execution. Treating every closing message as equivalent obscures what requires attention next.

**What supports the reported outcome?** A summary, a changed-file list, and a test log answer different questions. Review is easier when they refer to the same execution attempt and code state. A passing result from an earlier version should not appear to verify a later change.

**What should carry into the next session?** Reusing every earlier message is not the objective. The next task needs the current requirement, relevant constraints, applicable decisions, and unresolved findings—not every discarded approach or intermediate command.

These are workflow requirements drawn from planning and review, not a claim that every Codex user encounters the same failures.

## 04. The Engineering Foundation

### Project state, not a second transcript

The project would own the relationships among its conversations, tasks, decisions, execution attempts, results, and file references. Selecting a conversation could narrow what is displayed, but should not turn shared project information into unrelated copies. The interface must make the active project and any conversation filter clear.

The distinction between records is functional. A **task** describes intended work. A **decision** records an accepted choice and its rationale. A **rule** supplies applicable guidance. An **execution attempt** records work performed through the runtime. A **result** summarizes that attempt with supporting evidence. A **file reference** identifies material used or produced.

One task can have several attempts. An attempt can involve several agent interactions. A new result must not overwrite an earlier attempt, and an updated decision must not erase the version an earlier run relied on. These relationships make it possible to answer both “What is current?” and “Why did this implementation follow that approach?”

This should complement existing records rather than establish competing authorities: Git for code revisions, the runtime for execution events, repository guidance for its instructions, and developer-reviewed records for project choices. Where an external tracker is already authoritative, Studio should link to it instead of silently maintaining a conflicting task status.

### Continuity that builds on existing memory

Codex already has continuity mechanisms. OpenAI's [memory documentation](https://learn.chatgpt.com/docs/customization/memories) describes local Codex memories and their controls, while advising that required guidance remain in `AGENTS.md` or checked-in documentation. Its [project documentation](https://learn.chatgpt.com/docs/projects) also distinguishes saved chats from the current working tree.

Studio would therefore not introduce memory for the first time. The proposed addition is an explicit connection between recalled information and **approval, scope, version, and execution evidence**. A remembered suggestion should not acquire the authority of an approved engineering decision merely because it was retrieved.

Before a relevant task starts, Studio should assemble a compact, inspectable set of working context: the task and acceptance criteria; applicable instructions; approved decisions within scope; necessary file references; and the reviewed outcome or unresolved finding needed to continue. Other information remains available for retrieval when the work requires it.

This selection must preserve the runtime's actual instruction hierarchy and required guidance, not replace them with a custom ranking of convenient snippets. Missing files, superseded decisions, and conflicting constraints should be visible. If a decision changes during execution, the run should retain the version it started with and flag the change for review rather than silently rewriting its history.

The stored record of which sources and versions were supplied would make later diagnosis possible. It would not prove that the model understood or followed every instruction. Separating information in the interface is likewise not proof of context isolation or token savings.

### Reuse execution; add reliable attribution

OpenAI's [App Server engineering article](https://openai.com/index/unlocking-the-codex-harness/) describes a reusable Codex harness with thread persistence, tools, configuration, and authentication. The [App Server reference](https://learn.chatgpt.com/docs/app-server) exposes thread, turn, and item lifecycles, streamed changes, and approval interactions. These are relevant foundations to investigate, not evidence that Studio's proposed task and decision records already exist.

Studio would associate those runtime records with the work the developer intended. A runtime turn finishing should update its execution record, not automatically approve a decision or mark a feature Done. A task may span multiple turns or runs; a one-to-one mapping should not be assumed.

After a restart or disconnection, the workspace should reconcile recorded state with the runtime where supported, avoid duplicate results, and distinguish interrupted work from verified completion. Refreshing a view must never launch the task again. This integration would require engineering work and validation against supported runtime interfaces.

For parallel agents, each contribution should retain its task, attempt, and relevant branch or worktree identity. Isolated work does not prove that the combined changes are compatible; integration review and checks remain necessary. Evidence must distinguish an agent's individual result from the integrated outcome.

### Preserve the developer's authority

OpenAI documents [sandboxing and approval policies as distinct execution controls](https://learn.chatgpt.com/docs/agent-approvals-security). Studio should reuse those controls rather than substitute an Approved badge for permission to act.

Three permissions must stay separate: approving an engineering choice, authorizing an operation, and accepting its result. Agreeing to an API design does not authorize a production migration. A rule displayed in the sidebar cannot grant filesystem or network access. The workspace should make these boundaries easier to understand, not hide them behind automation.

## 05. The Workspace Experience

The interface keeps a familiar arrangement: projects and their conversations on the left, the active workspace in the center, and relevant tools on the right. The main navigation remains:

**Chat · Tasks · Decisions · Results · Library · More**

These views belong to a project. Ordinary conversations should not acquire a task-management interface by default. Switching tabs changes the view of the work, not the underlying project or its permissions.

*The existing mockups below illustrate the concept, not shipped functionality. Dates, counts, model labels, and sample outcomes are illustrative. The clarified behavior below takes precedence over illustrative labels.*

### Chat — Discuss, plan, and turn intent into work

Chat remains the place to understand a problem, inspect relevant code, explore alternatives, and direct Codex. A developer should not have to complete a task form before asking a question or making a small fix.

The proposed addition is a clear transition from conversation to structured work. **More Details** expands an explanation. **Add to Tasks** lets the developer select actionable items from a plan. **Create Task** opens one editable task draft. The draft preserves its source message and relevant attachments without copying the entire transcript.

These actions should not automatically approve the plan or begin execution. The developer can correct what Codex extracted, leave the work in Todo, and instruct the agent when ready.

The right panel defaults to **Sources**, with conversation context available below. Rules may remain accessible as a secondary option, but their content should not replace Sources while Sources is selected.

![Codex Studio concept: Chat with project conversations and contextual sources](../01-chat-project-workspace.png)

*Figure 1 — Planning stays conversational; selected parts of an answer can become traceable tasks instead of disappearing into the transcript.*

### Tasks — A work queue with a clear lifecycle

Tasks organizes intended work independently of any single execution attempt. Its filters are **All, Todo, Active, Review, Done, and Deferred**, with grouping by status by default. Todo means work not yet started; Active means work underway; Review identifies work awaiting evaluation; Done records accepted completion; Deferred marks deliberate postponement. **All is a filter, not a status.**

An agent finishing a run does not automatically make the task Done. It can present the outcome for review. A failed attempt also need not change the task into a new “Failed” status: the attempt's failure belongs in Results, while the task remains available for correction, review, or postponement. Manual status changes should identify the developer who made them; they must not invent an execution or test record.

**Stage, Section, and Parent Task solve different problems.** A Stage identifies a phase such as Analysis or Design. A Section groups work within that phase, such as Dashboard Components. Parent Task links a smaller task to a larger one. None requires a modular codebase or a particular development methodology.

The right panel retains the account identity, then offers **Stages / Sections** navigation and a compact Current Context area. Selecting a stage narrows the applicable sections; selecting either filters the task list. Tasks without a Stage or Section remain visible. The **New Task** button opens a right-panel subview with **Back to Tasks**, leaving the central list in place.

The creation form would have these bounded inputs:

| Field | Proposed behavior |
|---|---|
| **Title** | Required, concise description of the work. |
| **Description** | Optional explanation, constraints, and acceptance criteria. |
| **Priority** | Low, Medium, or High; Medium initially. |
| **Status** | A **dropdown**, initially Todo—not another navigation bar. |
| **Stage / Section** | Optional linked selectors, initially Not set. Section choices follow the selected stage. |
| **Parent Task** | Optional, initially None. Selecting a parent establishes the subtask relationship. |
| **Due Date** | No date, Today, Tomorrow, or Custom; No date initially. |
| **Selected Skills** | Optional selection from available skills, initially Not set. |
| **Task Attachments** | Optional upload or selection of an existing Library file. |

Changing Stage should clear an incompatible Section. A task cannot become its own ancestor. Parent selection may suggest the parent's organization without silently overriding the developer's choices. There is no separate Assignee, generic Related To, or Add Sub-task field in this form; relationships created through the workflow remain available without requiring manual bookkeeping.

OpenAI's [skills documentation](https://learn.chatgpt.com/docs/build-skills) describes loading skill instructions when a skill is used. Studio's selector would expose an explicit preference within that mechanism, not introduce a new skills engine. Leaving it unset should not disable normal skill discovery; unavailable selections should be flagged rather than silently substituted.

![Codex Studio concept: Tasks with status groups and Stages/Sections navigation](../02-tasks-stages-sections.png)

*Figure 2 — The central work queue and optional project organization answer different questions: what needs attention, and where does it belong? The early mockup omits the Todo quick filter specified above.*

*Additional interaction reference: [New Task subview with Back navigation and a Status dropdown](../03-tasks-new-task-form.png).*

### Decisions — Preserve the choice, its reason, and its authority

Decisions records choices that should survive the conversation in which they were made. A compact list offers **All, Proposed, Approved, and Superseded**, search, and a New Decision action. Opening a record reveals the problem, chosen approach, rationale, scope, source conversation, and related work. Alternatives belong in the detail view, not every row.

Codex can propose extracting a decision from Chat, but **an agent-authored proposal remains Proposed until the developer approves it**. A revised choice preserves its history; a superseded record points to its replacement. The latest message is not automatically the governing decision.

When Decisions is active, the right panel keeps the account identity and selects **Rules** instead of Sources. Project Rules then use the available panel height, rather than competing with unrelated source lists and task statistics.

A decision explains a choice; a rule guides future behavior. For example, a decision might establish that the affiliate page will reuse an existing commission API. An associated rule might require approval before changing that contract. They are connected, but they are not interchangeable.

Repository guidance must remain traceable. OpenAI's [AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md) describes how global and project instructions are discovered and layered. Studio should show the originating instruction file and applicable scope, preserve that precedence, and avoid creating an unsynchronized second copy. Editing a repository-backed rule should lead to a reviewable change to its authoritative source, not merely a different sentence in the sidebar.

Useful rules would be specific and bounded: preserve the agreed API shape; use existing localization keys; report which checks were actually run. These are working instructions, not substitutes for permission enforcement. Converting a decision into a reusable rule should be explicit, and a conflict between approved guidance should require resolution rather than an invented compromise.

![Codex Studio concept: decision records with Rules selected in the right panel](../04-decisions-project-rules.png)

*Figure 3 — Decisions retain the rationale and approval history; the Rules panel exposes applicable working guidance and its source.*

### Results — Separate what happened from what was accepted

Results presents evidence from execution attempts, not a duplicate list of completed tasks. The developer should be able to distinguish three things: whether execution ended, whether the intended work was achieved, and whether someone accepted the outcome.

The proposed quick filters remain **All, Completed, Partial, Failed, and Pending Review**. Their semantics need care: Completed, Partial, and Failed describe the reported outcome; **Pending Review describes review state and may overlap with an outcome**. It should therefore work as a review filter, not erase the outcome or imply mutually exclusive totals. An interrupted attempt must retain that fact in its detail record rather than masquerade as successful completion.

Each result should identify its task and attempt, summarize the actual scope of work, and link to the relevant code state. Its row can show the outcome, review state, changed-file count, recorded duration, and verification summary, with command details available on demand. For uncommitted changes, that requires a recorded patch or equivalent snapshot—not only a branch name whose contents may change.

Evidence includes available diffs, executed checks, test output, unresolved findings, and generated artifacts. Counts should come from recorded tooling where available, not be inferred from the agent's prose. **Passed, Failed, and Not Run must remain distinguishable.** A successful build does not establish that every acceptance criterion passed. Missing required verification prevents a claim of verified completion, even when the runtime turn ended normally.

The right panel shows the selected result and links to its evidence, with a compact summary rather than decorative charts. **Review Changes** opens the associated change set; **Open Task** returns to intended work; **Re-run** creates a new attempt after checking the current context and execution permissions. It must not overwrite the earlier evidence or blindly repeat operations with side effects.

Results owns the account of what happened. Library provides access to the files supporting it. A task can be Done because a specific result was accepted, not merely because the most recent agent message sounded complete.

![Codex Studio concept: execution results, verification details, and evidence links](../05-results-execution-evidence.png)

*Figure 4 — Review starts from an execution record and its evidence. Sample metrics are not benchmarks; Pending Review remains independent of execution outcome.*

### Library — Find files without losing their origin

Library provides **Project Files / Session Files**, with search, sorting, lightweight list or grid presentation, and file-type filters such as **All, Docs, Code, Images, Data, and Archives**. Inputs, Outputs, and Resources remain classifications inside Library, not additional main tabs. A generated report can therefore be both an Output and a document.

Project Files surfaces shared references, relevant repository files, and maintained artifacts. Session Files identifies attachments and artifacts introduced or produced in a particular conversation—not raw Codex session-log files. An item can appear in both views through its associations without requiring duplicate bytes. The session identity should remain visible so a similarly named file is not mistaken for another revision.

The file list should distinguish a live repository path from an uploaded attachment or a generated artifact. Where a result references historical evidence, opening it must not silently substitute today's file. A missing, moved, or inaccessible source should show that condition; the interface should not imply that a filename alone proves the evidence is available.

Below the account identity, **External Sources** could offer supported connections such as Google Drive or Dropbox, alongside selected-file details. Provider names in the mockup are examples to evaluate, not promised integrations. Connecting a provider should require explicit authorization and a chosen scope; it must not automatically expose an entire personal account to every project or agent. Revoked access should be reflected in file availability.

The first version can be useful with local references and project attachments alone. A universal file manager, unrestricted repository duplication, and automatic cloud synchronization are not prerequisites.

![Codex Studio concept: Library with Project Files, Session Files, and type filters](../06-library-files-external-sources.png)

*Figure 5 — Files remain discoverable by scope, type, and source, while result links preserve their relationship to the work. External connection controls illustrate optional future integrations.*

### More — Keep specialized controls out of the daily path

More provides a place for less frequent configuration, diagnostics, and detailed execution records. Execution is a process within the workflow, not a seventh main tab. Its inspectable record should contain available commands, tool events, approvals, and outputs—not a promise to expose private model reasoning.

Prompt-template galleries remain outside this proposal's current scope. Additional tools should earn their place through demonstrated workflow value rather than fill available space.

## 06. One Connected Workflow

*This scenario uses the affiliate marketer page illustrated in the mockups. It describes proposed behavior, not a completed Studio implementation or a measured test.*

**Start in Chat.** The developer asks Codex to inspect an existing commerce application and plan an affiliate page showing commission summaries, referral activity, and payout information. The initial request is for investigation and planning, not permission to change the database or deploy anything.

**Create actionable Tasks.** After reviewing the plan, the developer saves tasks for checking the existing data contract, preparing dashboard components, and connecting the page. The design task can belong to Design → Dashboard Components. The original request remains linked, while the task description specifies what the page must show and how empty and error states should behave.

**Approve the decision that matters.** Suppose inspection identifies an existing commission API. The developer chooses to reuse it rather than create another calculation path. That choice becomes an Approved decision with a reason and scope. The discarded alternative remains in the discussion; it does not become an instruction for another agent.

**Execute with relevant context.** The implementation task receives the approved contract decision, applicable repository guidance, selected file references, and its acceptance criteria. Studio records which versions were supplied. Codex performs the work using its existing execution controls, and the attempt remains associated with its code state and task.

**Review Results.** Suppose the implementation and available unit checks finish, but an integration check cannot run because its test environment is unavailable. Results shows that limitation as Not Run, links to the checks that did execute, and identifies the missing verification. The task remains open for review or follow-up; the interface does not manufacture a green completion signal.

**Follow the files through Library.** The developer opens the recorded diff and test report from the result. The report is available as a session output and can be associated with the project without duplicating it. A correction produces another attempt and another result; accepting that result does not erase the earlier limitation.

**Resume with the right state.** In a later session, the developer can find the accepted API decision, remaining work, and the specific reviewed result. A new agent receives relevant current guidance and unresolved findings. If the contract changed meanwhile, Studio flags the mismatch rather than treating the older result as proof that the new version works.

Not every task needs a decision record or this entire sequence. A typo can remain a quick conversation. The connected workflow becomes valuable when the work must survive handoffs, revisions, or time away.

## 07. Expected Value

The expected benefit is a clearer working relationship between developer and agents: less reconstruction before continuing, easier review of what actually happened, and fewer ambiguous transitions from discussion to implementation.

These are hypotheses to test, not established productivity gains. An evaluation should use the same multi-session tasks and compare Studio's workflow with a credible current setup using Codex, repository documentation, and an existing tracker—not an artificially disorganized baseline.

The measurements should pair convenience with correctness. Time to locate a decision matters only if the developer finds the current, applicable one. Faster resumption matters only if required constraints are preserved. Less review time is not a benefit if failed or missing checks become easier to overlook.

Useful observations would include time to recover project state, time to trace a result to its source and code revision, repeated clarification, accidental reuse of superseded guidance, and effort spent maintaining the new records. Where available, context usage and execution cost could also be measured without promising savings in advance.

The product succeeds only if the information it connects is more useful than the administrative work it introduces. That is how Studio could become an everyday engineering tool rather than another dashboard developers must keep updated.

## 08. A Practical Product Direction

I would start with a complete but narrow workflow: create a task from Chat, retain its source, attach an approved decision when necessary, run the work through supported Codex capabilities, and review a result linked to its evidence and files. Basic selection of relevant guidance belongs in that first workflow; sophisticated retrieval and multi-agent coordination can mature later.

The first version should keep organization optional, reuse repository instructions, and expose a small number of reliable transitions. It should not require recreating an existing backlog, configuring a hierarchy, or connecting cloud storage before doing useful work. Exportable project records would also help keep important engineering knowledge accessible outside the application.

A useful division of responsibility is to leave models, tools, and execution policies with Codex, while Studio connects project records, context selection, navigation, and review. This is an integration direction, not a claim that the public interfaces already supply every required lifecycle event or persistence guarantee. Those boundaries need validation.

**Reusing capability reduces duplication; it does not make the product free to build.** Durable records, recovery behavior, version-aware links, accessibility, compatibility, and secure integrations all require implementation and maintenance. Synchronization must also handle conflicting edits without silently replacing an approved decision or losing evidence.

I would keep the dedicated desktop product as the primary direction, while leaving the exact sharing of runtime and platform components to OpenAI's engineering assessment. Richer integrations and extensibility should follow demonstrated needs. Studio should become valuable because its core workflow is dependable, not because it promises to replace every tool on day one.

## 09. Feedback and Further Details

I would welcome feedback from developers maintaining long-running projects and from OpenAI's Codex product, engineering, and developer-experience teams.

**Which connection would improve your work most: decisions to tasks, tasks to execution evidence, or approved project context across sessions?**

**What would a dedicated workspace need to get right for you to open it alongside your IDE every day, rather than continue managing these relationships through conversations and separate tools?**

I plan to develop a **Full Product Concept RFC** covering detailed interactions, integration boundaries, technical relationships, and trade-offs. It is not yet complete. Interested reviewers are welcome to send me a private message to receive the fuller material when it is ready.

The central proposal is complete here: **keep the agent capabilities Codex already provides, and give the ongoing engineering work around them a connected, inspectable, persistent home.**

*— TechSoft*
