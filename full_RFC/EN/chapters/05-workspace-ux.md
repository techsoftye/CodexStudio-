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
**Related sections:** [06. Tasks and Development Planning](../chapters/06-tasks-planning.md#ch-06) · [07. Engineering Decisions and Project Rules](../chapters/07-decisions-rules.md#ch-07) · [08. Execution Results and Evidence](../chapters/08-results-evidence.md#ch-08) · [09. Project Library and Resources](../chapters/09-library-resources.md#ch-09) · [Appendix A. UI/UX Concept Gallery](../appendices/A-design-gallery.md#app-a)
<!-- related-end -->
