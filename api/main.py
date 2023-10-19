from fastapi import FastAPI

'''
Objective: Create a API to resolve requests from django local web server to AWS EC2
'''


#uvicorn main:app --port 8080
app = FastAPI()

#routes
#CRUD
@app.post("/create")
def create_data():
    return

@app.get("/read")
def read_data():
    return "Dados aqui"

@app.put("/update/{item_id}")
def update_data(item_id: int):
    return

@app.delete("/delete/{item_id}")
def delete_data(item_id: int):
    return