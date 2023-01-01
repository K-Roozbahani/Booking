from django.urls import path
from .views import AccommodationView, HomeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'accommodations', AccommodationView, basename='accommodations')
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('test/', test, name='test')

]

urlpatterns += router.urls
