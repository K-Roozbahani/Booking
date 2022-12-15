# from django.contrib import admin
# from .models import (LocationType, RoomType, AccommodationType,
#                      Accommodation, Room, AccommodationAttribute,
#                      RoomAttribute, DatePrice)
#
#
# @admin.register(LocationType)
# class LocationTypeAdmin(admin.ModelAdmin):
#     model = LocationType
#     search_fields = ['title']
#     list_display = ['id', 'title', 'is_valid', 'create_date']
#
#
# @admin.register(RoomType)
# class RoomTypeAdmin(admin.ModelAdmin):
#     model = RoomType
#     search_fields = ['title']
#     list_display = ['id', 'title', 'is_valid', 'create_date']
#
#
# @admin.register(AccommodationType)
# class AccommodationTypeAdmin(admin.ModelAdmin):
#     model = AccommodationType
#     search_fields = ['title']
#     list_display = ['id', 'title', 'is_valid', 'create_date']
#
#
# @admin.register(Accommodation)
# class AccommodationAdmin(admin.ModelAdmin):
#     search_fields = ['title']
#     list_display = ['id', 'title', 'base_price', 'owner', 'standard_capacity', 'build_size']
#     list_filter = ['owner', 'location_type', 'accommodation_type',
#                    'standard_capacity', 'maximum_capacity']
#
#
# @admin.register(Room)
# class RoomAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'room_type', 'accommodation']
#     list_filter = ['room_type']
#
