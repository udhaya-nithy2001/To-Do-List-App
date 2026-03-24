# Django Todo App

A simple and clean Todo List web application built with Django.

## Features
- User Registration & Login
- Add, Delete Tasks
- Mark Tasks as Complete/Incomplete
- Search Tasks
- Logout

## Screenshots
> Login Page, Home Page, Add Task, Delete Task

## Tech Stack
- Python
- Django
- HTML/CSS
- SQLite

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/udhaya-nithy2001/To-Do-List-App.git
cd To-Do-List-App
```

### 2. Install Django
```bash
pip install django
```

### 3. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Start the server
```bash
python manage.py runserver
```

### 5. Open in browser
```
http://127.0.0.1:8000/
```

## Project Structure
```
Todo/
├── static/css/style.css
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   ├── add.html
│   └── delete.html
├── Todo/
│   ├── settings.py
│   └── urls.py
└── todoapp/
    ├── models.py
    ├── views.py
    └── migrations/
```

## Author
**udhaya-nithy2001**  
GitHub: https://github.com/udhaya-nithy2001
## 🔄 Updated Project Structure

db.sqlite3  README.md	 requirements.txt  templates  test2.txt  todoapp
manage.py   req_old.txt  static		   test.txt   Todo
