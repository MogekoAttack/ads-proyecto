from wagtail.contrib.modeladmin.options import (ModelAdmin, ModelAdminGroup, modeladmin_register,)

from catalogo.models import TipoObra as Catalogo_TipoObra
from catalogo.models import Material as Catalogo_Material
from catalogo.models import Puesto as Catalogo_Puesto
from catalogo.models import Trabajador as Catalogo_Trabajador

#################################################################################
# Menus de catalogo                                                             #
#################################################################################
class TipoObraMenu(ModelAdmin):
    model = Catalogo_TipoObra
    
class MaterialMenu(ModelAdmin):
    model = Catalogo_Material

class PuestoMenu(ModelAdmin):
    model = Catalogo_Puesto
    
class TrabajadorMenu(ModelAdmin):
    model = Catalogo_Trabajador

#################################################################################
# Botón en grupo                                                                #
#################################################################################
class CatalogoMenu(ModelAdminGroup):
    menu_label = "Catálogo"
    items = [
        TipoObraMenu,
        MaterialMenu,
        PuestoMenu,
        TrabajadorMenu,
    ]
    
modeladmin_register(CatalogoMenu)