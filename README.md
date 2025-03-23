# Personnel Management System

## Overview
The Personnel Management System is a web-based application built using the Python Django framework. It is designed to streamline the management of personnel-related data within an organization. The system provides an intuitive interface for managing employee information, access permissions, department categories, and client details. Currently, a role-based login system tied to personnel permissions is under development to enhance security and access control.

## Features
1. Employee Information Management
    - Create, update, and delete employee profiles.
    - Store and manage details such as name, contact information, job title, and more.
2. Access Permission Management
    - Define and assign access levels to employees based on their roles.
    - Control permissions for different functionalities within the system.
3. Department Category Management
    - Organize employees into departments.
    - Add, edit, or remove department categories as needed.
4. Client Information Management
    - Maintain a database of client details.
    - Facilitate easy retrieval and updates of client-related data.

## Under Development
- Role-Based Login System
    - A secure authentication system linked to personnel permissions.
    - Users will log in with credentials tied to their assigned roles, ensuring restricted access based on permissions.
- Expected to include features such as password hashing, session management, and user-specific dashboards.

## Technologies Used
- Backend: Python, Django
Frontend: HTML, CSS, JavaScript (optional, depending on your implementation)
Database: SQLite (default) or configurable to PostgreSQL/MySQL
- Other Libraries: (Add any additional libraries or tools you’ve used, e.g., Django REST framework, if applicable)

## Installation
1. Clone the Repository
```bash
git clone <repository-url>
cd personnel-management-system
```

2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the Development Server
```bash
python manage.py runserver
Access the application at http://127.0.0.1:8000/.
```
## Usage
- Create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```
- Log in to the Django admin interface to manage employees, departments, clients, and permissions.
- Once the login system is complete, users will authenticate through a custom login page based on their assigned roles.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major updates, open an issue first to discuss your ideas.

## Contact
For questions or suggestions, feel free to reach out at gellar@tutanota.com or open an issue in the repository.