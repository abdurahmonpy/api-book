# Frontend Dasturchilar uchun API Qo'llanmasi (Kitoblar API) 📘

Ushbu hujjat frontend dasturchilar (React, Next.js, Vue, Flutter, mobil va veb ilovalar) uchun Kitoblar REST API bilan integratsiya qilish bo'yicha to'liq qo'llanmadir.

---

## 📌 Asosiy Ma'lumotlar

- **Mahalliy Base URL (Local):** `http://127.0.0.1:8000` yoki `http://localhost:8000`
- **Railway Base URL (Production):** `https://<sizning-loyihangiz>.up.railway.app`
- **Interaktiv Swagger UI:** `/api/docs/`
- **Redoc interfeysi:** `/api/redoc/`
- **OpenAPI 3 JSON sxemasi:** `/api/schema/`
- **Ruxsat (Auth):** Hozirda barcha endpointlar ochiq (`AllowAny`). Maxsus token talab qilinmaydi.
- **CORS:** Barcha domenlar uchun ruxsat berilgan (`Access-Control-Allow-Origin: *`).

---

## 🧩 TypeScript Interfeyslari (Types)

```typescript
// Kitob ob'ekti modeli
export interface IBook {
  id: number;
  title: string;
  slug: string;
  pdf: string | null;     // To'liq URL manzili (masalan: "http://.../media/books/pdfs/...")
  image: string | null;   // To'liq URL manzili (masalan: "http://.../media/books/images/...")
  created_at: string;     // ISO 8601 sana formati (masalan: "2026-10-29T14:11:00.128628+05:00")
}

// Yangi kitob qo'shish uchun payload
export interface ICreateBookPayload {
  title: string;
  pdf?: File | null;
  image?: File | null;
}
```

---

## 📋 Endpointlar Ro'yxati

| Metod | Endpoint | Tavsif | Content-Type |
|---|---|---|---|
| `GET` | `/api/books/` | Barcha kitoblar ro'yxatini olish | `application/json` |
| `POST` | `/api/books/` | Yangi kitob qo'shish | `multipart/form-data` |
| `GET` | `/api/books/:id/` | ID orqali bitta kitobni olish | `application/json` |
| `GET` | `/api/books/:slug/` | Slug orqali bitta kitobni olish (SEO uchun) | `application/json` |
| `PUT` | `/api/books/:id/` | Kitobni to'liq yangilash | `multipart/form-data` |
| `PATCH` | `/api/books/:id/` | Kitobning ayrim maydonlarini yangilash | `multipart/form-data` |
| `DELETE` | `/api/books/:id/` | Kitobni o'chirish | - |

---

## 🔍 Batafsil Endpointlar va Misollar

### 1. Barcha kitoblar ro'yxatini olish
- **URL:** `GET /api/books/`
- **Muvaffaqiyatli javob (`200 OK`):**
```json
[
  {
    "id": 3,
    "title": "Ufq",
    "slug": "ufq",
    "pdf": "http://127.0.0.1:8000/media/books/pdfs/sample_book.pdf",
    "image": "http://127.0.0.1:8000/media/books/images/sample_cover.jpg",
    "created_at": "2026-10-29T14:11:00.128628+05:00"
  },
  {
    "id": 2,
    "title": "Mehrobdan chayon",
    "slug": "mehrobdan-chayon",
    "pdf": null,
    "image": null,
    "created_at": "2026-10-29T14:11:00.123815+05:00"
  }
]
```

---

### 2. Bitta kitobni SLUG orqali olish (Tavsiya etiladi - Next.js / React Router uchun)
Sahifalararo o'tishda chiroyli va SEO ga qulay URL yaratish uchun juda qulay (masalan: `/books/otkan-kunlar`):
- **URL:** `GET /api/books/otkan-kunlar/`
- **Muvaffaqiyatli javob (`200 OK`):**
```json
{
  "id": 1,
  "title": "O'tkan kunlar",
  "slug": "otkan-kunlar",
  "pdf": null,
  "image": null,
  "created_at": "2026-10-29T14:11:00.116858+05:00"
}
```
- **Xatolik (`404 Not Found`):**
```json
{
  "detail": "Topilmadi."
}
```

---

### 3. Yangi kitob qo'shish (Fayl bilan birga)
Kitob muqova rasmi yoki PDF fayli bo'lsa, so'rov `multipart/form-data` formatida yuborilishi shart (`FormData`).
- **URL:** `POST /api/books/`
- **Headers:** `Content-Type: multipart/form-data`
- **Form-data maydonlari:**
  - `title` (matn, majburiy)
  - `image` (rasm fayli, ixtiyoriy)
  - `pdf` (PDF fayli, ixtiyoriy)

> [!NOTE]
> `slug` frontenddan yuborilishi shart emas. Backend `title` dan avtomatik generatsiya qiladi.

- **Muvaffaqiyatli javob (`201 Created`):**
```json
{
  "id": 4,
  "title": "Yulduzli tunlar",
  "slug": "yulduzli-tunlar",
  "pdf": "http://127.0.0.1:8000/media/books/pdfs/yulduzli_tunlar.pdf",
  "image": "http://127.0.0.1:8000/media/books/images/yulduzli_tunlar.jpg",
  "created_at": "2026-10-29T14:25:00.000000+05:00"
}
```

---

### 4. Kitobni o'chirish
- **URL:** `DELETE /api/books/:id/`
- **Muvaffaqiyatli javob (`204 No Content`):** Bo'sh javob qaytadi.

---

## 💻 Frontend Integratsiya Kod Misollari

### 1. `fetch` orqali kitoblarni yuklab olish (JavaScript / TypeScript):

```javascript
const BASE_URL = 'http://127.0.0.1:8000';

async function fetchBooks() {
  try {
    const response = await fetch(`${BASE_URL}/api/books/`);
    if (!response.ok) {
      throw new Error(`HTTP xatolik: ${response.status}`);
    }
    const books = await response.json();
    return books;
  } catch (error) {
    console.error("Kitoblarni yuklashda xatolik:", error);
    return [];
  }
}
```

---

### 2. `Axios` va `FormData` orqali yangi kitob va fayllarni yuklash:

```javascript
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000';

async function createBook(title, imageFile, pdfFile) {
  const formData = new FormData();
  formData.append('title', title);

  if (imageFile) {
    formData.append('image', imageFile);
  }
  if (pdfFile) {
    formData.append('pdf', pdfFile);
  }

  try {
    const response = await axios.post(`${BASE_URL}/api/books/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    console.error("Kitob qo'shishda xatolik:", error.response?.data || error.message);
    throw error;
  }
}
```

---

### 3. React / Next.js Hook misoli:

```tsx
import { useEffect, useState } from 'react';

export function useBooks() {
  const [books, setBooks] = useState<IBook[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/books/')
      .then((res) => {
        if (!res.ok) throw new Error("Serverdan xato javob keldi");
        return res.json();
      })
      .then((data) => {
        setBooks(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return { books, loading, error };
}
```

---

## 🖼 Fayllarni (Rasm va PDF) frontendda ko'rsatish:

Backend har bir rasm va PDF fayl uchun to'liq URL manzilini qaytaradi (masalan: `http://127.0.0.1:8000/media/books/images/...`).

```jsx
// Rasm ko'rsatish
<img 
  src={book.image || '/placeholder-book.png'} 
  alt={book.title} 
  className="w-48 h-64 object-cover rounded shadow"
/>

// PDF yuklab olish yoki ko'rish
{book.pdf ? (
  <a 
    href={book.pdf} 
    target="_blank" 
    rel="noopener noreferrer"
    className="btn btn-primary"
  >
    PDF-ni ochish
  </a>
) : (
  <span>PDF mavjud emas</span>
)}
```
