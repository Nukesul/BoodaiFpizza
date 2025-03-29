"""
Настройки Django для проекта backend.
Сгенерировано командой 'django-admin startproject' с использованием Django 4.2.
Для дополнительной информации об этом файле смотрите:
https://docs.djangoproject.com/en/4.2/topics/settings/
"""

from pathlib import Path
import os

# Построение путей внутри проекта, например: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ПРЕДУПРЕЖДЕНИЕ О БЕЗОПАСНОСТИ: держите секретный ключ в тайне в продакшене!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-%x&kg-nx75kirv^12#m@y0f486)4bphas#&6-m224qr%4iv$2o')

# ПРЕДУПРЕЖДЕНИЕ О БЕЗОПАСНОСТИ: не запускайте с включенным дебагом в продакшене!
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

# Разрешенные хосты
ALLOWED_HOSTS = [
    'localhost',                    # Локальный хост
    '127.0.0.1',                   # Локальный IP
    'vh438.timeweb.ru',            # Хостинг сервер
    'boodaikg.com',               # Основной домен
    'https://nukesul-boodaifpizza-5206.twc1.net',  # Дополнительный домен
    '0.0.0.0',                    # Для Docker
]

# Порт сервера (используется для запуска)
PORT = int(os.getenv('PORT', 3000))  # Изменен на 3000

# Определение приложений
INSTALLED_APPS = [
    'admin_interface',             # Интерфейс админки
    'colorfield',                 # Поля для цветов
    'django.contrib.admin',       # Админ панель
    'django.contrib.auth',        # Аутентификация
    'django.contrib.contenttypes',# Типы контента
    'django.contrib.sessions',    # Сессии
    'django.contrib.messages',    # Сообщения
    'django.contrib.staticfiles', # Статические файлы
    'rest_framework',            # REST API
    'rest_framework.authtoken',  # Токены для API
    'corsheaders',              # Поддержка CORS
    'shop',                    # Приложение магазина
]

# Промежуточное ПО
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',        # Безопасность
    'django.contrib.sessions.middleware.SessionMiddleware', # Сессии
    'corsheaders.middleware.CorsMiddleware',               # CORS (должен быть выше CommonMiddleware)
    'django.middleware.common.CommonMiddleware',          # Общие функции
    'django.middleware.csrf.CsrfViewMiddleware',         # Защита от CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Аутентификация
    'django.contrib.messages.middleware.MessageMiddleware',   # Сообщения
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Защита от кликджекинга
]

# Настройки CORS
CORS_ALLOWED_ORIGINS = [
    "https://boodaikg.com",  # Основной фронтенд домен
]

CORS_ALLOW_CREDENTIALS = True  # Разрешить отправку учетных данных

CORS_ALLOW_METHODS = [
    "DELETE",  # Удаление
    "GET",    # Получение
    "OPTIONS",# Опции
    "PATCH",  # Частичное обновление
    "POST",   # Создание
    "PUT",    # Полное обновление
]

CORS_ALLOW_HEADERS = [
    "accept",           # Принимаемые типы
    "accept-encoding", # Кодирование
    "authorization",   # Авторизация
    "content-type",    # Тип контента
    "dnt",            # Не отслеживать
    "origin",        # Источник
    "user-agent",    # Агент пользователя
    "x-csrftoken",   # CSRF токен
    "x-requested-with", # Запрос AJAX
]

# Доверенные источники CSRF
CSRF_TRUSTED_ORIGINS = [
    'https://boodaikg.com',  # Основной фронтенд домен
]

ROOT_URLCONF = 'backend.urls'  # Основной файл URL маршрутов

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "shop" / "templates"],  # Директория шаблонов
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',      # Дебаг
                'django.template.context_processors.request',    # Запрос
                'django.contrib.auth.context_processors.auth',   # Аутентификация
                'django.contrib.messages.context_processors.messages', # Сообщения
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'  # WSGI приложение

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} if DEBUG else {
    'default': {
        'ENGINE': 'django.db.backends.mysql',    # Движок MySQL
        'NAME': 'ch79145_boodai',               # Имя БД
        'USER': 'ch79145_boodai',              # Пользователь
        'PASSWORD': '16162007',               # Пароль
        'HOST': 'vh438.timeweb.ru',          # Хост
        'PORT': '3306',                     # Порт
        'OPTIONS': {
            'charset': 'utf8mb4',          # Кодировка
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", # Режим SQL
        },
    }
}

# Валидаторы паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'}, # Похожесть с данными пользователя
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},          # Минимальная длина
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},        # Обычные пароли
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},      # Только цифры
]

# Интернационализация
LANGUAGE_CODE = 'ru-ru'  # Русский язык
TIME_ZONE = 'UTC'       # Временная зона UTC
USE_I18N = True        # Поддержка интернационализации
USE_L10N = True       # Поддержка локализации
USE_TZ = False       # Отключение часовых поясов

# Статические файлы
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Директория статических файлов
STATIC_ROOT = BASE_DIR / "staticfiles"   # Сбор статических файлов

# Медиа файлы
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Директория медиа

# Ограничения загрузки файлов
FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10 МБ
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10 МБ

# Настройки REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',   # Токен аутентификация
        'rest_framework.authentication.SessionAuthentication', # Сессионная аутентификация
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly', # Доступ только для чтения без аутентификации
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,  # Размер страницы пагинации
}

# Настройки email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Вывод email в консоль

# Логирование
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},           # Вывод в консоль
        'file': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log',                 # Файл логов
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',                                   # Уровень логирования
        },
        'shop': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',                                 # Уровень для приложения shop
        },
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Тип автоинкрементного поля

# Настройки безопасности для продакшена
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # Прокси HTTPS
    SECURE_SSL_REDIRECT = True                                   # Перенаправление на HTTPS
    SESSION_COOKIE_SECURE = True                                # Безопасные cookies сессии
    CSRF_COOKIE_SECURE = True                                  # Безопасные CSRF cookies
    SECURE_HSTS_SECONDS = 31536000                            # HSTS на год
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True                    # HSTS для поддоменов
    SECURE_HSTS_PRELOAD = True                              # Предзагрузка HSTS
    SECURE_CONTENT_TYPE_NOSNIFF = True                     # Защита от MIME-сниффинга
    SECURE_BROWSER_XSS_FILTER = True                      # Фильтр XSS
    X_FRAME_OPTIONS = 'DENY'                             # Запрет фреймов