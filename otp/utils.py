import random
import string
from abc import abstractmethod, ABC


class OTPHelper(ABC):

    @abstractmethod
    def send_token(self, phone_number, country_code, via='sms'):
        pass

    @abstractmethod
    def verify_token(self, phone_number, country_code, token, via='sms'):
        pass


class PhoneOTPHelper(OTPHelper):
    def __init__(self, authy, *args, **kwargs):
        self.authy = authy
        super(PhoneOTPHelper, self).__init__(*args, **kwargs)

    @staticmethod
    def __generate_token(digits=6):
        return ''.join(random.choice(string.digits) for i in range(digits))

    def send_token(self, phone_number, country_code, via='sms'):
        token = self.__generate_token()
        return self.authy.phones.verification_start(phone_number, country_code, token)

    def verify_token(self, phone_number, country_code, token, via='sms'):
        return self.authy.phones.verification_check(phone_number, country_code, token, via)
