from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

#Endpoint: domain/student/1

#GET
#POST
#PUT
#DELETE
tasks = {
    1:{
        "task":"Do homework",
        "description":"WADS fastapi homework",
        "time":"60 minutes",
        "status":"Unfinished"
    },
    2:{
        "task":"Do dailies in game",
        "description":"Genshin and Honkai",
        "time":"60 minutes",
        "status":"Unfinished"
    }
}

class Task(BaseModel):
    task: str
    description: str
    time: str
    status: str

class UpdateTask(BaseModel):
        task: Optional[str] = None
        description: Optional[str] = None
        time: Optional[str] = None
        status: Optional[str] = None

#path parameter

@app.get("/get-task/{id}")
def get_task(id: int = Path(description="ID of task you want to view")):
    return tasks[id]

#POST method
@app.post("/create-task/menu")
def add_task(task_id: int, task: Task):
    if task_id in tasks:
        return {"Error": "Task ID is exist"}
    tasks[task_id] = task
    return tasks[task_id]

#PUT method
@app.put("/update-task/menu")
def update_task(task_id: int, task: UpdateTask):
    if task_id not in tasks:
        return {"Error": "tasks is NOT exist"}
    if tasks.task is not None:
        tasks[task_id].task = task.task

    if tasks.description is not None:
        tasks[task_id].description = task.description

    if tasks.time is not None:
        tasks[task_id].time = task.time

    if tasks.status is not None:
        tasks[task_id].status = task.status

    return tasks[task_id]

#Delete method
@app.delete("/delete-task/menu")
def delete_task(task_id: int):
    del tasks[task_id]
    return {"msg": "has been delete successfully"}