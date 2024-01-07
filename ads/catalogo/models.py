from django.db import models
from django.contrib import messages
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.api.v2.views import BaseAPIViewSet
from wagtail.api.v2.filters import OrderingFilter, FieldsFilter
from datetime import datetime
from modelcluster.models import ClusterableModel
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

import inspect
#################################################################################
# Elemento                                                                      #
#################################################################################
class TipoObra(ClusterableModel):
    nombre = models.CharField(
        verbose_name="Nombre",
        max_length=32,
        blank=False,
    )
    
    descripcion = models.CharField(
        verbose_name="Descripcción detallada",
        max_length=512,
        blank=False,
    )
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo de obra"
        verbose_name_plural = "Tipos de obra para usar"
        
#################################################################################
# Elemento                                                                      #
#################################################################################
class Material(ClusterableModel):
    nombre = models.CharField(
        verbose_name="Nombre",
        max_length=32,
        blank=False,
    )
    
    tipo = models.ForeignKey(
        TipoObra,
        verbose_name="¿En que será empleado?",
        on_delete=models.CASCADE,
    )

    descripcion = models.TextField(
        verbose_name="Descripcción (Máximo 512 caracterés)",
        max_length=512,
        blank=True,
    )

    cantidad = models.IntegerField(
        verbose_name="Cantidad",
        blank=False,
        validators=[
            MinValueValidator(0, message="El valor debe ser igual o mayor a 0."),
        ],
    )

    precio_unitario = models.IntegerField(
        verbose_name="Precio unitario (En caso de ser en gramos ingrese por kilo)",
        blank=False,
        validators=[
            MinValueValidator(0, message="El valor debe ser igual o mayor a 0."),
        ],
    )

    api_fields = [
        APIField('nombre'),
        APIField('tipo'),
        APIField('descripcion'),
        APIField('cantidad'),
        APIField('precio_unitario'),
    ]

    def clean(self):
        if self.precio_unitario < 0:
            raise ValidationError("El precio unitario no puede ser negativo")

    # panels = [FieldPanel("name"), FieldPanel("desc")]

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Listado de materiales"

class MaterialAPIViewSet(BaseAPIViewSet):
    body_fields = BaseAPIViewSet.body_fields + [
        "nombre",
        "tipo",
        "descripcion",
        "cantidad",
        "precio_unitario",
    ]

    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "nombre",
        "tipo",
        "descripcion",
        "cantidad",
        "precio_unitario",
    ]

    filter_backends = [
        FieldsFilter,
        OrderingFilter,
    ]

    name = "material"
    model = Material

        
#################################################################################
# Elemento                                                                      #
#################################################################################
class Puesto(ClusterableModel):
    nombre = models.CharField(
        verbose_name="Nombre del puesto",
        max_length=32,
        blank=False,
    )
    
    descripcion = models.TextField(
        verbose_name="Descripcción (Máximo 512 caracterés)",
        max_length=512,
        blank=True,
    )
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Puesto"
        verbose_name_plural = "Listado de puestos"

#################################################################################
# Elemento                                                                      #
#################################################################################
class Trabajador(ClusterableModel):
    nombre = models.CharField(
        verbose_name="Nombre completo",
        max_length=32,
        blank=False,
    )
    
    edad = models.IntegerField(
        verbose_name="Cantidad de años cumplidos",
        blank=False,
        validators=[
            MinValueValidator(18, message="El trabajador no puede ser menor de edad."),
        ],
    )
    
    seguridad_social = models.CharField(
        verbose_name="Número de seguridad social",
        max_length=32,
        blank=False,
    )
    
    puesto = models.ForeignKey(
        Puesto,
        verbose_name="Puesto del empleado",
        blank=False,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Listado de trabajadores"