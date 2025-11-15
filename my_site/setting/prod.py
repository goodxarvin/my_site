from my_site.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-r+ulnr2ojtxn7#msqppf&%3e0s*9de_h+@bn#(r6c8+esipl3l"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SITE_ID = 1

ALLOWED_HOSTS = []


STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"
STATICFILES_DIRS = [
    BASE_DIR / "statics"
]


# secure cookie csrf

CSRF_COOKIE_SECURE = True


# secure session cookie

SESSION_COOKIE_SECURE = True

# postgresql 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'arvinbeh_travelista',      # اسم کامل دیتابیس CPanel
        'USER': '-',        # یوزر دیتابیس
        'PASSWORD': '-',
        'HOST': "localhost",             # یا 127.0.0.1
        'PORT': '5432',
    }
}
