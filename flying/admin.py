from django.contrib import admin
from .models import Currency, CurrencyExchange, Airport, AirTravel, Flight


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    model = Currency


@admin.register(CurrencyExchange)
class CurrencyExchangeAdmin(admin.ModelAdmin):
    model = CurrencyExchange
    list_filter = ['currency_from', 'currency_to']


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    model = Airport
    search_fields = ('title', 'abbreviated_name')


class FlightAdmin(admin.ModelAdmin):
    model = Flight
    list_display = ('id', 'flight_number', 'source', 'destination', 'fly_datetime')


@admin.register(AirTravel)
class AirTravelAdmin(admin.ModelAdmin):
    model = AirTravel
    list_filter = ('origin', 'final_destination', 'is_international_flight')
