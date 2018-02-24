"""
Django settings for api project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from unipath import Path

BASE_DIR = Path(__file__).parent.parent.parent

# ADMINS = (
#('scott', 'qianlf2008@163.com'),
#)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v&luxlt&lq6^74$y3mfh3@2zxyxm9%jp$)5_tze8pef^4m4y_$'
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'corsheaders',
    'rest_framework',
    'plugins',
    'users',
    'auths',
    'woxerrors',
    'release',
    'dashboard',
)

REST_FRAMEWORK = {
    'PAGINATE_BY': 10,
    'PAGINATE_BY_PARAM': 'page_size',
    'MAX_PAGINATE_BY': 100,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer'
    ]
}

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'localhost:9000',
    '127.0.0.1:9000',
    'api.wox.one',
    'wox.one',
    'www.wox.one',
    'new2.wox.one',
)

MIDDLEWARE_CLASSES = (
    'api.middlewares.DisableCSRFMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'api.middlewares.APIExceptionMiddleware',
)

ROOT_URLCONF = 'api.urls'
WSGI_APPLICATION = 'api.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

ALLOWED_IMAGE_EXTENSIONS = [".jpg", ".png", ".gif", ".ico"]

EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'qianlf2008@163.com'
EMAIL_HOST_PASSWORD = 'SoRpHJMLBPL6GDmm6QbNGg'
