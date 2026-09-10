from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str= 'mango'
    age:Optional[int]=None
    email: EmailStr
    cgpa: float= Field(gt=0,lt=10,default=5)


new_stud={'name':'faizann','age':22 ,'email':"s@s.com"}

student=Student(**new_stud)
print(student)