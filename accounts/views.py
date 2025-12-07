from django.shortcuts import render
from django.views.generic import TemplateView

class SignInTemplateView(TemplateView):
    template_name = 'accounts/sign_in.html'
