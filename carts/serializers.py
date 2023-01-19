from rest_framework import serializers
from .old_models import PlaceOrder
from places.serializers import AccommodationDatePriceSerializer
from .models import Order, PlaceItem, FlyItem
from places.models import PlaceDatePrice
from flying.models import FlyTicket


class PlaceItemSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(read_only=False, queryset=PlaceDatePrice.objects.all())

    class Meta:
        model = PlaceItem
        field = ('order', 'is_valid', 'items', 'create_time', 'updated_time')


class FlyItemSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(read_only=False, queryset=FlyTicket.objects.all())

    class Meta:
        model = FlyItem
        field = ('order', 'is_valid', 'items', 'create_time', 'updated_time')


class OrderSerializer(serializers.ModelSerializer):
    place_item = PlaceItemSerializer()
    fly_itme = FlyItemSerializer()
    status = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()

    class Meta:
        model = Order
        field = ('user', 'status', 'created_time', 'updated_time', 'total_price', 'currency')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_currency(self, obj):
        return obj.get_currency_display()

    def create(self, validated_data):
        instance = super(OrderSerializer, self).create(validated_data)
        try:
            instance.total_price += instance.palce_item.get_price()
        except:
            print('failed to update place price')
        try:
            instance.Total_price += instance.fly_items.get_price()
        except:
            print('failed to update fly ticket price')
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance = super(OrderSerializer, self).update(instance, validated_data)
        total_price = 0
        try:
            total_price += instance.palce_item.get_price()
        except:
            print('failed to update place price')
        try:
            total_price += instance.fly_items.get_price()
        except:
            print('failed to update fly ticket price')
        instance.total_price = total_price
        instance.save()
        return instance
