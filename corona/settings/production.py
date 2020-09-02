from .base import *

DEBUG = True

try:
    from .local import *
except ImportError:
    pass

WSGI_APPLICATION = 'uniekgroen.wsgi.application'

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = os.environ['SECRET_KEY']
