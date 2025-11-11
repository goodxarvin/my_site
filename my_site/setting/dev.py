from my_site.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-r+ulnr2ojtxn7#msqppf&%3e0s*9de_h+@bn#(r6c8+esipl3l"

# SECURITY WARNING: don't run with debug turned on in production!

# INSTALLED_APPS = []



DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"
STATICFILES_DIRS = [
    BASE_DIR / "statics"
]
