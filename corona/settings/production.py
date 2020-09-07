from .base import *

DEBUG = True

try:
    from .local import *
except ImportError:
    pass

WSGI_APPLICATION = 'uniekgroen.wsgi.application'

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

SECURE_SSL_REDIRECT = True

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1', '.aws.amazon.com', '.herokuapp.com', 'www.planetvirus.org', 'www.planetvirus.net', 'www.planetvirus.info', '.planetvirus.org', '.planetvirus.net', '.planetvirus.info'
]
