# Generated by Django 5.0 on 2024-01-07 04:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("e_sur", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="general",
            name="presupuesto",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        0, message="El valor debe ser igual o mayor a 0."
                    )
                ],
                verbose_name="Presupuesto",
            ),
        ),
    ]