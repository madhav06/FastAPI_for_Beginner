from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "year 2019"
    }
}

'''
GET - GET an Information
POST - Create Something new
PUT - Update
DELETE - Delete something
'''

class Student(BaseModel):
    name: str
    age: int
    year: str



@app.get("/")
def index():
    return { "name": "First Data" } 

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want here.", gt=0)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id:int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student Exists"}

    students[student_id] = student
    return students[student_id]
