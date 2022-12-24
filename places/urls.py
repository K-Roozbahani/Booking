from django.urls import path
from .views import AccommodationView, HomeView
from rest_framework.generics import ListAPIView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('Accommodation', AccommodationView.as_view(), name='accommodation'),

]
