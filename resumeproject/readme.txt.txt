# Django Resume Project

## Overview

This is a resume project created using Python, Django, HTML, CSS, and Bootstrap. It provides a platform for users to showcase their professional experience, skills, and education.

## Features

- User-friendly interface for creating and managing resumes
- Sections for personal details, summary, experience, education, and skills
- Responsive design with Bootstrap for optimal viewing on different devices
- User authentication and authorization for secure resume management

## Prerequisites

- Python 
- Django 
- Additional requirements are listed in the `requirements.txt` file.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/codewithrajan/resume-project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd resume-project
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create an admin account for managing resumes.

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the resume project.

## Usage

- Log in with the superuser account to create, edit, and manage resumes.
- Fill in the required details in each section to create a comprehensive resume.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.

## Acknowledgments

- Thanks to the Django and Bootstrap communities for their fantastic tools and documentation.

