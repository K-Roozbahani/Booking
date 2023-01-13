from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import AirTravelListSerializer
class FlyingView(ViewSet):
    filterset_fields = ['origin', 'is_international_flight', 'is_international_flight', ]

    def list(self):
        quer
        serializer = AirTravelListSerializer(many=True)
        return Response()
