# Rest imports
from rest_framework import serializers

# models
from apps.contracts.models import Contract, Entity, OrdenOfWork


class ContractSerializer(serializers.ModelSerializer):

    entity = serializers.StringRelatedField()

    class Meta:
        model = Contract
        fields = '__all__'
