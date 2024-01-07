# Rest imports
from rest_framework import serializers

# models
from apps.contracts.models import (
    Contratos, OrdenDeTrabajo,
    Lotes)

from apps.user.models import User


class ContratosSerializer(serializers.ModelSerializer):

    tiempo_restante = serializers.CharField(
        source='dias_de_entrega_restantes', read_only=True)

    class Meta:
        model = Contratos
        fields = '__all__'


class OrdenDeTrabajoSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdenDeTrabajo
        fields = '__all__'


class LotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lotes
        fields = '__all__'
        


class PersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)
