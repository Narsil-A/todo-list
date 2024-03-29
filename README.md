# Django ToDo List Application

## Overview

This project is a ToDo List web application built with Django and styled with Tailwind CSS. It supports CRUD (Create, Read, Update, Delete) operations both through a web interface and a RESTful API.

## Features

- User-friendly web interface for managing tasks.
- RESTful API for programmatic task management.
- Secure handling of task data using Django's ORM.
- Stylish design using Tailwind CSS.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- pip
- Virtualenv (optional but recommended)


1. Set up a Python virtual environment (Optional)

python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate

2. Install the required packages

pip install -r requirements.txt

3. Run migrations to create the database schema

python manage.py makemigrations
python manage.py migrate

4. Start the development server

python manage.py runserver


API Endpoints DRF

The application provides the following RESTful API endpoints:

GET tasks/api/tasks/ - Retrieve a list of all tasks.
POST tasks/api/tasks/ - Create a new task.
GET tasks/api/tasks/<id>/ - Retrieve details of a specific task.
PUT tasks/api/tasks/<id>/ - Update a specific task.
DELETE tasks/api/tasks/<id>/ - Delete a specific task.