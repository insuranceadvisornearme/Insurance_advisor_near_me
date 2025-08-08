# advisor/sitemap_xml.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import InsurancePlan, ServiceArea
from django.http import HttpResponse
from django.template.loader import render_to_string
from .sitemaps import StaticViewSitemap, PlansSitemap, LocationSitemap

def sitemap_xml(request):
    sitemaps = {
        'static': StaticViewSitemap(),
        'plans': PlanSitemap(),
        'locations': LocationSitemap(),
    }
    
    xml = render_to_string('sitemap.xml', {'sitemaps': sitemaps})
    return HttpResponse(xml, content_type="application/xml")