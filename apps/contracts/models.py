# Python imports
# from datetime import datetime

# Django imports
from django.db import models
from django.utils import timezone

# models

from apps.user.models import User


class Contratos(models.Model):

    numero_contrato = models.CharField(max_length=100)
    entidad = models.CharField(max_length=100)
    objeto = models.CharField(max_length=255)
    plazo_de_ejecucion = models.DateTimeField()
    supervisor = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)  # (En progreso - Finalizado)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # @property
    # Valor total	Int	Valor del contrato 	Calculo de OT
    @property
    def dias_de_entrega_restantes(self):
        dias = (self.plazo_de_ejecucion - timezone.now()).days
        return dias if dias > 0 else 0

    def __str__(self):
        return f'{self.id} - No contrato: {self.numero_contrato}'


class OrdenDeTrabajo(models.Model):

    numero_de_orden = models.IntegerField()
    item = models.CharField(max_length=255)
    valor_unitario = models.IntegerField()
    cantidad = models.IntegerField()
    numero_de_contrato = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)  # (En progeso - Finalizado)
    # (Masculino - Femenino - Unisex - N/A)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - No order: {self.numero_de_orden}'


class Lotes(models.Model):

    numero_de_lote = models.IntegerField()
    numero_de_contrato = models.CharField(max_length=100)
    numero_de_orden = models.IntegerField()
    talla = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    # ( "Nadie"-Corte - Confeccion - Finalizado)
    asignado = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)  # (En progeso - Finalizado)
    fecha_recibido = models.DateTimeField()
    historial = models.CharField(max_length=100)
    novedad = models.CharField(max_length=100)


class Personal(models.Model):

    Usuario = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
