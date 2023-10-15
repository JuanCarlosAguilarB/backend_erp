# Django imports
from django.urls import path, include

# Views imports
from apps.contracts.views import ListContrats, OrdenOfWorkView, ItemsOrdenOfWorkView, LotView

urlpatterns = [
    path('contracts/', ListContrats.as_view(), name='list-contracts'),
    path('orden_of_work/', OrdenOfWorkView.as_view()),
    path('items/', ItemsOrdenOfWorkView.as_view()),
    path('lot/', LotView.as_view()),
]
