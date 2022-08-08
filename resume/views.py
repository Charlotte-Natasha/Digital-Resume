from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.views import generic
from .forms import *

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "resume/index.html"

def get_context_data(self, **kwargs):
	context = get_context_data(**kwargs)
	
	testimonials = Testimonial.objects.filter(is_active=True)
	certificates = Certificate.objects.filter(is_active=True)
	blogs = Blog.objects.filter(is_active=True)
	portfolio = Portfolio.objects.filter(is_active=True)
	
	context["testimonials"] = testimonials
	context["certificates"] = certificates
	context["blogs"] = blogs
	context["portfolio"] = portfolio
	return context

# class ContactView(generic.FormView):

#     template_name = 'resume/contact.html'
#     form_class = ContactForm
#     success_url = '/'

#     def form_valid(self, form):
#         form.save()
#         messages.success(self.request, 'Thankyou. We will be in touch soon')
#         return super().form_valid(form)