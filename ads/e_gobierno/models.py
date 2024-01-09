from django.db.models.signals import pre_save, post_save
from django.db import models
from django.dispatch import receiver
from django.contrib import messages

from django.core.validators import MinValueValidator, MaxValueValidator

from wagtail.api.v2.views import BaseAPIViewSet
from wagtail.api import APIField
from wagtail.api.v2.filters import OrderingFilter, FieldsFilter
from modelcluster.models import ClusterableModel

from modelcluster.models import ClusterableModel

from rest_framework import serializers

#################################################################################
# Elemento                                                                      #
#################################################################################
class General(models.Model):
    class Meta:
        verbose_name = "General gobierno"
    avance = models.IntegerField(
        default=0,
        verbose_name="Avances",
        blank=False,
        editable=False,
    )

    progreso = models.IntegerField(
        default=0,
        verbose_name="Porcentaje de avance",
        validators=[
            MinValueValidator(0, message="El valor debe ser igual o mayor a 0."),
            MaxValueValidator(100, message="El valor debe ser igual o menor a 100."),
        ],
        blank=False,
    )
    
    presupuesto = models.IntegerField(
        verbose_name="Presupuesto",
        blank=False,
        validators=[
            MinValueValidator(0, message="El valor debe ser igual o mayor a 0."),
        ],
    )

    api_fields = [
        APIField('avance'),
        APIField('progreso'),
        APIField('presupuesto'),
    ]

class GeneralAPIViewSet(BaseAPIViewSet):
    body_fields = BaseAPIViewSet.body_fields + [
        "avance",
        "progreso",
        "presupuesto",
    ]

    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "avance",
        "progreso",
        "presupuesto",
    ]

    filter_backends = [
        FieldsFilter,
        OrderingFilter,
    ]

    name = "general"
    model = General

#################################################################################
# Elemento                                                                      #
#################################################################################
class Trabajador(models.Model):
    nombre = models.ForeignKey(
        "catalogo.Trabajador",
        verbose_name = "Seleccione uno de la lista",
        on_delete = models.CASCADE,
        related_name='trabajadores_gobierno',
    )
    class Meta:
        verbose_name = "Trabajador del edificio de gobierno"
        verbose_name_plural = "Trabajadores del edificio de gobierno"

#################################################################################
# Elemento                                                                      #
#################################################################################        
class Material(models.Model):
    nombre = models.ForeignKey(
        "catalogo.Material",
        verbose_name = "Seleccione uno de la lista",
        on_delete = models.CASCADE,
        related_name='materiales_gobierno',
    )
    class Meta:
        verbose_name = "Material del edificio de gobierno"
        verbose_name_plural = "Materiales del edificio de gobierno"
        
class MaterialSerializer(serializers.Serializer):
    class Meta:
        model = Material
        fields = ("nombre",)

#################################################################################
# Elemento                                                                      #
#################################################################################
class Reporte(ClusterableModel):
    nombre = models.CharField(
        verbose_name="Nombre de la actualización",
        max_length=32,  
    )
    
    fecha_actual = models.DateField(
        default=models.DateField(auto_now_add=True),
        verbose_name="Fecha Actual",
        editable=False,
    )
    
    archivo = models.FileField(
        verbose_name="Documento de datos",
    )
    
    actualizador = models.CharField(
        verbose_name="Nombre de quien hace este reporte",
        max_length=64,
        blank=False,
    )
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Reporte gobierno"
        verbose_name_plural = "Listado de reportes"
    
class ReporteAPIViewSet(BaseAPIViewSet):
    body_fields = BaseAPIViewSet.body_fields + [
        "nombre",
        "fecha_actual",
        "archivo",
        "actualizador",
    ]

    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "nombre",
        "fecha_actual",
        "archivo",
        "actualizador",
    ]

    filter_backends = [
        FieldsFilter,
        OrderingFilter,
    ]

    name = "reporte"
    model = Reporte