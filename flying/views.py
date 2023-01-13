from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import AirTravelListSerializer, AirTravelRetrieveSerializer
from .models import AirTravel


class FlyingView(ViewSet):
    filterset_fields = ['origin', 'is_international_flight', 'is_international_flight', ]

    def list(self, request):
        queryset = AirTravel.objects.all()
        serializer = AirTravelListSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = get_object_or_404(AirTravel, pk=pk)
        currency = request.GET.get('currency')
        serializer = AirTravelRetrieveSerializer(instance=queryset, currency=currency)
        return Response(serializer.data)
