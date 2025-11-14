import os
from pathlib import Path
from dotenv import load_dotenv

# -----------------------
# Rutas base
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))

# -----------------------
# Seguridad y depuración
# -----------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'clave_segura_por_defecto')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS dinámico según entorno
if DEBUG:
    ALLOWED_HOSTS = ['*']  # Desarrollo local
else:
    ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'hospitalmanagement-sqlservergrupo2.onrender.com')]

# -----------------------
# Aplicaciones instaladas
# -----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hospital',
    'widget_tweaks',
]

# -----------------------
# Middleware
# -----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Archivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hospitalmanagement.urls'

# -----------------------
# Templates
# -----------------------
TEMPLATES_DIR = BASE_DIR / 'templates'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'hospitalmanagement.wsgi.application'

# -----------------------
# Base de datos PostgreSQL con SSL
# -----------------------
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
        'OPTIONS': {
            'sslmode': 'require',  # obligatorio en Render
        }
    }
}

# -----------------------
# Validadores de contraseña
# -----------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------
# Internacionalización
# -----------------------
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/El_Salvador'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -----------------------
# Archivos estáticos y media
# -----------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Servir media en desarrollo
if DEBUG:
    from django.conf.urls.static import static
    from django.urls import path
    urlpatterns = static(MEDIA_URL, document_root=MEDIA_ROOT)

# -----------------------
# Login / Logout
# -----------------------
LOGIN_REDIRECT_URL = '/afterlogin'
LOGOUT_REDIRECT_URL = '/'

# -----------------------
# Email
# -----------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')

# -----------------------
# DEFAULT_AUTO_FIELD
# -----------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'






