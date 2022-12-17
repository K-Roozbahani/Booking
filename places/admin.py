from django.contrib import admin
from .models import (Location, Place, LocationType, RoomType, AccommodationType,
                     Accommodation, Room, AccommodationAttribute,
                     RoomAttribute, DatePrice, AccommodationDatePrice, RoomDatePrice)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ['id', 'country', 'city']
    list_filter = ['country']
    search_fields = ['city']


@admin.register(LocationType)
class LocationTypeAdmin(admin.ModelAdmin):
    model = LocationType
    search_fields = ['title']
    list_display = ['id', 'title', 'is_valid']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = Place
    list_display = ['id', 'title', 'location', 'place_type']
    list_filter = ['id', 'title', 'location']
    search_fields = ['id', 'title']


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    model = RoomType
    search_fields = ['title']
    list_display = ['id', 'title', 'is_valid']


@admin.register(AccommodationType)
class AccommodationTypeAdmin(admin.ModelAdmin):
    model = AccommodationType
    search_fields = ['title']
    list_display = ['id', 'title']


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    model = Accommodation
    search_fields = ['title']
    list_display = ['id', 'title', 'base_price', 'owner', 'standard_capacity', 'build_size']
    list_filter = ['owner', 'location_type', 'accommodation_type',
                   'standard_capacity', 'maximum_capacity']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'accommodation']


@admin.register(AccommodationAttribute)
class AccommodationAttributeAdmin(admin.ModelAdmin):
    model = AccommodationAttribute


@admin.register(RoomAttribute)
class RoomAttributeAdmin(admin.ModelAdmin):
    model = RoomAttribute


@admin.register(AccommodationDatePrice)
class AccommodationDatePriceAdmin(admin.ModelAdmin):
    model = AccommodationDatePrice


@admin.register(RoomDatePrice)
class RoomDatePriceAdmin(admin.ModelAdmin):
    model = RoomDatePrice
