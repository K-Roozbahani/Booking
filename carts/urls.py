from django.urls import path
from .views import ReserveViewSet

urlpatterns = [
    path('', ReserveViewSet.as_view(), name='reserve')
]
