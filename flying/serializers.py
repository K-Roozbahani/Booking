from rest_framework import serializers
from .models import AirTravel, Airport
from places.serializers import LocationSerializer


class AirportSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Airport
        fields = ('id', 'title', 'abbreviated_name', 'location')


class AirTravelListSerializer(serializers.ModelSerializer):
    origin = AirportSerializer()
    final_destination = AirportSerializer()
    number_of_flights = serializers.SerializerMethodField()

    class Meta:
        model = AirTravel
        fields = ('is_international_flight', 'origin', 'final_destination', 'number_of_flights')

    def get_number_of_flights(self, obj):
        return obj.flights.alll().count()
