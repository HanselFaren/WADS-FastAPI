from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

#Endpoint: domain/student/1

#GET
#POST
#PUT
#DELETE
students = {
    1:{
        "name":"Hansel",
        "age":"20",
        "classes":"L4AC",
        "phone":"08213453261"
    },
    2:{
        "name":"Nicholas",
        "age":"17",
        "classes":"L4AC",
        "phone":"08132522235"
    }
}

class Student(BaseModel):
    name: str
    age: int
    classes: str
    phone: str

class UpdateStudent(BaseModel):
        name: Optional[str] = None
        age: Optional[int] = None
        classes: Optional[str] = None
        phone: Optional[str] = None

#path parameter
#/get-student/1
@app.get("/get-student/{id}")
def get_student(id: int = Path(description="ID of student that you want to view")):
    return students[id]

#query parameter
#google.com/menu?name="bagus"&age=12
@app.get("/get-student_by_name/menu")
def get_student(name: Optional[str]= None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Error": "Student name not found"}

#POST method
@app.post("/create-student/menu")
def add_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student ID is exist"}
    students[student_id] = student
    return students[student_id]

#PUT method
@app.put("/update-student/menu")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "students is NOT exist"}
    if students.name is not None:
        students[student_id].name = student.name

    if students.age is not None:
        students[student_id].age = student.age

    if students.classes is not None:
        students[student_id].classes = student.classes

    if students.phone is not None:
        students[student_id].phone = student.phone

    return students[student_id]

#Delete method
@app.delete("/delete-student/menu")
def delete_student(student_id: int):
    del students[student_id]
    return {"msg": "has been delete successfully"}