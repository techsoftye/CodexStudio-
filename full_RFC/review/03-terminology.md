> **Historical review record (supplied with RFC v1.1).** This records checks performed for the author’s earlier archive. The current repository packaging checks are recorded separately in [publication validation](../../publication/VALIDATION.json). Brand spelling and navigation may have been normalized for this publication package.

# Terminology and editorial conventions / المصطلحات والاتفاقات التحريرية

English is the reference language. Arabic is a complete equivalent translation. Stable English UI tokens and identifiers are retained where needed to prevent state ambiguity. Proposed requirements use MUST = يجب, SHOULD = ينبغي, MAY = يجوز.

| English | العربية | Meaning constraint / حد المعنى |
|---|---|---|
| Project | المشروع | Persistent organizational/access boundary / حد التنظيم والوصول المستمر |
| Conversation | المحادثة | Discussion record; runtime thread mapping is explicit / سجل نقاش بربط صريح ببيئة التنفيذ |
| Task | المهمة | Intended work / العمل المطلوب |
| Task state | حالة المهمة | Todo / Active / Review / Done / Deferred |
| Execution Attempt | محاولة التنفيذ | Runtime activity, may include several turns / نشاط قد يشمل عدة turns |
| Result | النتيجة | Attributed summary and evidence links / ملخص منسوب وروابط أدلة |
| Result outcome | حصيلة النتيجة | Completed / Partial / Failed, independent of review |
| Check | الفحص | Passed / Failed / Not Run / Inconclusive |
| Review | المراجعة | Judgment on an exact version / حكم على إصدار محدد |
| Acceptance | قبول النتيجة | Does not grant operation permission / لا يمنح إذن عملية |
| Decision approval | اعتماد القرار | Choice and rationale, not execution consent / خيار ومبرر لا إذن تنفيذ |
| Operation authorization | تفويض العملية | Subject to runtime and managed policy / تابع لضوابط البيئة والإدارة |
| Rule | القاعدة | Applicable instruction from authoritative source / توجيه من مصدر مرجعي |
| Provenance | المنشأ / معلومات المصدر | Source, capture, author and version / المصدر والالتقاط والمؤلف والإصدار |
| Source of truth | المصدر المرجعي للحقيقة | Declared ownership, not model confidence / ملكية معلنة لا ثقة النموذج |
| Context manifest | بيان السياق | Immutable supplied-source inventory / جرد ثابت للمصادر المقدمة |
| Context resolver | محلل السياق | Selects relevant, authorized, current context / يختار السياق المنطبق والمخول والحالي |
| Snapshot | اللقطة | Identified historical state / حالة تاريخية محددة |
| Drift | تغير عن الحالة المسجلة | Version mismatch, not automatic invalidity / اختلاف إصدار لا بطلان آلي |
| Superseded | مستبدل | Retained history with successor / تاريخ محفوظ مع خلف |
| Deferred | مؤجل | Planning choice, not process interruption / قرار تخطيط لا مقاطعة عملية |
| Interrupted | متوقف بالمقاطعة | Confirmed interruption / مقاطعة مؤكدة |
| Unknown | غير معلوم | Runtime observation uncertain / رصد البيئة غير مؤكد |
| Idempotent | غير مكرر الأثر | Same logical request cannot repeat local mutation / الطلب المنطقي لا يكرر التعديل المحلي |
| Optimistic concurrency | التحكم المتفائل بالتزامن | Expected-version check / فحص الإصدار المتوقع |
| Tombstone | سجل دال على الإزالة | Metadata explaining unavailability / بيانات تفسر عدم الإتاحة |
| Worktree | نسخة عمل Git معزولة / Worktree | Does not prove semantic integration / لا تثبت صحة الدمج |
| Runtime | بيئة التنفيذ | Supported Codex execution surface / سطح تنفيذ Codex المدعوم |
| Harness | بيئة تشغيل الوكيل | Reused, not rebuilt / يعاد استخدامها |
| Project Files | ملفات المشروع | Primary Library scope / نطاق رئيسي للمكتبة |
| Session Files | ملفات الجلسة | Attachments/outputs, not raw session logs / مرفقات ومخرجات لا سجلات خام |
| Input / Output / Resource | مدخل / مخرج / مورد | Library usage classifications / تصنيفات استخدام داخل المكتبة |
| Existing | قائم | Officially documented at check date / موثق رسميًا بتاريخ التحقق |
| Proposed | مقترح | RFC design / تصميم الوثيقة |
| Requires Validation | يتطلب تحققًا | Not established by this review / لم تثبته هذه المراجعة |
| MVP | النسخة الأولية القابلة للتقييم | Complete narrow workflow / مسار محدود متكامل |

Numbering uses Latin digits in both editions. Chapter and appendix filenames match between EN/AR. Figure A-01–A-06 are inherited PNGs; Figure 11-1 and D-1 are textual diagrams. Tables use chapter-qualified numbers. No separate Arabic image was generated. Diagram entity names and all sample IDs are intentionally stable.

## Version 1.1 extension terminology

| English | العربية | Meaning / المعنى |
|---|---|---|
| Project Group | مجموعة مشاريع | Optional product umbrella / مظلة اختيارية للمنتج |
| Environment Profile | ملف تعريف البيئة | Versioned execution target specification / وصف هدف تنفيذ ذي إصدار |
| Change Set | حزمة تغيير | Coordination across project-local tasks / تنسيق مهام محلية للمشاريع |
| Integration Manifest | بيان التكامل | Exact combined revision/evidence set / مجموعة إصدارات وأدلة مدمجة دقيقة |
| Contract Reference | مرجع العقد | Authoritative interface revision / إصدار واجهة مرجعي |
| Principal | هوية مخولة | Authenticated human/service identity / هوية إنسان أو خدمة موثقة |
| Agent Instance | نسخة تشغيل الوكيل | Attributable execution actor / فاعل تنفيذ معلوم الإسناد |
| Role Binding | ربط الدور | Scoped role assigned to a principal / دور محدد مرتبط بهوية |
| Work Assignment | إسناد العمل | Responsibility, not access / مسؤولية لا وصول |
| Delegation Grant | منحة تفويض | Narrow, expiring execution authority / سلطة تنفيذ محدودة ومنتهية |
| Hybrid Team | فريق هجين | Humans and attributable agents / بشر ووكلاء معلومة هوياتهم |
| Multimodal provenance | منشأ متعدد الوسائط | Traceable audio/visual source / مصدر صوتي أو مرئي قابل للتتبع |
