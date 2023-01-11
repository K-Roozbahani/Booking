from django.urls import path
from .views import PlaceView, HomeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PlaceView, basename='places')
urlpatterns = [
    # path('', PlaceView.as_view({'get': 'list'}), name='places'),
    # path('<int:pk>/', PlaceView.as_view({'get': 'retrieve'}), name='places-retrieve')

]

urlpatterns += router.urls
