# -*- coding: utf8 -*-
from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["*"]

ADMINS = (('qianlifeng', 'qianlf2008@163.com'),)

CSRF_COOKIE_DOMAIN = ".getwox.com"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wox',  # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',  # Set to empty string for default.
    }
}

STATIC_ROOT = "/var/www/wox_static"
MEDIA_ROOT = "/var/www/wox_media"
