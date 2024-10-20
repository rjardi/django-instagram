# Django Instagram Clone

A simple Instagram-like application built with Django, allowing users to create accounts, upload photos, follow other users, like and comment on posts.

## Features
- User registration and authentication (Login, Logout, Signup)
- Profile creation and updates
- Photo uploads with captions
- Like and comment on photos
- Follow and unfollow users
- News feed of followed users
- Search functionality to find users

## Tech Stack
- **Backend**: Django, Django Rest Framework
- **Frontend**: Django Templates
- **Database**: SQLite (for development)
- **Storage**: Local storage (for development)

## Setup Instructions

### Prerequisites
- Django 5.1.2
- Virtualenv (Optional but recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rjardi/django-instagram.git
   cd django-instagram-clone
   
Create and activate virtual environment

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install dependencies

pip install -r requirements.txt
Run migrations

python manage.py migrate
Create a superuser (admin)

python manage.py createsuperuser
Run the server

python manage.py runserver
Visit http://127.0.0.1:8000 to view the app.

Environment Variables
Create a .env file in the project root to set the environment variables for the project:

DEBUG=True
SECRET_KEY='your-secret-key'
DATABASE_URL='your-database-url'  # If using a cloud database like PostgreSQL
Testing
Run the following command to execute tests:

Contribution Guidelines
Fork the repository.
Create a new branch for your feature:

git checkout -b feature-name
Commit your changes:

git commit -m 'Add some feature'
Push to the branch:

git push origin feature-name
Open a pull request.
License
This project is licensed under the MIT License.
