Recipe Vault

Project Overview

Recipe Vault is a Django-based web application used to create, store, update, delete, and search recipes. It allows users to upload images, categorize recipes, and manage their personal recipe collection. The project demonstrates Django MVT architecture, CRUD operations, image handling using Pillow, responsive HTML/CSS, and a clean UI.


---

Features

Add new recipes with image upload

Search recipes by name or ingredients

Delete recipes

Upload and display recipe images

Fully responsive user interface

Category-based filtering (optional)

Template inheritance for cleaner code structure



---

Folder Structure

recipe-book/ (project root)
│── manage.py
│
├── recipebook/ (project settings)
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── recipes/ (main app)
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       ├──  dashboard.html
│   │       ├── add_recipe.html
│   │       ├── add_profile.html
│   │       └── recipe_detail.html
│   ├── static/
│   │   └── recipes/
│   │       ├── app.css
│   │       ├── style.css
│   └── models.py
│   └── views.py
│   └── urls.py
│   └── forms.py
│
└── media/
    └── recipe_images/


---

Explanation of Important Files

manage.py

Entry point of the Django project. Used to run server, make migrations, create admin user, etc.

settings.py

Central configuration file for the whole project. Controls installed apps, database, static/media files, templates, security settings, etc.

project-level urls.py

Root URL router. It includes and redirects to the app-level urls.py.

app-level urls.py

Defines URLs for the recipes app (add, edit, delete, view, home, etc.).

models.py

Defines the structure of the Recipe model and creates database tables. Example fields: name, ingredients, instructions, image.

views.py

Contains all logic. Handles CRUD operations, interacts with the database, and sends data to templates.

templates/

Contains HTML files. Uses Django Template Language ({% for %}, {% if %}, {% csrf_token %}).

static/

Contains CSS, JS, or static images. Loaded using {% load static %}.

media/

Stores uploaded user images. Uses MEDIA_URL and MEDIA_ROOT from settings.


---

Database

SQLite is used as the default database. It requires no installation and automatically generates db.sqlite3.


---

Technologies Used

Python

Django

SQLite

HTML5 / CSS3

Pillow library

Git & GitHub



---

How to Run the Project

1. Install dependencies

pip install django pillow

2. Run the server

python manage.py runserver

3. Open in browser

http://127.0.0.1:8000/

What Happens If Key Files Don’t Exist?

File	Result if Missing

models.py	No database tables; CRUD will not work
views.py	No backend logic; pages cannot load
urls.py	Project/app becomes unreachable
settings.py	Project will not run
templates/	TemplateDoesNotExist errors
static/	CSS/JS will not load
media/	Image uploads will fail
init.py	Python will not treat folder as a package



---

Conclusion

Recipe Vault is a complete Django project showcasing CRUD operations, template inheritance, responsive UI, and image handling. It is ideal for academic presentations, showcasing Django fundamentals, and demonstrating real-world web development skills.