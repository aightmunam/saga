from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from .models import User


UserPydantic = pydantic_model_creator(User)
UserInPydantic = pydantic_model_creator(
    User, name='UserIn', exclude_readonly=True
)
UserPydanticList = pydantic_queryset_creator(User, name='UserList')
