from rest_framework.routers import DefaultRouter
from .views import LoginByOtpView
router = DefaultRouter()
router.register(r'login', LoginByOtpView, basename='login')
urlpatterns = router.urls
