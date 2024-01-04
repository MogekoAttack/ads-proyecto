from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from catalogo.models import TipoObra as Catalogo_TipoObra
from catalogo.models import Material as Catalogo_Material
from catalogo.models import Puesto as Catalogo_Puesto
from catalogo.models import Trabajador as Catalogo_Trabajador

from e_gobierno.models import General as EGobiernoGeneral
from e_gobierno.models import Reporte as EGobiernoReporte

from e_norte.models import General as ENorteGeneral
from e_norte.models import Reporte as ENorteReporte

from e_sur.models import General as ESurGeneral
from e_sur.models import Reporte as ESurReporte

from e_ia.models import General as EIAGeneral
from e_ia.models import Reporte as EIAReporte


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
# Menus de gobierno                                                            #
#################################################################################
class EGobiernoGeneralMenu(ModelAdmin):
    model = EGobiernoGeneral


class EGobiernoReporteMenu(ModelAdmin):
    model = EGobiernoReporte


#################################################################################
# Menus de norte                                                                #
#################################################################################
class ENorteGeneralMenu(ModelAdmin):
    model = ENorteGeneral


class ENorteReporteMenu(ModelAdmin):
    model = ENorteReporte


#################################################################################
# Menus de sur                                                                  #
#################################################################################
class ESurGeneralMenu(ModelAdmin):
    model = ESurGeneral


class ESurReporteMenu(ModelAdmin):
    model = ESurReporte


#################################################################################
# Menus de ia                                                                   #
#################################################################################
class EIAGeneralMenu(ModelAdmin):
    model = EIAGeneral


class EIAReporteMenu(ModelAdmin):
    model = ESurReporte


#################################################################################
# Botón en grupo catalogo                                                       #
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
    
#################################################################################
# Botón en grupo gobierno                                                       #
#################################################################################
class EGobiernoMenu(ModelAdminGroup):
    menu_label = "E. Gobierno"
    items = [
        EGobiernoGeneralMenu,
        EGobiernoReporteMenu,
    ]
modeladmin_register(EGobiernoMenu)

#################################################################################
# Botón en grupo norte                                                          #
#################################################################################
class ENorteMenu(ModelAdminGroup):
    menu_label = "E. Norte"
    items = [
        ENorteGeneralMenu,
        ENorteReporteMenu,
    ]
modeladmin_register(ENorteMenu)

#################################################################################
# Botón en grupo sur                                                            #
#################################################################################
class ENorteMenu(ModelAdminGroup):
    menu_label = "E. Sur"
    items = [
        ESurGeneralMenu,
        ESurReporteMenu,
    ]
modeladmin_register(ENorteMenu)

#################################################################################
# Botón en grupo ia                                                            #
#################################################################################
class EIAMenu(ModelAdminGroup):
    menu_label = "E. IA"
    items = [
        EIAGeneralMenu,
        EIAReporteMenu,
    ]
modeladmin_register(EIAMenu)