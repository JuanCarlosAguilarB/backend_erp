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
from apps.contracts.models import Contract, Entity, OrdenOfWork

# serializers
from apps.contracts.serializers import ContractSerializer


class ListContrats(generics.ListAPIView):
    """
    List all contracts
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the contracts
    #     for the currently authenticated user.
    #     """
    #     user = self.request.user
    #     return Contract.objects.filter(supervisor=user)
