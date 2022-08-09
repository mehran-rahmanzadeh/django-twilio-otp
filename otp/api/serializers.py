from rest_framework import serializers
from django.core.validators import RegexValidator

from users.models import INTERNATIONAL_PHONE_NUMBER_REGEX


class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=15,
        validators=[RegexValidator(INTERNATIONAL_PHONE_NUMBER_REGEX)]
    )
    country_code = serializers.CharField(max_length=10)


class SendTokenSerializer(PhoneNumberSerializer):
    via = serializers.CharField(max_length=4, default='sms')


class VerifyTokenSerializer(PhoneNumberSerializer):
    token = serializers.CharField(max_length=6)
    via = serializers.CharField(max_length=4, default='sms')
