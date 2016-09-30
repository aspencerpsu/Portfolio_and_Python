if __name__ == "__main__" and __package__ == None:
    from sys import path
    from os.path import direname as dir
    path.append(dir(path[0]))
    __package__ = "settings"

# When ready to ship to a local worker like apache, vmware,
# or  NGINX, be sure to follow all the rules and parameters with hosting the site.


"""
Django settings for portfolio_revamp project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import psycopg2
import sys
import gettext
import locale
from django.conf import locale as site_locale

current_locale, encoding = locale.getdefaultlocale()

# LOCALE_PATHS = os.path.join(sys.prefix, 'Lib', 'site-packages', 'django', 'conf', 'locale')

# language = gettext.translation("django", LOCALE_PATHS, [current_locale[0][0:2]])
# language.install("django", LOCALE_PATHS, [current_locale[0][0:2]])


sys.dont_write_bytecode = True

SITE_URL = 'http://localhost.com'

ABSOLUTE_URL_OVERRIDES = {}

AUTH_USER_MODEL = 'auth.User'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

## PLACE THIS KEY IN THE SYSTEM ENVIRONMENT!
SECRET_KEY = 'pn&8y9l8!8n9fq9*x=@qr^fm*7%j*3%a0%urg!e*(q&=cp!wkb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SITE_ID = 1

ALLOWED_HOSTS = ['*']

ALLOWED_INCLUDE_ROOTS = []


ADMINS = ("Akeem Spencer", "aspencerpsu@gmail.com")

AccessToken = "457888099-zEIwcezHpVbznLivoMfZ0dzXUgZdN8w3DfcFP1Kl"

AccessTokenSecret = "cfsPMsazvavdOMQnZUoRUSVzoZHnmuyOv0Kw0UDP1kBSg"

Consumer_Secret = " wOokX8k54HrrWEXGORnarOYzZFiISSVxT90xOJgvX3FcMUX0QB"

Consumer_key = "pX0OETs87mPD0CROfEl5xNSKL"

OWNER = "Dagen1ous"

OWNERID = 457888099

oauth_nonce="1044602964"

OAUTH_CONSUMER_KEY = "DC0sePOBbQ8bYdC8r4Smg"

OAUTH_SIGNATURE_METHOD="HMAC-SHA1"

OAUTH_TOKEN="457888099-NTtTfXOZ4kJGHAqmp8Moigiq2hIVNCGy1VAFwDWd"

OAUTH_SIGNATURE="oi61wx1nzF2%2FiDRBD5QlDWPuYac%3D"


MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django.contrib.postgres.operations',
    'django.template.loader',
    'blogs',
    'employees',
    'posts',
    'comments',

    # Third Party Apps
    'twitter',
    'tweepy',
    'kombu.transport.django',
    # 'm2m_history',
    # 'taggit',
    # 'oauth_tokens',
    'rest_framework',
    'crispy_forms',
    'pagedown',
    'markdown_deux',

)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = "portfolio_revamp.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {

            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.tz',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                # 'django.template.loaders.eggs.Loader',
            ],
            'string_if_invalid': '',
            'debug': True,       
        },
    },
]

# TEMPLATE_DIRS = []

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'django.template.context_processors.request',
#     'django.template.context_processors.debug',
#     'django.contrib.messages.context_processors.messages',
#     'django.template.context_processors.tz',
#     'django.template.context_processors.i18n',
#     'django.template.context_processors.media',
#     'django.template.context_processors.static',
# )

INTERNAL_IPS = ["127.0.0.1"]

FILE_CHARSET = 'utf-8'

FORMAT_MODULE_PATH = None

WSGI_APPLICATION = 'portfolio_revamp.wsgi.application'

ADMIN_MEDIA_PREFIX = '/media/'
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'd0mainframe',
        'HOST': 'localhost',
        'PORT': '3005',
        'CONN_MAX_AGE': None,
        'client_encoding': 'UTF8',
        'default_transaction_isolation': 'read committed',
        'BROKER_URL': 'django://',
        'TEST': {
            'CHARSET': 'UTF8',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'd0mainframe',
            'USER': 'postgres',
            'CREATE_DB': 'TRUE',
            'CREATE_USER': 'TRUE',
        }
    }
}

DATABASE_ROUTERS = []

LOGGING = {500: True, 404: True}

LOGGING_CONFIG = None

MIGRATION_MODULES = {'blog': 'blog.migrations', 'portfolio_revamp': None, 'employees': 'employees.migrations', }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True

DEFAULT_INDEX_TABLESPACE = ''

DEFAULT_TABLESPACE=''
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

STATIC_URL = '/static/'

STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static"), ]

STATICFILES_FINDERS = (
                    'django.contrib.staticfiles.finders.FileSystemFinder',
                    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")

FORCE_SCRIPT_NAME = None

SILENCED_SYSTEM_CHECKS = []

SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_SECONDS = 0
SECURE_REDIRECT_EXEMPT = []
SECURE_SSL_HOST = None
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = None

DEBUG_PROPAGATE_EXCEPTIONS = False

DEFAULT_EXCEPTION_REPORTER_FILTER = 'django.views.debug.SafeExceptionReporterFilter'

DEFAULT_CHARSET = 'utf-8'

DEFAULT_CONTENT_TYPE = 'text/html'

USE_X_FORWARDED_HOST = False

DECIMAL_SEPARATOR = '.'

NUMBER_GROUPING = 0

USE_THOUSAND_SEPARATOR = False

THOUSAND_SEPARATOR = ','

SESSION_COOKIE_NAME = 'sessionid'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

SESSION_SAVE_EVERY_REQUEST = False

USE_ETAGS = False

DISALLOWED_USER_AGENTS = []

PREPEND_WWW = False

APPEND_SLASH = True

MEDIA_ROOT="c:/Python27/Lib/site-packages/django/bin/portfolio_revamp/MEDIA_REP"

MEDIA_URL="/media/"

MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

CSRF_COOKIE_NAME = 'csrftoken'
CSRF_COOKIE_AGE = 60 * 60 * 24
CSRF_COOKIE_DOMAIN = None
CSRF_COOKIE_PATH = '/'
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False

FILE_UPLOAD_PERMISSIONS = None
FILE_UPLOAD_DIRECTORY_PERMISSIONS = None

FIXTURE_DIRS = ()