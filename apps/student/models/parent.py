import uuid
from django.db.models import Model, UUIDField, CharField, ForeignKey, CASCADE


class Parent(Model):
    id = UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    mother_name = CharField("Nome da Mãe", max_length=100)
    father_name = CharField("Nome do Pai", max_length=100)
    phone = CharField("Telefone", max_length=11, null=True, blank=True)
    address = ForeignKey("core.Address", verbose_name="Endereço", on_delete=CASCADE)

    class Meta:
        verbose_name = "Responsável"
        verbose_name_plural = "Responsáveis"

    def __str__(self):
        return (
            f"{self.mother_name} e {self.father_name}"
            if self.father_name
            else self.mother_name
        )
