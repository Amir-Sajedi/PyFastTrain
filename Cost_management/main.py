from fastapi import FastAPI

app = FastAPI()

costs ={}

@app.post("/items/{item_id}", status_code=201)
def new_item(item_id: int , item_cost: float, item_description: str ):
    costs[item_id] = {"cost": item_cost, "description": item_description}
    print(costs)
    return costs[item_id] 
    
@app.get("/items/total_cost", status_code=200)
def total_cost():
    total = sum(item["cost"] for item in costs.values())
    return {"total_cost": total}

@app.get("items/idvidual_cost/{item_id}", status_code=200)
def individual_cost(item_id: int):
    if item_id in costs:
        return costs[item_id]
    else:
        return {"status_code":404, "content":"Item not found"}
    
@app.put("/items/edit_item/{item_id}", status_code=200)
def edit_item(item_id: int, item_cost: float = None, item_description: str = None):
    if item_id in costs:
        if item_cost is not None:
            costs[item_id]["cost"] = item_cost
        if item_description is not None:
            costs[item_id]["description"] = item_description
        return costs[item_id]
    else:
        return {"content": "Item not found"}
    

@app.delete("/items/delete_item/{item_id}", status_code=200)
def delete_item(item_id: int):
    if item_id in costs:
        del costs[item_id]
        return {"message": "Item deleted successfully"}
    else:
        return {"status_code":200 , "content":"Item not found"}