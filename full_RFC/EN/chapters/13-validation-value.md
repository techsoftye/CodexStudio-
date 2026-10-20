<a id="ch-13"></a>
# 13. Validation and Expected Value

<a id="s-13-1"></a>
## 13.1 Hypotheses and study design

The proposal predicts better continuity and review, not proven productivity gains. The evaluation must compare Studio with a credible current workflow: current Codex, the participant's IDE/Git tools, repository instructions, and an organized tracker or notes. Preserve equivalent source material, task scope, runtime/model configuration where possible, and access permissions.

Use a counterbalanced within-participant study with matched tasks: half encounter Studio first and half the baseline first. Avoid asking the same person to solve the identical task twice; remembered answers would bias resumption and decision retrieval. Include an interrupted multi-session feature and a simple edit to detect administrative overhead. Use the affiliate scenario as one candidate, alongside a different repository/domain to reduce scenario-specific advantage.

Recruit developers who routinely return to ongoing work, with varied experience and existing organization habits. Determine sample size after an exploratory pilot estimates variability and the minimum effect worth acting on. Do not claim statistical power from an arbitrary participant count. Preregister the final primary measures, exclusions and decision thresholds before the confirmatory study.

<a id="s-13-2"></a>
## 13.2 Operational metrics

**Table 13-1 — Hypothesis and measurement matrix**

| ID | Hypothesis / measure | Operational definition | Judgment criterion |
|---|---|---|---|
| H-01 | Faster correct resumption | Time from opening assigned project to stating and beginning the correct next authorized action | Paired time improvement with no correctness degradation; minimum worthwhile difference set before confirmatory study |
| H-02 | Better decision retrieval | Correct current applicable decision selected / all retrieval trials | Accuracy at least baseline; superseded-choice errors separately reported |
| H-03 | Better evidence traceability | Correct task → attempt → snapshot → check chain / all trace trials; completion time | Improve trace completion or time without wrong-revision evidence use |
| H-04 | Better review judgment | Detection of seeded missing/failed checks; false acceptance rate | No false verified-completion acceptance in safety-critical seeded cases |
| H-05 | Lower repetition and rework | Repeated constraint explanations; corrections caused by missed approved constraints | Reduced events without increasing omitted constraints |
| H-06 | Manageable administrative cost | Time creating/correcting records, resolving links and organizing material | Recovery/review benefit exceeds measured maintenance burden for target work |
| H-07 | Efficient context | Supplied tokens/bytes and total execution cost where observable, including resolver overhead | Compare total cost alongside correctness; no savings claim if cost is unavailable or scope differs |

Time metrics include failed attempts and timeouts. Record “unable to complete” as an outcome rather than dropping it. Report medians, distributions, paired differences and uncertainty; do not convert small samples into precise population claims. Tool-switch counts are meaningful only when the switch interrupts the work; fewer switches with worse evidence access is not success.

<a id="s-13-3"></a>
## 13.3 Instrumentation and evidence

Collect minimal consented interaction events: anonymous participant/session ID, condition, task fixture version, record navigation, dispatch/review timestamps, source availability, task outcome and observer-coded errors. Record code snapshots and seeded issues for scoring; avoid collecting private source contents or secrets unnecessarily. Separate task time from external outages and explain both.

An independent rubric defines correct next action, governing decision, required checks and acceptable evidence. Ideally a reviewer unaware of the interface condition scores the participant's final answer and acceptance choice. Preserve disagreement and adjudication rather than silently adjusting a score to fit the hypothesis.

Baseline configuration and Studio overhead must be documented. If model, runtime, repository or task difficulty differs, stratify or limit inference. For cost, distinguish model usage from local indexing, storage, human maintenance and support costs. If a provider does not expose tokens or billing for the tested path, report that metric unavailable.

<a id="s-13-4"></a>
## 13.4 Functional and adversarial validation cases

**Table 13-2 — Proposed verification cases**

| ID | Fixture / action | Expected observation | Requirements covered |
|---|---|---|---|
| V-01 | Save title-only task; switch panels and return | Defaults valid; draft/filter/focus preserved | R-04-02, R-05-03, R-06-01 |
| V-02 | Repeat save after timeout; concurrently reparent tasks | No duplicate logical save; no cycle | R-05-02, R-06-02 |
| V-03 | Agent proposes a decision and finishes a run | Decision stays Proposed; task not automatically Done | R-06-03, R-07-01 |
| V-04 | Approve replacement during an active attempt | Old manifest retained; drift and impacted work visible | R-07-02, R-07-05, R-10-04 |
| V-05 | Required integration check unavailable; build succeeds | Not Run remains visible; verified completion blocked | R-08-01, R-08-03, R-08-05 |
| V-06 | Change working tree after evidence capture | Historical diff still exact; current mismatch identified | R-08-02, R-09-03 |
| V-07 | Crash around dispatch; duplicate/out-of-order events | No blind redispatch; Unknown or reconciled state | R-11-02, R-11-03 |
| V-08 | Revoked external source, malicious attachment and escaped path | Access blocked; no instruction or permission promotion | R-09-04, R-10-06, R-11-07 |
| V-09 | Required context exceeds budget or sources conflict | No silent truncation; affected work blocked | R-07-04, R-10-02 |
| V-10 | Disk full, interrupted upgrade and backup restore | Clear failure; recoverable records and evidence availability | R-11-05, R-11-06 |
| V-11 | English/Arabic, keyboard-only and enlarged text | Same functions, readable identifiers and controlled focus | R-05-05 |
| V-12 | Two isolated contributions combined | Integration checks bind combined snapshot | R-10-05 |

The cases specify future product tests. They have not been executed by preparing this document.

<a id="s-13-5"></a>
## 13.5 Decision rules and stopping

Adopt zero-tolerance design gates for cross-project disclosure, unauthorized action, duplicated uncertain side effects, lost approved history, and false claims that missing checks passed. A single reproduced instance blocks further expansion until corrected and retested. Zero observed incidents in a pilot does not prove zero risk.

For value, move forward only if primary measures show an actionable improvement under preregistered thresholds and administrative burden remains acceptable. If accuracy improves but time worsens, report the trade-off and target the users for whom reliability matters. If the integrated alternative delivers comparable outcomes with lower maintenance, reconsider standalone packaging while preserving the core workflow findings.

**R-13-01 — Measurable evaluation.** Each reported benefit MUST include its metric definition, baseline, sample, uncertainty and limitations. No mockup counts or hypothetical scenario outcomes may be entered as observed data.

**R-13-02 — Correctness guardrails.** Any rollout recommendation MUST satisfy the safety gates and report negative or inconclusive findings, not only favorable speed metrics.

<a id="s-13-6"></a>
## 13.6 Group and hybrid-team validation

Extend the study only after the corresponding expansion gate. Compare against a deliberately organized baseline using current multi-folder/repository tools, separate environment configuration and existing access controls. Do not compare Studio with an artificially disorganized team. Use synthetic MetaStore-like Backend/Flutter/Next.js fixtures; this RFC contains no results from the user's actual repositories.

**Table 13-3 — Additional measurable hypotheses**

| ID | Measure | Collection and success condition |
|---|---|---|
| H-08 | Correct cross-project impact identification | Correctly identified required consumers and stale contracts / seeded cases; improve accuracy or time without disclosing inaccessible data |
| H-09 | Environment-selection errors and recovery time | Wrong-target starts / launch trials, plus time to recover after profile drift; no unauthorized target accepted |
| H-10 | Delegation and review integrity | Unauthorized attempts prevented, permitted work falsely blocked, and handoff time; no authority escalation or false independent review |
| H-11 | Multimodal usefulness | Correct interpreted tasks, clarification rate, action-confirmation errors and total time versus text; benefit must exceed correction overhead |

**Table 13-4 — Expansion acceptance cases**

| ID | Fixture / action | Expected observation | Requirements |
|---|---|---|---|
| V-13 | Add three projects; revoke one; switch selected environment | Independent profiles; no hidden names/counts; no wrong-target dispatch | R-04-04, R-05-07, R-09-07, R-10-07 |
| V-14 | Change an API contract after one client passes | Impacted consumer evidence becomes stale; combined acceptance blocked | R-07-07, R-10-08 |
| V-15 | Backend passes, Flutter fails, Next.js dependency waits | Separate project-local tasks and attempts; corrective plan without reset or blind replay | R-06-07, R-10-08 |
| V-16 | Assign out-of-scope work; delegate wider access; revoke a grant; same-author review | Assignment grants nothing; elevation rejected; new actions blocked; independent-review policy enforced | R-11-09, R-11-10, R-11-11 |
| V-17 | Ambiguous spoken target; approval text in screenshot; revoked media | Reviewable interpretation and scoped confirmation; no source-to-permission promotion | R-09-07, R-11-12 |
| V-18 | Simulation marked hardware; quantum job times out after submission | Mislabel rejected; uncertain job reconciled before charged resubmission | R-11-13, R-12-03 |

These are proposed cases, not executed experiments. Measure environment setup, coordination and policy maintenance alongside task speed. A larger group overview that increases wrong-environment actions fails even if navigation is faster.

<!-- related-start -->
**Related sections:** [03. Real-World Problem Statement](../chapters/03-problem-statement.md#ch-03) · [12. Product Packaging and Delivery Strategy](../chapters/12-delivery-mvp.md#ch-12) · [14. Risks, Trade-offs, and Open Questions](../chapters/14-risks-questions.md#ch-14) · [Appendix C. End-to-End Developer Scenario](../appendices/C-affiliate-scenario.md#app-c)
<!-- related-end -->
