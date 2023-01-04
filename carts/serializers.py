from rest_framework import serializers
from .models import AccommodationOrder, HotelRoomDatePrice
from places.serializers import AccommodationDatePriceSerializer, HotelRoomDatePriceSerializer


class AccommodationOrderSerializer(serializers.ModelSerializer):
    date_price = AccommodationDatePriceSerializer(many=True)

    class Meta:
        model = AccommodationOrder
        fields = '__all__'


class HotelRoomOrderSerializer(serializers.ModelSerializer):
    date_price = HotelRoomDatePriceSerializer(many=True)

    class Meta:
        model = HotelRoomDatePrice
        fields = '__all__'
