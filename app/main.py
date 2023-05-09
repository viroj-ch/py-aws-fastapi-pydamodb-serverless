import os

from fastapi import FastAPI
from mangum import Mangum

stage = os.getenv('ENVIRONMENT_NAME')
app = FastAPI(
    # if not custom domain
    openapi_prefix=f"/{stage}"
)
lambda_handler = Mangum(app)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/search")
def search(query: str):
    return {"message": f"You searched for {query}"}
