from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.status import *
from redistCache import setCache, getCache

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
def process_orders(orders: list[OrdersModel], criterion: CriterionModel):
    try:
        total_price: float = 0
        if criterion.name != 'all':
            for order in orders:
                if order.status == criterion.name:
                    total_price += order.price * order.quantity
        else:
            for order in orders:
                    total_price += order.price * order.quantity
        cache = getCache(total_price)
        if cache != None:
            return {"total_price": float(cache)}
        setCache(total_price)
        return {"total_price": total_price}
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))