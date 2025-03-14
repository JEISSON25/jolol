from rest_framework.routers import DefaultRouter
from django.urls import path, include

# Importamos los ViewSet de cada app
from apps.estudiantes.views import EstudianteViewSet
from apps.empresas.views import EmpresaViewSet
from apps.candidatos.views import CandidatoViewSet, VotoViewSet
from apps.mesas.views import MesaViewSet
from apps.puestos.views import DetailPuestoVotacionViewSet, PuestoVotacionViewSet

# Creamos el router y registramos cada ruta
router = DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet, basename='estudiantes')
router.register(r'empresas', EmpresaViewSet, basename='empresas')
router.register(r'candidatos', CandidatoViewSet, basename='candidatos')
router.register(r'votos', VotoViewSet, basename='votos')
router.register(r'mesas', MesaViewSet, basename='mesas')
router.register(r'puesto', PuestoVotacionViewSet, basename='puesto')
router.register(r'detailpuesto', DetailPuestoVotacionViewSet, basename='detailpuesto')

urlpatterns = [
    path('', include(router.urls)),
]
