from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from .models import Order


OrderPydantic = pydantic_model_creator(Order)
OrderInPydantic = pydantic_model_creator(
    Order, name='OrderIn', exclude_readonly=True, exclude=('create_date', 'last_modified')
)
OrderPydanticList = pydantic_queryset_creator(Order, name='OrderList')
