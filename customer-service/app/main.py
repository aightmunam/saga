import uuid

from fastapi import FastAPI

from .users.models import User
from .users.schemas import UserInPydantic, UserPydantic

from .database import init_db


app = FastAPI()
init_db(app)


@app.post('/users/', response_model=UserPydantic)
async def register_user(user: UserInPydantic):
    user = await User.create(**user.dict(exclude_unset=True), id=uuid.uuid4())
    return await UserPydantic.from_tortoise_orm(user)


@app.get('/users/{pk}/', response_model=UserPydantic)
async def get_user(pk: uuid.UUID):
    return await UserPydantic.from_queryset_single(User.get(id=pk))

