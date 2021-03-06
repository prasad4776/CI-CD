# Generated by Django 2.2.13 on 2020-06-17 08:56

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("module", models.CharField(max_length=20)),
                ("kind", models.CharField(max_length=20)),
                ("priority", models.PositiveIntegerField()),
                ("filters", django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
        )
    ]
