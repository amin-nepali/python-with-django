# Python with Django Training in Nepal — Complete Notes Until Day 6

This note is based on the course advertised on Code IT: Python Django Training in Nepal – REST API, ORM & Full Stack.

Course focus:
- Python + Django
- Django MVT architecture
- ORM and database work
- Authentication and user management
- REST API development
- Full-stack web app building
- Real project + deployment
- Internship opportunity

Course summary from the page:
- Duration: around 1.5 months
- Format: live online classes and classroom sessions in Dharan
- Time: 8:00 PM to 9:30 PM (Google Meet)
- Audience: beginners to intermediate learners, especially those who know Git and basic HTML/CSS/Python
- Outcome: build real, production-style web applications and get internship support
- Includes: lifetime recorded video access, certificate, internship

Important idea: this is not just a Python course. It is a full-stack web development path where Python becomes the backend engine and Django handles web apps, database logic, user login, APIs, and much more.

---

## 1) What this course is trying to teach

The training page promises that after this course you will be able to:
- Understand the full web stack
- Build complete web applications using Django
- Use Django MVT (Model-View-Template)
- Work with databases using ORM
- Make login/signup and authentication systems
- Build REST APIs
- Create admin panels and manage data
- Deploy projects to the web
- Build a real-world final project

This means the course is designed to help you go from beginner to job-ready backend/full-stack developer.

---

## 2) Foundation before Django

Before Django, you need a strong base. The course description clearly says the training starts with HTML, CSS, Tailwind CSS, JavaScript, and Python fundamentals.

### HTML
HTML gives structure to a webpage.
Example:
```html
<!DOCTYPE html>
<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h1>Hello, Django!</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
```

HTML teaches:
- headings
- paragraphs
- links
- forms
- buttons
- layout structure

### CSS
CSS gives style.
```css
body {
  background-color: #f3f3f3;
  font-family: Arial, sans-serif;
}

h1 {
  color: #333;
}
```

CSS teaches:
- colors
- spacing
- layout
- responsive design
- cards, navbars, forms, buttons

### Tailwind CSS
Tailwind is a utility-first CSS framework. Instead of writing a lot of custom CSS, you use classes like:
```html
<div class="bg-blue-500 text-white p-4 rounded-lg">Hello</div>
```

Why it matters:
- faster UI development
- clean code
- modern design workflow

### JavaScript / ES6+
JavaScript makes pages interactive.
```javascript
const name = 'Alice';
console.log(`Hello ${name}`);
```

You learn:
- variables
- functions
- arrays / objects
- DOM manipulation
- events
- form validation

This foundation matters because Django handles backend logic, while HTML/CSS/JS handle frontend experience.

---

## 3) Python fundamentals (core part before Django)

The page mentions Python topics such as:
- data structures
- functions
- OOP (inheritance and polymorphism)
- decorators
- generators
- NumPy
- Pandas

### Why Python is important for Django
Django is a Python framework. You write Python code for:
- handling requests
- connecting to database
- validating data
- creating business logic
- generating HTML templates or JSON responses

### Python basics to know
```python
# Variables
name = "Rahul"
age = 22

# Data structures
numbers = [1, 2, 3, 4]
student = {"name": "Amit", "age": 20}

# Function
def add(a, b):
    return a + b

print(add(3, 5))
```

### Object-oriented programming (OOP)
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

p = Person("Sita")
print(p.greet())
```

OOP concepts in Django matter because apps often use classes, models, and reusable logic.

### Why decorators and generators matter
Decorators modify function behavior.
```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def hello():
    print("Hello")

hello()
```

Generators produce values lazily.
```python
def numbers():
    for i in range(5):
        yield i

for n in numbers():
    print(n)
```

These are not always used heavily in beginner Django, but they are important for understanding Python deeply.

---

## 4) Course goal: from frontend basics to backend full stack

The page says the course starts from HTML/CSS/JS and then moves into Python and Django. This is a very smart teaching approach.

The practical view:
- Frontend: HTML, CSS, JS, Tailwind
- Backend: Python, Django
- Database: ORM + SQL understanding
- API: Django REST Framework
- Deployment: hosting, environment config, cloud deployment

This is the full web stack.

---

# DAY 1 — Introduction to Web Development and Setup

## Goal
Understand how websites work and set up the tools needed for Django development.

## Topics
- What is web development?
- Frontend vs backend
- Client-server model
- HTML, CSS, JS roles
- How browsers request pages
- What Django does in a web app
- Installing Python
- Creating virtual environments
- Installing Django
- Git basics
- VS Code / IDE setup

## Important concept: client-server model
A user opens a browser (client), sends a request to a server, and the server responds with HTML, JSON, CSS, or files.

Example:
- Browser asks for `/products`
- Django view receives the request
- Django queries database
- Django renders HTML or returns JSON
- Browser displays the result

## Setup flow
```bash
python --version
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
pip install django
```

## Basic Django project creation
```bash
django-admin startproject myproject
cd myproject
python manage.py runserver
```

This creates the base project and a local development server.

## What you should understand after Day 1
- web app request flow
- how Python and Django fit into the full stack
- how to create a Django project
- how a project is structured

## Exercise for Day 1
- Create a virtual environment
- Install Django
- Run `python manage.py runserver`
- Open local URL and see the default Django page

---

# DAY 2 — Python Fundamentals for Django

## Goal
Learn the Python concepts that Django depends on.

## Topics
- Python syntax
- Variables and data types
- Lists, tuples, dictionaries, sets
- Loops and conditionals
- Functions
- Modules
- File handling
- OOP basics
- Classes and objects
- Inheritance and polymorphism

## Example code
```python
# List
students = ["Aarati", "Bibek", "Chandra"]
print(students[0])

# Dictionary
student = {"name": "Aarati", "age": 21}
print(student["name"])

# Function
def welcome(name):
    return f"Welcome, {name}"

print(welcome("Nisha"))
```

## OOP essentials
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        return f"{self.name} has grade {self.grade}"

s = Student("Nabin", "A")
print(s.show())
```

## Why this matters for Django
Django uses classes and functions heavily. For example:
- models are Python classes
- views are functions or class-based views
- URL patterns map to view functions
- forms and serializers are Python objects

## Exercise for Day 2
- Create a Python script that:
  - accepts a student name
  - stores marks in a dictionary
  - calculates average
- Create a class called `Book` with title, author, and `info()` method

---

# DAY 3 — HTML, CSS, Tailwind, and Django Project Structure

## Goal
Understand how frontend design connects with backend logic.

## Topics
- HTML structure basics
- CSS layout and styling
- Forms and input fields
- Tailwind fundamentals
- How a Django project is organized
- `manage.py`
- `settings.py`
- `urls.py`
- app structure
- templates directory

## Django project structure
```text
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    app_name/
        __init__.py
        admin.py
        apps.py
        models.py
        views.py
        tests.py
        urls.py
        templates/
```

## Django's MVT concept
Django follows MVT:
- Model: database structure
- View: handles business logic and request processing
- Template: HTML markup shown to user

This is the standard architecture emphasized by the course.

## Simple Django view example
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from Django!")
```

## URL mapping example
```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```

## Template example
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Hello, {{ user_name }}</h1>
</body>
</html>
```

## Why this matters
Django is not only backend; it connects backend logic to user-facing pages.

## Exercise for Day 3
- Create a new Django app named `blog`
- Add a home view
- Map a URL to it
- Render a simple HTML page with a heading

---

# DAY 4 — Django Models, ORM, and Database Work

## Goal
Learn how Django stores and retrieves data using ORM.

## Topics
- What is ORM?
- Django models
- Fields: `CharField`, `TextField`, `DateField`, `IntegerField`, `ForeignKey`
- Migrations
- Admin panel
- CRUD basics (Create, Read, Update, Delete)
- QuerySet basics

## What is ORM?
ORM (Object Relational Mapping) lets you work with database tables using Python objects instead of writing raw SQL most of the time.

Example:
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

This creates a table structure in the database behind the scenes.

## Migration flow
```bash
python manage.py makemigrations
python manage.py migrate
```

These commands create database tables based on model changes.

## Django admin panel
Django gives a built-in admin interface.
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Then you can log in to the admin panel and manage records.

## CRUD examples
```python
# Create
post = Post.objects.create(title='My first post', content='Hello world')

# Read
posts = Post.objects.all()

# Filter
filtered_posts = Post.objects.filter(title__contains='first')

# Update
post.title = 'Updated title'
post.save()

# Delete
post.delete()
```

## Relationship modeling
```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

This is important because real web apps often have user-to-post, category-to-product, or order-to-user relationships.

## Why ORM matters
ORM helps you:
- avoid writing raw SQL everywhere
- focus on Python logic
- handle database logic more cleanly
- manage relationships more naturally

## Exercise for Day 4
- Create a `Product` model with name, price, and description
- Migrate it
- Add 3 products in admin or shell
- Query products by price or name

---

# DAY 5 — Authentication, User Management, and REST APIs

## Goal
Add login, signup, and API functionality to web apps.

## Topics
- User authentication in Django
- Registration and login
- Sessions and cookies
- Password handling
- Permissions
- Django REST Framework (DRF)
- Serializers
- API views
- JSON responses

## Django authentication
Django already includes a user system.
```python
from django.contrib.auth.models import User
```

Typical features:
- sign up
- login
- logout
- password reset
- session handling

### Simple login flow
```python
from django.contrib.auth import authenticate, login

user = authenticate(username=username, password=password)
if user is not None:
    login(request, user)
```

## Sessions
Django stores session data on the server. It helps with keeping a user logged in and managing app state.

## User profile example
```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
```

This pattern is common in real apps.

## REST API with Django REST Framework
The training page explicitly mentions REST API. In effective Django learning, this usually means using Django REST Framework (DRF).

### Why REST APIs matter
REST APIs let your app communicate with frontend apps, mobile apps, or other services using JSON.

### Simple serializer example
```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
```

### Example API view
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
```

This returns JSON data instead of HTML.

## Why this is important
This is how modern apps work:
- Django backend handles business logic
- API returns JSON to frontend or mobile app
- frontend consumes JSON and renders UI

## Exercise for Day 5
- Create a `User` login page
- Add sign up form
- Create a `Post` API that returns all posts as JSON
- Test in browser or using Postman

---

# DAY 6 — Full-Stack Project Integration and Deployment

## Goal
Put everything together into a real app and prepare for deployment.

## Topics
- Project architecture
- Connecting frontend and backend
- Using templates with dynamic data
- CRUD pages
- Database and forms integration
- API + frontend together
- Deployment basics
- Cloud hosting
- Final project workflow

## Example full-stack flow
A typical project flow in Django is:
1. User visits a page
2. URL matches a view
3. View fetches data from database
4. View passes data to template
5. Template renders HTML
6. User submits form
7. Django validates and saves data

## Example: blog post page
```python
from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})
```

```html
{% for post in posts %}
  <h2>{{ post.title }}</h2>
  <p>{{ post.content }}</p>
{% endfor %}
```

## Deployment basics
The course mentions cloud deployment. In real projects, deployment often includes:
- environment variables
- `settings.py` changes for production
- database setup
- static files handling
- hosting on a cloud platform
- ensuring app runs with debug off

## Example safe deployment settings
```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'localhost']
```

## Final project mindset
The training page emphasizes that the final project is not a toy example—it is a real-world application built from architecture to deployment.

A good final project could be:
- Blog system
- Student management system
- Ecommerce app
- Job portal
- Inventory system
- HR management app

## Suggested Day 6 project structure
- User login/signup
- Dashboard
- Database models
- List and detail pages
- Forms for create/update/delete
- Admin panel
- API for data access
- Deployment-ready code

## Exercise for Day 6
Build a mini project such as a student portal or blog with:
- login/signup
- post creation
- database model
- listing page
- detail page
- admin access
- API endpoint for posts

---

# 5) Why the course structure matters

The course description is very specific: it does not stop at basic Django. It includes:
- frontend basics
- Python fundamentals
- Django MVT
- ORM and databases
- authentication
- admin and forms
- REST API
- real project deployment

This is exactly what most employers want in a backend or full-stack Django developer.

---

# 6) Core concepts to remember by Day 6

By the end of Day 6, you should be able to explain these clearly:

## Django MVT
- Model = database structure
- View = logic and requests
- Template = HTML shown to users

## ORM
- Convert Python code to database operations
- Avoid writing SQL manually in many cases
- Use QuerySet for filtering and retrieval

## Authentication
- User login/signup
- password security
- session management

## REST API
- return JSON
- build endpoints for data exchange
- integrate frontend or mobile apps

## Deployment
- host your application online
- configure environment settings
- make app production ready

---

# 7) Simple project idea you can build by Day 6

## Project: Student Management System
Features:
- Admin login
- Student registration
- Course list
- Attendance tracking
- Marks and result display
- API for students
- Dashboard page

Database models:
```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
```

This is a strong beginner-to-intermediate Django project.

---

# 8) Quick revision checklist

Before moving to the next stage, make sure you can do the following:
- start a Django project
- create a Django app
- understand MVT
- create models and run migrations
- use Django admin
- create views and templates
- use forms
- add login/signup
- create a simple REST API
- explain deployment basics

---

# 9) Interview-friendly explanation of Django

If someone asks: "What is Django?"

Answer:
> Django is a high-level Python web framework that helps developers build secure, scalable web applications quickly. It follows the MVT pattern, supports ORM for databases, includes authentication built-in, and allows REST API development using Django REST Framework.

If someone asks: "Why learn Django?"

Answer:
> Because Django is powerful, developer-friendly, and used by production-level companies. It is ideal for building blogs, e-commerce sites, portals, dashboards, and APIs.

---

# 10) Final takeaway

The Code IT Django course page is not just about learning syntax. It is about becoming capable of building real web applications using a modern full-stack workflow.

By Day 6, your learning journey should include:
- frontend understanding
- Python confidence
- Django project setup
- database handling with ORM
- authentication and API work
- deployment awareness
- practical project building

If you study this note carefully and practice each concept, you will understand both the structure of the course and the core skills behind Django development.

This is your foundation. From here, you can continue with advanced Django topics like:
- class-based views
- custom user models
- pagination
- search filters
- payment integration
- file uploads
- Celery jobs
- deployment to Render, Railway, or VPS

---

# 11) Suggested simple daily study plan

## Day 1
- Learn web basics
- install Python and Django
- run a demo project

## Day 2
- revise Python basics and OOP
- build small scripts

## Day 3
- build pages using HTML/CSS
- setup Django app and URL + view

## Day 4
- create models
- run migrations
- use admin

## Day 5
- add auth
- create an API
- test JSON response

## Day 6
- combine everything
- build a mini project
- present the app

---

# 12) Very important mindset

Do not memorize only. Understand why each part exists:
- Why do we need URLs?
- Why do we need models?
- Why do we need migrations?
- Why do we need authentication?
- Why do we need serializers for APIs?
- Why do we need deployment settings?

When you understand the reason behind the tool, the learning becomes easier and more lasting.

---

This is a complete beginner-friendly Django note up to Day 6, based on the course description and standard Django learning path. If you want, I can also turn this into:
1. a more detailed Day-1-to-Day-6 class notebook format, or
2. a step-by-step project-based Django roadmap with real code examples.
