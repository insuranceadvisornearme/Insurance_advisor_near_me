from django.conf import settings

def get_meta_tags(page_title, description=None, keywords=None, extra=None):
    return {
        'title': f"{page_title} | LIC Insurance Advisor",
        'description': description or "Certified LIC Agent",
        'keywords': keywords or ['LIC', 'insurance', 'advisor']
    }