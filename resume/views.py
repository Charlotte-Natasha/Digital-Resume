from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.views import generic
from .forms import *

# Create your views here.
# class ContactView(generic.FormView):

#     template_name = 'resume/contact.html'
#     form_class = ContactForm
#     success_url = '/'

#     def form_valid(self, form):
#         form.save()
#         messages.success(self.request, 'Thankyou. We will be in touch soon')
#         return super().form_valid(form)