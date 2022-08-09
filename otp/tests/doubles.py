class VerificationDouble:
    is_ok = False

    def __init__(self, *args, **kwargs):
        super(VerificationDouble, self).__init__(*args, **kwargs)

    def ok(self):
        return self.is_ok


class AuthyPhonesDouble:
    sent = {}

    def __init__(self, *args, **kwargs):
        self.verification = VerificationDouble()
        super(AuthyPhonesDouble, self).__init__(*args, **kwargs)

    def verification_start(self, phone_number, country_code, token):
        self.sent[phone_number] = token

    def verification_check(self, phone_number, country_code, token, via):
        if self.sent.get(phone_number) == token:
            self.verification.is_ok = True
        else:
            self.verification.is_ok = False
        return self.verification


class AuthyDouble:
    def __init__(self, *args, **kwargs):
        self.phones = AuthyPhonesDouble()
        super(AuthyDouble, self).__init__(*args, **kwargs)
