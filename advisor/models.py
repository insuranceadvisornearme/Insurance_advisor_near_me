# advisor/models.py
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

class ServiceArea(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Service Area'
        verbose_name_plural = 'Service Areas'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('location_detail', kwargs={'location_slug': self.slug})

class InsurancePlan(models.Model):
    PLAN_TYPES = (
        ('endowment', 'Endowment Plan'),
        ('moneyback', 'Money Back Plan'),
        ('term', 'Term Insurance'),
        ('ulip', 'ULIP Plan'),
        ('pension', 'Pension Plan'),
        ('child', 'Child Plan'),
        ('health', 'Health Plan'),
    )
    
    number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    plan_type = models.CharField(max_length=20, choices=PLAN_TYPES)
    short_description = models.TextField()
    full_description = models.TextField()
    features = models.TextField(help_text="List features separated by new lines")
    benefits = models.TextField(help_text="List benefits separated by new lines")
    eligibility = models.TextField(help_text="List eligibility criteria separated by new lines")
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['plan_type', 'name']
        verbose_name = 'Insurance Plan'
        verbose_name_plural = 'Insurance Plans'

    def __str__(self):
        return f"{self.name} (Plan {self.number})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.number}")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('plan_detail', kwargs={'plan_slug': self.slug})

    def get_features_list(self):
        return self.features.split('\n') if self.features else []

    def get_benefits_list(self):
        return self.benefits.split('\n') if self.benefits else []

    def get_eligibility_list(self):
        return self.eligibility.split('\n') if self.eligibility else []

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    location = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"Testimonial from {self.client_name}"

class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    plan_interest = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=True)
    is_contacted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Request'
        verbose_name_plural = 'Contact Requests'

    def __str__(self):
        return f"Contact from {self.name} - {self.phone}"