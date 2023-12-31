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


class PersonasMeView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        print(user)
        persona = Personal.objects.filter(user=user).first()

        data = {
            'id': user.id,
            # 'username': user.username,
            # 'email': user.email,
            'phone': user.phone,
            'photo': user.photo.url if user.photo else '',
            'first_name': user.first_name,
            'last_name': user.last_name,
            'cargo': persona.cargo if persona else None,
        }
        return Response(data, status=status.HTTP_200_OK)


class OrdenDeTrabajoPorContrato(APIView, LimitOffsetPagination):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def get(self, request, format=None, *args, **kwargs):

        id = kwargs['id']
        contrato = Contratos.objects.filter(id=id).first()

        if not contrato:
            return Response({'detail': 'No existe el contrato'},
                            status=status.HTTP_400_BAD_REQUEST)

        ordenes_de_trabajo = OrdenDeTrabajo.objects.filter(
            numero_de_contrato=contrato.numero_contrato)

        data = OrdenDeTrabajoSerializer(ordenes_de_trabajo, many=True).data

        return Response(data, status=status.HTTP_200_OK)
