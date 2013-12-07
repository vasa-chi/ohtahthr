# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "3uyg8b5o^3i2a!%4wo@ju@hhtuphz@(hza4uplmkh^vez42%0l"

SETTINGS_ROOT = os.path.dirname(__file__)
PROJECT_ROOT = os.path.dirname(SETTINGS_ROOT)

ADMINS = (
    ("andr", "andrewshkovskii@gmail.com"),
    ("vasa.chi", "vasa.chi@gmail.com"),
)

MANAGERS = ADMINS


SITE_NAME = "ohthathr"
SITE_PROTOCOL = "http"
SITE_DOMAIN = "ohthathr.ru"

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
LOCAL_HOST = "127.0.0.1"

ALLOWED_HOSTS = [LOCAL_HOST, LOCAL_HOST + ":8000"]
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "ohthathr",
        "USER": "ohthathr",
        "PASSWORD": "Q3Pg8Tz9n5",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    #"social.apps.django_app.default"
    "taggit",
    "south",
    "ohthathr",
    "vacancies",
    "comments",
    "interviews"
)

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

AUTHENTICATION_BACKENDS = (
      #"social.backends.github.GithubOAuth2",
      #"social.backends.facebook.FacebookOAuth2",
      #"social.backends.twitter.TwitterOAuth",
      #"social.backends.vk.VKOAuth2",
      #"social.backends.google.GoogleOAuth2",
      #"social.backends.google.GooglePlusAuth"
      "django.contrib.auth.backends.ModelBackend",
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.csrf",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    #"social.apps.django_app.context_processors.backends",
    #"social.apps.django_app.context_processors.login_redirect"
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "uploads/")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/uploads/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static/")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don"t forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # "django.contrib.staticfiles.finders.DefaultStorageFinder",
)

ROOT_URLCONF = "ohthathr.urls"

WSGI_APPLICATION = "ohthathr.wsgi.application"


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

try:
    from local_settings import *
except ImportError:
    pass