import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'change-me-in-env')  # Keep secret in Render ENV
DEBUG = os.getenv('DEBUG', 'False') == 'True'  # False in production

ALLOWED_HOSTS = [
    'www.insuranceadvisornearme.com',
    'insuranceadvisornearme.com',
    'insurance-advisor-near-me-7v6l.onrender.com',
    'localhost',
]

# Security settings for production
if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'advisor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for static files in Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'insuranceadvisor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'advisor/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'advisor.context_processors.seo_meta',
                'advisor.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'insuranceadvisor.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use Postgres in production if needed
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static & Media settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'advisor/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings (from environment variables)
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)
CONTACT_EMAIL = os.getenv('CONTACT_EMAIL', DEFAULT_FROM_EMAIL)

# SEO Settings
SEO_SITE_NAME = "LIC Insurance Advisor - Avinash Chauhan"
SEO_BASE_URL = "https://www.insuranceadvisornearme.com"
SEO_DEFAULT_DESCRIPTION = "Certified LIC Agent Avinash Chauhan (Code: 02927-91N) serving Virar, Vasai, Nallasopara and nearby areas"
SEO_DEFAULT_KEYWORDS = [
    "LIC agent", "insurance advisor", "Virar", "Vasai", "Nallasopara",
    "Naigaon", "Bhayandar", "Mira Road", "Dahisar", "Borivali", "Palghar",
    "Mumbai", "life insurance", "policy advisor", "Avinash Chauhan"
]
SEO_DEFAULT_IMAGE = f"{SEO_BASE_URL}/static/images/lic-advisor-avinash-chauhan.png"
SEO_TWITTER_HANDLE = "@yourtwitterhandle"

# Local Business Info
LOCAL_BUSINESS_NAME = "LIC Insurance Advisor - Avinash Chauhan"
LOCAL_BUSINESS_PHONE = "+917620485529"
LOCAL_BUSINESS_ADDRESS = {
    "street": "Virar East",
    "locality": "Palghar",
    "region": "Maharashtra",
    "postal_code": "401303",
    "country": "India"
}
LOCAL_BUSINESS_GEO = {
    "latitude": "19.4558",
    "longitude": "72.8116"
}
LOCAL_BUSINESS_HOURS = "Mo-Sa 09:00-18:00"
LOCAL_BUSINESS_LOGO = f"{SEO_BASE_URL}/static/images/lic-logo.png"

SITE_ID = 1

# Custom 404 handler
handler404 = 'advisor.views.custom_404'
