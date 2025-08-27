import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# کلید مخفی ساده برای توسعه (در پروداکشن حتما تغییرش بده)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'unsafe-secret-key-for-dev-only')

# فعال بودن حالت دیباگ
DEBUG = os.getenv('DJANGO_DEBUG', 'True').lower() in ['true', '1', 'yes']

# میزبان‌های مجاز (localhost و 127.0.0.1 پیش‌فرض)
ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# برای محیط تست، ریدایرکت HTTPS رو غیرفعال کن
SECURE_SSL_REDIRECT = False

# کوکی‌ها بدون secure برای تست
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# غیرفعال کردن header پراکسی برای محیط تست (در صورت نیاز فعال کن)
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# CORS باز برای تست
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
    'x-csrftoken',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'tasks',
    'user',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # حتما بالاتر از CommonMiddleware
    'django.middleware.common.CommonMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'planning.urls'

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

WSGI_APPLICATION = 'planning.wsgi.application'

# دیتابیس: پیش‌فرض SQLite برای توسعه، می‌تونی با env تغییر بدی
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('POSTGRES_USER', ''),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', ''),
    }
}

# تنظیمات DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'planning.authentication.CustomTokenAuthentication',  # یا برای تست از SessionAuthentication استفاده کن
        # 'rest_framework.authentication.SessionAuthentication',
    )
}

#AUTH_PASSWORD_VALIDATORS = [
    # در تست می‌تونی اینارو غیرفعال کنی یا نگه داری
#]

AUTH_USER_MODEL = 'user.User'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ایمیل برای توسعه
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# لاگینگ در حالت DEBUG
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler'}},
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
