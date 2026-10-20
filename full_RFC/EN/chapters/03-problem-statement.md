<a id="ch-03"></a>
# 03. Real-World Problem Statement

<a id="s-03-1"></a>
## 03.1 Available observation

The starting evidence is TechSoft's supplied account of recurring planning, implementation, review, and resumption in ongoing software projects. It describes scattered requirements, decisions and outputs. It does not include time measurements, interview transcripts, or an incident dataset. The proposal therefore treats the problem as plausible and concrete, with prevalence and commercial significance still unmeasured.

The relevant unit is a feature continued across sessions. A developer can locate a conversation yet still need to establish whether a suggestion was adopted, whether a later correction superseded it, and whether the evidence refers to the current code. That reconstruction is distinct from simply retrieving text.

<a id="s-03-2"></a>
## 03.2 Problem register

**Table 03-1 — Observations, interpretations, and falsifiable consequences**

| ID | Qualitative observation in supplied drafts | Interpretation to test | Observable failure in an evaluation |
|---|---|---|---|
| P-01 | Alternatives and accepted choices share discussion history | Approval is expensive to recover | Participant selects a superseded or unapproved choice |
| P-02 | A closing response may leave verification unfinished | Task progress is conflated with agent progress | Participant calls a feature Done while a required check is Not Run |
| P-03 | Diffs, logs, and summaries require manual association | Evidence identity is difficult to assess | Participant uses a passing check from a different revision |
| P-04 | Relevant constraints must be restated on resumption | Context recovery requires avoidable work | Participant omits a known applicable constraint or repeats its explanation |
| P-05 | Organization itself requires upkeep | A structured product may add burden | More maintenance time than recovery time saved |

These are evaluation failure definitions, not claims that such failures occurred at measured rates. Their proposed remedies belong in Chapters 05–11; Chapter 13 specifies how to compare them fairly.

<a id="s-03-3"></a>
## 03.3 Existing workarounds

A developer can keep repository decision records, issue descriptions, checklists, Git history, and links to relevant conversations. This is a credible baseline. It offers explicit review and portable knowledge; the effort lies in keeping relationships and freshness current. A skilled team may already maintain these well enough that Studio adds little value.

Another workaround is to keep a feature in one long conversation. It can preserve detail but does not by itself specify independent task acceptance, versioned decisions, or the relationship between a test and a code snapshot. This statement is a distinction in the conceptual model, not a diagnosis of undisclosed Codex storage.

Studio should therefore reduce bookkeeping by capturing provenance when actions occur. It must not require a developer to rewrite every useful message, manually duplicate source files, or categorize every question before receiving help. If reliable automatic attribution is unavailable, the interface should expose the limitation rather than conceal manual maintenance.

<a id="s-03-4"></a>
## 03.4 Scenario and scope

Appendix C uses the affiliate marketer page already present in the mockups. The illustrative request is to inspect the existing application and plan the page; implementation requires a subsequent instruction. The example considers commission summaries, referral activity, and payout information without establishing a real endpoint, schema, balance, or financial result.

The scenario is useful because it has a consequential reuse decision, interface work, evidence review, and a later return to unfinished verification. It does not justify adding financial logic to Studio. The host application remains responsible for domain data and authorization.

<a id="s-03-5"></a>
## 03.5 Evidence needed before investment

Recruit participants who actually return to software work after an interruption, including developers with organized repository documentation. Observe current practice before introducing Studio terminology. Ask them to retrieve an approved constraint, explain an incomplete result, and identify the next safe action. Record errors and maintenance effort as well as speed.

**R-03-01 — Honest problem evidence.** The evaluation MUST separate self-reported friction from observed task errors and measured time. Acceptance: the study dataset identifies its evidence type and does not report the illustrative scenario or mockup values as participant results. If participants already recover state reliably and quickly, reduce or reject the corresponding product claim.

<!-- related-start -->
**Related sections:** [Appendix C. End-to-End Developer Scenario](../appendices/C-affiliate-scenario.md#app-c) · [13. Validation and Expected Value](../chapters/13-validation-value.md#ch-13)
<!-- related-end -->
