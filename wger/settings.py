#!/usr/bin/env python
# -*- coding: utf-8 -*-

# wger
from wger.settings_global import *


# Use 'DEBUG = True' to get more details for server errors
DEBUG = True

# List of administrations
ADMINS = (
    ('Your name', 'your_email@example.com'),
)
MANAGERS = ADMINS

# SERVER_EMAIL = 'info@my-domain.com'
# The email address that error messages (and only error messages, such as
# internal server errors) come from, such as those sent to ADMINS and MANAGERS.


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'C:/Users/a/Desktop/itfz/itfz/wger/database.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Timezone for this installation. Consult settings_global.py for more information
TIME_ZONE = 'Europe/Berlin'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ikmvkutg@god2xg-v&ptevj#vy2c2+051th%$ekx%3xwhw-#j4'

# Your reCaptcha keys
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
NOCAPTCHA = True

# The site's URL (e.g. http://www.my-local-gym.com or http://localhost:8000)
# This is needed for uploaded files and images (exercise images, etc.) to be
# properly served.
SITE_URL = 'https://itfz.herokuapp.com/'

# Path to uploaded files
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = 'C:/Users/a/Desktop/itfz/wger/media'
MEDIA_URL = '/media/'

# Allow all hosts to access the application. Change if used in production.
ALLOWED_HOSTS = '*'

# This might be a good idea if you setup redis
#SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# Configure a real backend in production
# See: https://docs.djangoproject.com/en/dev/topics/email/#email-backends
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Sender address used for sent emails
WGER_SETTINGS['EMAIL_FROM'] = 'wger Workout Manager <wger@example.com>'

# Your twitter handle, if you have one for this instance.
#WGER_SETTINGS['TWITTER'] = ''

