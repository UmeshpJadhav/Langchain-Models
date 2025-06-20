from pydantic import BaseModel

class Student(BaseModel):

    name: str

new_student = {"name": "John Doe"}

Student = Student(**new_student)

print(Student)

