from enum import Enum

from tortoise.models import Model
from tortoise import fields


class OrderStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    CANCELLED = "cancelled"
    FAILED = "failed"
    PREPARING = "preparing"
    READY = "ready"


class Order(Model):
    id = fields.UUIDField(pk=True)
    user_id = fields.UUIDField()
    status = fields.CharEnumField(max_length=50, enum_type=OrderStatus, default=OrderStatus.PENDING.value)
    create_date = fields.DatetimeField(auto_now_add=True)
    last_modified = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.status}"
