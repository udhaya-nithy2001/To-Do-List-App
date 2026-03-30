# 🚀 Django Todo App with REST API

## 📌 Overview

A full-stack task management application built using **Django** and **Django REST Framework (DRF)**.
This app allows users to manage tasks with authentication, search, soft delete, priority, and due date features.

---

## 🔥 Features

* User Authentication (Register, Login, Logout)
* CRUD Operations (Create, Read, Update, Delete)
* Soft Delete System (no permanent data loss)
* Task Priority (Low / Medium / High)
* Due Date support
* Mark tasks as complete/incomplete
* Search functionality
* REST API using Django REST Framework (DRF)
* Secure user-based task handling

---

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework (DRF)
* SQLite
* HTML, CSS

---

## 📡 API Endpoints

| Method | Endpoint         | Description      |
|--------|----------------|------------------|
| GET    | /api/tasks/      | Get all tasks    |
| POST   | /api/tasks/      | Create task      |
| GET    | /api/tasks/{id}/ | Get single task  |
| PUT    | /api/tasks/{id}/ | Update task      |
| PATCH  | /api/tasks/{id}/ | Partial update   |
| DELETE | /api/tasks/{id}/ | Soft delete task |

---
## ⚙️ Setup Instructions

```bash
git clone https://github.com/udhaya-nithy2001/To-Do-List-App.git
cd To-Do-List-App
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🔐 Authentication

* Django session-based authentication
* API protected using `IsAuthenticated`

---

## 🚀 Future Improvements

* JWT Authentication
* Deployment (Render)
* React frontend

---

## 👨‍💻 Author

**Udhayanithy S**
GitHub: https://github.com/udhaya-nithy2001

## 🔄 Updated Project Structure

db.sqlite3  README.md	 requirements.txt  templates  test2.txt  todoapp
manage.py   req_old.txt  static		   test.txt   Todo
