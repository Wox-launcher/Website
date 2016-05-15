# -*- coding: utf8 -*-

from .base import *

DEBUG = True

STATIC_ROOT = os.path.join(BASE_DIR, "static_test")
MEDIA_ROOT = os.path.join(BASE_DIR, "media_test")

REST_FRAMEWORK.get("DEFAULT_RENDERER_CLASSES").append('rest_framework.renderers.BrowsableAPIRenderer')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test.sqlite3'),
    }
}
