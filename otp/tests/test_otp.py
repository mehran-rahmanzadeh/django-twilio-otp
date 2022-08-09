import string

from django.test import TestCase

from otp.tests.doubles import AuthyDouble
from otp.utils import PhoneOTPHelper


class TestOTP(TestCase):
    def setUp(self) -> None:
        self.authy = AuthyDouble()
        self.otp_helper = PhoneOTPHelper(self.authy)

    def test_send_token(self):
        self.otp_helper.send_token('+79123456789', 'RU')
        self.assertIsNotNone(self.authy.phones.sent['+79123456789'])

    def test_token_generate_digits(self):
        self.otp_helper.send_token('+79123456789', 'RU')
        token = self.authy.phones.sent['+79123456789']
        self.assertEqual(len(token), 6)
        self.assertTrue(all(c in string.digits for c in token))

    def test_verify_token_success(self):
        self.otp_helper.send_token('+79123456789', 'RU')
        verification = self.otp_helper.verify_token('+79123456789', 'RU', self.authy.phones.sent['+79123456789'])
        self.assertTrue(verification.is_ok)

    def test_verify_token_fail(self):
        self.otp_helper.send_token('+79123456789', 'RU')
        verification = self.otp_helper.verify_token('+79123456789', 'RU', '123456')
        self.assertFalse(verification.is_ok)
