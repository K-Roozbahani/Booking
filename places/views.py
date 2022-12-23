# from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView
from .models import *
from .serializers import *
from rest_framework.response import Response

class AccommodationView(ListAPIView):
    print('my_view')
    queryset = Accommodation.objects.prefetch_related('date_price', 'location_type').all()
    serializer_class = AccommodationSerialize


class TestApi(ListAPIView):

    def get(self, request):
        accommodations = Accommodation.objects.prefetch_related('date_price', 'location_type').all()
        serializer_class = AccommodationSerialize(many=True, instance=accommodations)

        # date_price = AccommodationDatePriceSerializer(many=True, instance=accommodations.date_price.all())
        serializer_class.date_price = date_price
        return Response(serializer_class.data)
