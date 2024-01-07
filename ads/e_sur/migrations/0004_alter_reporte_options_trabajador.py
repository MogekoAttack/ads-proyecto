# Generated by Django 5.0 on 2024-01-07 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalogo", "0002_alter_material_cantidad_and_more"),
        ("e_sur", "0003_alter_general_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reporte",
            options={
                "verbose_name": "Reporte Sur",
                "verbose_name_plural": "Listado de reportes",
            },
        ),
        migrations.CreateModel(
            name="Trabajador",
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
                        related_name="trabajadores_sur",
                        to="catalogo.trabajador",
                        verbose_name="Seleccione uno de la lista",
                    ),
                ),
            ],
            options={
                "verbose_name": "Trabajador del edificio de gobierno",
                "verbose_name_plural": "Trabajadores del edificio de gobierno",
            },
        ),
    ]
