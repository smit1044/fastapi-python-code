from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = {}

# Pydantic model for student data
class Student(BaseModel):
    name: str
    age: int
    year: str  


class UpdateStudent(BaseModel):
    name: str | None = None
    age: int | None = None
    year: str | None = None

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}

    students[student_id] = student
    return students[student_id]

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    del students[student_id]
    return {"Message": "Student deleted successfully"}
