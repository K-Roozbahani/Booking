from rest_framework import serializers
from .models import (Place, Accommodation, AccommodationRoom, Location,
                     LocationType, AccommodationType, RoomType, PlaceDatePrice)
from utils.redis_utils import get_exchange_rate


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['country', 'province', 'city']


class CurrencyExtraInputSerializer(serializers.ModelSerializer):
    currency = serializers.SerializerMethodField()

    def __init__(self, instance=None, currency=None, *args, **kwargs):
        currencies = ['IRR', 'USD', 'EUR', 'CAD']
        super(CurrencyExtraInputSerializer, self).__init__(instance, *args, **kwargs)
        self.exchange_currency = currency.upper() if currency in currencies else None

    def get_exchange_rate(self, obj):
        if self.exchange_currency:
            currency_from = self.exchange_currency
            currency_to = obj.get_currency_display()
            exchange_rate = get_exchange_rate(currency_from, currency_to)
            return exchange_rate
        return 1

    def get_currency(self, obj):
        return self.exchange_currency if self.exchange_currency else obj.get_currency_display()


class LocationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationType
        fields = ('title',)


class PlaceSerializer(CurrencyExtraInputSerializer):
    location_type = LocationTypeSerializer(many=True)
    place_type = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    location = LocationSerializer()
    currency = serializers.SerializerMethodField()

    class Meta:
        model = Place

        fields = ('title', 'place_type', 'location', 'location_type', 'price', 'currency', 'description')

    def get_place_type(self, obj):
        return obj.get_place_type_display()

    def get_exchange_rate(self, obj):

        try:
            accommodation = obj.accommodation.all().first()
            if accommodation:
                return super(PlaceSerializer, self).get_exchange_rate(accommodation)
            else:
                return 1
        except:
            return 1

    def get_price(self, obj):
        try:
            accommodation = obj.accommodation.all().first()
            if accommodation:
                return accommodation.base_price * self.get_exchange_rate(obj)
        except:
            return None

    def get_currency(self, obj):
        try:
            accommodation = obj.accommodation.all().first()
            if accommodation:
                return self.exchange_currency if self.exchange_currency else accommodation.get_currency_display()
        except:
            return None


# class PlaceRetrieveSerializer(PlaceSerializer):


# class OptionSerializer(serializers.ModelSerializer):
#     place = PlaceSerializer()
#
#     class Meta:
#         model = Option

class PlaceRetrieSerializers(serializers.ModelSerializer):
    location_type = LocationTypeSerializer(many=True)
    location = LocationSerializer()

    class Meta:
        model = Place
        fields = '__all__'


class AccommodationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationType
        fields = ('title',)


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = 'title'


class AccommodationDatePriceSerializer(CurrencyExtraInputSerializer):
    currency = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    extra_price = serializers.SerializerMethodField()

    class Meta:
        model = PlaceDatePrice
        fields = ('date', 'is_reserve', 'price', 'currency', 'extra_price')

    def get_price(self, obj):
        return obj.price * self.get_exchange_rate(obj)

    def get_extra_price(self, obj):
        return obj.extra_price * self.get_exchange_rate(obj)


# class AccommodationListSerializer(serializers.ListSerializer):
#     place = PlaceSerializer()
#     location_type = LocationTypeSerializer(many=True)
#     accommodation_type = AccommodationTypeSerializer(many=True)
#     date_price = AccommodationDatePriceSerializer(many=True)
#
#     class Meta:
#         model = Accommodation
#         fields = ('title', 'place', 'maximum_capacity', 'location_type', 'accommodation_type')


class AccommodationSerialize(CurrencyExtraInputSerializer):
    place = PlaceRetrieSerializers()
    accommodation_type = AccommodationTypeSerializer(many=True)
    base_price = serializers.SerializerMethodField()
    extra_person_price = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()
    date_price = serializers.SerializerMethodField()
    number_of_rooms = serializers.SerializerMethodField()

    class Meta:
        model = Accommodation
        fields = ('title', 'place', 'base_price', 'extra_person_price', 'currency', 'standard_capacity',
                  'maximum_capacity', 'entry_time', 'exit_time', 'area_size', 'accommodation_size', 'is_charter',
                  'accommodation_type', 'number_of_rooms', 'description', 'date_price')

    def get_base_price(self, obj):
        return obj.base_price * self.get_exchange_rate(obj)

    def get_extra_person_price(self, obj):
        return obj.base_price * self.get_exchange_rate(obj)

    def get_number_of_rooms(self, obj):
        return obj.rooms.all().count()

    def get_date_price(self, obj):
        date_prices = AccommodationDatePriceSerializer(instance=obj.date_price, currency=self.exchange_currency,
                                                       many=True)
        return date_prices.data


# class HotelRoomSerializer(serializers.ModelSerializer):
#     place = PlaceSerializer()
#     room_type = RoomTypeSerializer()
#
#     class Meta:
#         model = HotelRoom
#         fields = '__all__'


class AccommodationRoomSerializer(serializers.ModelSerializer):
    accommodation = AccommodationSerialize()
    room_type = RoomTypeSerializer()

    class Meta:
        model = AccommodationRoom
        fields = '__all__'

# class HotelRoomDatePriceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HotelRoomDatePrice
#         fields = ('date', 'is_reserve', 'price',)

# class RetrievePlaceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Accommodation
#         fields = ('title', 'place', 'base_price', 'extra_person_price', 'standard_capacity',
#                   'maximum_capacity', 'entry_time', 'exit_time', 'area_size', 'build_size', 'is_charter',
#                   'location_type', 'accommodation_type', 'description', 'date_price')
