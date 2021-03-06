"""
Django settings for VcrTStore project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import sys
import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extrac'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1hje@*e6j-i+tvuoz7xyw_x_7fjif5i30-6edbv1i32@qf+v5x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# 替换系统用户
AUTH_USER_MODEL = 'users.UserProfile'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',
    'DjangoUeditor',
    'extrac.xadmin',
    # 依赖包：django-crispy-forms~=1.6\django-reversion~=2.0\django-formtools~=1.0\future~=0.15\httplib2~=0.9\six~=1.10
    # 导出包：xlwt\xlsxwriter
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken',

    'corsheaders',
    'social_django',
    'raven.contrib.django.raven_compat',

    'apps.goods',
    'apps.users',
    'apps.trade',
    'apps.operation'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'VcrTStore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'Template') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'VcrTStore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# pip install -i https://pypi.douban.com/simple mysqlclient
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vcrtstore',
        'USER': 'root',
        'PASSWORD': 'ZT123zlt',
        'HOST': '39.107.96.126',
        'PORT': '3306',
        'OPTIONS': { 'init_command': 'SET default_storage_engine=INNODB;'}
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 认证
AUTHENTICATION_BACKENDS = (
    'apps.users.views.CustomBackend',
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GITHUB_KEY = '01fb1af15192d9f585e4'
SOCIAL_AUTH_GITHUB_SECRET = 'd808bedb8fcbfe5b3581d4c695a5a34708260426'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/index/'

# rest_framework
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
        # 429 http code : to many request
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
        'user': '1000/day'
    }
}

# rest_framework_extensions
REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 5
}

# JWT 认证
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

# 手机号码正则表达式
REGEX_PHONE = '^[358]\d{9}$|^147\d{8}$|^176\d{8}$'

# 发送短信，云片网设置
API_KEY = '9b11127a9701975c734b8aee81ee3525'

# 阿里云支付
ALIPAY = {
    'APPID': '2016091500519949',
    'NOTIFY_URL': 'http://39.107.96.126:8000/alipay/return',
    'RETURN_URL': 'http://39.107.96.126:8000/alipay/return',
    'APP_PRIVATE_KEY': os.path.join(BASE_DIR, 'extrac', 'private_2048.txt'),
    'ALIPAY_PUBLIC_KEY': os.path.join(BASE_DIR, 'extrac', 'alipay_key_2048.txt'),
    'DEBUG': True,

    'ALIPAY_URL': 'https://openapi.alipaydev.com/gateway.do'
}

# redis 缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}