"used for data validation and serialization. it allows us to define data models using python classes and provides automatic validation and parsing of incoming data. it also supports features like type hints, default values, and custom validation logic"
from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, description='name in less than 50 chars',title='name of the patient')]
    age: int
    email: EmailStr
    url: AnyUrl
    weight: float=Field(gt=0 , lt =200)
    married: bool
    allergies:Optional[List[str]]=  Field( max_length=5)
    contact: Dict[str,str]=None

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.url)
    print(patient.weight)
    print(patient.married)
    print(patient.contact)

    print("inserted")

patient_info= {'name':'nitish', 'age':30, 'email':'faizanmir@gmail.com','url':"http://www.danzanchus.com"  ,'weight':70.1, 'married':False, 'allergies':['pollen','presewrvatives'], 'contact':{'fateher':'apple', 'mother':'mango'} }

patient1= Patient(**patient_info)

insert_patient_data(patient1)

