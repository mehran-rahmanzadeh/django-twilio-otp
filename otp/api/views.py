from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from otp.api.messages import APIMessages
from otp.api.serializers import SendTokenSerializer, VerifyTokenSerializer
from otp.utils import PhoneOTPHelper

from authy.api import AuthyApiClient

authy_client = AuthyApiClient(settings.TWILIO_ACCOUNT_SECURITY_API_KEY)
messages = APIMessages()


class SendTokenAPIView(APIView):
    """Send OTP to user's phone number"""
    permission_classes = (AllowAny,)
    serializer_class = SendTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp_helper = PhoneOTPHelper(authy=authy_client)
        otp_helper.send_token(
            phone_number=serializer.validated_data['phone_number'],
            country_code=serializer.validated_data['country_code'],
            via=serializer.validated_data['via']
        )
        return Response(data=messages.build_message_body('TOKEN_SEND_SUCCESS'), status=status.HTTP_201_CREATED)


class VerifyTokenAPIView(APIView):
    """Verify OTP token"""
    permission_classes = (AllowAny,)
    serializer_class = VerifyTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp_helper = PhoneOTPHelper(authy=authy_client)
        verification = otp_helper.verify_token(
            phone_number=serializer.validated_data['phone_number'],
            country_code=serializer.validated_data['country_code'],
            token=serializer.validated_data['token'],
            via=serializer.validated_data['via']
        )
        if verification.ok():
            user = get_user_model().objects.get(phone_number=serializer.validated_data['phone_number'])
            user.is_phone_verified = True
            refresh = user.generate_jwt()
            user.save()
            response = {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=messages.build_message_body('TOKEN_VERIFY_FAIL'), status=status.HTTP_400_BAD_REQUEST)
