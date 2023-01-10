from rest_framework import serializers
from .models import PlaceOrder
from places.serializers import AccommodationDatePriceSerializer


class PlaceOrderSerializer(serializers.ModelSerializer):
    date_prices = AccommodationDatePriceSerializer(many=True)

    class Meta:
        model = PlaceOrder
        fields = '__all__'


# class HotelRoomOrderSerializer(serializers.ModelSerializer):
#     date_prices = HotelRoomDatePriceSerializer(many=True)
#
#     class Meta:
#         model = HotelRoomDatePrice
#         fields = '__all__'

