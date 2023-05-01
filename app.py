from fastapi import FastAPI, Response
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.status import *
from typing import List

from models.ordersModel import OrdersModel
from models.criterionModel import CriterionModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Content-Type", "Set-Cookie", "Authorization", "Accept"],
)

@app.post('/solution')
def process_orders(orders: List[OrdersModel], criterion: CriterionModel):
    try:
        total_price: float = 0
        for order in orders:
            if order.status == criterion.name:
                total_price += order.price * order.quantity

        return total_price
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))