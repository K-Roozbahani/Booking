from django.urls import path
from .views import ReserveViewSet, PaymentView

urlpatterns = [
    path('', ReserveViewSet.as_view(), name='reserve'),
    path('<int:pk>/', ReserveViewSet.as_view(), name='detail_reserve'),
    path('payment/<int:pk>/', PaymentView.as_view(), name='payment'),
    path('payment/resolve/', PaymentView.as_view(), name='payment'),
]
