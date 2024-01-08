from rest_framework.permissions import AllowAny  # Importar AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
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
    Lotes)

from apps.user.models import User

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
    queryset = User.objects.all()
    serializer_class = PersonalSerializer
    # permission_classes = [permissions.IsAuthenticated]


class LotView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lotes.objects.all()
    serializer_class = LotesSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PersonasMeView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = PersonalSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        print(user)

        data = {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.area,
            'cargo': user.cargo,
        }
        return Response(data, status=status.HTTP_200_OK)


class OrdenDeTrabajoPorContrato(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    permission_classes = [AllowAny]  # Permitir cualquier persona

    def get(self, request, format=None, *args, **kwargs):

        id = kwargs['id']
        contrato = Contratos.objects.filter(id=id).first()

        if not contrato:
            return Response({'detail': 'No existe el contrato'},
                            status=status.HTTP_400_BAD_REQUEST)

        ordenes_de_trabajo = OrdenDeTrabajo.objects.filter(
            numero_de_contrato=contrato.numero_contrato)

        # Paginar los resultados
        paginator = PageNumberPagination()
        paginated_ordenes = paginator.paginate_queryset(
            ordenes_de_trabajo, request)

        data = OrdenDeTrabajoSerializer(paginated_ordenes, many=True).data

        return paginator.get_paginated_response(data)


class LotesDeTrabajoPorContrato(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [AllowAny]  # Permitir cualquier persona

    def get(self, request, format=None, *args, **kwargs):
        id = kwargs['id']
        contrato = Contratos.objects.filter(id=id).first()

        if not contrato:
            return Response({'detail': 'No existe el contrato'},
                            status=status.HTTP_400_BAD_REQUEST)

        lotes_de_trabajo = Lotes.objects.filter(
            numero_de_contrato=contrato.numero_contrato)

        # Paginar los resultados
        paginator = PageNumberPagination()
        paginated_lotes = paginator.paginate_queryset(
            lotes_de_trabajo, request)

        data = LotesSerializer(paginated_lotes, many=True).data

        return paginator.get_paginated_response(data)
