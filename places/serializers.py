from rest_framework import serializers
from .models import (Place, Accommodation, AccommodationRoom, HotelRoom, Location,
                     Option, LocationType, AccommodationType, RoomType, AccommodationDatePrice, HotelRoomDatePrice)
from utils.redis_utils import get_exchange_rate


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['country', 'province', 'city']


class PlaceSerializer(serializers.ModelSerializer):

    def __init__(self, instance=None, currency=None, *args, **kwargs):
        super(PlaceSerializer, self).__init__(instance, *args, **kwargs)
        self.exchange_currency = currency

    place_type = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    location = LocationSerializer()
    currency = serializers.SerializerMethodField()

    class Meta:
        model = Place

        fields = ('title', 'place_type', 'location', 'price', 'currency', 'description')

    def get_currency(self, obj):
        if self.exchange_currency:
            return self.exchange_currency
        try:
            currencies = {1: 'IRR', 2: 'USD', 3: 'EUR', 4: 'CAD'}
            accommodation = obj.accommodation.all().first()
            room = obj.hotel_room.all().first()
            if room:
                return currencies[room.currency]
            elif accommodation:
                return currencies[accommodation.currency]
        except:
            return None

    def get_place_type(self, obj):
        return obj.get_place_type_display()

    def get_price(self, obj):
        currencies = {1: 'IRR', 2: 'USD', 3: 'EUR', 4: 'CAD'}
        exchange_rate = 1
        try:
            accommodation = obj.accommodation.all().first()
            room = obj.hotel_room.all().first()

            if room:
                if self.exchange_currency:
                    exchange_display = currencies[room.currency]
                    print(exchange_display)
                    exchange_rate = get_exchange_rate(exchange_display, self.exchange_currency.upper())
                    print(exchange_rate)
                return room.base_price * exchange_rate
            elif accommodation:
                if self.exchange_currency:
                    exchange_display = currencies[accommodation.currency]
                    print(exchange_display)
                    exchange_rate = get_exchange_rate(exchange_display, self.exchange_currency.upper())
                    print(exchange_rate)
                return accommodation.base_price * exchange_rate
        except:
            return None


class OptionSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()

    class Meta:
        model = Option


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


class HotelRoomDatePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomDatePrice
        fields = ('date', 'is_reserve', 'price',)
