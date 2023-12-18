import sys
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize the dot-env
env = environ.Env()
env.read_env(env_file=f"{BASE_DIR}/.env")

# Define applications directory  |  /TaxiService/config/settings.py - 2  ==  /TaxiService/
ROOT_DIR = environ.Path(start=__file__) - 2
SRC_DIR = ROOT_DIR.path("source")
sys.path.append("source/apps")

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env.bool("DJANGO_DEBUG")

ALLOWED_HOSTS = (env("DJANGO_ALLOWED_HOSTS"),)

# Application definition
DJANGO_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)

LOCAL_APPS = ("source.apps.home.apps.HomeConfig",)

THIRD_PARTY_APPS = ()

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": (str(SRC_DIR.path("templates")),),
        "OPTIONS": {
            "debug": DEBUG,
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "uk"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATICFILES_DIRS = (str(SRC_DIR.path("static")),)


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#  ---------------  Logging settings  |  https://docs.python.org/3/library/logging.html  ---------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "()": "config.logger.CustomFormatter",
            "format": "%(asctime)s | %(levelname)s | %(name)s.%(funcName)s() | line: %(lineno)d | %(message)s",
        },
        "file": {
            "format": "%(asctime)s | %(levelname)s | %(name)s.%(funcName)s() | line: %(lineno)d | %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "formatter": "file",
            "filename": env("LOGGING_FILENAME"),
        },
    },
    "loggers": {
        "": {"level": "DEBUG", "handlers": ("file", "console"), "propagate": True},
    },
}
