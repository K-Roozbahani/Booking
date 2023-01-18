from rest_framework import serializers

from users.models import User
from .models import AirTravel, Airport, Airline, Flight, FlightRule, FlyTicket, PassengerInformation
from places.serializers import LocationSerializer, CurrencyExtraInputSerializer


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ('id', 'title', 'logo')


class AirportSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Airport
        fields = ('id', 'title', 'abbreviated_name', 'location')


class FlightRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightRule
        fields = ('id', 'title', 'is_penalty', 'description')


class FlightSerializer(serializers.ModelSerializer):
    source = AirportSerializer()
    destination = AirportSerializer()
    airline = AirlineSerializer()
    carried_by = AirlineSerializer()
    flight_rules = FlightRuleSerializer(many=True)

    class Meta:
        model = Flight
        fields = ('flight_number', 'source', 'destination',
                  'fly_datetime', 'landing_datetime', 'airline',
                  'carried_by', 'flight_rules')


class AirTravelListSerializer(serializers.ModelSerializer):
    origin = AirportSerializer()
    final_destination = AirportSerializer()
    number_of_flights = serializers.SerializerMethodField()
    airline = AirlineSerializer()

    class Meta:
        model = AirTravel
        fields = ('id', 'airline', 'is_international_flight', 'origin', 'final_destination', 'number_of_flights',)

    def get_number_of_flights(self, obj):
        return obj.flights.all().count()


class PassengerInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerInformation
        fields = ('first_name', 'last_name', 'gender', 'birthday', 'nationality',
                  'national_id', 'passport_name', 'passport_expire_date')


class FlyTicketSerializer(CurrencyExtraInputSerializer):
    passenger = PassengerInformation()
    user = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.get())

    class Meta:
        model = FlyTicket
        fields = ('air_travel', 'passenger', 'date', 'user', 'is_reserve', 'price', 'currency')



class AirTravelRetrieveSerializer(CurrencyExtraInputSerializer):
    origin = AirportSerializer()
    final_destination = AirportSerializer()
    airline = AirlineSerializer()
    flights = FlightSerializer(many=True)
    adults_price = serializers.SerializerMethodField()
    children_price = serializers.SerializerMethodField()
    infant_price = serializers.SerializerMethodField()

    class Meta:
        model = AirTravel
        fields = ('id', 'airline', 'is_international_flight', 'origin', 'final_destination', 'flight_time',
                  'stop_time', 'stop_in', 'flights', 'adults_price', 'children_price', 'infant_price', 'currency')

    def get_adults_price(self, obj):
        return obj.adults_price * self.get_exchange_rate(obj)

    def get_children_price(self, obj):
        return obj.children_price * self.get_exchange_rate(obj)

    def get_infant_price(self, obj):
        return obj.infant_price * self.get_exchange_rate(obj)
