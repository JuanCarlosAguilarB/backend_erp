from django.shortcuts import render
# Create your views here.

# Rest Framework imports
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView

# models
from apps.contracts.models import (
    Contratos, OrdenDeTrabajo,
    Lotes, Personal)

# serializers
from apps.contracts.serializers import (
    ContratosSerializer, OrdenDeTrabajoSerializer,
    LotesSerializer, PersonalSerializer,
)


class ListContrats(viewsets.ModelViewSet):
    """
    List all contracts
    """
    queryset = Contratos.objects.all()
    serializer_class = ContratosSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrdenOfWorkView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OrdenDeTrabajo.objects.all()
    serializer_class = OrdenDeTrabajoSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PersonasView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    # permission_classes = [permissions.IsAuthenticated]


class LotView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lotes.objects.all()
    serializer_class = LotesSerializer
    # permission_classes = [permissions.IsAuthenticated]
