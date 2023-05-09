from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
lambda_handler = Mangum(app)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/search")
def search(query: str):
    return {"message": f"You searched for {query}"}
