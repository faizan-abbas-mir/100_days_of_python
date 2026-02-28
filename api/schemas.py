"used for data validation and serialization. it allows us to define data models using python classes and provides automatic validation and parsing of incoming data. it also supports features like type hints, default values, and custom validation logic"
from pydantic import BaseModel
from typing import List,Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies:List[str]
    contact: Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.contact)

    print("inserted")

patient_info= {'name':'nitish', 'age':30, 'weight':70.1, 'married':False, 'allergies':['pollen','presewrvatives'], 'contact':{'fateher':'apple', 'mother':'mango'} }

patient1= Patient(**patient_info)

insert_patient_data(patient1)