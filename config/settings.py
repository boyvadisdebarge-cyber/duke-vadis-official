import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "development-only-change-me")
DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() == "true"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")
CSRF_TRUSTED_ORIGINS = [v for v in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",") if v]
INSTALLED_APPS = ["django.contrib.admin","django.contrib.auth","django.contrib.contenttypes","django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles","core"]
MIDDLEWARE = ["django.middleware.security.SecurityMiddleware","whitenoise.middleware.WhiteNoiseMiddleware","django.contrib.sessions.middleware.SessionMiddleware","django.middleware.common.CommonMiddleware","django.middleware.csrf.CsrfViewMiddleware","django.contrib.auth.middleware.AuthenticationMiddleware","django.contrib.messages.middleware.MessageMiddleware","django.middleware.clickjacking.XFrameOptionsMiddleware"]
ROOT_URLCONF = "config.urls"
TEMPLATES = [{"BACKEND":"django.template.backends.django.DjangoTemplates","DIRS":[BASE_DIR/"templates"],"APP_DIRS":True,"OPTIONS":{"context_processors":["django.template.context_processors.request","django.contrib.auth.context_processors.auth","django.contrib.messages.context_processors.messages"]}}]
WSGI_APPLICATION = "config.wsgi.application"
database_url = os.environ.get("DATABASE_URL")
if database_url:
    DATABASES = {"default": dj_database_url.parse(database_url, conn_max_age=600, ssl_require=not DEBUG)}
else:
    DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}
AUTH_PASSWORD_VALIDATORS = [{"NAME":"django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},{"NAME":"django.contrib.auth.password_validation.MinimumLengthValidator"},{"NAME":"django.contrib.auth.password_validation.CommonPasswordValidator"},{"NAME":"django.contrib.auth.password_validation.NumericPasswordValidator"}]
LANGUAGE_CODE="en-gb"
TIME_ZONE="Europe/London"
USE_I18N=True
USE_TZ=True
STATIC_URL="static/"
STATIC_ROOT=BASE_DIR/"staticfiles"
STATICFILES_DIRS=[BASE_DIR/"static"]
MEDIA_URL="/media/"
MEDIA_ROOT=BASE_DIR/"media"
# --- Cloudinary media storage -------------------------------------------------
# Credentials come only from the environment. Either set CLOUDINARY_URL
# (cloudinary://API_KEY:API_SECRET@CLOUD_NAME) or all three of
# CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY and CLOUDINARY_API_SECRET.
# With neither, uploads fall back to local disk (fine for local dev only).
def _env(name):
    return os.environ.get(name, "").strip()

_CLD_PARTS = {"CLOUD_NAME": _env("CLOUDINARY_CLOUD_NAME"), "API_KEY": _env("CLOUDINARY_API_KEY"), "API_SECRET": _env("CLOUDINARY_API_SECRET")}
CLOUDINARY_URL_VALID = _env("CLOUDINARY_URL").startswith("cloudinary://") and "@" in _env("CLOUDINARY_URL")
CLOUDINARY_PARTS_COMPLETE = all(_CLD_PARTS.values())
CLOUDINARY_PARTIAL = (bool(_env("CLOUDINARY_URL")) and not CLOUDINARY_URL_VALID) or (any(_CLD_PARTS.values()) and not CLOUDINARY_PARTS_COMPLETE and not CLOUDINARY_URL_VALID)
USE_CLOUDINARY = CLOUDINARY_URL_VALID or CLOUDINARY_PARTS_COMPLETE
if USE_CLOUDINARY:
    INSTALLED_APPS += ["cloudinary_storage", "cloudinary"]
    if not CLOUDINARY_URL_VALID:
        CLOUDINARY_STORAGE = dict(_CLD_PARTS)
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage" if USE_CLOUDINARY else "django.core.files.storage.FileSystemStorage"
    },
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"
