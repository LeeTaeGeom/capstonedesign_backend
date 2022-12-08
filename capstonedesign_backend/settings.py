"""
Django settings for capstonedesign_backend project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os,json
from datetime import timedelta
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


secret_file=os.path.join(BASE_DIR,'secrets.json')

with open(secret_file,'r') as f:
    secrets = json.loads(f.read())
    
def get_secret(setting,secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable.".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret('SECRET_KEY')

SMS_ACCESS=get_secret("SMS_ACCESS")
SMS_SECRET=get_secret("SMS_SECRET")
SMS_SERVICE_ID=get_secret("SMS_SERVICE_ID")
SEND_PHONE=get_secret("SEND_PHONE")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'web',
    # for rest_framework
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
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

ROOT_URLCONF = 'capstonedesign_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"capstonedesign_backend","templates")],
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

AUTH_USER_MODEL = "app.User"

WSGI_APPLICATION = 'capstonedesign_backend.wsgi.application'

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
          'rest_framework.authentication.BasicAuthentication',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # )
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1000),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1000),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "users.User",
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'web','static')]
STATIC_ROOT=os.path.join(BASE_DIR,'static')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL='/media/' 
MEDIA_ROOT=BASE_DIR/'media' #업로드 한 파일이 이동할 폴더

# EMAIL_HOST='smtp.gmail.com' #메일을 호스트하는 서버
# EMAIL_POST='587' #HOST와 통신하는 포트번호
# EMAIL_HOST_USER=get_secret("GMAIL_ID") #발신할 이메일 계정
# EMAIL_HOST_PASSWORD=get_secret("GMAIL_PASSWORD")#발신할 이메일 비밀번호 -> 22년 5월부터 그냥 비밀번호는 안돼서 2단계 인증으로 앱 비밀번호 설정해서 작성
# EMAIL_USE_TLS=True #TLS보안 설정 여부