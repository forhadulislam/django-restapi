# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from payment.models import Accounts, Transfers, Transactions, Merchants

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'balance','reserved','currency')

class MerchantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','country','mcc')

class TransfersAdmin(admin.ModelAdmin):
    pass

class TransactionsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Accounts, AccountsAdmin)
admin.site.register(Transfers, TransfersAdmin)
admin.site.register(Merchants, MerchantsAdmin)
admin.site.register(Transactions, TransactionsAdmin)

