"""
Django settings for hvillas project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k$z!e*sjrozxx12=f&s_x=yh(efdkbbi+!%=4n_+c1@un2(p%$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',       # for database migration
    'villas',      # app name
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# for djang_tables2 (display a model as table )
TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.request' ,
                               'django.contrib.auth.context_processors.auth')
ROOT_URLCONF = 'hvillas.urls'

WSGI_APPLICATION = 'hvillas.wsgi.application'   # for deployment


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # i used postgresql
            'NAME': 'villasdb',                      # database name.
            'USER': 'postgres',                      #postgresql default username                                   
            'PASSWORD': '123456',                       #postgresql password
            'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
    }
}

# for djang_tables2 (display a model as table )
TEMPLATE_CONTEXT_PROCESSORSv='django.core.context_processors.request'
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# if login is successful go to resident page
LOGIN_REDIRECT_URL ='resident'      # if login is successful go to /resident

LOGIN_URL ='login'    # overriding the default 'profiles/login'
LOGOUT_URL = '/'    # overriding default 'profiles/logout'



