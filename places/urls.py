from django.urls import path
from .views import AccommodationView
urlpatterns = [
    path('accommodation/', AccommodationView.as_view, name='accommodation')
]
