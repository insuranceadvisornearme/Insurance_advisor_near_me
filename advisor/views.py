# advisor/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from .models import InsurancePlan, ServiceArea, Testimonial
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .seo.meta_tags import get_meta_tags
from django.shortcuts import render

def handler404(request, exception):
    return render(request, 'advisor/404.html', status=404)

def handler500(request):
    return render(request, 'advisor/500.html', status=500)

class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'current_year': datetime.now().year,
            'service_areas': ServiceArea.objects.filter(is_active=True),
            'testimonials': Testimonial.objects.filter(is_active=True),
            'current_month': datetime.now().strftime("%B %Y"),
            'meta': get_meta_tags(
                "LIC Insurance Advisor",
                "Certified LIC Agent Avinash Chauhan (Code: 02927-91N) serving Virar, Vasai, Nallasopara and nearby areas",
                ["LIC agent", "insurance advisor", "Virar", "Vasai", "Mumbai"]
            )
        })
        return context

class HomeView(BaseView):
    template_name = 'advisor/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_plans'] = InsurancePlan.objects.filter(is_active=True, is_featured=True)[:6]
        return context

class LocationView(BaseView):
    template_name = 'advisor/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        location_slug = self.kwargs.get('location_slug')
        try:
            location = ServiceArea.objects.get(slug=location_slug)
            context.update({
                'location': location.name,
                'meta': get_meta_tags(
                    f"LIC Agent in {location.name} | Avinash Chauhan",
                    f"Certified LIC Agent serving {location.name} and nearby areas. Get expert advice on LIC policies.",
                    [f"LIC agent in {location.name}", "insurance advisor", location.name]
                )
            })
        except ServiceArea.DoesNotExist:
            pass
        return context

class PlanListView(ListView):
    model = InsurancePlan
    template_name = 'advisor/plan_list.html'
    context_object_name = 'plans'
    
    def get_queryset(self):
        return InsurancePlan.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta'] = get_meta_tags(
            "All LIC Insurance Plans | Compare Policies",
            "Compare all LIC insurance plans with features, benefits and eligibility criteria",
            ["LIC plans", "insurance policies", "compare LIC"]
        )
        return context

class PlanDetailView(DetailView):
    model = InsurancePlan
    template_name = 'advisor/plan_detail.html'
    context_object_name = 'plan'
    slug_field = 'slug'
    slug_url_kwarg = 'plan_slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plan = self.get_object()
        context['meta'] = get_meta_tags(
            f"{plan.name} (Plan {plan.number}) - Details",
            plan.short_description,
            [f"LIC {plan.name}", f"Plan {plan.number}", "insurance policy"]
        )
        return context

class ServiceAreaView(BaseView):
    template_name = 'advisor/service_areas.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta'] = get_meta_tags(
            "LIC Service Areas | Virar, Vasai, Nallasopara",
            "Certified LIC Agent serving multiple areas in Palghar and Mumbai",
            ["LIC service areas", "coverage areas", "insurance advisor near me"]
        )
        return context

class AboutView(BaseView):
    template_name = 'advisor/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta'] = get_meta_tags(
            "About LIC Agent Avinash Chauhan",
            "Learn about certified LIC Agent Avinash Chauhan with years of experience in insurance advisory",
            ["about LIC agent", "Avinash Chauhan profile", "insurance advisor"]
        )
        return context

class ContactView(BaseView):
    template_name = 'advisor/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta'] = get_meta_tags(
            "Contact LIC Insurance Advisor",
            "Get in touch with certified LIC Agent Avinash Chauhan for policy advice and consultation",
            ["contact LIC agent", "insurance consultation", "policy inquiry"]
        )
        return context

class TestimonialsView(ListView):
    model = Testimonial
    template_name = 'advisor/testimonials.html'
    context_object_name = 'testimonials'
    
    def get_queryset(self):
        return Testimonial.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta'] = get_meta_tags(
            "Client Testimonials | LIC Insurance Advisor",
            "Read what our clients say about our LIC insurance advisory services",
            ["LIC testimonials", "client reviews", "insurance feedback"]
        )
        return context

@require_POST
def contact_submit(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    location = request.POST.get('location')
    plan_interest = request.POST.get('plan_interest', 'Not specified')
    
    # Save to database (you would create a Contact model for this)
    # Contact.objects.create(name=name, phone=phone, location=location, plan_interest=plan_interest)
    
    # Send email
    subject = f"New LIC Inquiry from {name}"
    message = (
        f"Name: {name}\n"
        f"Phone: {phone}\n"
        f"Location: {location}\n"
        f"Interested Plan: {plan_interest}\n\n"
        f"Please contact them as soon as possible."
    )
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.CONTACT_EMAIL],
        fail_silently=False,
    )
    
    messages.success(request, 'Thank you! We will contact you shortly.')
    return redirect('home')

@csrf_exempt
@require_POST
def ajax_contact(request):
    try:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Process the data (save to DB, send email, etc.)
        
        return JsonResponse({'status': 'success', 'message': 'Thank you for your inquiry!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

def handler404(request, exception):
    return render(request, 'advisor/404.html', status=404)

def handler500(request):
    return render(request, 'advisor/500.html', status=500)