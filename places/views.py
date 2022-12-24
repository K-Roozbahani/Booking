# from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView
from .models import *
from .serializers import *
from rest_framework.response import Response

class AccommodationView(ListAPIView):
    print('my_view')
    queryset = Accommodation.objects.prefetch_related('date_price', 'location_type').all()
    serializer_class = AccommodationSerialize


class HomeView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
