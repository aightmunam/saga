import uuid

from fastapi import FastAPI

from .orders.models import Order
from .orders.schemas import OrderInPydantic, OrderPydantic, OrderPydanticList

from .database import init_db


app = FastAPI()
init_db(app)


@app.post('/orders/', response_model=OrderPydantic)
async def place_order(order: OrderInPydantic):
    order = await Order.create(**order.dict(exclude_unset=True))
    return await OrderPydantic.from_tortoise_orm(order)


@app.get('/orders/{order_id}/', response_model=OrderPydantic)
async def get_order(order_id: uuid.UUID):
    return await OrderPydantic.from_queryset_single(Order.get(id=order_id))


@app.get('/orders/', response_model=OrderPydanticList)
async def get_orders():
    return await OrderPydanticList.from_queryset(Order.all())
