#make an app. the doctor can maintain a profile of each patient and sore it at one place . instead of using a database, we store it in json format.CRUD operations are vailabble"
"""endpoints:
1. create a patient profile
2. read a patient profile
3. update a patient profile
4. delete a patient profile
5. view all profies
"""
from fastapi import FastAPI
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