from django.contrib import admin
from .models import (Holiday, Location, Place, Option, LocationType, RoomType, AccommodationType,
                     Accommodation, AccommodationRoom, HotelRoom, AccommodationAttribute,
                     HotelRoomAttribute, AccommodationRoomAttribute,
                     AccommodationDatePrice, HotelRoomDatePrice)


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    model = Holiday
    list_display = ['date', 'description']
    search_fields = ['date']


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


class OptionTabularInline(admin.TabularInline):
    model = Option
    fields = ['title', 'is_free', 'price']
    extra = 0


class HotelRoomTabularInline(admin.TabularInline):
    model = HotelRoom
    fields = ('room_number', 'size', 'room_type', 'room_star',
              'capacity', 'currency', 'base_price', 'description')
    extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = Place
    inlines = [OptionTabularInline, HotelRoomTabularInline]
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


class AccommodationRoomTabularInline(admin.TabularInline):
    model = AccommodationRoom
    fields = ['title', 'room_type', 'size', 'description']
    extra = 0


@admin.register(AccommodationAttribute)
class AccommodationAttributeAdmin(admin.ModelAdmin):
    model = AccommodationAttribute
    list_display = ('title', 'description')
    search_fields = ('title',)
    extra = 0


class AccommodationDatePriceTabularInline(admin.TabularInline):
    model = AccommodationDatePrice
    fields = ('date', 'is_reserve', 'price', 'currency',)
    extra = 0


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    model = Accommodation
    search_fields = ['title']
    list_display = ['id', 'title', 'base_price', 'place', 'standard_capacity', 'build_size']
    list_filter = ['owner', 'location_type', 'accommodation_type',
                   'standard_capacity', 'maximum_capacity']
    inlines = [AccommodationRoomTabularInline, AccommodationDatePriceTabularInline]


# @admin.register(AccommodationAttribute)
# class AccommodationAttributeAdmin(admin.ModelAdmin):
#     model = AccommodationAttribute


@admin.register(HotelRoomAttribute)
class HotelRoomAttributeAdmin(admin.ModelAdmin):
    model = HotelRoomAttribute
    search_fields = ['title']


@admin.register(AccommodationRoomAttribute)
class RoomAttributeAdmin(admin.ModelAdmin):
    model = AccommodationRoomAttribute
    search_fields = ['title']


class HotelRoomDatePriceTabularInline(admin.TabularInline):
    model = HotelRoomDatePrice
    fields = ('date', 'is_reserve', 'price', 'currency')


class HotelRoomAdmin(admin.ModelAdmin):
    model = HotelRoom
    search_fields = ['place__location__city']
    inlines = [HotelRoomDatePriceTabularInline]
