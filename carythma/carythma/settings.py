"""
Django settings for carythma project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import environ 
import  os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g^sqlix5i#2#yka(1+mgi+rir@n_b1v9w(8*oa=615y3wf$6er'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#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
ALLOWED_HOSTS = [] # ["postcarythma.cgwpfubo8wvn.us-east-1.rds.amazonaws.com"  , "http://18.205.34.124/"]


MY_ACCOUNT_SID = "AC4f4516dd1894fa8d162842e79ae660d1"
TWILIO_AUTH_TOKEN="72017c407c0c855f9d7cdc7377f7528f"
MY_TWILIO_NUMBER="+16187871636"

'''
env = environ.Env()
environ.Env.read_env()
'''

TWILIO_ACCOUNT_SID = os.getenv("MY_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("MY_TWILIO_NUMBER")


SMS_BROADCAST_TO_NUMBERS = [
   "+22661396930"
   #"+22677797813"
    # use the format +1XXXXXXXXXX
 ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'testsms',
    'authentication',
    'rest_framework',
    "corsheaders",
    'rest_framework.authtoken',
    'rest_auth',
    'django_filters',
    'userjwt'
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'carythma.urls'
CORS_ALLOW_ALL_ORIGINS: True
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

WSGI_APPLICATION = 'carythma.wsgi.application'

DATABASES = { "default": {
	 "ENGINE": "django.db.backends.sqlite3", "NAME":
        BASE_DIR / "db.sqlite3",
    }


}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postcarythma' ,
        'USER': 'usercarythma',
        'PASSWORD': 'passwordcarythmadb',
        'HOST':'postcarythma.cgwpfubo8wvn.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
'''

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
AUTH_USER_MODEL = 'api.Client'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
	'rest_framework.authentication.TokenAuthentication',
    ]
}


'''
AWS_ACCESS_KEY_ID = 'AKIAYVWY5P3PBD3HJYW4'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'bucketcarythma'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
'''
