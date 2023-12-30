# Rest imports
from rest_framework import serializers

# models
from apps.contracts.models import (
    Contratos, OrdenDeTrabajo,
    Lotes, Personal)


class ContratosSerializer(serializers.ModelSerializer):

    entity = serializers.StringRelatedField()

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
        model = Personal
        fields = '__all__'
