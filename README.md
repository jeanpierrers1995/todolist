
# ToDo List API [CREHANA]

## Project Description

1. [ ] This project is a To-Do List API built using Django Rest Framework and GraphQL with Strawberry. It provides RESTful API endpoints for managing tasks, including creating, updating, and deleting tasks. Additionally, it offers a GraphQL API for more flexible and efficient data querying and manipulation.
2. [ ] The application supports error handling, including custom error messages when tasks are not found, and includes unit tests for ensuring the correctness of the functionality.

## You can upload the postman file to test the endpoints

[![Run in Postman](https://run.pstmn.io/button.svg)](https://api.postman.com/collections/1665438-3cf40187-09bb-4d47-9809-3261d734e1fc?access_key=PMAT-01J7FQF6ZTB7NTN1ZVH2RDAV6G)

### Or you can also import the file `todolist.postman_collection.json` in postman


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

   The API will now be available at `http://localhost:8000/api/tasks/`.

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

   This will expose the application at `http://localhost:8000`.

# GraphQL with Django and strawberry


- **GraphQL API Endpoints**:
  - `/graphql/`: Endpoint for interacting with the GraphQL API.
  
### Supported Operations:
  
- **Queries (Fetch Data)**:
  - `allTasks`: Fetches all tasks.


- **Mutations (Modify Data)**:
  - `createTask`: Creates a new task.
  - `updateTask`: Updates an existing task.
  - `deleteTask`: Deletes a task by ID.

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
