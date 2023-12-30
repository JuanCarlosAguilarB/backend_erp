# Django imports
from django.urls import path, include

# Views imports
from apps.contracts.views import ListContrats, OrdenOfWorkView, PersonasView, LotView

# import router of drf
from rest_framework import routers

# router
router = routers.DefaultRouter()
router.register(r'lotes', LotView, basename='lotes')
router.register(r'orden_de_trabajo', OrdenOfWorkView, basename='orden_of_work')
router.register(r'personas', PersonasView, basename='items')
router.register(r'contract', ListContrats, basename='contracts')

urlpatterns = [
    # path('contracts/', ListContrats.as_view(), name='list-contracts'),
    path('', include(router.urls)),

]
