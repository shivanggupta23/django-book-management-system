# Django Book Management System

A beginner-friendly Django web application for managing books. This project was built from scratch to understand the fundamentals of Django, especially the request/response cycle, templates, URL routing, Django ORM, and CRUD operations.

## Features

- Home page
- View all books
- View individual book details
- Add a new book
- Edit an existing book
- Delete a book with confirmation
- CSRF protection for POST forms
- Django ORM for database operations
- Server-side page rendering with Django templates

## Tech Stack

- Python
- Django
- SQLite
- HTML
- Django Templates

## Project Structure

```text
book_workspace/
│
├── manage.py
│
├── bookproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── books/
    ├── migrations/
    ├── templates/
    │   └── books/
    │       ├── home.html
    │       ├── book_list.html
    │       ├── book_detail.html
    │       ├── add_book.html
    │       ├── edit_book.html
    │       └── delete_book.html
    ├── models.py
    ├── views.py
    └── ...
```

## CRUD Operations

### Create

Books are created using a normal HTML form. Submitted values are read using `request.POST` and saved using the Django ORM.

```python
Book.objects.create(
    title=title,
    author=author,
    price=price,
    published_date=published_date
)
```

### Read

All books:

```python
Book.objects.all()
```

A single book:

```python
get_object_or_404(Book, id=id)
```

### Update

The existing book is retrieved, its fields are changed, and `save()` updates the database row.

```python
book = get_object_or_404(Book, id=id)

book.title = request.POST["title"]
book.author = request.POST["author"]
book.price = request.POST["price"]
book.published_date = request.POST["published_date"]

book.save()
```

### Delete

The existing book is retrieved and deleted after a POST confirmation.

```python
book = get_object_or_404(Book, id=id)

if request.method == "POST":
    book.delete()
```

## Request Flow

The project demonstrates the basic Django flow:

```text
HTML Form
    ↓
HTTP Request
    ↓
Django URL
    ↓
View
    ↓
request.POST / Django ORM
    ↓
Database
    ↓
Context
    ↓
Template
    ↓
HTTP Response
```

## Why This Project Uses Plain HTML Forms

This version intentionally does **not** depend on `ModelForm` for CRUD operations.

The goal is to understand what Django is doing internally:

```text
HTML input
    ↓
request.POST
    ↓
Python variables
    ↓
Django ORM
    ↓
Database
```

ModelForms can be introduced later after understanding this fundamental flow.

## Setup and Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd book_workspace
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows Command Prompt:

```bash
venv\Scripts\activate
```

PowerShell:

```bash
venv\Scripts\Activate.ps1
```

### 4. Install Django

```bash
pip install django
```

If the project contains a `requirements.txt` file, you can instead run:

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Main URLs

| URL | Purpose |
|---|---|
| `/` | Home page |
| `/books/` | List all books |
| `/books/add/` | Add a book |
| `/books/<id>/` | View book details |
| `/books/<id>/edit/` | Edit a book |
| `/books/<id>/delete/` | Delete a book |

## Learning Objectives

This project was created to practice:

- Django project vs Django app
- URL routing
- Views
- Templates
- Template context
- GET and POST requests
- HTML forms
- CSRF tokens
- Django models
- Django ORM
- Database CRUD operations
- `get_object_or_404()`
- Redirects
- Dynamic URLs
- Separating application code into a Django app

## Future Improvements

Possible next steps:

- Add Django ModelForms
- Add form validation
- Add user authentication
- Associate books with users
- Add search and filtering
- Add pagination
- Add styling with CSS/Bootstrap
- Add automated tests
- Convert the project into a REST API using Django REST Framework

##Project Link- https://django-book-management-system.onrender.com/

## Author

Built as a Django learning project to develop strong backend fundamentals and prepare for Django/Python backend interviews.
