import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# .env faylini yuklash
load_dotenv(BASE_DIR / '.env')

# Xavfsizlik sozlamalari
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-$mko2&wr=o&ei0n#2hv29nr5sm)=&8!%2yw&dwya3mq8nanfqj'
)

DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    # Jazzmin admin panel (django.contrib.admin dan oldin turishi SHART)
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Uchinchi tomon ilovalari
    'rest_framework',
    'drf_spectacular',
    'corsheaders',

    # Loyiha ilovalari
    'books.apps.BooksConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise statik fayllarni server orqali tezkor tarqatish uchun
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # CORS middleware (Frontend va Mobile ilovalar uchun)
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Railway Volume sozlamalari
# Masalan, Railway Volume o'rnatilgan yo'l: /data yoki /app/media
VOLUME_PATH = os.getenv('RAILWAY_VOLUME_MOUNT_PATH') or os.getenv('VOLUME_PATH')

if VOLUME_PATH:
    volume_dir = Path(VOLUME_PATH)
    volume_dir.mkdir(parents=True, exist_ok=True)
    MEDIA_ROOT = volume_dir / 'media'
    default_db_url = f"sqlite:///{volume_dir / 'db.sqlite3'}"
else:
    MEDIA_ROOT = Path(os.getenv('MEDIA_ROOT', BASE_DIR / 'media'))
    default_db_url = f"sqlite:///{BASE_DIR / 'db.sqlite3'}"

MEDIA_ROOT.mkdir(parents=True, exist_ok=True)

# Database: Agar DATABASE_URL (masalan PostgreSQL) bo'lsa uni ishlatadi,
# bo'lmasa volume yoki lokal sqlite3 faylini ishlatadi.
DATABASES = {
    'default': dj_database_url.config(
        default=default_db_url,
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Password validation
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
LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}
WHITENOISE_MANIFEST_STRICT = False

# Media files (PDFs, Images)
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# Swagger / OpenAPI sozlamalari
SPECTACULAR_SETTINGS = {
    'TITLE': 'Kitoblar API (Book API)',
    'DESCRIPTION': 'Kitoblar uchun REST API - Swagger UI va OpenAPI 3.0 hujjatlari',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
}

# CORS sozlamalari
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# CSRF sozlamalari (Railway domenlari uchun)
CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
    'https://*.up.railway.app',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

# Django Jazzmin sozlamalari
JAZZMIN_SETTINGS = {
    "site_title": "Kitoblar Admin",
    "site_header": "Kutubxona Boshqaruvi",
    "site_brand": "Kitob API",
    "welcome_sign": "Kitoblar boshqaruv paneliga xush kelibsiz!",
    "copyright": "Kitoblar API",
    "search_model": ["books.Book"],
    "topmenu_links": [
        {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Swagger UI", "url": "/api/docs/", "new_window": True},
        {"name": "Kitoblar API", "url": "/api/books/", "new_window": True},
    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "books.Book": "fas fa-book",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "show_sidebar": True,
    "navigation_expanded": True,
    "changeform_format": "horizontal_tabs",
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "default_theme_mode": "auto",
}
