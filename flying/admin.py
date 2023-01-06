from django.contrib import admin
from .models import Currency, CurrencyExchange


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    model = Currency


@admin.register(CurrencyExchange)
class CurrencyExchangeAdmin(admin.ModelAdmin):
    model = CurrencyExchange
    list_filter = ['currency_from', 'currency_to']
