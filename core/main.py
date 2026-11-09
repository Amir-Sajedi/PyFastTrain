from fastapi import FastAPI

app = FastAPI()

name_list = [
    {"id" : 1, "name" : "ali"},
    {"id" : 2, "name" : "maryam"},
    {"id" : 3, "name" : "arousha"},
    {"id" : 4, "name" : "aziz"},
    {"id" : 5, "name" : "zahra"}
]

# /names (GET(RETRIVE), POST(CREATE))
# /names/:id (GET(RETRIVE), PUT/PATCH((UPDATE), DELETE))


@app.get("/")
def root():
    return {
        "message": "Hello World!"
            }
    
@app .get("/names")
def retrive_names_list():
    return name_list