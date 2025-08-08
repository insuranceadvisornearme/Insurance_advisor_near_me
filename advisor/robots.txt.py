# advisor/robots.txt.py
from django.http import HttpResponse
from django.template.loader import render_to_string

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /static/admin/",
        "Allow: /",
        "",
        f"Sitemap: {request.build_absolute_uri(reverse('sitemap'))}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")