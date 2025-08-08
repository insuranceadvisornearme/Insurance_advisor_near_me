from django.conf import settings

def seo_meta(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_URL': settings.SITE_URL,
        'SEO_DESCRIPTION': settings.SEO_DEFAULT_DESCRIPTION,
        'SEO_KEYWORDS': ', '.join(settings.SEO_DEFAULT_KEYWORDS),
        'LOCAL_BUSINESS': settings.LOCAL_BUSINESS,
        'CANONICAL_URL': request.build_absolute_uri(request.path),
    }
