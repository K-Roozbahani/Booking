from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import User
from django.core.cache import cache
from rest_framework_simplejwt.tokens import RefreshToken


def otp_generator(*args, **kwargs):
    return '1234567890'


def send_sms_to_user(*args, **kwargs):
    pass


class LoginByOtpView(viewsets.ViewSet):

    @action(methods=['post'], detail=False, url_path='get-phone-number')
    def get_phone_number(self, request):
        if request.data.get('phone'):
            otp = otp_generator()
            cache.set(request.data['phone'], otp, 60 * 2)

        else:
            data = {"error": "phone field required"}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        # send_sms_to_user.delay(request.data['phone'], otp) ---> for use celery task
        send_sms_to_user(request.data['phone'], otp)
        return Response(data={'phone': request.data.get('phone')}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='get-otp')
    def get_otp(self, request):
        if request.data.get('phone') and request.data.get('otp'):
            phone = request.data['phone']
            otp = request.data["otp"]

            user_otp = cache.get(phone)

            if user_otp == otp:
                try:
                    user = User.objects.get(phone_number=phone)
                except User.DoesNotExist:
                    user = User.objects.create_user(username=phone[1:], phone_number=phone)

                refresh = RefreshToken.for_user(user)
                context = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response(context)
            else:
                raise AuthenticationFailed("{} invalid otp".format(request.data["otp"]))

        else:
            data = {"error": "phone and otp fields required"}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
