# Generated by Django 5.0 on 2024-01-07 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalogo", "0002_alter_material_cantidad_and_more"),
        ("e_gobierno", "0004_alter_reporte_options_alter_general_avance_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Material",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="materiales_gobierno",
                        to="catalogo.material",
                        verbose_name="Seleccione uno de la lista",
                    ),
                ),
            ],
            options={
                "verbose_name": "Material del edificio de gobierno",
                "verbose_name_plural": "Materiales del edificio de gobierno",
            },
        ),
    ]
