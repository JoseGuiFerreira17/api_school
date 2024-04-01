import uuid
from django.db.models import Model, UUIDField, CharField, ForeignKey, CASCADE


class Discipline(Model):
    id = UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField("Nome", max_length=100)
    workload = CharField("Carga Horária", max_length=100)
    teacher = ForeignKey(
        "teacher.Teacher",
        verbose_name="Professor",
        on_delete=CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

    def __str__(self):
        return f"{self.name} - {self.teacher}" if self.teacher else self.name
