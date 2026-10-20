<a id="ch-08"></a>
# 08. Execution Results and Evidence

<a id="s-08-1"></a>
## 08.1 Purpose and independent state dimensions

Results answers what happened during an execution attempt and what evidence supports the reported outcome. A Task describes intended work; an Execution Attempt records runtime activity; a Result summarizes that attempt; a Check records verification; a Review records human acceptance. A File is supporting material, not the result itself.

**Table 08-1 — State dimensions**

| Dimension | Proposed values | Meaning |
|---|---|---|
| Task | Todo / Active / Review / Done / Deferred | Planning and accepted completion |
| Attempt lifecycle | Queued / Starting / Running / WaitingApproval / Interrupted / Finished / Failed / Unknown | Runtime activity, independent of work quality |
| Result outcome | Completed / Partial / Failed; unset while undetermined | Reported achievement against captured task scope |
| Check | Passed / Failed / Not Run / Inconclusive | Evidence from a specific check on a specific snapshot |
| Result review | Pending Review / Accepted / Changes Requested | Human judgment of an exact result version |

Unknown means runtime state cannot currently be established; it is not success or confirmed failure. Interrupted means interruption is confirmed. Finished means execution ended normally, not that the task passed. An unavailable test environment yields Not Run, while a test that ran but produced insufficient usable evidence is Inconclusive. A suite with mixed results is represented by individual checks or an explicitly partial suite, never a misleading single pass.

The preserved quick filters are **All / Completed / Partial / Failed / Pending Review**. Pending Review selects a separate review dimension and may overlap all outcomes. An unknown or unfinished attempt remains discoverable from All with outcome unset. Any summary counts must state their dimensions and must not add overlapping buckets into a total.

<a id="s-08-2"></a>
## 08.2 Result contents and evidence capture

A result identifies project, task and task version, attempt, relevant runtime references, execution environment, start/end observations where known, context manifest, work summary, changed files, check records, unresolved findings and linked artifacts. Outcome is an attributed assessment, not a direct reading of an agent's confidence.

The code identity must include a commit or equivalent immutable base and the actual change snapshot. For dirty working trees, capture the preexisting state and resulting patch or artifact hashes. A branch name alone is insufficient. Untracked and binary files need explicit inclusion or exclusion. If safe capture is unavailable, label evidence incomplete and prevent a verified-completion claim.

A changed-file count derives from the captured change set. Test counts derive from a parser or tool output with a known source. If the tool emits only exit status, display that fact rather than inventing test totals. A command record includes command description, working directory, environment identifier, relevant tool version when available, timestamps, exit status and accessible output reference. Secrets must be redacted without concealing that redaction occurred.

**Table 08-2 — Evidence identity and limits**

| Evidence | Minimum binding | Limit displayed |
|---|---|---|
| Diff | Base revision plus captured patch and included file set | Preexisting changes, untracked exclusions or unsupported binaries |
| Test report | Command/check ID, snapshot, environment, observation time | Failed / Not Run / Inconclusive checks; parser limitations |
| Screenshot or generated report | File version/hash, origin and capture context | Illustration versus runtime observation |
| Agent summary | Authoring attempt and supporting references | Reported interpretation; not independent test evidence |
| External check link | Provider identity, external record and revision if available | Unavailable content or unverifiable current access |

<a id="s-08-3"></a>
## 08.3 Review workflow

The user selects a result; the right panel shows that result and its evidence links. **Review Changes** opens the captured change set by default, clearly distinguishing it from the current checkout. **Open Task** returns to intended scope and criteria. **Re-run** opens a new execution intent after current context, side effects, repository and authorization are checked.

Review proceeds against the captured task version and acceptance criteria. The reviewer can accept, request changes, or leave the result pending. A request for changes records specific findings and moves the task to Active only through the corresponding task transition. An Accepted result remains an immutable historical judgment even when later code changes make it inapplicable to the current tree.

Task completion can cite several accepted results if no single attempt covers the full scope. The completion record must identify which result or manual evidence supports each criterion. A latest-run shortcut is insufficient. Accepting an inspection-only result may close an analysis task; it cannot establish implementation completion for a different task.

<a id="s-08-4"></a>
## 08.4 Missing verification and exceptions

A required Not Run, Failed or Inconclusive check blocks **verified completion**. If the responsible human intentionally accepts a narrower outcome or waives a criterion within their authority, record the exception, reason, actor, affected criterion and follow-up. The result and task visibly retain “accepted with verification exception”; no missing check becomes Passed.

Mandatory policy requirements cannot be waived through a Studio button. If a release check is required by repository or organization policy, the result may be accepted for limited development review, but cannot claim release readiness. Closing a task and granting permission to deploy are separate operations.

When a check is rerun after code changes, it belongs to the new snapshot and usually a new attempt. If additional evidence is attached without changing the code, create a new result version; existing acceptance remains bound to the old version until reviewed again. Corrections to summaries cannot mutate underlying command output.

<a id="s-08-5"></a>
## 08.5 Retry, interruption and recovery

Re-run is not command replay. It creates a new attempt linked to its predecessor and includes unresolved findings and current guidance. Before repeating an operation with external side effects, establish whether the earlier operation occurred. An uncertain dispatch or timeout must be reconciled before another start.

An interrupted attempt retains partial changes and available evidence. The user can inspect, continue where supported, or start a correction. Studio never silently resets a worktree. A crash before result finalization produces an incomplete record that can be reconciled from available runtime events; refreshing Results cannot execute work.

<a id="s-08-6"></a>
## 08.6 Acceptance criteria

**Table 08-3 — Evidence requirements**

| ID | Proposed requirement and acceptance test |
|---|---|
| R-08-01 | All five state dimensions MUST remain independent. A Finished attempt with a Not Run required check stays unverified and Pending Review. |
| R-08-02 | Review Changes MUST open the recorded snapshot or explain its unavailability; it cannot substitute today's file. |
| R-08-03 | Counts and check states MUST be evidence-derived. A successful build cannot populate unrelated acceptance checks as Passed. |
| R-08-04 | Re-run MUST create a new attributable attempt and preserve earlier evidence; unknown side effects require reconciliation. |
| R-08-05 | Acceptance MUST bind actor, exact result version and task criteria; exceptions remain visible and cannot bypass enforced policy. |
| R-08-06 | Additional evidence or corrected summaries MUST preserve review history and require renewed acceptance when its subject changes. |

Figure A-05 contains illustrative counts only. Chapter 11 defines event ingestion and recovery; Appendix C demonstrates the distinctions in a continuous example.

<a id="s-08-7"></a>
## 08.7 Attempt transition contract

**Table 08-4 — Execution-attempt transitions**

| From | Trigger | To and guard |
|---|---|---|
| Queued | Explicit dispatch after context and permission validation | Starting; durable intent exists |
| Starting | Runtime acknowledges active work | Running; runtime identity persisted |
| Starting | Explicit launch rejection | Failed; preserve rejection and any known side effects |
| Starting or Running | Connection lost or acknowledgement ambiguous | Unknown; retain last confirmed observation |
| Running | Runtime requests operation consent | WaitingApproval; request identity and scope visible |
| WaitingApproval | Valid consent and runtime continuation | Running; never infer continuation from the UI click alone |
| WaitingApproval | Denial, expiry or cancellation | Follow observed runtime outcome: Running with denied action, Interrupted or Failed; no invented terminal state |
| Running | Normal terminal event | Finished; result outcome and review remain separate |
| Running | Confirmed runtime failure or interruption | Failed or Interrupted; preserve partial evidence |
| Unknown | Supported reconciliation finds current/terminal state | Corresponding observed state; no automatic new dispatch |
| Interrupted | Explicit supported continuation | Running with context amendment, or a new linked attempt if continuity cannot be established |
| Finished or Failed | User requests Re-run | New Queued attempt; original remains terminal |

**R-08-07 — Observable transitions.** Attempt state MUST follow confirmed runtime events or an explicitly uncertain observation. Lost connectivity cannot establish Finished, and a rejected approval cannot be translated into an assumed cancellation without runtime evidence.

<a id="s-08-8"></a>
## 08.8 Group integration evidence

Each member task retains its own results and acceptance history. The Change Set's integration assessment references these results and an immutable Integration Manifest; it is not a File and cannot be represented by a count of green task badges. Record missing platforms, stale contracts and failed member checks explicitly.

Acceptance of a group outcome requires an authorized human judgment on the combined evidence. A member's accepted result remains historical if later contract drift invalidates compatibility; the integration assessment becomes stale and needs renewed evidence/review. Accepting integration does not grant deployment authority. Sections 10.8 and D.8 define the coordination relationships; V-14/V-15 specify the partial-failure cases.

<!-- related-start -->
**Related sections:** [06. Tasks and Development Planning](../chapters/06-tasks-planning.md#ch-06) · [09. Project Library and Resources](../chapters/09-library-resources.md#ch-09) · [11. Technical Integration and Trust](../chapters/11-integration-trust.md#ch-11) · [Appendix C. End-to-End Developer Scenario](../appendices/C-affiliate-scenario.md#app-c) · [Appendix D. Conceptual Data Model](../appendices/D-conceptual-data-model.md#app-d) · [Appendix A. UI/UX Concept Gallery](../appendices/A-design-gallery.md#app-a)
<!-- related-end -->
