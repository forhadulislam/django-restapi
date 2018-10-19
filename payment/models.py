# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

# Some currencies list

CURRENCY_CHOICES = (
        ('EUR', 'EURO'),
        ('USD', 'US Dollar'),
    )

# Create your models here.


class Accounts(models.Model):
    id = models.CharField(max_length=128,primary_key=True, default=uuid.uuid4().hex[:8].upper(), editable=False)
    balance = models.DecimalField(decimal_places=2, max_digits=9)
    reserved = models.DecimalField(decimal_places=2, max_digits=9)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="EUR")
    
    class Meta:
        verbose_name_plural = "Accounts"


class Transfers(models.Model):
    #receiver = models.ForeignKey(Question, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Accounts)
    amount = models.DecimalField(decimal_places=2, max_digits=9, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Transfers"
    
class Transactions(models.Model):
    #transfer = models.ForeignKey(Transfers, on_delete=models.CASCADE)
    transfer = models.ForeignKey(Transfers)
    amount = models.DecimalField(decimal_places=2, max_digits=9, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Transactions"