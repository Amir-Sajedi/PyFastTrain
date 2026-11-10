from fastapi import FastAPI, status, HTTPException
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
def retrieve_names_list(q: str | None = None):
    if q:
        return [item for item in name_list if item["name"] == q]
    # follow the oic rule (operation iteration condition)
    return name_list

@app.post("/names", status_code =status.HTTP_201_CREATED )
def create_name(name: str):
    name_obj = {"id":random.randint(6,100),"name":name }
    name_list.append(name_obj)
    return name_obj


# /names/:id (GET(RETRIVE), PUT/PATCH((UPDATE), DELETE))
@app.get("/names/{name_id}", status_code=status.HTTP_200_OK)
def retrieve_name_detail(name_id: int):
    for name in name_list:
        if name["id"] == name_id:
            return name
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="object not found") 

@app.put("/names/{name_id}")
def update_name_detail(name_id: int, name:str):
    for item in name_list:
            if item["id"] == name_id:
                item["name"] = name
                return {"name": name}
            
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
    
