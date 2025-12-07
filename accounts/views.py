from django.shortcuts import render
from django.views.generic import TemplateView

class SignInTemplateView(TemplateView):
    template_name = 'accounts/sign_in.html'


class SignUpTemplateView(TemplateView):
    template_name = 'accounts/sign_up.html'


class ForgotPasswordTemplateView(TemplateView):
    template_name = 'accounts/forgot_password.html'
