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


# site protection

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
# X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
# Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'
