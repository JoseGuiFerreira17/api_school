# Generated by Django 5.0.3 on 2024-03-21 14:43

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("street", models.CharField(max_length=100, verbose_name="Rua")),
                ("number", models.CharField(max_length=10, verbose_name="Número")),
                ("neighborhood", models.CharField(max_length=100, verbose_name="Bairro")),
                ("city", models.CharField(max_length=100, verbose_name="Cidade")),
                ("state", models.CharField(max_length=2, verbose_name="Estado")),
                ("zip_code", models.CharField(max_length=8, verbose_name="CEP")),
            ],
        ),
    ]
