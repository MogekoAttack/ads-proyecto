from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet

from catalogo.models import MaterialAPIViewSet

from e_gobierno.models import GeneralAPIViewSet as EGobiernoGeneral
from e_gobierno.models import ReporteAPIViewSet as EGobiernoReporte

from e_ia.models import GeneralAPIViewSet as EIAGeneral
from e_ia.models import ReporteAPIViewSet as EIAReporte

from e_norte.models import GeneralAPIViewSet as ENorteGeneral
from e_norte.models import ReporteAPIViewSet as ENorteReporte

from e_sur.models import GeneralAPIViewSet as ESurGeneral
from e_sur.models import ReporteAPIViewSet as ESurReporte

# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (such as pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)
api_router.register_endpoint('material', MaterialAPIViewSet)
#################################################################################
# Elemento                                                                      #
#################################################################################
api_router.register_endpoint('egobierno_general', EGobiernoGeneral)
api_router.register_endpoint('egobierno_reporte', EGobiernoReporte)
#################################################################################
# Elemento                                                                      #
#################################################################################
api_router.register_endpoint('eia_general', EIAGeneral)
api_router.register_endpoint('eia_reporte', EIAReporte)
#################################################################################
# Elemento                                                                      #
#################################################################################
api_router.register_endpoint('enorte_general', ENorteGeneral)
api_router.register_endpoint('enorte_reporte', ENorteReporte)
#################################################################################
# Elemento                                                                      #
#################################################################################
api_router.register_endpoint('esur_general', ESurGeneral)
api_router.register_endpoint('esur_reporte', ESurReporte)