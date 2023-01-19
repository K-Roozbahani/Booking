from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser


class OrderView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.request.user.orders.all()
