from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from .utils import taking_order, reserve_date_price, get_all_or_one_order, validate_payment
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

    def get(self, request, pk=None):
        try:
            response = get_all_or_one_order(request, pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(response)


class PaymentView(APIView):
    def get(self, request, pk):
        try:
            print(pk)
            print(type(pk))
            order = AccommodationOrder.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if order.is_free():
            return self.post(order)
        else:
            if request.user == order.user:
                order.delete()
            return Response({'error': 'This place is already reserved'})

    def post(self, secure_data):
        payment_data = validate_payment(secure_data)
        if payment_data:
            reserve_date_price(payment_data)
            return Response({'status': 'Successful payment'})
        else:
            return Response({'status': 'Unsuccessful payment'})
