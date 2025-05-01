# 🕒 Telegram Vaqt Boti 🕒

## 📝 Bot haqida

Bu Telegram bot sizning profilingizni avtomatik ravishda yangilab turadi va hozirgi vaqtni ko'rsatadi. Bot doimo onlayn holatda bo'ladi va spam holatiga tushmaslik uchun maxsus himoya bilan ta'minlangan.

## ✨ Asosiy xususiyatlar

- ⌚️ Profilning "about" qismida aniq vaqtni ko'rsatadi
- 🛡️ Spam holatiga tushmaslik uchun himoya
- 🟢 Doimo onlayn holat
- 📊 `/info` buyrug'i orqali bot holati haqida ma'lumot olish

## 🔧 Talablar

- 🐍 Python 3.7+
- 📦 Telethon kutubxonasi
- 🌐 Telegram API ma'lumotlari (API ID va API hash)
- 🕰️ pytz kutubxonasi (vaqt mintaqalari uchun)
- ⏳ asyncio kutubxonasi

## 📥 O'rnatish

1. Kerakli kutubxonalarni o'rnating:

```
pip install telethon pytz asyncio
```

2. Telegram API ma'lumotlarini oling:
   - [my.telegram.org](https://my.telegram.org) saytiga kiring
   - "API development tools" bo'limini tanlang
   - Yangi dastur yarating va API ID hamda API hash ni oling

3. Skriptni yuklab oling va API ma'lumotlarini kiriting:
   - `api_id` va `api_hash` qiymatlarini o'zgartiring
   - `userid` o'rniga kerakli foydalanuvchi ID sini kiriting

## 🚀 Ishga tushirish

```
python bot_nomi.py
```

## 💡 Qo'llanma

- Bot ishga tushgandan so'ng, profilingizning "about" qismida joriy vaqt ko'rsatiladi
- Vaqt har 5 daqiqada yangilanadi
- Bot holatini tekshirish uchun `/info` buyrug'ini yuboring

## ⚙️ Sozlamalar

- Vaqt mintaqasini o'zgartirish uchun `pytz.timezone('Asia/Tashkent')` qismini o'zgartiring
- Yangilanish vaqtini o'zgartirish uchun `await asyncio.sleep(300)` qismidagi 300 sonini o'zgartiring (sekundlarda)

## 🔔 Muhim eslatmalar

- Bot ishlashi uchun kompyuter yoki server doimo yoqiq bo'lishi kerak
- API ma'lumotlarini hech kimga bermang
- Telegram hisobingizni himoya qilish uchun ikki bosqichli autentifikatsiyani yoqing

## 🆘 Yordam

Agar muammolarga duch kelsangiz, quyidagi narsalarni tekshiring:
- Internet aloqasi mavjudligi
- API ma'lumotlarining to'g'riligi
- Barcha kutubxonalar to'g'ri o'rnatilganligi

## 🔄 Yangilanishlar

Bot yangi funksiyalar bilan doimiy ravishda yangilanib turadi. Yangilanishlardan xabardor bo'lish uchun repozitoriyani kuzatib boring!

---

⭐️ Agar bot sizga foydali bo'lsa, yulduzcha qo'yishni unutmang! ⭐️
```

<Actions>
  <Action name="Botni ishga tushirish" description="Botni o'rnatish va ishga tushirish" />
  <Action name="Vaqt mintaqasini o'zgartirish" description="Boshqa vaqt mintaqasini tanlash" />
  <Action name="Yangilanish vaqtini o'zgartirish" description="Vaqt yangilanish oralig'ini o'zgartirish" />
  <Action name="Qo'shimcha funksiyalar qo'shish" description="Botga yangi funksiyalar qo'shish" />
</Actions>







```

