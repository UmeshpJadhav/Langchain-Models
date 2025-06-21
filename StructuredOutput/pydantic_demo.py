from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = "Umesh"
    age : Optional[int] = None
    email : EmailStr = "umesh@gmail.com"
    cgpa : float = Field(gt=0, lt=10,default=5, description="CGPA must be between 0 and 10")

new_student = { "cgpa": 1 }

Student = Student(**new_student)

student_dict = dict(Student)

print(student_dict ['age'])

student_json = Student.model_dump_json()
