from django.contrib import admin
from .models import PlaceOrder


@admin.register(PlaceOrder)
class PlaceOrderAdmin(admin.ModelAdmin):
    model = PlaceOrder
    search_fields = ['user__username', 'create_date']
    list_filter = ['status']

# class AccommodationOrderAdmin(admin.ModelAdmin):
#     model = AccommodationOrder
#     search_fields = ['user__username', 'create_date']
#     list_filter = ['status']
