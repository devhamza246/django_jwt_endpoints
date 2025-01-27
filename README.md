# Django JWT Endpoints

A Django project that provides user authentication and protected endpoints using JWT (JSON Web Tokens). This project demonstrates how to create custom JWT-based authentication middleware and integrate it with Django REST Framework (DRF).

## Features
- Custom `CustomUser` model with email-based authentication.
- JWT-based authentication system.
- Public and protected endpoints.
- Middleware for validating JWT tokens.
- Swagger UI integration for API documentation and testing.

## Requirements
- Python 3.8+
- Django 4.x
- Django REST Framework (DRF)
- drf-yasg (for API documentation)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/devhamza246/django_jwt_endpoints.git
   cd django_jwt_endpoints
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the Swagger UI at:
   ```
   http://127.0.0.1:8000/
   ```


## API Endpoints

### Public Endpoints
- **GET /public/**
  - Response: `{ "message": "Hello, this is the public endpoint." }`

### User Endpoints
- **POST /users/signup/**
  - Create a new user.
  - Request Body:
    ```json
    {
        "username": "example",
        "email": "example@example.com",
        "password": "password123"
    }
    ```

- **POST /users/login/**
  - Authenticate user and return a JWT token.
  - Request Body:
    ```json
    {
        "email": "example@example.com",
        "password": "password123"
    }
    ```
  - Response:
    ```json
    {
        "token": "<JWT_TOKEN>"
    }
    ```

### Protected Endpoints
- **GET /protected/**
  - Requires `Authorization` header with a valid JWT token.
  - Response:
    ```json
    {
        "id": 1,
        "username": "example",
        "email": "example@example.com"
    }
    ```