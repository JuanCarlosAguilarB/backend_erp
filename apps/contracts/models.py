# Python imports
# from datetime import datetime

# Django imports
from django.db import models
from django.utils import timezone

# models

from apps.user.models import User


class Entity(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Contract(models.Model):

    # entity = models.ForeignKey(Entity, on_delete=models.CASCADE,
    #                            null=True, blank=True)
    number_contrat = models.CharField(max_length=100, primary_key=True)
    company = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField()
    amount = models.IntegerField()
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def remaining_days(self):
        return (self.delivery_date - timezone.now()).days

    def __str__(self):
        return f'{self.id} - {self.name}'


class OrdenOfWork(models.Model):

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    number_orden = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_delivery_date = models.DateTimeField()
    amount_of_order = models.IntegerField()

    @property
    def remaining_days(self):
        return (self.delivery_date - timezone.now()).days

    # def save(self, *args, **kwargs):

    #     # sum of amount_of_order of all orders
    #     sum_amount_of_order = OrdenOfWork.objects.filter(
    #         contract=self.contract).aggregate(models.Sum('amount_of_order'))['amount_of_order__sum']

    #     # throw error if the sum of amount_of_order of all orders is greater than amount of contract
    #     if sum_amount_of_order > self.contract.amount:
    #         raise ValueError(
    #             'The amount of order is greater than amount of contract')

    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} - No order: {self.number_orden}'


class ItemsOrdenOfWork(models.Model):

    orden_of_work = models.ForeignKey(OrdenOfWork, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} - No order: {self.number_orden.number_orden}'


class Size(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)


class StateLot(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)


class NoteLot(models.Model):

    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Lot(models.Model):

    orden_of_work = models.ForeignKey(OrdenOfWork, on_delete=models.CASCADE)
    item_orden_of_work = models.ForeignKey(
        ItemsOrdenOfWork, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    amount = models.IntegerField()
    state = models.ForeignKey(StateLot, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    date_received = models.DateTimeField(null=True, blank=True)
    note = models.ForeignKey(
        NoteLot, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    @property
    def remaining_days(self):
        return (self.delivery_date - timezone.now()).days

    def save(self, *args, **kwargs):

        # # sum of amount_of_order of all orders
        # sum_amount_of_order = OrdenOfWork.objects.filter(
        #     contract=self.contract).aggregate(models.Sum('amount_of_order'))['amount_of_order__sum']

        # # throw error if the sum of amount_of_order of all orders is greater than amount of contract
        # if sum_amount_of_order > self.contract.amount:
        #     raise ValueError(
        #         'The amount of order is greater than amount of contract')

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} - No order: {self.number_orden}'
