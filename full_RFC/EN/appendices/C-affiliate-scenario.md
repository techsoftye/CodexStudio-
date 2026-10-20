<a id="app-c"></a>
# Appendix C. End-to-End Developer Scenario

<a id="s-c-1"></a>
## C.1 Scenario assumptions

This is a worked **illustration of proposed Studio behavior**, not a report of actual execution. Names, IDs, revisions and outcomes below are fictional identifiers for tracing relationships. No real affiliate endpoint, database schema, financial balance, measured test count or production operation is asserted.

The developer maintains an existing commerce application and asks for an affiliate marketer page showing commission summaries, referral activity and payout information. The initial request is inspection and planning. The example assumes inspection later finds a reusable API contract and existing UI conventions. If inspection instead finds no suitable contract, the decision and plan must change before implementation.

**Table C-1 — Example record inventory**

| ID | Meaning | Initial relation |
|---|---|---|
| P-AFF | Example project | Owns all records below |
| C-PLAN / M-01 | Planning conversation and request | Source of three tasks |
| T-101 | Inspect existing affiliate contract | Analysis task |
| T-102 | Prepare page components | Design → Dashboard Components |
| T-103 | Connect and verify page | Parent T-102 optional only if decomposition is intended |
| D-07 v1 | Reuse existing contract for the page | Proposed, then explicitly Approved |
| U-01 | Preserve existing authorization and localization guidance | Repository-backed rule reference |
| X-21 / X-22 | First implementation and corrective attempts | Both belong to T-103 |
| S-21 / S-22 | Results of those attempts | Separate evidence and review history |

<a id="s-c-2"></a>
## C.2 Planning and approval

In Chat the developer says: “Inspect the current affiliate implementation and prepare a plan before changing code.” Codex reads authorized sources and identifies assumptions. The response may describe future implementation steps, but those steps remain a plan.

The user selects Add to Tasks and edits T-101–T-103. Each retains M-01. Stage and Section are optional; T-102 is placed in Design → Dashboard Components for illustration. T-101's acceptance criterion is a sourced contract assessment. T-103's illustrative criteria are: use the agreed contract, preserve existing access control, show loading/empty/error states, and obtain relevant implementation and integration evidence. These criteria are scenario assumptions, not discovered facts about the repository.

Suppose inspection confirms a suitable contract. The agent drafts D-07 v1 with rationale: reuse the existing source of commission data and avoid an independent calculation path. The developer reviews scope and approves it. U-01 remains linked to its authoritative repository instruction. Approving D-07 does not authorize a schema change, payout operation or deployment.

<a id="s-c-3"></a>
## C.3 Execution and incomplete verification

The developer then explicitly authorizes implementing T-103 within the inspected scope. Studio checks project/root, task version, source availability and current permissions. It records context manifest CM-21 containing T-103 v1, D-07 v1, U-01's source revision and selected files. X-21 begins with code snapshot K-21-base and preserves preexisting changes.

For the illustration, implementation produces a captured change set K-21-result. A relevant unit check runs and passes; an integration check cannot start because its fixture environment is unavailable. These are hypothetical outcomes, with no fabricated counts.

**Table C-2 — First result without state conflation**

| Dimension | Example value | Interpretation |
|---|---|---|
| Attempt X-21 | Finished | Runtime work ended normally |
| Result S-21 | Partial | Required verification remains incomplete |
| Unit check | Passed on K-21-result | Evidence applies only to recorded scope/snapshot |
| Integration check | Not Run; environment unavailable | No inferred pass |
| Review | Pending Review | Human has not accepted the result |
| Task T-103 | Review | Intended work awaits evaluation |

The reviewer opens Review Changes, inspects K-21-result and the check log, and records Changes Requested because integration evidence is required. T-103 returns to Active. The generated report appears as a Session File Output and can also be associated with Project Files without duplicating bytes.

<a id="s-c-4"></a>
## C.4 Correction and acceptance

After the test environment becomes available, the developer requests a correction and verification attempt. Re-run prepares X-22; it does not replay every command from X-21. The resolver includes the unresolved finding and checks current sources. If code has changed since K-21-result, the new checks bind the new snapshot.

For the example only, X-22 completes the required integration check and produces S-22 with sufficient evidence for the agreed criteria. The reviewer accepts S-22's exact version. T-103 can become Done with a completion record mapping criteria to S-22 and, where still applicable, explicitly referenced evidence from S-21. S-21 remains Partial/Changes Requested in history; later acceptance does not rewrite it.

If the reviewer instead accepts with an authorized verification exception, the exception remains visible. The scenario cannot claim verified completion or release readiness from that exception. A production deployment or payout action would require separate authorization.

<a id="s-c-5"></a>
## C.5 Return in a later session

A later conversation C-RETURN opens the same project. The developer sees the current tasks, D-07, accepted S-22 and any unresolved follow-up. The context resolver selects these records and verifies their source revisions. It does not load all historical discussion by default.

Suppose the contract source has changed. Studio flags drift, retains CM-21 and S-22 as historical evidence, and asks for a scoped investigation before claiming that the accepted implementation remains valid. A new decision may supersede D-07; the prior approval is still explainable. The task is reopened or a new follow-up created according to whether the intended outcome changed.

<a id="s-c-6"></a>
## C.6 Failure branches and review walkthrough

**Table C-3 — Alternate branches**

| Trigger | Required response | Why it matters |
|---|---|---|
| No suitable API found | Keep decision Proposed; revise plan and seek choice | Scenario assumptions cannot force a false source of truth |
| Runtime disconnect after launch | Mark observation Unknown; reconcile X-21 | Avoid duplicate changes or side effects |
| Rule conflicts with proposed implementation | Block affected action and show sources | Decision cannot override higher authority silently |
| Source attachment revoked | Mark unavailable; exclude from new context or stop if required | A cached file is not perpetual authorization |
| User chooses Deferred during execution | Show active attempt and explicit interruption choice | Planning state does not stop a process |
| Historical diff missing | Show Version Unavailable | Today's checkout cannot impersonate reviewed evidence |

A reviewer can walk the example from M-01 to T-103, D-07, CM-21, X-21, S-21, X-22 and S-22, then return through Library to the same evidence. This is the reference narrative for V-03 through V-09. Its purpose is to test semantic consistency before product implementation.

<a id="s-c-7"></a>
## C.7 MetaStore group extension and hybrid handoff

The following extension uses the user's Backend + Flutter + Next.js structure. All record IDs and contract versions remain fictional; no real schema, endpoint, secret or repository state is asserted. G-META contains P-BACK, P-MOBILE and P-WEB, each with its own Environment Profile. The original single-project affiliate narrative remains valid independently.

The human technical lead requests an impact assessment for exposing an affiliate summary consistently to both clients. The coordinator agent can read authorized contract references and propose a Change Set CS-AFF; it has no blanket write access. A Backend specialist receives a grant for P-BACK development paths and fixture checks. Mobile and Web specialists receive separate grants for their own projects. A human reviewer receives evidence access; a review agent can provide findings but cannot accept the result.

Inspection first decides whether an API change is necessary. If the existing contract is sufficient, retain it and create only consumer work; the scenario does not require a gratuitous Backend change. If a change is needed, a proposed group decision identifies affected consumers, compatibility/deprecation options and the authoritative contract version. Approval by the responsible human is followed by consumer acknowledgments, not automatic client acceptance.

For illustration, tasks T-B, T-M and T-W remain in their owning Projects and CS-AFF records their dependencies. Attempts X-B, X-M and X-W pin separate profiles and snapshots. Suppose Backend and Web evidence pass but the required Flutter device is unavailable. The Flutter CheckRecord remains Not Run. CS-AFF stays Awaiting Integration or Held with a stated blocker; no single green Backend result closes the product outcome.

A handoff records the missing target, current contract version, accessible snapshots, permitted next action and grant expiry. When a human or new agent resumes, it revalidates identity, profile and contract rather than reusing expired credentials. If the contract changed, dependent evidence is stale and new checks bind the revised snapshot set.

Only an authorized integration attempt with IM-AFF covering required member revisions, followed by human review, can establish the agreed integrated outcome. Deployment remains a separate action. An optional spoken request such as “resume the mobile check” first resolves P-MOBILE and its profile visibly; it cannot accidentally launch the Backend service or approve production release.

<!-- related-start -->
**Related sections:** [06. Tasks and Development Planning](../chapters/06-tasks-planning.md#ch-06) · [07. Engineering Decisions and Project Rules](../chapters/07-decisions-rules.md#ch-07) · [08. Execution Results and Evidence](../chapters/08-results-evidence.md#ch-08) · [10. Context, Memory, and Agent Orchestration](../chapters/10-context-orchestration.md#ch-10) · [Appendix D. Conceptual Data Model](../appendices/D-conceptual-data-model.md#app-d)
<!-- related-end -->
