from django.contrib import admin
from .models import HotelRoomOrder, AccommodationOrder


class HotelOrderAdmin(admin.ModelAdmin):
    model = HotelRoomOrder
    search_fields = ['user__username', 'create_date']
    list_filter = ['status']


class AccommodationOrderAdmin(admin.ModelAdmin):
    model = AccommodationOrder
    search_fields = ['user__username', 'create_date']
    list_filter = ['status']

