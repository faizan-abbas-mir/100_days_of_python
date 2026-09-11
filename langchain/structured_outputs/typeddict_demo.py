from typing import TypedDict

class person(TypedDict):
    name:int = None
    age:str

new_person=person(name=1,age="fifty")
