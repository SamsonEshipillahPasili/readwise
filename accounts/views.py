from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'

class SignUpTemplateView(TemplateView):
    template_name = 'accounts/sign_up.html'


class ForgotPasswordTemplateView(TemplateView):
    template_name = 'accounts/forgot_password.html'

class ResetPasswordTemplateView(TemplateView):
    template_name = 'accounts/reset_password.html'
