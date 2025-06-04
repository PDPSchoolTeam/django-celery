# 🚀 Celery nima va u nega kerak?

## ✨ Asosiy sabablari

Dasturchilar quyidagi ikki sabab tufayli Celery’dan foydalanishni boshlashadi:

1. 🧠 Og‘ir yoki uzoq davom etadigan ishlarni (masalan, email yuborish, rasmni qayta ishlash) asosiy ilovadan ajratib, alohida jarayonda bajarish.
2. ⏰ Belgilangan vaqtda yoki davriy ravishda avtomatik ishlarni bajarish (masalan, har kuni soat 9:00 da hisobot yuborish).

Celery o‘zini quyidagicha ta’riflaydi:

> “Real vaqtli ishlov berishga yo‘naltirilgan vazifalar navbati, shu bilan birga rejalashtirishni ham qo‘llab-quvvatlaydi.”

---

## ⚙️ Celery qanday ishlaydi?

### 🔧 `Celery Worker`
Celery ishchi jarayonlari (`workers`) — bu sizning asosiy Django ilovangizdan mustaqil ishlaydigan fon jarayonlaridir. Ular og‘ir vazifalarni bajaradi va ilovani sekinlashtirmaydi.

### 🕒 `Celery Beat`
Agar sizga vazifalarni rejalashtirish kerak bo‘lsa (masalan, har 5 daqiqada bajariladigan task), `Celery Beat` yordamida vaqt asosida ishlarni belgilashingiz mumkin.

> ℹ️ Celery Beat — bu faqat rejalashtiruvchi. Haqiqiy ishni yana worker bajaradi.

---

## 🛠 Django ilovasida Celery nima uchun kerak?

Quyidagi holatlarda Celery ilovangizga katta foyda keltiradi:

- 📧 **Email yuborish** – Tasdiqlash yoki tiklash email’lari sekin yuborilishi mumkin. Celery bilan bu ishlar fonda bajariladi.
- 🖼 **Rasmni qayta ishlash** – Avatarning o‘lchamini o‘zgartirish yoki rasmga filtr qo‘shish.
- 📝 **Matnni tahlil qilish** – So‘kinish so‘zlarini aniqlash, tarjima qilish, spam filtrlari.
- 🌐 **API chaqiruvlar** – Uchinchi tomon xizmatlariga so‘rov yuborish (masalan, Telegram, Stripe).
- 📊 **Ma’lumot tahlili** – Katta dataset ustida hisob-kitoblar.
- 🧠 **ML/AI modellari** – Model natijalarini hisoblashda foydalanuvchini kutdirmaslik.
- 📄 **Hisobot generatsiyasi** – PDF yoki Excel fayl yaratish fonda amalga oshiriladi.

---
