# Core Skills Drill: Descriptive Analytics 📊

هذا المشروع هو جزء من تدريب **AI.SPIRE**، ويهدف إلى إجراء تحليل إحصائي وصفي (Descriptive Analytics) لمجموعة بيانات مبيعات تجريبية باستخدام مكتبات **Pandas**, **Matplotlib**, و **Seaborn**.

## 🛠️ المهام المنجزة (Tasks)
تم تنفيذ العمليات التالية في سكربت `drill_eda.py`:
1. **الإحصاء الوصفي (Summary Statistics):** حساب المتوسط، الوسيط، الانحراف المعياري، والقيم الدنيا والعليا.
2. **توزيع البيانات (Data Distribution):** رسم Histograms مع KDE لكل من الكمية (`quantity`) وسعر الوحدة (`unit_price`).
3. **تحليل الارتباط (Correlation Analysis):** إنشاء خريطة حرارية (Heatmap) لفهم العلاقة بين المتغيرات الرقمية.

## 📁 مخرجات التحليل (Output Files)
تجد جميع النتائج في مجلد `output/`:
- `summary.csv`: يحتوي على الأرقام الإحصائية الأساسية.
- `distributions.png`: يوضح شكل توزيع البيانات وتكرارها.
- `correlation.png`: يوضح قوة العلاقة بين الأعمدة الرقمية.

## 🚀 طريقة التشغيل
لتشغيل التحليل وتحديث المخرجات، تأكد من تفعيل البيئة الافتراضية ثم شغل الأمر:
```bash
python drill_eda.py