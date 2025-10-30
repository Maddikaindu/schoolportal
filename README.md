School Portal – Django Project
### Overview

The School Portal is a Django-based web application that manages students, teachers, and admin activities efficiently.
It provides secure role-based authentication where users can register, log in, and access dashboards based on their roles.

This project contains three Django apps:

Accounts – handles custom user models, registration, authentication, and role-based access.

Students – manages student profiles, dashboards, and mark details.

Teachers – manages teacher profiles, assigned students, and grading functions.

###  User Roles
🧑‍💼 Admin

Approves new teacher and student registrations.

Assigns students to teachers.

Manages all users, profiles, and records through Django Admin panel.

👩‍🏫 Teacher

Views only students assigned by the admin.

Can add, update, and delete marks for their assigned students.

Cannot access unassigned student data (data security enforced).

🎓 Student

Can view their personal dashboard with profile details and marks.

Can log in and update limited personal information.

Cannot see other students’ information.

### Features

Role-based user authentication (Admin / Teacher / Student)

Registration and login system

Dashboard for each user type

Admin-student-teacher linking

CRUD operations for student marks

Automatic user profile creation using Django signals

UUIDs for unique identification

Access control using custom decorators

One-to-One relationships between user and profile models

### Tech Stack

Framework: Django (Python)

Database: SQLite

Frontend: HTML

Authentication: Django AbstractUser (custom)

UUIDs: for unique user and profile IDs

Signals: post_save decorator from django.dispatch

### 🧱 Project Architecture

Apps:

accounts – Handles AbstractUser, roles, signals, decorators, UUIDs.

teachers – Teacher dashboards, assigned students, and marks management.

students – Student dashboard and personal data view.

Relationships:

User → TeacherProfile → OneToOneField

User → StudentProfile → OneToOneField

Signals automatically create a profile after each new user registration.

### 🚀 Installation (Local Setup)

Clone the repository:

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>


Create and activate virtual environment:

python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux


Install dependencies:

pip install django


Apply migrations:

python manage.py migrate


Create admin user:

python manage.py createsuperuser


Run the server:

python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

### 🧠 Key Learning

This project helped me strengthen my understanding of:

Django MVT architecture

Custom user model using AbstractUser

UUIDs and unique identifiers

Signals (@receiver, post_save) for auto profile creation

One-to-one relationships

Decorators for role-based access

Database operations using Django ORM

Role-based dashboards and access management
