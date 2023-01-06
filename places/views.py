from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView


class AccommodationView(viewsets.ReadOnlyModelViewSet, viewsets.GenericViewSet):
    queryset = Accommodation.objects.prefetch_related('date_price', 'location_type').all()
    serializer_class = AccommodationSerialize


class HomeView(APIView):
    def get(self, request):
        currencies = ['IRR', 'USD', 'EUR', 'CAD']
        currency = request.GET.get('currency')
        print(currency)
        places = Place.objects.all()
        serializer = PlaceSerializer(instance=places, many=True)
        if currency and currency in currency.upper() in currencies:
            serializer = PlaceSerializer(instance=places, currency=currency, many=True)
        return Response(serializer.data)

# def test(request):
#     serializer = AccommodationSerialize(many=True)
#     model = Accommodation.objects.all()
#     serializer.instance = model
#     print(serializer.data)
#     return Response(serializer.data)
