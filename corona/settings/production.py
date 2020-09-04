from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

WSGI_APPLICATION = 'uniekgroen.wsgi.application'

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.aws.amazon.com', '.herokuapp.com', 'planetvirus.org', 'planetvirus.net', 'planetvirus.info']
