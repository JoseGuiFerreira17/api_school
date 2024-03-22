import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import (
    UUIDField,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    EmailField,
    ForeignKey,
    PROTECT,
)
from apps.accounts.managers import UserManager
from apps.core.validators import validate_cpf


class User(AbstractBaseUser, PermissionsMixin):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(verbose_name="nome completo", max_length=255)
    email = EmailField(verbose_name="endereço de e-mail", unique=True)
    phone = CharField(verbose_name="telefone", max_length=20, blank=True, null=True)
    birth_date = DateField(verbose_name="data de nascimento", blank=True, null=True)
    cpf = CharField(
        verbose_name="CPF",
        max_length=14,
        blank=True,
        null=True,
        validators=[validate_cpf],
    )
    address = ForeignKey(
        "core.Address",
        verbose_name="endereço",
        on_delete=PROTECT,
        blank=True,
        null=True,
        related_name="user_address",
    )

    is_staff = BooleanField(verbose_name="Pode acessar o painel", default=True)
    is_active = BooleanField(verbose_name="ativo", default=True)
    created_at = DateTimeField(verbose_name="criado em", auto_now_add=True)
    modified_at = DateTimeField(verbose_name="modificado em", auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["name", "-created_at"]

    def __str__(self):
        return self.name
