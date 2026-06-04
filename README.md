# Django Authentication System

A simple Django Authentication System that allows users to register, login, logout, and access protected pages.

## Features

- User Registration
- User Login
- User Logout
- Session Authentication
- Password Hashing
- Protected Dashboard
- Django Messages Framework
- Responsive UI

## Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap (Optional)
- SQLite


## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd project-name
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

## Authentication Flow

### Registration

- User enters username, email, and password.
- Data is validated.
- New user account is created.

### Login

- User enters username and password.
- Django authenticates the user.
- User is redirected to dashboard.

### Logout

- User clicks logout button.
- Session is terminated.
- User is redirected to login page.

## Security Features

- Passwords stored in hashed format.
- Session-based authentication.
- CSRF Protection.
- Login required decorators for protected pages.

## Screenshots

Add screenshots here:

- Registration Page
- Login Page
- Dashboard
- Logout Page

## Future Improvements

- Email Verification
- Password Reset
- Profile Management
- Two-Factor Authentication (2FA)
- Social Login (Google/GitHub)

## Author

**Abhishek Kumar**

- MCA Graduate
- Python Django Developer
- Skills: Python, Django, SQL, HTML, CSS, JavaScript, Power BI


