"""
Django settings for openbook_org project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import raven

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Environment flags
ENVIRONMENT = os.environ.get('ENVIRONMENT')

IS_PRODUCTION_ENVIRONMENT = True if ENVIRONMENT == 'production' else False

DEBUG = not IS_PRODUCTION_ENVIRONMENT

# Django secrets

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Hosts

ALLOWED_HOSTS = [] if not IS_PRODUCTION_ENVIRONMENT else [os.environ.get('DJANGO_ALLOWED_HOSTNAME')]

# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'rest_framework',
    'openbook_org_contact',
    'raven.contrib.django.raven_compat'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware'
]

ROOT_URLCONF = 'openbook_org.urls'

TEMPLATES = []

WSGI_APPLICATION = 'openbook_org.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

# Sentry Config

RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN'),
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}

# Mailgun config

MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')

# Django rest framework config

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'UNAUTHENTICATED_USER': None
}

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# App config

OPENBOOK_CONTACT_FORM_MAIL = os.environ.get('OPENBOOK_CONTACT_FORM_MAIL')
