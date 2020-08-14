"""
Django settings for home project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from .variables import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = VAR_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    #my apps
    'blog.apps.BlogConfig',
    'map.apps.MapConfig',
    #3rd-party apps
    'markdownx',
    'leaflet',
    #default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms',
    'django.contrib.gis',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'home.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'home.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': DB_NAME,
        'USER': DB_user,
        'PASSWORD': DB_PASS, 
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
)

#media file settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MARKDOWNX_IMAGE_MAX_SIZE = {'size': (1000, 1000), 'quality': 100}

#marldownx
MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',  
    'markdown.extensions.toc',
    'markdown.extensions.tables',
]

#markdownx form setting
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

#leaflet settings
LEAFLET_CONFIG = {
  'DEFAULT_CENTER': (34.987528,135.759323),
  'DEFAULT_ZOOM': 5,
  'MIN_ZOOM': 3,
  'MAX_ZOOM': 18,
  'TILES':[('白地図','http://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png',{'attribution': "<a href='https://maps.gsi.go.jp/development/ichiran.html' target='_blank'>地理院タイル</a>"}),
           ('国土地理院地図','https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png',{'attribution': "<a href='https://maps.gsi.go.jp/development/ichiran.html' target='_blank'>地理院タイル</a>"}),
           ('OpenStreetMap','https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{'attribution': "&copy; <a href='http://osm.org/copyright' target='_blank'>OpenStreetMap</a> contributors" }),
          ]
}

#Geojson settings
SERIALIZATION_MODULES = {
     "geojson": "django.contrib.gis.serializers.geojson",
}
