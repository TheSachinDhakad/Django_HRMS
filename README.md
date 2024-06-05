# HRMS - Human Resource Management System

This is a Django-based application for managing employee attendance, login/logout, reports, and departments.

## Features

- **Attendance Management:** Track employee attendance with login/logout times.
- **Employee Management:** Create and manage employee accounts.
- **Report Generation:** Download comprehensive attendance reports.
- **Department Management:** Add and manage departments to categorize employees.

## Installation

**Prerequisites:**

- Python 3 (https://www.python.org/downloads/)
- pip (package installer that comes with Python 3)

**Steps:**

1. Clone this repository.
2. Install Python 3 and pip if not already installed.
3. Create a virtual environment (recommended) to isolate dependencies:

   ```bash
   python -m venv venv  # Create a virtual environment named 'venv'
   source venv/bin/activate  # Activate on Linux/macOS
   venv\Scripts\activate.bat  # Activate on Windows

Activate the virtual environment.

Install dependencies: pip install -r requirements.txt.

Make database migrations: python manage.py makemigrations.
Apply migrations: python manage.py migrate.
Create a superuser account: python manage.py createsuperuser.


Usage
Run the development server: python manage.py runserver.
Access the application in your browser (typically http://127.0.0.1:8000/).
Log in with your superuser credentials.
