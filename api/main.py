#make an app. the doctor can maintain a profile of each patient and sore it at one place . instead of using a database, we store it in json format.CRUD operations are vailabble"
"""endpoints:
1. create a patient profile
2. read a patient profile
3. update a patient profile
4. delete a patient profile
5. view all profies
"""
from fastapi import FastAPI,Path,HTTPException,Query
import json

app=FastAPI()

def load_data():
    with open("patients.json", 'r') as f:
        data=json.load(f)
        return data

@app.get("/")
def hello():
    return{"message":"patient management system"}

@app.get("/aboot")
def  about():
    return {"message":"fully functional patient management system"}

@app.get("/view")
def view():
    data=load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id:str = Path(...,description="enter the patient id of the patient whose details you want to see",example="P002")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException( status_code=404,detail="patient not found")

"""query parameter are optional and endpoint can be used without them as well. they are seperated by &"""

@app.get("/sorte")
def sort_patient(sort_by: str =Query(..., description="sort on the basis of height,weight,bmi"), order:str =Query("asc" ,description="order of sorting")):
    valid_fields=["height","weight","bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"invalid field, seect from {valid_fields}")
    
    if order not in ["asc","desc"]:
        raise HTTPException(status_code=400, detail="please select from asc,desc")
    data=load_data()
    sort_order=True if order=="desc" else False
    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by,0),reverse=sort_order)
    return sorted_data


