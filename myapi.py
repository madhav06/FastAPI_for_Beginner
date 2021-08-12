from typing import Optional

from fastapi import FastAPI

app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 2019"
    }
}

'''
GET - GET an Information
POST - Create Something new
PUT - Update
DELETE - Delete something
'''
@app.get("/")
def index():
    return { "name": "First Data" } 

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]
