
# ToDo List API [CREHANA]

## Project Description

This is a RESTful API project to manage a To-Do List.

## Requirements

- Python 3.9+
- Docker
- pip (Python package manager)
- Git (to clone the repository)

## Features

- **API Endpoints**:
  - `GET /tasks/` - Get all tasks.
  - `POST /tasks/` - Create a new task.
  - `GET /tasks/{id}/` - Get a task by its ID.
  - `PUT /tasks/{id}/` - Update a task by its ID.
  - `DELETE /tasks/{id}/` - Delete a task by its ID.

- **Error Handling**:
  - 404 errors when a task is not found.

- **Testing**:
  - Unit and integration tests using pytest.

## Local Environment Setup

Follow these steps to set up the project in your local environment:

1. Clone the repository:

   ```bash
   git clone https://github.com/jeanpierrers1995/todolist.git
   cd todolist
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply the migrations to set up the SQLite database:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

   The API will now be available at `http://127.0.0.1:8000/api/tasks/`.

## Instructions to Run the Application with Docker

You can use Docker to run the application without additional local setup.

1. **Build the Docker image**:

   ```bash
   docker build -t todolist .
   ```

2. **Run the container**:

   ```bash
   docker run -p 8000:8000 todolist
   ```

   This will expose the application at `http://127.0.0.1:8000`.

## Instructions to Run the Tests

The project includes unit and integration tests using `pytest`. To run the tests:

1. Ensure `pytest` is installed (it is already listed in `requirements.txt`).

2. Run the tests:

   ```bash
   pytest
   ```

   If you want to generate a code coverage report, you can run:

   ```bash
   pytest --cov=app
   ```

This will run the tests and generate a code coverage report.

## Linting and Code Formatting

This project uses **flake8** to ensure the code follows best practices and **black** to automatically format the code.

### Run flake8

1. Run flake8 to check the code:

   ```bash
   flake8
   ```

### Run black

1. Run black to format your code:

   ```bash
   black .
   ```

This will automatically format all the files in the project according to black's standards.
