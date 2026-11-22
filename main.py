from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1.Define the data model (pydantic)
class Student(BaseModel):
    name : str
    grade : int
    course : str
    
# This is our "database" for now
students_db = []

#2.Endpoint : Get all students
@app.get("/students")
def get_students():
    return {"students": students_db}

# 3. Endpoint: Add student
@app.post("/students")
def add_student(student: Student):
    # FastAPI automatically ensures 'name', 'grade', and 'course' are provided
    student_db.append(student)
    return {"message": "Student added successfully", "student": student}