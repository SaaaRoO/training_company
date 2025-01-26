
# Training Company Management System

A Django web application for managing courses, trainers, and payments with CRUD operations and reporting.

## Features
- **Courses Management**: Create, read, update, and delete courses.
- **Trainers Management**: Manage trainer profiles and expertise.
- **Payment Tracking**: Record and track payments to trainers.
- **Relationships**: Link courses to multiple trainers.
- **Reporting**: Basic reporting and list views.
- **Security**: Built-in Django security features and CSRF protection.

## Technical Stack
- **Backend**: Django 4.2
- **Database**: SQLite (Development), PostgreSQL (Production-ready)
- **Frontend**: HTML, CSS, JavaScript
- **Testing**: Django Test Framework, pytest
- **APIs**: Django REST Framework (Optional)



## Setup & Installation

### 1. Clone the Repository
  ```bash
   git clone https://github.com/SaaaRoO/training_company.git
   cd training_company


## 2. Install Dependencies
```bash
 pip install -r requirements.txt

### 3. Database Setup
```bash
  python manage.py migrate

### 4. Run the Development Server
```bash
  python manage.py runserver

Visit http://localhost:8000 in your browser.


## Key Test Cases

* Model Validation

*  Course-trainer relationships

* Payment amount validation

##View Functionality

* CRUD operations for all models

* Form submissions and redirects

##Security

* Authentication requirements

* CSRF validation




