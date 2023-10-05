from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise


def init_db(app: FastAPI) -> None:
    Tortoise.init_models(['app.users.models'], 'models')
    register_tortoise(
        app,
        db_url='postgres://order:order@order-postgres:5432/order',
        modules={'models': ['app.users.models']},
        generate_schemas=True,
        add_exception_handlers=True,
    )


TORTOISE_ORM = {
    'connections': {'default': 'postgres://order:order@order-postgres:5432/order'},
    'apps': {
        'models': {
            'models': ['app.users.models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}