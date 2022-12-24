from rest_framework import serializers
from .models import Place, Accommodation, Room, Location, Option, LocationType, AccommodationType, RoomType, \
    AccommodationDatePrice


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
    class Meta:
        model = Option
        fields = '__all__'


class LocationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationType
        fields = '__all__'


class AccommodationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationType
        fields = '__all__'


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class AccommodationDatePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationDatePrice
        fields = ('date', 'is_reserve', 'price', )


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


class RoomSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    accommodation = AccommodationSerialize()
    room_type = RoomTypeSerializer(many=True)

    class Meta:
        model = Room
        fields = '__all__'
