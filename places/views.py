# from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView
from .models import *
from .serializers import *


class AccommodationView(ListAPIView, GenericAPIView):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerialize
