# Generated by Django 5.0 on 2024-01-02 01:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="General",
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
                ("avance", models.IntegerField(default=0, verbose_name="Avances")),
                (
                    "progreso",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, message="El valor debe ser igual o mayor a 0."
                            ),
                            django.core.validators.MaxValueValidator(
                                100, message="El valor debe ser igual o menor a 100."
                            ),
                        ],
                        verbose_name="Porcentaje de avance",
                    ),
                ),
                ("presupuesto", models.IntegerField(verbose_name="Presupuesto")),
            ],
        ),
        migrations.CreateModel(
            name="Reporte",
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
                    models.CharField(
                        max_length=32, verbose_name="Nombre de la actualización"
                    ),
                ),
                (
                    "fecha_actual",
                    models.DateField(
                        default=models.DateField(auto_now_add=True),
                        editable=False,
                        verbose_name="Fecha Actual",
                    ),
                ),
                (
                    "archivo",
                    models.FileField(upload_to="", verbose_name="Documento de datos"),
                ),
                (
                    "actualizador",
                    models.CharField(
                        max_length=64, verbose_name="Nombre de quien hace este reporte"
                    ),
                ),
            ],
            options={
                "verbose_name": "Reporte",
                "verbose_name_plural": "Listado de reportes",
            },
        ),
    ]
