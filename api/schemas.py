"used for data validation and serialization. it allows us to define data models using python classes and provides automatic validation and parsing of incoming data. it also supports features like type hints, default values, and custom validation logic"
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated

class address(BaseModel):
    city: str
    state: str
    pin: int
    

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, description='name in less than 50 chars',title='name of the patient')]
    age: int
    email: EmailStr
    address:address
    url: Optional[AnyUrl]
    height: float=Field(gt=0 )
    weight: float=Field(gt=0 , lt =200)
    married: bool
    allergies:Optional[List[str]]=  Field(default=None, max_length=5)
    contact: Dict[str,str]=None

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domails="hdfc.com"
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domails:
            raise ValueError('not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def name_transform(cls,value):
        value=value.upper()
        return value

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact:
            raise ValueError(" patients above 60 add emergency details")
        return model
    @computed_field
    @property
    def bmi(self)-> float:
        bmi=round(self.weight/(self.height/100)**2)
        return bmi

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.url)
    print(patient.weight)
    print(patient.married)
    print(patient.contact)

    print("inserted")
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.url)
    print(patient.bmi)
    print(patient.weight)
    print(patient.married)
    print(patient.contact)

    print("inserted")

def fetch_address(patient:Patient):
    print(patient.address)



address_dict={'city':'gurugram','state':'haryana','pin':110011}
address1=address(**address_dict)

patient_info= {'name':'nitish', 'age':61, 'email':'faizanmir@hdfc.com','address':address1,'url':"http://www.danzanchus.com" ,'height':'185' ,'weight':70.1, 'married':False, 'allergies':['pollen','presewrvatives'], 'contact':{'fateher':'apple', 'mother':'mango', 'emergency':'ddd'} }
patient1= Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
fetch_address(patient1)
print(patient1.address.pin)