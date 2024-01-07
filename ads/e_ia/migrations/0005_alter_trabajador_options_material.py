# Generated by Django 5.0 on 2024-01-07 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalogo", "0002_alter_material_cantidad_and_more"),
        ("e_ia", "0004_alter_reporte_options_trabajador"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="trabajador",
            options={
                "verbose_name": "Trabajador del edificio de ia",
                "verbose_name_plural": "Trabajadores del edificio de ia",
            },
        ),
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
                        related_name="materiales_ia",
                        to="catalogo.material",
                        verbose_name="Seleccione uno de la lista",
                    ),
                ),
            ],
            options={
                "verbose_name": "Material del edificio de ia",
                "verbose_name_plural": "Materiales del edificio de ia",
            },
        ),
    ]
