# Django Student CRUD System

## Overview

This is a CRUD (Create, Read, Update, Delete) system for managing student records, created using Python, Django, MySQL, HTML, CSS, and Bootstrap.

## Features

- Student registration with basic details
- View, edit, and delete student records
- User-friendly interface with Bootstrap for a responsive design
- MySQL database for storing student data

## Prerequisites

- Python 
- Django 
- MySQL database
- Additional requirements are listed in the `requirements.txt` file.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/codewithrajan/student-crud-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd student-crud-system
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MySQL database:
   - Create a new MySQL database.
   - Update the `DATABASES` configuration in the `settings.py` file with your database details.

5. Run migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create an admin account for managing student records.

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the student CRUD system.

## Usage

- Log in with the superuser account to view, add, edit, and delete student records.
- Users can register and log in to view student details.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.

## Acknowledgments

- Thanks to the Django and Bootstrap communities for their fantastic tools and documentation.

