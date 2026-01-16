# FastAPI JWT Authentication & CRUD Master

Project ini dibuat sebagai **technical test backend (Python/FastAPI)**.

Fitur utama:

* JWT Authentication (Login)
* Protected API (Bearer Token)
* CRUD Master Data
* Swagger UI

---

## 🚀 Tech Stack

* Python 3.10+
* FastAPI
* Uvicorn
* JWT (python-jose)
* Pydantic

---

## 📂 Struktur Project

```
app/
├── main.py
├── auth/
│   └── auth.py
├── master/
│   └── master.py
└── models/
    └── schemas.py
```

---

## ⚙️ Instalasi & Menjalankan Aplikasi

### 1️⃣ Clone Repository

```bash
git clone https://github.com/nillakusuma/testpy-ptcbn-2022.git
cd testpy-ptcbn-2022
```

### 2️⃣ Buat Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependency

```bash
pip install -r requirements.txt
```

### 4️⃣ Jalankan Server

```bash
uvicorn app.main:app --reload
```

Server berjalan di:

```
http://127.0.0.1:8000
```

---

## 🔐 Authentication

### Login

Endpoint:

```
POST /api/auth/login
```

Credential demo:

```json
{
  "username": "nilla",
  "password": "CBN123!"
}
```

Response:

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

Gunakan token tersebut pada Swagger **Authorize**.

---

## 📦 CRUD Master

Semua endpoint master **memerlukan Authorization**.

### Create Master

```
POST /api/master/
```

```json
{
  "name": "test data",
  "description": "untuk HRD"
}
```

### Get All Master

```
GET /api/master/
```

### Get Master By ID

```
GET /api/master/{id}
```

### Update Master

```
PUT /api/master/{id}
```

### Delete Master

```
DELETE /api/master/{id}
```

---

## 📖 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## ✅ Status Project

* Authentication JWT: ✅
* Protected API: ✅
* CRUD berjalan: ✅
* Swagger UI: ✅

Project ini siap digunakan sebagai **submission technical test**.

---

## 👤 Author

Nilla Kusuma Dewi
