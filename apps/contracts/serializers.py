# Rest imports
from rest_framework import serializers

# models
from apps.contracts.models import (
    Contract, OrdenOfWork,
    ItemsOrdenOfWork, Size, StateLot,
    NoteLot, Lot)


class ContractSerializer(serializers.ModelSerializer):

    entity = serializers.StringRelatedField()

    class Meta:
        model = Contract
        fields = '__all__'


class ItemsOrdenOfWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemsOrdenOfWork
        fields = '__all__'


class OrdenOfWorkSerializer(serializers.ModelSerializer):

    items = ItemsOrdenOfWorkSerializer(source='ordenofwork_set', many=True)

    class Meta:
        model = OrdenOfWork
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'


class StateLotSerializer(serializers.ModelSerializer):

    class Meta:
        model = StateLot
        fields = '__all__'


class NoteLotSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoteLot
        fields = '__all__'


class LotSerializer(serializers.ModelSerializer):

    size = SizeSerializer()
    note = NoteLotSerializer()
    state = StateLotSerializer()

    class Meta:
        model = Lot
        fields = '__all__'
