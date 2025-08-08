from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    HomeView,
    LocationView,
    PlanListView,
    PlanDetailView,
    ServiceAreaView,
    AboutView,
    ContactView,
    TestimonialsView,
    contact_submit,
    ajax_contact
)
from advisor.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # Main pages
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('testimonials/', TestimonialsView.as_view(), name='testimonials'),
    path('service-areas/', ServiceAreaView.as_view(), name='service_areas'),
    path('about-lic-agent/', AboutView.as_view(), name='about_lic_agent'),
    path('contact-lic-agent/', ContactView.as_view(), name='contact_lic_agent'),
    path('client-testimonials/', TestimonialsView.as_view(), name='client_testimonials'),
    
    # SEO URLs
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    
    # Location pages
    path('lic-agent-virar/', LocationView.as_view(), kwargs={'location_slug': 'virar'}, name='virar'),
    path('lic-agent-vasai/', LocationView.as_view(), kwargs={'location_slug': 'vasai'}, name='vasai'),
    path('lic-agent-nallasopara/', LocationView.as_view(), kwargs={'location_slug': 'nallasopara'}, name='nallasopara'),
    path('lic-agent-naigaon/', LocationView.as_view(), kwargs={'location_slug': 'naigaon'}, name='naigaon'),
    path('lic-agent-bhayandar/', LocationView.as_view(), kwargs={'location_slug': 'bhayandar'}, name='bhayandar'),
    path('lic-agent-mira-road/', LocationView.as_view(), kwargs={'location_slug': 'mira-road'}, name='mira_road'),
    path('lic-agent-dahisar/', LocationView.as_view(), kwargs={'location_slug': 'dahisar'}, name='dahisar'),
    path('lic-agent-borivali/', LocationView.as_view(), kwargs={'location_slug': 'borivali'}, name='borivali'),
    path('lic-agent-palghar/', LocationView.as_view(), kwargs={'location_slug': 'palghar'}, name='palghar'),
    path('lic-agent-mumbai/', LocationView.as_view(), kwargs={'location_slug': 'mumbai'}, name='mumbai'),
    
    # Plan pages
    path('lic-plans/', PlanListView.as_view(), name='plan_list'),
    path('lic-plans/<slug:plan_slug>/', PlanDetailView.as_view(), name='plan_detail'),
    
    # Form submissions
    path('contact-submit/', contact_submit, name='contact_submit'),
    path('ajax-contact/', ajax_contact, name='ajax_contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'advisor.views.handler404'
handler500 = 'advisor.views.handler500'