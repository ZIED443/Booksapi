import os

DJANGO_ENV = os.getenv('DJANGO_ENV', 'test')

if DJANGO_ENV == 'prod':
    from .prod import *
else :
    from .test import *

        