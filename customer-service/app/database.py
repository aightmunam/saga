from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url='postgres://customer:customer@customer-postgres:5432/customer',
        modules={'models': ['app.users.models']},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    Tortoise.init_models(['app.users.models'], 'models')


TORTOISE_ORM = {
    'connections': {'default': 'postgres://customer:customer@customer-postgres:5434/customer'},
    'apps': {
        'models': {
            'models': ['app.users.models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}