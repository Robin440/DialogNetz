from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "member",
    "organization",
    "api",
    "drf_yasg",
    "drf_spectacular",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "accounts.User"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# from corsheaders.defaults import default_headers

# CORS_ALLOW_HEADERS = list(default_headers) + [
#     "X-organization-uuid",
#     "X-ui-role",
#     "HTTP_X_ANALYTICS_TOKEN",
#     "HTTP-X-ANALYTICS-TOKEN",
#     "HTTP-X-NEXT-JS-AUTH-TOKEN",
#     "HTTP_X_NEXT_JS_AUTH_TOKEN",
#     "HTTP_X_UI_ROLE",
#     "HTTP-X-UI-ROLE",
# ]


# # Session settings for development
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
# ]

# CORS_ALLOW_CREDENTIALS = True

# # Session settings for development
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS
# SESSION_COOKIE_HTTPONLY = True  # Typically should be True for security
# SESSION_COOKIE_SAMESITE = 'Lax'

# # CSRF settings for development
# CSRF_COOKIE_SECURE = False  # Set to True if using HTTPS
# CSRF_COOKIE_HTTPONLY = False
# CSRF_COOKIE_SAMESITE = 'Lax'


# CORS settings
from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = list(default_headers) + [
    "X-organization-uuid",
    "X-ui-role",
    "HTTP_X_ANALYTICS_TOKEN",
    "HTTP-X-ANALYTICS-TOKEN",
    "HTTP-X-NEXT-JS-AUTH-TOKEN",
    "HTTP_X_NEXT_JS_AUTH_TOKEN",
    "HTTP_X_UI_ROLE",
    "HTTP-X-UI-ROLE",
]


CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "https://stirred-monkfish-luckily.ngrok-free.app"
]
CORS_ALLOWED_ORIGINS = [
    "https://stirred-monkfish-luckily.ngrok-free.app",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOW_CREDENTIALS = True

# CSRF settings
CSRF_COOKIE_SECURE = False  # Set to True if using HTTPS
CSRF_COOKIE_HTTPONLY = False  # Typically should be True for security
CSRF_COOKIE_SAMESITE = "Lax"

# Session settings for development
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS
SESSION_COOKIE_HTTPONLY = True  # Typically should be True for security
SESSION_COOKIE_SAMESITE = "Lax"
