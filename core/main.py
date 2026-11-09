from fastapi import FastAPI
import random as random

app = FastAPI()

name_list = [
    {"id" : 1, "name" : "ali"},
    {"id" : 2, "name" : "maryam"},
    {"id" : 3, "name" : "arousha"},
    {"id" : 4, "name" : "aziz"},
    {"id" : 5, "name" : "zahra"}
]

# /names (GET(RETRIVE), POST(CREATE))
@app .get("/names")
def retrieve_names_list():
    return name_list

@app.post("/names")
def create_name(name: str):
    name_obj = {"id":random.randint(6,100),"name":name }
    name_list.append(name_obj)
    return name_obj


# /names/:id (GET(RETRIVE), PUT/PATCH((UPDATE), DELETE))
@app.get("/names/{name_id}")
def retrieve_name_detail(name_id: int):
    for name in name_list:
        if name["id"] == name_id:
            return name
    return {"detail": "object not found"}



@app.get("/")
def root():
    return {
        "message": "Hello World!"
            }
    
