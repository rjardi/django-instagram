# Django Instagram Clone

A simple Instagram-like application built with Django, allowing users to create accounts, upload photos, follow other users, like and comment on posts.

## Features
- User registration and authentication (Login, Logout, Signup)
- Profile creation and updates
- Photo uploads with captions
- Like and comment on photos
- Follow and unfollow users
- News feed of followed users

## Tech Stack
- **Backend**: Django, Django Rest Framework
- **Frontend**: Django Templates and Bootstrap5 with django-crispy-forms
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
   ```
   
2. **Create and activate virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin)**

   ```bash
   python manage.py createsuperuser
   ```
6. **Run the server**

   ```bash
   python manage.py runserver
   ```
7. **Visit http://127.0.0.1:8000 to view the app.**