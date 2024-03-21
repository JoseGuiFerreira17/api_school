import uuid
from django.db.models import Model, UUIDField, CharField, DateField, ForeignKey, FileField, CASCADE
from core.utils import GENDER_CHOICE

def upload_to(instance, filename, dir):
    return f"{dir}/{instance.pk}/{filename}"



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
        return self.name


class Student(Model):
    id = UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    registration = CharField("Matrícula", max_length=10, null=True, blank=True)
    name = CharField("Nome", max_length=100)
    gender = CharField("Sexo", max_length=9, choices=GENDER_CHOICE)
    birth_date = DateField("Data de Nascimento")
    rg = CharField("RG", max_length=9, null=True, blank=True)
    cpf = CharField("CPF", max_length=11)
    parent = ForeignKey("student.Parent", verbose_name="Informações dos responsáveis", on_delete=CASCADE)
    flie_rg = FileField("Arquivo RG", upload_to=upload_to(dir="rg"), blank=True, null=True)
    file_cpf = FileField("Arquivo CPF",upload_to=upload_to(dir="cpf"), blank=True, null=True)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return self.name if not self.registration else f"{self.registration}-{self.name}"
    
    @property
    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    
