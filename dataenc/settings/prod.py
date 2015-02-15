"""
Django settings for dataenc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from decouple import config
from dj_database_url import parse as db_url
from os.path import join
from sys import path
from unipath import Path

BASE_DIR = Path(__file__).absolute().ancestor(2)

# insert path to apps
path.insert(0, BASE_DIR.child('apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = DEBUG

PROJECT_NAME = 'dataenc'
ALLOWED_HOSTS = ['*', ]

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'dataset',
)

THIRD_PARTY_APPS = (
    'gunicorn',
    'djangobower',
    'bootstrap3',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dataenc.urls'

WSGI_APPLICATION = 'dataenc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///{0}/{1}'.format(BASE_DIR.child('db'),
                                           'dataenc.sqlite3'),
        cast=db_url),
}

FIXTURE_DIRS = (join(BASE_DIR.child('db'), 'fixtures'), )

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (BASE_DIR.child('locale'), )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = config('STATIC_ROOT', default=BASE_DIR.child('staticfiles'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR.child('static'), )
BOWER_COMPONENTS_ROOT = join(BASE_DIR, 'vendor')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

# Media files
MEDIA_ROOT = config('MEDIA_ROOT', default=BASE_DIR.child('media'))
MEDIA_URL = '/media/'

# Template files
TEMPLATE_DIRS = (BASE_DIR.child('templates'), )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

BOWER_INSTALLED_APPS = (
    'bootstrap',
    'bootstrap-sass-official',
    'font-awesome',
    'jquery',
    'underscore',
)

# ALL OTHER KEYS
from keys import *
