# 🚀 Blog Application (FastAPI + Streamlit + Supabase)

## 📌 Overview

This is a full-stack blog application where users can perform CRUD operations on posts.

The project is built using:

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Database:** Supabase (PostgreSQL)
* **Deployment:** Render

---

## 🌐 Live Demo

* 🔗 Link: https://blogapp-fronted.onrender.com/

---

## 🏗️ Architecture

```
User → Streamlit Frontend → FastAPI Backend → Supabase Database
```

* Frontend sends HTTP requests
* Backend processes logic
* Data is stored in Supabase

---

## ⚙️ Features

* ✅ Create a post
* ✅ Read posts
* ✅ Update posts
* ✅ Delete posts
* ✅ REST API with FastAPI
* ✅ Interactive UI with Streamlit

---

## 🧪 API Endpoints

| Method | Endpoint    | Description |
| ------ | ----------- | ----------- |
| POST   | /posts/     | Create post |
| GET    | /posts/{id} | Get post    |
| PUT    | /posts/{id} | Update post |
| DELETE | /posts/{id} | Delete post |

---

## ⚠️ Important Notes

* Frontend does NOT directly access the database
* Backend handles all database operations
* Environment variables are used for secure configuration

---

## 🚀 Future Improvements

* 🔐 Add authentication (JWT)
* 👤 User-specific posts
* 🎨 Better UI

---

## 👨‍💻 Author

Jashandeep Kaur
