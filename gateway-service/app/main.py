import uuid

from fastapi import FastAPI, APIRouter
from starlette import status
from starlette.requests import Request
from starlette.responses import Response
from fastapi_gateway import route


app = FastAPI(title="API Gateway Service")
router1 = APIRouter()


ORDER_SERVICE_URL = "http://order-service:8001"
CUSTOMER_SERVICE_URL = "http://customer-service:8002"


@route(
    request_method=router1.get,
    service_url=ORDER_SERVICE_URL,
    gateway_path='/users/{user_id}/orders/',
    service_path='/users/{user_id}/orders/',
    status_code=status.HTTP_200_OK,
    override_headers=False,
)
async def get_user_orders(user_id: uuid.UUID, request: Request, response: Response):
    pass


@route(
    request_method=router1.get,
    service_url=CUSTOMER_SERVICE_URL,
    gateway_path='/users/{pk}/',
    service_path='/users/{pk}/',
    status_code=status.HTTP_200_OK,
    override_headers=False,
)
async def get_user(pk: uuid.UUID, request: Request, response: Response):
    pass


app.include_router(router1)
