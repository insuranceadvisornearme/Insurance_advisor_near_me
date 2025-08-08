# advisor/context_processors.py
from django.conf import settings
from .models import ServiceArea
from datetime import datetime

def seo_meta(request):
    return {
        'SEO_SITE_NAME': settings.SEO_SITE_NAME,
        'SEO_BASE_URL': settings.SEO_BASE_URL,
        'SEO_DEFAULT_IMAGE': settings.SEO_DEFAULT_IMAGE,
    }

def site_settings(request):
    return {
        'SITE_PHONE': settings.LOCAL_BUSINESS_PHONE,
        'SITE_EMAIL': settings.CONTACT_EMAIL,
        'SERVICE_AREAS': ServiceArea.objects.filter(is_active=True),
        'CURRENT_YEAR': datetime.now().year,
    }