# Generated by Django 5.0.3 on 2024-03-22 23:15

import apps.accounts.managers.user_managers
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("Masculino", "Masculino"), ("Femenino", "Femenino")],
                        max_length=9,
                        null=True,
                        verbose_name="gênero",
                    ),
                ),
                (
                    "degree",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Grad.", "Graduado"),
                            ("Esp.", "Especialista"),
                            ("Me.", "Mestre"),
                            ("Dr.", "Doutor"),
                        ],
                        max_length=255,
                        null=True,
                        verbose_name="formação",
                    ),
                ),
            ],
            options={
                "verbose_name": "professor",
                "verbose_name_plural": "professores",
                "ordering": ("name",),
            },
            bases=("accounts.user",),
            managers=[
                ("objects", apps.accounts.managers.user_managers.UserManager()),
            ],
        ),
    ]
