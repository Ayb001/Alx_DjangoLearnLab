# Alx_DjangoLearnLab

Django learning projects from the ALX curriculum.

## Project Structure

```
Alx_DjangoLearnLab/
└── Introduction_to_Django/
    ├── LibraryProject/          # Django project
    │   ├── bookshelf/           # Book management app
    │   └── manage.py
    └── CRUD_operations.md       # Database operations
```

## Features

- **Book Model**: Title, author, publication year
- **Django Admin**: Custom admin interface
- **CRUD Operations**: Create, read, update, delete books
- **Database**: SQLite with Django ORM

## Quick Start

```bash
# Clone and setup
git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/Introduction_to_Django

# Install dependencies
python3 -m venv django_env
source django_env/bin/activate
pip3 install django

# Run project
cd LibraryProject
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

**Access:** 
- App: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Technologies

Python 3, Django 4, SQLite, Django Admin

---

*ALX Software Engineering Program - Django Learning Project*