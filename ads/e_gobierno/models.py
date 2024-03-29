from django.db.models.signals import pre_save, post_save
from django.db import models
from django.dispatch import receiver
from django.contrib import messages

from django.core.validators import MinValueValidator, MaxValueValidator

from wagtail.api.v2.views import BaseAPIViewSet
from wagtail.api.v2.filters import OrderingFilter, FieldsFilter
from modelcluster.models import ClusterableModel

from catalogo.models import Material
from modelcluster.models import ClusterableModel

#################################################################################
# Elemento                                                                      #
#################################################################################
class General(models.Model):
    avance = models.IntegerField(
        default=0,
        verbose_name="Avances",
        blank=False,
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
    )

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
    )
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Listado de reportes"
    
