from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView


class PlaceView(viewsets.ViewSet):
    def list(self, request):
        queryset = Place.objects.all()
        currency = request.GET.get('currency')
        serializer = PlaceSerializer(instance=queryset, currency=currency, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = get_object_or_404(Accommodation, place__id=pk)
        currency = request.GET.get('currency')
        serializer = AccommodationSerialize(instance=queryset, currency=currency)
        return Response(serializer.data)


class HomeView(APIView):
    def get(self, request, pk=None):
        currencies = ['IRR', 'USD', 'EUR', 'CAD']
        currency = request.GET.get('currency')
        if not pk:
            places = Place.objects.all()
            serializer = PlaceSerializer(instance=places, many=True)
            if currency and currency in currency.upper() in currencies:
                serializer = PlaceSerializer(instance=places, currency=currency, many=True)
            return Response(serializer.data)

        else:
            place = get_object_or_404(Place, pk=pk)
            serializer = PlaceSerializer(place)
            return Response(serializer.data)
# def test(request):
#     serializer = AccommodationSerialize(many=True)
#     model = Accommodation.objects.all()
#     serializer.instance = model
#     print(serializer.data)
#     return Response(serializer.data)
