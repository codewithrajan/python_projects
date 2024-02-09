# Django Quiz System

## Overview

This is a quiz system project created using Python, Django, MySQL, HTML, CSS, and Bootstrap. It allows users to create quizzes, take quizzes, and view their quiz results.

## Features

- User authentication and authorization
- Quiz creation and management
- Quiz-taking functionality with automatic scoring
- User-friendly interface with Bootstrap for a responsive design
- MySQL database for storing quiz and user data

## Prerequisites

- Python
- Django 
- MySQL database
- Additional requirements are listed in the `requirements.txt` file.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/codewithrajan/quiz-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd quiz-system
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

    Follow the prompts to create an admin account for managing quizzes.

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the quiz system.

## Usage

- Log in with the superuser account to create, edit, and manage quizzes.
- Users can register, log in, and take quizzes.
- View quiz results and scores after completing a quiz.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.



## Acknowledgments

- Thanks to the Django and Bootstrap communities for their fantastic tools and documentation.

