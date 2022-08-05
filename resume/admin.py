from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')

admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name')

admin.site.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')

admin.site.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug')

admin.site.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug')

admin.site.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
