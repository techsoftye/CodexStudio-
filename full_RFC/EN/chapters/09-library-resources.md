<a id="ch-09"></a>
# 09. Project Library and Resources

<a id="s-09-1"></a>
## 09.1 Purpose, views and classifications

Library provides access to the material used or produced in project work while preserving origin and version. Its primary views are **Project Files / Session Files**. Project Files contains project-associated references, selected repository paths and maintained artifacts. Session Files contains attachments and generated outputs associated with an identified conversation. It is not a browser for all raw runtime session logs.

A single file version may appear in both views through associations. Inputs, Outputs and Resources are classifications within Library. A generated report can be an Output and a document; when reused by another task it may also be that task's Input. Classification belongs to the relationship or usage, not an exclusive permanent label on the bytes.

Type filters remain **All / Docs / Code / Images / Data / Archives**. Search matches visible metadata and, only when explicitly supported and authorized, indexed content. Sorting uses named fields such as modified time or filename. Optional list/grid presentation must not change selection or permissions. No mandatory cloud connection is required.

<a id="s-09-2"></a>
## 09.2 File identity and provenance

**Table 09-1 — Reference kinds**

| Kind | Identity and version | Expected behavior |
|---|---|---|
| Live repository file | Project root binding plus relative path; current revision/hash when read | Opening live source shows current content, with a live indicator |
| Uploaded attachment | Stable artifact identity, original name, content hash and capture time | Immutable captured version; replacement creates a new version |
| Generated artifact | Attempt/conversation origin, file identity and hash | Linked from Results; cannot be mistaken for a measured test if illustrative |
| External reference | Provider/account scope, external ID, version when available | Availability depends on authorization; cache behavior is explicit |
| Historical evidence file | Exact recorded version/hash and evidence relation | Opening never silently resolves to a newer same-named file |

A filename is a label, not identity. Two sessions can contain different files with the same name. The list must show enough source/session information to distinguish them. Deduplicating identical bytes is optional storage optimization within an authorized boundary; it must not leak that another project possesses a file.

<a id="s-09-3"></a>
## 09.3 Ingest, selection and preview

Users can upload a file, select an existing authorized reference, or associate a generated output with the project. An agent may propose that association; it does not automatically expose every generated or personal file to future tasks. Import stages are selected, validating, available, or failed. Validation checks safe path resolution, content type, size limits provided by implementation, readable content where required, and permissions.

The right panel shows selected-file metadata, location, origin, availability, linked work and **Open / Preview** actions. Preview should use a safe renderer appropriate to type. Unsupported formats offer an explicit open/download route without executing embedded content. Archives are listed without automatically extracting them. An invalid path, denied access, corrupt file or unsupported preview yields a specific message while preserving the reference.

Removing an association from a task or session does not delete the underlying file. Deleting an owned artifact is a separate action showing affected evidence links and retention implications. Live repository deletion should remain an explicit file operation under runtime permissions, not a side effect of clearing a Library row.

<a id="s-09-4"></a>
## 09.4 Availability and lifecycle

Availability is independent of classification: Available, Missing, Access Denied, Offline, or Version Unavailable. An external reference may remain a visible historical record after revocation while its content becomes inaccessible. The UI should not infer that cached bytes are authorized for continued use merely because they exist.

Moving a repository root changes the binding only after identity and containment are checked. If the same relative path resolves to different bytes, historical links remain attached to their recorded version. Results' evidence retention rules take priority over convenience cleanup. If policy requires removal, leave a tombstone stating what is no longer available and why; do not retain prohibited content under the guise of auditability.

Search indexing respects project access and deletion. A deleted or revoked document must not remain retrievable through a stale index. Index rebuilds are derivable operations and cannot alter authoritative records or approval state.

<a id="s-09-5"></a>
## 09.5 Optional external sources

The inherited mockup names Google Drive, Dropbox, OneDrive, Import from URL and Sync from Git repository. Those are design examples. This RFC does not verify their compatibility with a standalone Studio or promise them in the MVP. Provider authorization, scopes, revocation, revision access, rate limits and retention must be evaluated individually.

A future connection flow must identify provider account, chosen resource scope, project association and intended agent access. Connecting an account does not grant all projects its entire contents. A URL import is content retrieval, not permission to execute instructions inside the page. “Sync from Git repository” must not imply an automatic pull, branch change or overwrite when viewing Library. These behaviors require separate approved integration design.

<a id="s-09-6"></a>
## 09.6 Acceptance criteria

**Table 09-2 — Library requirements**

| ID | Proposed requirement and acceptance test |
|---|---|
| R-09-01 | Project Files and Session Files MUST remain primary views; Input/Output/Resource and type filters do not replace them. |
| R-09-02 | A file shared by project and session associations MUST retain one logical identity and distinguish revisions. |
| R-09-03 | Live and historical references MUST open their stated versions; a missing historical artifact cannot fall back silently to the live path. |
| R-09-04 | Preview and import MUST validate access and safe handling; malformed files cannot trigger executable content. |
| R-09-05 | Removing an association MUST NOT delete bytes; deleting retained evidence requires an explicit policy-aware action and availability record. |
| R-09-06 | External access MUST be scoped and revocable; unavailable providers remain unavailable rather than suggesting a working integration. |

Figure A-06 illustrates navigation. Chapter 08 owns interpretation of evidence; Chapter 11 owns storage, containment, retention and export.

<a id="s-09-7"></a>
## 09.7 Shared contracts and multimodal evidence

A group-shared reference is a permission-checked FileAssociation exposed within a member's Project Files; it is not a third primary Library division. Session attachments remain Session Files, and Input/Output/Resource remain usage classifications. Shared API contracts retain producer project, immutable version/hash, consumer associations and availability. Membership changes invalidate access and cached previews.

Optional voice/video interaction produces consented SourceReferences: transcript or frame/time range, origin, capture time, model interpretation and retention choice. An interpretation is separate from the captured media. Screen images can contain secrets; scope the capture, redact exports and preserve an explicit omission marker. Audio/video collection is off unless the user invokes it and the selected integration supports it. A transcript cannot authorize a repository write merely by quoting “approved.”

**R-09-07 — Shared and multimodal provenance.** Shared contracts and media-derived context MUST retain source/version and access scope. Acceptance: revocation removes future retrieval, an uncertain transcript stays uncertain, and a visual claim links to the captured frame or declares its absence.

<!-- related-start -->
**Related sections:** [08. Execution Results and Evidence](../chapters/08-results-evidence.md#ch-08) · [11. Technical Integration and Trust](../chapters/11-integration-trust.md#ch-11) · [Appendix D. Conceptual Data Model](../appendices/D-conceptual-data-model.md#app-d) · [Appendix A. UI/UX Concept Gallery](../appendices/A-design-gallery.md#app-a)
<!-- related-end -->
