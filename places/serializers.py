from rest_framework import serializers
from .models import (Place, Accommodation, AccommodationRoom, HotelRoom, Location,
                     Option, LocationType, AccommodationType, RoomType, AccommodationDatePrice)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['country', 'province', 'city']


class PlaceSerializer(serializers.ModelSerializer):
    place_type = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    location = LocationSerializer()

    class Meta:
        model = Place

        fields = ('title', 'place_type', 'location', 'price', 'description')

    def get_place_type(self, obj):
        return obj.get_place_type_display()

    def get_price(self, obj):
        try:
            accommodation = obj.accommodation.all().first()
        except:
            try:
                room = obj.room.all().first()
            except:
                return None
            return room.base_price
        return accommodation.base_price


class OptionSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()

    class Meta:
        model = Option
        fields = ('title', 'is_free', 'price', 'place')


class LocationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationType
        fields = ('title',)


class AccommodationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationType
        fields = ('title',)


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = 'title'


class AccommodationDatePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationDatePrice
        fields = ('date', 'is_reserve', 'price',)


class AccommodationListSerializer(serializers.ListSerializer):
    place = PlaceSerializer()
    location_type = LocationTypeSerializer(many=True)
    accommodation_type = AccommodationTypeSerializer(many=True)
    date_price = AccommodationDatePriceSerializer(many=True)

    class Meta:
        model = Accommodation
        fields = ('title', 'place', 'maximum_capacity', 'location_type', 'accommodation_type')


class AccommodationSerialize(serializers.ModelSerializer):
    place = PlaceSerializer()
    location_type = LocationTypeSerializer(many=True)
    accommodation_type = AccommodationTypeSerializer(many=True)
    date_price = AccommodationDatePriceSerializer(many=True)

    class Meta:
        model = Accommodation
        fields = ('title', 'place', 'base_price', 'extra_person_price', 'standard_capacity',
                  'maximum_capacity', 'entry_time', 'exit_time', 'area_size', 'build_size', 'is_charter',
                  'location_type', 'accommodation_type', 'description', 'date_price')
        list_serializer_class = AccommodationListSerializer


class HotelRoomSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    room_type = RoomTypeSerializer()

    class Meta:
        model = HotelRoom
        fields = '__all__'


class AccommodationRoomSerializer(serializers.ModelSerializer):
    accommodation = AccommodationSerialize()
    room_type = RoomTypeSerializer()

    class Meta:
        model = AccommodationRoom
        fields = '__all__'
