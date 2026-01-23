# Trying to build a basic API for a CRUD Application for managing student data
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    enroll: int
    name: str
    fname: str
    cgpa: int

btech: List[Student] = [] #btech replaces teas and Student replaces tea

# Base Decorator towards our base route
@app.get("/")
def read_root():
    return {"message": "Welcome to Student API"}

# Adding more Decorators
@app.get("/btech")
def get_btech():
        return btech

# more CRUDstuff
@app.post("/btech")
def post_btech(student: Student): #to add a Student
    btech.append(student)
    return student

@app.put("/btech/{id}")
def update_student(id:int, updated_student: Student):
    for index, student in enumerate(btech): # TODO: Understand enumerations better
        if Student.enroll == id:
            btech[index] = updated_student
            return updated_student
    return {"error": "Database not Updated"}

@app.delete("/btech/{id}")
def delete_student(id: int):
    for index, student in enumerate(btech):
        if Student.enroll == id:
            deleted_student = btech.pop(index)
            return deleted_student
    return {"error": "Student not deleted"}
