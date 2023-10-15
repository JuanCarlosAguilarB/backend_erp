# Django imports
from django.urls import path, include

# Views imports
from apps.contracts.views import ListContrats, OrdenOfWorkView, ItemsOrdenOfWorkView, LotView

# import router of drf
from rest_framework import routers

# router
router = routers.DefaultRouter()
router.register(r'lot', LotView, basename='contract')
router.register(r'orden_of_work', OrdenOfWorkView, basename='orden_of_work')
router.register(r'items', ItemsOrdenOfWorkView, basename='items')

urlpatterns = [
    path('contracts/', ListContrats.as_view(), name='list-contracts'),
    path('', include(router.urls)),

]
