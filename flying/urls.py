from django.urls import path
from .views import FlyingView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', FlyingView, basename='flying')
urlpatterns = [
    # path('', FlyingView.as_view({'get': 'list'}), name='flying_list'),

]

urlpatterns += router.urls
