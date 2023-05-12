import os
from typing import Union

from fastapi import FastAPI
from mangum import Mangum

from app.shared.model import dealer

stage = os.getenv('ENVIRONMENT_NAME')
app = FastAPI(
    # if not custom domain
    root_path=f"/{stage}"
)
lambda_handler = Mangum(app)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/search")
def search(query: str):
    return {"message": f"You searched for {query}"}


@app.get("/dealer")
def get_dealer(dealer_status: str,
               priority_id: Union[str, None] = 'BLANK'
               ):
    if dealer_status:
        return dealer.query_by_dealer_status_and_priority_id(dealer_status, priority_id, 10)
    else:
        return {"message": "query params are required"}


if __name__ == '__main__':
    print(dealer.query_by_dealer_status_and_priority_id('A'))
