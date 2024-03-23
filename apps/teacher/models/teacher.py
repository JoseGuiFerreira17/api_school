from django.db.models import CharField, ForeignKey, PROTECT
from apps.accounts.models import User
from apps.core.utils import GENDER_CHOICE, DEGREE_CHOICE


class Teacher(User):
    gender = CharField(
        "gênero", max_length=9, choices=GENDER_CHOICE, null=True, blank=True
    )
    degree = CharField(
        "formação", max_length=255, choices=DEGREE_CHOICE, null=True, blank=True
    )
    address = ForeignKey(
        "core.Address",
        verbose_name="endereço",
        on_delete=PROTECT,
        blank=True,
        null=True,
        related_name="user_address",
    )

    class Meta:
        verbose_name = "professor"
        verbose_name_plural = "professores"
        ordering = ("name",)

    def __str__(self):
        if self.degree:
            return f"Prof. {self.degree} {self.name}"
        return f"Prof. {self.name}"
