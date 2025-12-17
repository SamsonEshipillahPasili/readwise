from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import CreateAccountRequestForm

class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'

class SignUpView(FormView):
    template_name = 'accounts/sign_up.html'
    form_class = CreateAccountRequestForm
    success_url = '/accounts/sign-up'

class ForgotPasswordTemplateView(TemplateView):
    template_name = 'accounts/forgot_password.html'

class ResetPasswordTemplateView(TemplateView):
    template_name = 'accounts/reset_password.html'
