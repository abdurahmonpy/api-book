# Kitoblar REST API (Book API) 📚

Django va Django REST Framework asosida yaratilgan zamonaviy kitoblar API xizmati. Ushbu loyihada kitoblar ro'yxati, PDF fayllar, muqova rasmlari, avtomatik `slug`, OpenAPI 3 / Swagger interaktiv hujjatlari, Jazzmin zamonaviy boshqaruv paneli va Railway serveriga deploy qilish sozlamalari mavjud.

> 📖 **Frontend dasturchilar uchun to'liq qo'llanma:** [FRONTEND_DOCS.md](FRONTEND_DOCS.md)

---

## 🚀 Imkoniyatlar

- **Kitoblar API:**
  - Barcha kitoblar ro'yxatini olish (`GET /api/books/`)
  - Yangi kitob qo'shish (`POST /api/books/`)
  - Bitta kitobni `ID` orqali ko'rish, o'zgartirish, o'chirish (`GET, PUT, PATCH, DELETE /api/books/<id>/`)
  - Bitta kitobni `SLUG` orqali ko'rish (`GET /api/books/<slug>/`)
- **Fayllar:**
  - Kitob muqovasi rasmi (`image`)
  - Kitob elektron PDF fayli (`pdf`)
- **Dokumentatsiya:**
  - **Frontendchilar uchun yo'riqnoma:** [FRONTEND_DOCS.md](FRONTEND_DOCS.md)
  - **Swagger UI:** `/api/docs/` yoki `/api/swagger/`
  - **Redoc:** `/api/redoc/`
  - **OpenAPI 3.0 Sxemasi:** `/api/schema/`
- **Admin Panel:**
  - **Django Jazzmin** zamonaviy boshqaruv paneli (`/admin/`)
- **Deploy:**
  - Railway serveriga to'liq tayyor (`Procfile`, `railway.json`, `WhiteNoise`, PostgreSQL / SQLite integratsiyasi)

---

## 🛠 O'rnatish va Mahalliy Ishga Tushirish

1. **Repozitoriyani klonlash:**
   ```bash
   git clone https://github.com/abdurahmonpy/api-book.git
   cd api-book
   ```

2. **Virtual muhitni yaratish va faollashtirish:**
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   ```

3. **Kutubxonalarni o'rnatish:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Migratsiyalarni qo'llash:**
   ```bash
   python manage.py migrate
   ```

5. **Serverni ishga tushirish:**
   ```bash
   python manage.py runserver
   ```

Brauzerda:
- **Swagger Dokumentatsiyasi:** [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- **Kitoblar API:** [http://127.0.0.1:8000/api/books/](http://127.0.0.1:8000/api/books/)
- **Admin panel (Jazzmin):** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🌐 Railway Serveriga Deploy Qilish

1. Ushbu repozitoriyani GitHub'ga yuklang.
2. [railway.app](https://railway.app) ga kiring va yangi loyiha yarating (**Deploy from GitHub repo**).
3. `api-book` repozitoriyasini tanlang.
4. Xohishingizga ko'ra **PostgreSQL** qo'shing (Railway avtomatik `DATABASE_URL` parametrini ulaydi).
5. Loyiha `Procfile` va `railway.json` orqali avtomatik tarzda build qilinadi va ishga tushadi!
