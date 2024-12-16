
#  Project management tool - an API

a project management tool that allows
teams to collaborate on projects. The tool needs an API to manage users, projects,
tasks, and comments. The API will be consumed by their front-end web application
and mobile application.



## Features

- JWT Authentication
- Custom User Model
- Full CRUD functionality
- API Doc by Swagger
- And many more.


## Technologies Used

### Backend

- **Python**: 3.x
- **Django**: 5.x
- **DRF**: 3.x
- **SQLite**: (default database for Django projects)


## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/fahadfoysal/project-management-api.git
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - **Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations to set up the database:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (optional, for accessing the admin interface):**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the application in your web browser:**

    Open your browser and navigate to: [http://localhost:8000](http://localhost:8000)

## Usage/Examples

```
Access the Django admin panel at http://localhost:8000/admin/ to manage everything.

Access Swagger UI for better API doc at http://127.0.0.1:8000/swagger/


## REST API Endpoints:

- Register User (POST /api/users/register/): Create a new user.
- Login User (POST /api/users/login/): Authenticate a user and return a token.
- Get User Details (GET /api/users/{id}/): Retrieve details of a specific user.
- Update User (PUT/PATCH /api/users/{id}/): Update user details.
- Delete User (DELETE /api/users/{id}/): Delete a user account.

## Token Authentication

Token-based authentication is used for API endpoints. After logging in, obtain a token and include it in the header of subsequent requests as follows:

## API Endpoints for Projects

- List Projects (GET /api/projects/): Retrieve a list of all projects.
- Create Project (POST /api/projects/): Create a new project.
- Retrieve Project (GET /api/projects/{id}/): Retrieve details of a specific project.
- Update Project (PUT/PATCH /api/projects/{id}/): Update project details.
- Delete Project (DELETE /api/projects/{id}/): Delete a project.

## API Endpoints for Task

- List Tasks (GET /api/projects/{project_id}/tasks/): Retrieve a list of all tasks in
a project.
- Create Task (POST /api/projects/{project_id}/tasks/): Create a new task in a
project.
- Retrieve Task (GET /api/tasks/{id}/): Retrieve details of a specific task.
- Update Task (PUT/PATCH /api/tasks/{id}/): Update task details.
- Delete Task (DELETE /api/tasks/{id}/): Delete a task.

## API Endpoints for Comments

- List Comments (GET /api/tasks/{task_id}/comments/): Retrieve a list of all
comments on a task.
- Create Comment (POST /api/tasks/{task_id}/comments/): Create a new
comment on a task.
- Retrieve Comment (GET /api/comments/{id}/): Retrieve details of a specific
comment.
- Update Comment (PUT/PATCH /api/comments/{id}/): Update comment
details.
- Delete Comment (DELETE /api/comments/{id}/): Delete a comment.
