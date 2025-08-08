# advisor/admin.py
from django.contrib import admin
from .models import InsurancePlan, ServiceArea, Testimonial, ContactRequest

class InsurancePlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'plan_type', 'is_active', 'is_featured')
    list_filter = ('plan_type', 'is_active', 'is_featured')
    search_fields = ('name', 'number', 'short_description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')

class ServiceAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'location', 'rating', 'is_active')
    list_filter = ('is_active', 'rating')
    search_fields = ('client_name', 'location', 'content')
    readonly_fields = ('created_at', 'updated_at')

class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'location', 'is_contacted', 'created_at')
    list_filter = ('is_contacted', 'location')
    search_fields = ('name', 'phone', 'email', 'message')
    readonly_fields = ('created_at',)

admin.site.register(InsurancePlan, InsurancePlanAdmin)
admin.site.register(ServiceArea, ServiceAreaAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(ContactRequest, ContactRequestAdmin)