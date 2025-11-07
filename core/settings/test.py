from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'testdb'),
        'USER': os.environ.get('POSTGRES_USER', 'testuser'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'testpassword'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', 5432),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
