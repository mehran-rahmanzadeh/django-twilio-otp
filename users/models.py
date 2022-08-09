import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from users.managers import CustomUserManager

INTERNATIONAL_PHONE_NUMBER_REGEX = r'^\+?1?\d{9,15}$'


class User(AbstractUser):
    username = None
    phone_number = models.CharField(
        _('phone number'),
        unique=True,
        max_length=15,
        validators=[
            RegexValidator(
                INTERNATIONAL_PHONE_NUMBER_REGEX,
                _('Phone number must be entered in the format: +999999999. Up to 15 digits allowed.'),
                'invalid'
            )],
    )
    email = models.EmailField(
        _('email address'),
        null=True,
        unique=True,
        blank=True
    )
    secret = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    is_phone_confirmed = models.BooleanField(
        _('Is phone confirmed'),
        default=False
    )
    is_email_confirmed = models.BooleanField(
        _('Is email confirmed'),
        default=False
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.get_full_name()}-{self.phone_number}'

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
