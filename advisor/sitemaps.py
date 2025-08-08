from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import InsurancePlan, ServiceArea

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return [
            'home',
            'about',
            'contact',
            'testimonials',
            'service_areas',
            'plan_list',
            'plans',
        ]

    def location(self, item):
        return reverse(item)

class PlansSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return InsurancePlan.objects.filter(is_active=True)

    def location(self, obj):
        return reverse('plan_detail', args=[obj.slug])

class LocationSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return ServiceArea.objects.filter(is_active=True)

    def location(self, obj):
        return reverse(obj.slug)