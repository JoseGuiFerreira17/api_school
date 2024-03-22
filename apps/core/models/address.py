import uuid
from django.db.models import Model, UUIDField, CharField
from apps.core.utils import STATE_CHOICE


class Address(Model):
    id = UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    street = CharField("Rua", max_length=100)
    number = CharField("Número", max_length=10)
    neighborhood = CharField("Bairro", max_length=100)
    city = CharField("Cidade", max_length=100)
    state = CharField("Estado", max_length=2, choices=STATE_CHOICE)
    zip_code = CharField("CEP", max_length=8)

    def __str__(self):
        return self.street
