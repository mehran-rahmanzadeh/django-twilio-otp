from django.utils.translation import ugettext_lazy as _


class APIMessages:
    """APIMessages observer class stores the api endpoint messages"""
    instance = None  # used in Singleton pattern

    def __init__(self, *args, **kwargs):
        super(APIMessages, self).__init__(*args, **kwargs)

    def __new__(cls):
        """Implement the Singleton pattern"""
        if not getattr(cls, 'instance', None):
            cls.instance = super(APIMessages, cls).__new__(cls)
        return cls.instance

    def get_message(self, key):
        """Get the message for the given key"""
        if hasattr(self, key):
            return getattr(self, key)
        raise KeyError(key)

    def build_message_body(self, key):
        return {
            'message': self.get_message(key),
        }

    TOKEN_SEND_SUCCESS = _('Token sent successfully')
    TOKEN_VERIFY_SUCCESS = _('Token verified successfully')
    TOKEN_VERIFY_FAIL = _('Token verification failed')
