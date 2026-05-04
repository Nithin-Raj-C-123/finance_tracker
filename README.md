# 💰 Finance Tracker API

## 🚀 Overview

Finance Tracker API is a backend system built using **FastAPI** that allows users to manage financial records such as income and expenses.
It supports full CRUD operations, filtering, and advanced analytics like summaries and monthly insights.

The project demonstrates clean backend architecture, proper validation, and structured API design.

---

## ✨ Features & Advantages

### 🔹 Core Features

* Create, Read, Update, Delete (CRUD) financial transactions
* Filter transactions by type (income/expense) and category
* User management with roles (basic implementation)

### 📊 Analytics

* Total income calculation
* Total expense calculation
* Balance calculation
* Category-wise breakdown
* Monthly summary of transactions

### ⚙️ Advantages

* Clean and modular architecture
* Fast and efficient API using FastAPI
* Automatic API documentation (Swagger UI)
* Strong validation using Pydantic
* Easy to extend and maintain

---

## 🛠️ Tech Stack

### Backend Framework

* **FastAPI** – High-performance web framework for building APIs

### Database

* **SQLite** – Lightweight database for simplicity
* **SQLAlchemy** – ORM for database interaction

### Validation & Serialization

* **Pydantic** – Data validation and parsing

### Server

* **Uvicorn** – ASGI server for running FastAPI

### Language

* **Python 3.11+**

---

## ⚙️ Setup & Run Instructions


# 🚀 Setup & Run Instructions

Follow these steps to run the Finance Tracker API project on your local machine.

---

## 📌 1. Clone the Repository

```bash
git clone <your-repo-link>
cd finance_tracker-main
```

---

## 📌 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 📌 3. Activate Virtual Environment

### 👉 For Windows (PowerShell)

```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

### 👉 For Windows (CMD alternative)

```bash
venv\Scripts\activate.bat
```

---

## 📌 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📌 5. Install Required Packages (if missing)

```bash
pip install fastapi uvicorn
```

---

## 📌 6. Run the Server

```bash
python -m uvicorn app.main:app --reload
```

---

## 📌 7. Open in Browser

Once the server starts, open:

👉 http://127.0.0.1:8000

---

## 📌 8. API Documentation (Swagger UI)

👉 http://127.0.0.1:8000/docs

---

## ❗ Troubleshooting

### 🔹 Error: `uvicorn not recognized`

```bash
pip install uvicorn
```

### 🔹 Error: `No module named fastapi`

```bash
pip install fastapi
```

### 🔹 Error: `running scripts is disabled`

```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 🔹 Virtual environment not activating

Use CMD instead:

```bash
venv\Scripts\activate.bat
```

---

## ✅ You're Done!

Your FastAPI server should now be running successfully 🎉


### 🔹 1. Clone the repository

```bash
git clone <your-repo-link>
cd finance_tracker
```

---

### 🔹 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 3. Run the server

```bash
uvicorn app.main:app --reload
```

---

### 🔹 4. Open API Docs

👉 http://127.0.0.1:8000/docs

---

## 🧪 API Usage (Step-by-Step)

---

### ✅ STEP 1: Create User

Open: **POST /users/**

Click **Try it out**

```json
{
  "name": "Nithin",
  "role": "admin"
}
```

Click **Execute**

---

### ✅ STEP 2: Add Transactions (One by One)

Open: **POST /transactions/**

#### ➤ First:

```json
{
  "amount": 5000,
  "type": "income",
  "category": "salary",
  "notes": "monthly salary"
 "date":"2026-04-01T10:00:00"

}
```

#### ➤ Second:

```json
{
  "amount": 1000,
  "type": "expense",
  "category": "food",
  "notes": "groceries"
    "date": "2026-04-02T13:30:00"

}
```

#### ➤ Third:

```json
{
  "amount": 2000,
  "type": "expense",
  "category": "rent",
  "notes": "house rent"
    "date": "2026-04-03T09:00:00"

}
```

---

### ✅ STEP 3: View All Transactions

Open: **GET /transactions/**
Click **Execute**

---

### ✅ STEP 4: Filtering

Open: **GET /transactions/**

* Only income:

```
type = income
```

* Only food:

```
category = food
```

---

### ✅ STEP 5: Update Transaction

Open: **PUT /transactions/{txn_id}**

```json
{
  "amount": 6000,
  "type": "income",
  "category": "salary",
  "notes": "updated salary"
}
```

---

### ✅ STEP 6: Delete Transaction

Open: **DELETE /transactions/{txn_id}**

Example:

```
txn_id = 2
```

---

### 📊 STEP 7: Analytics

#### ➤ Summary

GET `/analytics/summary`

#### ➤ Category

GET `/analytics/category`

#### ➤ Monthly

GET `/analytics/monthly`

---

### 🟣 STEP 8: Root Check

GET `/`

```json
{
  "message": "Finance Tracker API is running 🚀"
}
```

---

## 🚧 Potential Improvements

* Add authentication (JWT-based login system)
* Implement role-based access control (RBAC)
* Add pagination for large datasets
* Improve error handling and logging
* Add unit and integration tests
* Export data to CSV/JSON
* Deploy using Docker or cloud platforms (AWS, Render, etc.)

---

## 🎯 Conclusion

This project demonstrates strong backend fundamentals including API design, database handling, validation, and analytics processing.
It is designed to be scalable, clean, and easy to extend for real-world applications.

---
