# Django imports
from django.urls import path, include

# Views imports
from apps.contracts.views import ListContrats

urlpatterns = [
    path('contracts/', ListContrats.as_view(), name='list-contracts'),
]
