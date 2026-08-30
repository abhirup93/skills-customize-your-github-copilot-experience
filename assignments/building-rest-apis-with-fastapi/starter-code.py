from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")

# In-memory task storage for the assignment
tasks = [
    {"id": 1, "title": "Write project plan", "done": False},
    {"id": 2, "title": "Review API design", "done": True},
]


class TaskCreate(BaseModel):
    title: str
    done: bool = False


class Task(TaskCreate):
    id: int


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}


@app.get("/tasks")
def get_tasks():
    # TODO: return the full list of tasks
    pass


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    # TODO: create a new task using the in-memory list
    # Remember to assign a unique id and return the created task
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: find the task by id and return it
    # If no task matches, raise HTTPException(status_code=404, detail="Task not found")
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    # TODO: update the matching task and return the updated task
    pass


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    # TODO: remove the task from memory and return no content
    pass
