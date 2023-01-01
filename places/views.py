from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *
from rest_framework.response import Response


class AccommodationView(viewsets.ReadOnlyModelViewSet, viewsets.GenericViewSet):
    queryset = Accommodation.objects.prefetch_related('date_price', 'location_type').all()
    serializer_class = AccommodationSerialize


class HomeView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


# def test(request):
#     serializer = AccommodationSerialize(many=True)
#     model = Accommodation.objects.all()
#     serializer.instance = model
#     print(serializer.data)
#     return Response(serializer.data)
