from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Tasks API")


class Task(BaseModel):
    title: str
    completed: bool = False


tasks = [
    {"id": 1, "title": "Read the API documentation", "completed": False},
    {"id": 2, "title": "Write the first endpoint test", "completed": True},
]


@app.get("/tasks")
def list_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    new_task = {"id": max(item["id"] for item in tasks) + 1, **task.model_dump()}
    tasks.append(new_task)
    return new_task
