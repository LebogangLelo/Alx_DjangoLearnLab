# Social Media API
This project is a foundational setup for a social media API built using Django and Django REST Framework (DRF). It supports user registration, authentication, and profile management using a custom user model.

# Setup Process
1. Clone the Repository
bash
Copy code
git clone https://github.com/LebogangLelo/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
2. Create a Virtual Environment
python -m venv env
source env/bin/activate  ##On Windows, use `env\Scripts\activate`
3. Install Dependencies
pip install django djangorestframework
4. Apply Migrations
python manage.py makemigrations
python manage.py migrate
5. Start the Development Server
python manage.py runserver
The server will be available at http://127.0.0.1:8000/.

# User Registration and Authentication
## Endpoints
Register a New User: method:POST /accounts/register/
Login: method:POST /accounts/login/
User Profile Management: method:GET, PUT, PATCH  /accounts/profile/<int:pk>/
Use the token generated during registration or login for authentication.

1. Register a User
Send a POST request to /accounts/register/ with the following JSON payload:

json
{
    "username": "john_doe",
    "password": "password123",
    "email": "john.doe@example.com",
    "bio": "Hello, I'm John!",
    "profile_picture": null
}

Response (Success):
json
{
    "token": "a_long_generated_token_string"
}

2. Authenticate a User (Login)
Send a POST request to /accounts/login/ with the following JSON payload:

json
{
    "username": "john_doe",
    "password": "password123"
}

Response (Success):
json
{
    "token": "a_long_generated_token_string"
}
Use the token in subsequent requests to authenticate, including it in the Authorization header as follows:

makefile
Authorization: Token a_long_generated_token_string

# Overview of the Custom User Model
The project uses a custom user model, CustomUser, which extends Django's AbstractUser. This model adds the following additional fields:

bio: A text field for the user to provide a brief biography.
profile_picture: An image field for uploading a profile picture.
followers: A self-referential ManyToManyField to allow users to follow each other (non-symmetrical).

Model Code
python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username
This custom model is specified in settings.py as the default user model:

python
AUTH_USER_MODEL = 'accounts.CustomUser'

# Testing
Use Postman, curl, or any HTTP client to test the API endpoints. Verify that tokens are generated and returned correctly upon registration and login.

# Social Media API - Posts and Comments

## API Endpoints

### Posts
- **List Posts**: `GET /api/posts/`
- **Create Post**: `POST /api/posts/`
  - **Request Body**:
    ```json
    {
        "title": "Post Title",
        "content": "Post content"
    }
    ```
- **Retrieve Post**: `GET /api/posts/{id}/`
- **Update Post**: `PUT /api/posts/{id}/`
- **Delete Post**: `DELETE /api/posts/{id}/`

### Comments
- **List Comments**: `GET /api/comments/`
- **Create Comment**: `POST /api/comments/`
  - **Request Body**:
    ```json
    {
        "post": 1,
        "content": "Comment content"
    }
    ```
- **Retrieve Comment**: `GET /api/comments/{id}/`
- **Update Comment**: `PUT /api/comments/{id}/`
- **Delete Comment**: `DELETE /api/comments/{id}/`

## Features
- Pagination: List endpoints return paginated results.
- Filtering: Search posts by `title` or `content`.

## Permissions
- Only authors can edit/delete their own posts or comments.
