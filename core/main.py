from fastapi import FastAPI, status, HTTPException, Query, Path, Form, Body, File, UploadFile
import random as random
from dataclasses import dataclass
from typing import List
from fastapi import UploadFile
from contextlib import asynccontextmanager
from schemas import PersonCreateSchema, PersonResponseSchema, PersonUpdateSchema

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("application startup")
    yield
    
    print("application shutdown")



app = FastAPI(lifespan=lifespan) # watch it, for lifespan u will need to assign that context manager function into this one

name_list = [
    {"id" : 1, "name" : "ali"},
    {"id" : 2, "name" : "maryam"},
    {"id" : 3, "name" : "arousha"},
    {"id" : 4, "name" : "aziz"},
    {"id" : 5, "name" : "zahra"}
]

# # deprecrated method
# @app.on_event("startup")
# async def startup_event():
#     print("starting the application")

# @app.on_event("shutdown")
# async def startup_event():
#     print("shutting down the application")




# /names (GET(RETRIVE), POST(CREATE))
@app .get("/names")
def retrieve_names_list(q: str | None = Query(description="it will be searched with the title that you have already     provided",default=None, max_length= 50, response_model=List[PersonResponseSchema])): # the List() wont work here
    if q:
        return [item for item in name_list if item["name"] == q]
    # follow the oic rule (operation iteration condition)
    return name_list

@dataclass
class Student:
    name: str
    age: int
@dataclass
class StudetnResponse:
    id: int
    name: str



@app.post("/names", status_code =status.HTTP_201_CREATED, response_model=PersonResponseSchema)
def create_name(person : PersonCreateSchema): # the aint an equal sign here
    name_obj = {"id":random.randint(6,100),"name":person.name }
    name_list.append(name_obj)
    return name_obj


# /names/:id (GET(RETRIVE), PUT/PATCH((UPDATE), DELETE))
@app.get("/names/{name_id}", status_code=status.HTTP_200_OK, response_model=PersonResponseSchema)
def retrieve_name_detail(name_id: int = Path(alias="object_id",title="object id", description="the id of the name in names list")):
    for name in name_list:
        if name["id"] == name_id:
            return name
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="object not found") 

@app.put("/names/{name_id}")
def update_name_detail( person = PersonUpdateSchema ,name_id: int = Path()):
    for item in name_list:
            if item["id"] == name_id:
                item["name"] = person.name
                return item
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="object not found")     

@app.delete("/names/{name_id}")
def delete_name_detail(name_id: int):
    for item in name_list:
            if item["id"] == name_id:
                name_list.remove(item)
                return {"detail": "object has been removed successfully"}
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="object not found")     





@app.get("/")
def root():
    return {
        "message": "Hello World!"
            }
    


@app.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    print(file.__dict__)
    return {"filename": file.filename, "content_type" : file.content_type, "file_size": len(content) }



@app.post("/upload_multiple")
async def upload_multiple(files: list[UploadFile] = File(...)):
    return [
        {
            "filename": file.filename,
            "content_type": file.content_type
        }
        for file in files
    ]