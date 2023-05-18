import os
from typing import Union

from fastapi import FastAPI, HTTPException
from mangum import Mangum

from app.shared.models import dealer

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
def get_dealer(
        dealer_status: str,
        priority_id: Union[str, None] = 'BLANK'
):
    if not dealer_status:
        return {"message": "dealer_status is required"}

    return dealer.query_by_dealer_status_and_priority_id(dealer_status, priority_id, 10)


@app.get("/dealer/{dealer_code}")
async def get_dealer_by_dealer_code(dealer_code: str):
    if not dealer_code:
        return {"message": "dealer_code is required"}

    item = dealer.query_by_dealer_code(dealer_code)
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")


if __name__ == '__main__':
    print(dealer.query_by_dealer_status_and_priority_id('A'))
