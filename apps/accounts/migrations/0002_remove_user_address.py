# Generated by Django 5.0.3 on 2024-03-23 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="address",
        ),
    ]
