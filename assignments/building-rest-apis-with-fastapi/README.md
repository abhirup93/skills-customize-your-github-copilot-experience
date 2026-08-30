# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for managing tasks using FastAPI. You will practice creating routes, handling HTTP methods, validating request data, and returning JSON responses in a clean, production-ready structure.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App

#### Description
Initialize a FastAPI application and create a basic home route that confirms the API is running.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Add a GET route at `/` that returns a welcome message
- Use a simple JSON response format
- Run the app locally with Uvicorn for development

### 🛠️ Create a Task Model and List Endpoint

#### Description
Define a data model for tasks and create an endpoint to return all current tasks.

#### Requirements
Completed program should:

- Use Pydantic models to define the task structure
- Include fields such as `id`, `title`, and `done`
- Add a GET route at `/tasks` that returns the task list
- Store tasks in memory for this exercise

### 🛠️ Add Create and Read Operations

#### Description
Implement endpoints to create new tasks and retrieve a single task by ID.

#### Requirements
Completed program should:

- Add a POST route at `/tasks` to create a new task
- Accept JSON input with a title and optional completion status
- Return the created task with a `201` status code
- Add a GET route at `/tasks/{task_id}` to find and return one task
- Return a `404` error if the task does not exist

### 🛠️ Update and Delete Tasks

#### Description
Add full CRUD support so items can be updated and removed through the API.

#### Requirements
Completed program should:

- Add a PUT route at `/tasks/{task_id}` to update existing data
- Allow changes to task details like title and completion status
- Add a DELETE route at `/tasks/{task_id}` to remove a task
- Return appropriate status codes for successful updates and deletions
- Keep the API behavior consistent and easy to test

### 🛠️ Validate and Document the API

#### Description
Ensure the API is easy to use and clearly documented using FastAPI's built-in features.

#### Requirements
Completed program should:

- Use Pydantic validation for incoming data
- Handle invalid or missing fields gracefully
- Confirm the API can be explored through FastAPI's `/docs` page
- Keep route names, response models, and JSON output clear and consistent
