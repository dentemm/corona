from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


import dj_database_url
DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = os.environ['SECRET_KEY']
