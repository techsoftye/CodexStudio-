# رفع حزمة Codex Studio إلى المستودع

**المستودع:** https://github.com/techsoftye/CodexStudio-  
**الفرع:** `main`  
**الاسم المعتمد:** TechSoft

## 1. فك الضغط

الحزمة تحتوي على مجلد واحد اسمه `CodexStudio-`. ضعه مثلًا هنا:

```text
D:\techsoft\2026\studies_and_resarches\Research\Codex\CodexStudio-
```

داخل هذا المجلد يجب أن ترى `README.md` و`index.html` و`full_RFC` و`article`. لا ترفع ملف ZIP نفسه، ولا تضع مجلد الأرشيف القديم كاملًا داخل المستودع.

## 2. الرفع من PowerShell

افتح PowerShell داخل مجلد الحزمة، ثم نفذ الأوامر التالية **لنسخة الحزمة الجديدة غير المهيأة سابقًا بـGit**:

```powershell
Set-Location "D:\techsoft\2026\studies_and_resarches\Research\Codex\CodexStudio-"
git init -b main
git add .
git commit -m "Publish Codex Studio proposal and bilingual RFC draft"
git remote add origin https://github.com/techsoftye/CodexStudio-.git
git push -u origin main
```

توقف عند أي خطأ ولا تستمر إلى الأمر التالي. لا تستخدم `--force`. استخدم `git add .` لإضافة الصور والصفحات وكل ملفات الوثيقة؛ `git add README.md` وحده لا يرفعها. لا تستخدم أمر `echo` لإنشاء README؛ الملف جاهز بالفعل.

هناك أيضًا سكربت اختياري يتحقق من المسار والهوية والـremote ويتوقف عند الأخطاء:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\Publish.ps1
```

هذا السماح يخص عملية PowerShell الحالية فقط. السكربت يسألك للتأكيد قبل الإرسال، ولا يجبر الرفع ولا يغير صلاحية المستودع ولا يُفعّل Pages.

إذا ظهر `remote origin already exists` فافحص:

```powershell
git remote -v
```

إن كان يشير للمستودع نفسه، لا تضفه ثانية ونفذ `git push -u origin main`. إن كان يشير لمستودع آخر، تحقق من أنك داخل المجلد الصحيح قبل تغييره.

إذا طلب Git اسمًا وبريدًا للـcommit، اضبط هويتك الحقيقية أو بريد GitHub noreply الخاص بك؛ لا تستخدم بريدًا مفترضًا من هذه الحزمة. بيانات اعتماد GitHub لا تُحفظ في الملفات.

## 3. تفعيل صفحة HTML والصور

بعد نجاح الرفع افتح:

https://github.com/techsoftye/CodexStudio-/settings/pages

اختر:

```text
Source: Deploy from a branch
Branch: main
Folder: /(root)
Save
```

انتظر نجاح النشر في صفحة Pages/Actions. رابط صفحة المقال المتوقع بعد ذلك:

https://techsoftye.github.io/CodexStudio-/

العربية:

https://techsoftye.github.io/CodexStudio-/ar.html

RFC الإنجليزي:

https://techsoftye.github.io/CodexStudio-/full_RFC/EN/index.html

RFC العربي:

https://techsoftye.github.io/CodexStudio-/full_RFC/AR/index.html

ملف `.nojekyll` موجود في الحزمة. لا يحتاج الموقع إلى npm أو خدمة خلفية أو Workflow مخصص. لا يكفي فتح `index.html` داخل واجهة ملفات GitHub لعرضه كموقع؛ القراءة المنسقة العامة تتم عبر Pages. أما ملفات Markdown فتُقرأ مباشرة في المستودع بعد الرفع.

## 4. تعديل خاتمة موضوع المنتدى

انسخ نص `publication/CLOSING-PARAGRAPH-EN.md` مكان الفقرة التي تبدأ بـ `I plan to expand the concept` **بعد نجاح الرفع وفتح رابط الوثيقة للتأكد منه**.

الخاتمة تشير إلى RFC موجود فعليًا ضمن الحزمة، لكنها تصفه بأنه مسودة للمراجعة؛ لا تقول إنه منتج منفذ أو معتمد.

إذا كانت صورك موجودة في محرر المنتدى بالفعل، أبقها كما هي. لا تحذف الصور لإعادة بناء المقال. ملف `publication/COMMUNITY-POST-EN.md` نسخة احتياطية كاملة بتسلسل المقال نفسه وروابط صور GitHub مباشرة، وتصبح تلك الروابط متاحة بعد الـpush دون اشتراط Pages. قد تطبق المنصة قيودًا على الصور الخارجية؛ عندها استخدم رفع المنتدى الأصلي.

## 5. فحص أخير قبل نشر الموضوع

افتح المقال بالإنجليزية، ثم إحدى الصور بحجمها الأصلي، ثم RFC الإنجليزي والعربي. افحص رابط الخاتمة من نافذة خاصة للتأكد من أنه متاح للجمهور. بعد ذلك انشر الموضوع.

المستودع يضم مواد للمشاركة العامة. تقارير مصادر RFC التاريخية محفوظة كشواهد وموضحة الحالة؛ المقال المعتمد هو `article/Article-EN.md`.

## مصدر تعليمات Pages

[وثائق GitHub الرسمية](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
