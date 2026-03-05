"""Django settings for DataPulse project."""

import os
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Environment-driven settings (same env vars as original FastAPI project) ---
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://datapulse:datapulse@db:5432/datapulse")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))
UPLOAD_DIR = os.getenv("UPLOAD_DIR", os.path.join(BASE_DIR, "uploads"))

DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")
ALLOWED_HOSTS = ["*"]

# --- Application definition ---
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "corsheaders",
    "rest_framework",
    "authentication",
    "datasets",
    "rules",
    "checks",
    "reports",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "datapulse.urls"
WSGI_APPLICATION = "datapulse.wsgi.application"

# --- CORS (same as original: allow all origins) ---
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# --- Database ---
# Parse DATABASE_URL into Django DATABASES dict
_db_url = DATABASE_URL
if _db_url.startswith("postgresql://"):
    _parts = _db_url.replace("postgresql://", "").split("@")
    _user_pass = _parts[0].split(":")
    _host_db = _parts[1].split("/")
    _host_port = _host_db[0].split(":")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": _host_db[1] if len(_host_db) > 1 else "datapulse",
            "USER": _user_pass[0],
            "PASSWORD": _user_pass[1] if len(_user_pass) > 1 else "",
            "HOST": _host_port[0],
            "PORT": _host_port[1] if len(_host_port) > 1 else "5432",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- Custom user model ---
AUTH_USER_MODEL = "authentication.User"

# --- Django REST Framework ---
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",
    ),
    "UNAUTHENTICATED_USER": None,
}

# --- SimpleJWT (replaces python-jose from FastAPI project) ---
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    "ALGORITHM": ALGORITHM,
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# --- Password hashing ---
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
]
