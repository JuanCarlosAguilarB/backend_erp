# Django imports
from django.urls import path, include

# Views imports
from apps.contracts.views import (
    ListContrats, OrdenOfWorkView,
    PersonasView, LotView, PersonasMeView,
    OrdenDeTrabajoPorContrato, LotesDeTrabajoPorContrato,
    LotesDeTrabajoPorOrdenDeTrabajo, LotesDeTrabajoAsignado, SatelitesView, 
    ExcelGeneratorView)

# import router of drf
from rest_framework import routers

# router
router = routers.DefaultRouter()
router.register(r'lotes', LotView, basename='lotes')
router.register(r'orden_de_trabajo', OrdenOfWorkView, basename='orden_of_work')
router.register(r'personas', PersonasView, basename='items')
router.register(r'contract', ListContrats, basename='contracts')
router.register(r'satelites', SatelitesView, basename='satelites')

urlpatterns = [
    # path('contracts/', ListContrats.as_view(), name='list-contracts'),
    path('personas/me/', PersonasMeView.as_view(), name='list-contract'),
    path('orden_de_trabajo/<int:id>/lotes/',
         LotesDeTrabajoPorOrdenDeTrabajo.as_view(),
         name='list-contract_'),
    path('lotes/asignado/<str:area>/',
         LotesDeTrabajoAsignado.as_view(),
         name='list-contract_'),
    path('contract/<int:id>/orden_de_trabajo',
         OrdenDeTrabajoPorContrato.as_view(), name='list-contracts_'),
    path('contract/<int:id>/lotes',
         LotesDeTrabajoPorContrato.as_view(), name='list-lotes_'),
    path('', include(router.urls)),
    path('excel/', ExcelGeneratorView.as_view(), name='excel'),
]
