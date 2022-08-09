from django.urls import path

from otp.api.views import SendTokenAPIView, VerifyTokenAPIView

urlpatterns = [
    path('send-token/', SendTokenAPIView.as_view(), name='send-token'),
    path('verify-token/', VerifyTokenAPIView.as_view(), name='verify-token'),
]