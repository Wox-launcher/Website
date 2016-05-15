# -*- coding: utf8 -*-
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
    'rest_framework_swagger',
    'debug_toolbar',
)

REST_FRAMEWORK.get("DEFAULT_RENDERER_CLASSES").append('rest_framework.renderers.BrowsableAPIRenderer')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wox',  # Or path to database file if using sqlite3.
        'USER': 'postgres',
        'PASSWORD': 'scott',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',  # Set to empty string for default.
    }
}
