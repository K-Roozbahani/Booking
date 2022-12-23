from django.urls import path
from .views import AccommodationView, TestApi
from rest_framework.generics import ListAPIView
urlpatterns = [
    path('', AccommodationView.as_view(), name='accommodation'),
    path('test/', TestApi.as_view(), name='test'),
]
