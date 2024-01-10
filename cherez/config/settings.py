"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from django.utils.translation import gettext_lazy as _
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "django-insecure-218z(wi3+a5!^q6#jn++7rp*_r_97onxh(w9pid-xf)o96qns-")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=1))
PROD = int(os.environ.get("PROD", default=0))
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INITIAL_APPS = [
    "modeltranslation"
]

THIRD_PARTY_APPS = [
    "django_extensions",
    "ckeditor",
    "widget_tweaks",
    "rosetta",
    "corsheaders",
]

MY_APPS = [
    "core.apps.CoreConfig",
    "blog.apps.BlogConfig",
    "product.apps.ProductConfig",
]

INSTALLED_APPS = INITIAL_APPS + BASE_APPS + THIRD_PARTY_APPS + MY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",  # Multilanguage
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# # SQLite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB", 'db_name'),
        'USER': os.environ.get("POSTGRES_USER", 'postgres'),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", 12345),
        # 'localhost' or droplet_ip
        'HOST': os.environ.get("POSTGRES_HOST", 'localhost'),
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'az'

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_TZ = True

USE_L10N = True

LANGUAGES = [
    ("az", _("Azerbaijani")),
    ("en", _("English")),
    ("ru", _("Russian")),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

# Modeltranslation
MODELTRANSLATION_DEFAULT_LANGUAGE = 'az'
MODELTRANSLATION_LANGUAGES = ('az', 'en', 'ru')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

if PROD:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
    ]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CKEditor configs
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        # 'height': 300,
        # 'width': '100%',
    },
}


# CORS Headers config
if PROD:
    CORS_ALLOW_ALL_ORIGINS: False
    CORS_ALLOWED_ORIGINS = os.environ.get(
        'CORS_ALLOWED_ORIGINS', 'http://*,https://*').split(',')
else:
    CORS_ALLOW_ALL_ORIGINS: True


# CSRF TRUSTED ORIGINS config
if PROD:
    CSRF_TRUSTED_ORIGINS = os.environ.get(
        'CSRF_TRUSTED_ORIGINS', 'http://*,https://*').split(',')
