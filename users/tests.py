from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError


class TestUser(TestCase):

    def setUp(self) -> None:
        self.phone_number = '+999999998'
        self.email = 'test@test.com'
        self.password = 'secure'
        self.user = get_user_model().objects.create_user(
            phone_number=self.phone_number,
            password=self.password,
            email=self.email
        )

    def test_user_creation(self):
        user = get_user_model().objects.create_user(
            phone_number='+999999999',
            password='password'
        )
        self.assertEqual(user.phone_number, '+999999999')

    def test_user_unique_phone_number(self):
        with self.assertRaises(IntegrityError):
            get_user_model().objects.create_user(
                phone_number=self.phone_number,
                password='secure2'
            )

    def test_user_unique_email(self):
        with self.assertRaises(IntegrityError):
            get_user_model().objects.create_user(
                phone_number='+999999999',
                password='secure2',
                email=self.email
            )

    def test_user_password_hash(self):
        self.assertNotEqual(self.user.password, self.password)

    def test_user_check_password(self):
        self.assertTrue(self.user.check_password(self.password))
