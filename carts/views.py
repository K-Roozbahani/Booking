from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from .utils import taking_order, reserve_date_price
from places.models import HotelRoomDatePrice, AccommodationDatePrice
from .serializers import HotelRoomOrderSerializer, AccommodationOrderSerializer
from .models import AccommodationOrder, HotelRoomOrder
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework import status
from django.utils.translation import gettext_lazy as _


class ReserveViewSet(APIView):

    def post(self, request):
        try:
            data = taking_order(request)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = data['serializer']
        order = data['order']
        try:
            order.save()
        except:
            return Response({'error': _('It is reserved during this period')}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
