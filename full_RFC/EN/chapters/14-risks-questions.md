<a id="ch-14"></a>
# 14. Risks, Trade-offs, and Open Questions

<a id="s-14-1"></a>
## 14.1 Risk register

Severity below is a design assessment, not a measured probability. Owners are proposed responsibility roles, not named OpenAI teams or commitments.

**Table 14-1 — Material risks**

| Risk | Consequence / severity | Mitigation and evidence required | Residual uncertainty |
|---|---|---|---|
| RISK-01: Duplicate organization | More bookkeeping and abandonment; high | Narrow workflow, optional structure, H-06 maintenance measurement | User habits and existing tools vary |
| RISK-02: Runtime drift | Broken attribution or controls; high | Versioned adapter, contract tests, explicit unsupported state | Public interface stability and support |
| RISK-03: Stale guidance | Wrong implementation under obsolete decision; high | Versioned context, supersession impact, V-04/V-09 | Semantic conflict detection remains fallible |
| RISK-04: Misleading completion | Unverified work accepted as ready; high | Independent states and criterion-based review, V-05 | Humans can still accept exceptions unwisely |
| RISK-05: Lost/incorrect evidence | Review cannot be reproduced; high | Snapshot hashes, retention, backup restore, V-06/V-10 | Storage cost and policy constraints |
| RISK-06: Permission confusion | Unauthorized action or data disclosure; critical | Separate authority records, exact approvals, V-08 | Runtime/provider enforcement differences |
| RISK-07: Standalone lifecycle cost | Product maintenance exceeds value; high | G3 assessment including support and updates | No cost estimate available yet |
| RISK-08: Synchronization conflicts | Approved state silently overwritten; high | Defer sync; design conflict protocol before expansion | Multi-device identity and deletion semantics |
| RISK-09: Overspecialized UX | Small tasks become slow or inaccessible; medium | Quick chat, title-only tasks, bilingual keyboard tests | Layout needs real user testing |
| RISK-10: Overstated evidence | Unsupported novelty or endorsement claims; high | Dated claim register and bounded baseline | Documentation changes after verification |

<a id="s-14-2"></a>
## 14.2 External decisions required

**Table 14-2 — Open decision register**

| ID | Decision and owner role | Impact / alternatives | Gate and proposed interim position |
|---|---|---|---|
| Q-01 | Supported runtime adapter and transport — integration engineering | Local App Server, SDK or bounded noninteractive execution; differing lifecycle visibility | Before G1; use only validated public contract, no private database scraping |
| Q-02 | Authentication, entitlement, distribution and naming — product/platform/legal owners | Independent app, integrated workspace or constrained companion | Before external pilot/distribution; no entitlement or trademark availability assumed |
| Q-03 | Retention, encryption, backup and deletion policy — security/data owner | Managed artifact retention versus minimal local references; different auditability/cost | Before pilot with real data; use non-sensitive fixtures meanwhile |
| Q-04 | Recovery and event guarantees — runtime integration owner | Reconcile supported state or require manual resolution of Unknown | Before unattended or side-effecting prototype work; no blind retry |
| Q-05 | Completion exceptions and team authority — product/security owner | Single local owner, required peer review, or managed roles | MVP single owner; team expansion blocked until policy defined |
| Q-06 | Standalone maintenance viability — product/engineering owner | Continue primary direction or adopt integrated delivery after comparison | G3; no schedule/cost promise |
| Q-07 | External sources and tracker authority — integration/product owner | Reference-only links, scoped read integration, or later bidirectional sync | After local value pilot; links only in MVP |
| Q-08 | Study thresholds and sample — research owner | Minimum useful improvement and correctness margin based on pilot variability | Before confirmatory study; no invented success threshold or result |
| Q-09 | Target operating systems and accessibility acceptance — desktop owner | Limited first platform versus simultaneous parity | Before implementation plan; bilingual content does not prove platform parity |

These questions do not leave unwritten RFC chapters. They mark decisions that require authority, engineering evidence or user data outside document preparation. Each has a bounded interim behavior so an implementation review can proceed without guessing.

<a id="s-14-3"></a>
## 14.3 Rejected shortcuts

A last-message-wins rule would be easy to implement but would conflate discussion with authority. A universal context dump would avoid selection logic but would increase stale/conflicting material. A latest-branch evidence link would simplify storage but lose the state actually reviewed. Automatic retry after a timeout would improve apparent responsiveness but risk duplicated side effects. None is acceptable in the proposed core workflow.

<a id="s-14-4"></a>
## 14.4 Reassessment triggers

Reopen the concept if existing product capabilities substantially change, if a supported integration cannot preserve approval semantics, if users consistently avoid record upkeep, or if standalone distribution cannot be maintained responsibly. A complete RFC is an input to that decision, not a reason to proceed despite contrary evidence.

**R-14-01 — Explicit unresolved decisions.** Every unresolved high-impact dependency MUST have an owner role, consequence, alternatives and gate. An implementation plan must not treat an interim position as external approval.

<a id="s-14-5"></a>
## 14.5 Expansion risks and external decisions

**Table 14-3 — Additional risks**

| Risk | Consequence | Mitigation and remaining evidence |
|---|---|---|
| RISK-11: Wrong environment or stale contract | Valid local change breaks a consumer or targets production | Profile pinning, dependency versions, combined manifest; V-13–V-15 |
| RISK-12: Assignment confused with authority | Agent or human gains unintended access; self-approval appears independent | Separate principals/grants, deny enforcement, revocation and review policy; V-16 |
| RISK-13: Roadmap exceeds evidence | Trend-driven scope growth, unsafe device action or unjustified provider cost | Optional adapters, explicit modality consent and scope gates; V-17/V-18 |

**Table 14-4 — Expansion decisions**

| ID | Decision and owner | Alternatives / impact | Gate and interim position |
|---|---|---|---|
| Q-10 | Group membership and contract authority — product/architecture owners | One or multiple groups per Project; shared contracts or external authoritative registry | Before group prototype; use explicit flat membership and versioned references, no inherited code access |
| Q-11 | Team identity, shared service and enforcement — security/platform owners | Existing identity provider and policy service versus dedicated managed backend | Before shared editing; local owner model remains; no self-issued agent privileges |
| Q-12 | Modality retention and specialist-provider scope — privacy/domain owners | Ephemeral media versus retained excerpts; simulation versus separately approved hardware/provider jobs | Before each adapter pilot; opt-in capture and no implied actuation/spend |

The proposed matrix answers the design question at review level; the actual organization must approve bindings, independent-review policy and provider enforcement. Q-05 remains open for that adoption decision. No future technology forecast resolves Q-01/Q-02 or licenses unsupported integration.

<!-- related-start -->
**Related sections:** [11. Technical Integration and Trust](../chapters/11-integration-trust.md#ch-11) · [12. Product Packaging and Delivery Strategy](../chapters/12-delivery-mvp.md#ch-12) · [13. Validation and Expected Value](../chapters/13-validation-value.md#ch-13) · [Appendix E. References and Evidence](../appendices/E-references-evidence.md#app-e)
<!-- related-end -->
