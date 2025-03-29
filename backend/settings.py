# backend/settings.py

from pathlib import Path
import os
# Библиотека для работы с переменными окружения (например, из файла .env)
# Рекомендуется установить: pip install python-dotenv
# и добавить в начало файла manage.py и wsgi.py:
# import dotenv
# dotenv.load_dotenv()
# Это позволит хранить секреты (SECRET_KEY, пароль БД) вне кода.
from dotenv import load_dotenv

load_dotenv() # Загружаем переменные из .env файла, если он есть

BASE_DIR = Path(__file__).resolve().parent.parent

# ВАЖНО: Секретный ключ не должен быть в коде в открытом виде.
# Используй переменные окружения. Значение по умолчанию здесь только для примера.
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-%x&kg-nx75kirv^12#m@y0f486)4bphas#&6-m224qr%4iv$2o')

# DEBUG = True - режим разработки (подробные ошибки, автоперезагрузка)
# DEBUG = False - продакшен режим (нужно настроить статику, ALLOWED_HOSTS)
# Берем значение из переменной окружения DJANGO_DEBUG. Если ее нет, по умолчанию False.
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

# Список хостов/доменов, с которых разрешено обслуживать сайт.
# Обязательно для DEBUG = False.
ALLOWED_HOSTS = [
    'localhost',        # Для локальной разработки
    '127.0.0.1',        # Для локальной разработки
    'vh438.timeweb.ru', # Хост базы данных (возможно, не нужен здесь, если он не для доступа к сайту)
    'boodaikg.com',     # Твой основной домен
    'www.boodaikg.com', # Твой основной домен с www
    'nukesul-boodaifpizza-5206.twc1.net', # Технический домен TimeWeb Cloud
    # Добавь сюда IP-адрес сервера, если обращаешься по IP
]


# Приложения Django
INSTALLED_APPS = [
    'admin_interface',          # Сторонний пакет для кастомизации админки
    'colorfield',               # Сторонний пакет для полей цвета в админке
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # Для работы со статическими файлами (CSS, JS, картинки)
    'rest_framework',           # Django REST framework для API
    'rest_framework.authtoken', # Для токен-аутентификации в API
    'corsheaders',              # Для обработки CORS-запросов (с других доменов, например, фронтенда)
    'shop',                     # Твое приложение магазина
    # 'whitenoise.runserver_nostatic', # Можно добавить для ТЕСТА статики с DEBUG=False локально
]

# Промежуточные обработчики запросов (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # ВАЖНО: WhiteNoise для обслуживания статики в продакшене (когда DEBUG=False)
    # Должен быть СРАЗУ ПОСЛЕ SecurityMiddleware и ПЕРЕД SessionMiddleware
    # Нужно установить: pip install whitenoise
    # Раскомментируй строку ниже после установки whitenoise
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Обработка CORS (важно для API и фронтенда на другом домене)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Настройки CORS (Cross-Origin Resource Sharing)
# Разрешаем запросы с этих доменов (например, с твоего фронтенда на React/Vue)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", # Для локальной разработки фронтенда
    "https://boodaikg.com",
    "https://www.boodaikg.com",
    "https://nukesul-boodaifpizza-5206.twc1.net",
]
CORS_ALLOW_CREDENTIALS = True # Разрешаем передавать куки и заголовки авторизации в CORS-запросах

# Домены, с которых разрешены POST/PUT/DELETE запросы (защита от CSRF)
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'https://boodaikg.com',
    'https://www.boodaikg.com',
    'https://nukesul-boodaifpizza-5206.twc1.net',
]

ROOT_URLCONF = 'backend.urls' # Главный файл URL-маршрутов

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], # Папка с общими шаблонами проекта
        'APP_DIRS': True, # Искать шаблоны также в папках приложений (shop/templates)
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application' # Точка входа для WSGI-серверов (Gunicorn/uWSGI)

# --- Настройки Базы Данных ---
# Используем MySQL. Данные лучше брать из переменных окружения.
DB_NAME = os.getenv('DB_NAME', 'ch79145_boodai')
DB_USER = os.getenv('DB_USER', 'ch79145_boodai')
DB_PASSWORD = os.getenv('DB_PASSWORD', '16162007') # ВАЖНО: Пароль брать ТОЛЬКО из окружения
DB_HOST = os.getenv('DB_HOST', 'vh438.timeweb.ru')
DB_PORT = os.getenv('DB_PORT', '3306')

DATABASES = {
    'default': {
        # Убедись, что установлен драйвер: pip install mysqlclient (или PyMySQL)
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'OPTIONS': {
            # Используем utf8mb4 для поддержки эмодзи и др. символов
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# УБРАН БЛОК try/except ДЛЯ ПРОВЕРКИ СОЕДИНЕНИЯ С БД ПРИ ЗАГРУЗКЕ НАСТРОЕК.
# Это была плохая практика. Django сам обработает ошибки соединения,
# когда попытается выполнить реальный запрос к БД. Это не будет
# замедлять старт приложения и даст более понятные ошибки в логах,
# если БД недоступна во время запроса.

# Валидаторы паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Настройки локализации
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Bishkek' # Установил для Кыргызстана, можно поменять на нужный
USE_I18N = True # Использовать интернационализацию (переводы)
USE_L10N = True # Использовать локализацию (форматы дат, чисел)
USE_TZ = True   # Использовать часовые пояса (рекомендуется True для корректной работы с датами/временем)

# --- Настройки статических файлов (CSS, JS, картинки) ---
STATIC_URL = '/static/' # URL-префикс для статических файлов
# Папки, где Django будет искать статику ВНЕ приложений (например, общие CSS/JS)
STATICFILES_DIRS = [BASE_DIR / "static"]
# Папка, КУДА будет собираться вся статика командой collectstatic
# Эту папку должен раздавать веб-сервер (Nginx) или WhiteNoise
STATIC_ROOT = BASE_DIR / "staticfiles"

# Настройки медиа-файлов (загружаемые пользователями)
MEDIA_URL = '/media/' # URL-префикс для медиа-файлов
# Папка на сервере, где будут храниться загруженные файлы
MEDIA_ROOT = BASE_DIR / 'media'

# Ограничения на размер загружаемых файлов (примерно 10 МБ)
FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024

# --- Настройки Django REST Framework ---
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',   # Аутентификация по токенам
        'rest_framework.authentication.SessionAuthentication', # Аутентификация по сессиям Django (для админки и browsable API)
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # Разрешать запросы всем (для GET), но требовать аутентификацию для POST/PUT/DELETE и т.д.
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12, # Количество элементов на странице по умолчанию
}

# Настройки Email (пример для вывода в консоль, для реальной отправки нужно настроить SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# --- Настройки логирования ---
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Вывод логов в консоль (удобно для Docker/платформ)
        'console': {'class': 'logging.StreamHandler'},
        # Запись логов в файл (полезно для отладки на сервере)
        'file': {
            'level': 'DEBUG', # Писать все уровни от DEBUG и выше
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log', # Путь к файлу логов
            'formatter': 'verbose', # Используем подробный форматтер
        },
    },
    'formatters': { # Добавляем форматтеры для логов
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'loggers': {
        # Логи самого Django
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO', # Писать сообщения уровня INFO и выше (WARNING, ERROR, CRITICAL)
            'propagate': False, # Не передавать сообщения вышестоящим логгерам
        },
        # Логи твоего приложения 'shop'
        'shop': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG', # Писать все сообщения от DEBUG и выше для твоего приложения
            'propagate': True, # Можно оставить True или False
        },
         # Логи базы данных (могут быть очень объемными!)
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR', # Писать только ошибки БД
            'propagate': False,
        },
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Настройки безопасности для продакшена (когда DEBUG=False) ---
# Эти настройки применяются только если DEBUG = False
if not DEBUG:
    # Сообщать Nginx/прокси, что используется HTTPS
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    # Принудительно перенаправлять все HTTP запросы на HTTPS
    SECURE_SSL_REDIRECT = True
    # Использовать secure cookies для сессий (передаются только по HTTPS)
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # Настройки HSTS (Strict Transport Security) - защита от MITM атак
    # Браузер будет принудительно использовать HTTPS для этого сайта в течение года
    SECURE_HSTS_SECONDS = 31536000 # 1 год
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True # Распространить на поддомены
    SECURE_HSTS_PRELOAD = True # Разрешить добавление в списки предзагрузки HSTS браузеров
    # Защита от XSS: Запретить браузеру угадывать Content-Type
    SECURE_CONTENT_TYPE_NOSNIFF = True
    # Защита от XSS: Включить встроенный в браузер XSS-фильтр
    SECURE_BROWSER_XSS_FILTER = True
    # Защита от кликджекинга: Запретить встраивание сайта во фреймы на других доменах
    X_FRAME_OPTIONS = 'DENY'

    # --- Оптимизация статики с WhiteNoise (опционально, но рекомендуется) ---
    # Раскомментируй эту строку, чтобы WhiteNoise сжимал статику (gzip/brotli) и кешировал ее надолго
    # Это уменьшит размер файлов и ускорит загрузку сайта.
    # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'