from Medical_Supplies_Core.settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^5ngjc8=2=-+#xueyw7co_92mw!j1b2-exn#wv9t6^!ct%_==6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'medicaldb',
        'USER': 'postgres',
        'PASSWORD': '123456654321',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
'''

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'youremail'
EMAIL_HOST_PASSWORD = 'passwordapp'

SITE_ID = 2
