# insuranceadvisor/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from advisor.sitemaps import StaticViewSitemap, PlansSitemap, LocationSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'plans': PlansSitemap,
    'locations': LocationSitemap,
}

urlpatterns = [
    path('adminAVINASHLIC/', admin.site.urls),
    path('', include('advisor.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]


# ये लाइनें अंत में जोड़ें
handler404 = 'advisor.views.handler404'  # 404 error के लिए
handler500 = 'advisor.views.handler500'  # 500 error के लिए