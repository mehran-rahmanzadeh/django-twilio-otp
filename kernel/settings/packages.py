import os
from datetime import timedelta

from decouple import config
from django.conf import settings

from .base import (
    INSTALLED_APPS, MIDDLEWARE,
    STATIC_ROOT, BASE_DIR, STATICFILES_DIRS
)

# ############## #
#   EXTENSIONS   #
# ############## #

# admin
INSTALLED_APPS.append('django.contrib.admindocs')
INSTALLED_APPS.append('django.contrib.sites')

# packages
INSTALLED_APPS.append('admin_footer')
INSTALLED_APPS.append('admin_honeypot')

# Log

# Security

# Applications
INSTALLED_APPS.append('users')
INSTALLED_APPS.append('otp')

# ########### #
#   UPLOAD    #
# ########### #
# FILE_UPLOAD_HANDLERS = [
#     'painless.utils.handlers.upload.ChunkFileUploadHandler'
# ]
# UPLOAD_CHUNK_SIZE = 2500 * 2 ** 10  # 2500 KB

# #################### #
# IMPORTANT VARIABLES  #
# #################### #
AUTH_USER_MODEL = 'users.User'

TWILIO_ACCOUNT_SECURITY_API_KEY = config('TWILIO_ACCOUNT_SECURITY_API_KEY')
