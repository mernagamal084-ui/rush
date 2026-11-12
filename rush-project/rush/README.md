# RUSH — Ride Your Own Chaos
- `index.html` : الموقع كامل (ملف واحد، الصور مدمجة). افتحه في المتصفح مباشرة (محتاج إنترنت لـ React/GSAP/الخطوط من CDN).
- `src/template.html` : الكود المصدري (React + GSAP). عدّل `PRODUCTS` و `CFG` في أول السكريبت (الأسماء/الأسعار بالجنيه/المواصفات/الألوان/الاتصال).
- `assets/` : صور الموتوسيكلات (r_* = زوايا CRIMSON KAPOW الشفافة، والباقي صور الأربع موتوسيكلات الأصلية).
- `build.py` : `python3 build.py` يعيد بناء index.html بعد أي تعديل.
- أسعار ومواصفات وبيانات التواصل كلها placeholders. الدفع/الطلبات/المخزون محتاجة backend (شوف صفحة Dev notes).
