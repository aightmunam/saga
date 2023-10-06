from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.UUIDField(pk=True)
    email = fields.CharField(max_length=100, unique=True)
    password_hash = fields.CharField(max_length=128, null=True)
    first_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    is_blocked = fields.BooleanField(default=False)
    is_verified = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    verified_at = fields.DatetimeField(null=True)

    def __str__(self):
        return f'{self.email} - {self.full_name}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class PydanticMeta:
        exclude = ('created_at', 'verified_at', 'password_hash')
        computed = ('full_name',)
