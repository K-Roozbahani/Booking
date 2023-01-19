from django.contrib import admin
from .models import Order, PlaceItem, FlyItem


class PlaceItemTabularInline(admin.TabularInline):
    model = PlaceItem
    fields = ['is_valid', 'items']
    extra = 0


class FlyItemTabularInline(admin.TabularInline):
    model = FlyItem
    fields = ['is_valid', 'items']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [PlaceItemTabularInline, FlyItemTabularInline]
