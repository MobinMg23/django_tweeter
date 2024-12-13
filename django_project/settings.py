from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jp0a+#!)bv#-fhw)#5md(^x*js=h%!ts#+d@ci4we)ewxwj0%^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# user
AUTH_USER_MODEL = "django_app.User"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_app',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'minio_storage',
    'rest_framework', 
    'rest_framework_simplejwt',
    'corsheaders',
    'rest_framework.authtoken',
    'django_elasticsearch_dsl',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_app.middleware.jwt_session_middleware.JWTSessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'django_project.urls'

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'django_project.wsgi.application'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=20),  # عمر توکن دسترسی
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # عمر توکن رفرش
    'ROTATE_REFRESH_TOKENS': True,  # توکن رفرش جدید بعد از رفرش صادر شود
    'BLACKLIST_AFTER_ROTATION': True,  # توکن‌های رفرش قدیمی باطل شوند
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,  # کلید امضای JWT
}

# gmail verification setting

# SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Elasticsearch


ELASTICSEARCH_DSL = {
    'default': {
        'hosts': ['http://elastic:Mg1383013830@elasticsearch:9200']
    },
}



# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # برای اجباری کردن تایید ایمیل
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1  # مدت اعتبار تایید ایمیل

# تنظیمات ایمیل
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'mobin1383.11.20@gmail.com'  # ایمیل شما
# EMAIL_HOST_PASSWORD = 'Mg1383013830'  # پسورد ایمیل شما


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'online_shop',
        'USER': 'Mobin',
        'PASSWORD': 'Mg1383013830',  
        'HOST': 'db', 
        'PORT': '3306', 
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# Redis/Cache
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],  # کانتینر Redis
        },
    },
}

import os

# تنظیم مسیر موقت برای STATIC_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MinIo settings

MINIO_STORAGE_ENDPOINT = 'localhost:9000'
MINIO_STORAGE_ACCESS_KEY = 'minioadmin'
MINIO_STORAGE_SECRET_KEY = 'minioadmin'
MINIO_STORAGE_USE_HTTPS = False

# Static
STATICFILES_STORAGE = 'django_minio_storage.storage.MinioStaticStorage'
MINIO_STORAGE_STATIC_BUCKET_NAME = 'static-bucket'

# Media
DEFAULT_FILE_STORAGE = 'django_minio_storage.storage.MinioMediaStorage'
MINIO_STORAGE_MEDIA_BUCKET_NAME = 'media-bucket'

MINIO_STORAGE_ENDPOINT = 'minio:9000'

STATIC_URL = 'http://minio:9000/static-bucket/'
MEDIA_URL = 'http://minio:9000/media-bucket/'