import uuid
import logging

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.views import View
from django.contrib.auth.views import (
    LoginView, PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from django.urls import reverse, reverse_lazy
from django.contrib.messages import error, success
from django.contrib.auth import login

from .forms import CreateAccountRequestForm
from .models import CreateAccountRequest

logger = logging.getLogger(__name__)

class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'

class SignUpView(FormView):
    template_name = 'accounts/sign_up.html'
    form_class = CreateAccountRequestForm
    success_url = reverse_lazy('accounts:sign_up_started')

    def form_valid(self, form):
        # Save the registration request to db.
        request = CreateAccountRequest.objects.create_request(
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
            username=form.cleaned_data.get('username'),
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password'),
        )

        # Send registration email.
        request.send_registration_email()

        return super().form_valid(form)

class AccountsResetPasswordView(PasswordResetView):
    template_name = 'accounts/reset_password.html'
    success_url = reverse_lazy('accounts:reset_password_done')

    # email configuration
    from_email = 'inotifiers@gmail.com'
    email_template_name = 'accounts/reset_password_email.txt'
    subject_template_name = 'accounts/reset_password_subject.txt'

class AccountsResetPasswordDoneView(PasswordResetDoneView):
    template_name = 'accounts/reset_password_done.html'

class AccountsResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/reset_password_confirm.html'
    success_url = reverse_lazy('accounts:reset_password_complete')

class AccountsResetPasswordCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/reset_password_complete.html'

class SignUpStartedView(TemplateView):
    template_name = 'accounts/sign_up_started.html'


class CompleteSignUpView(View):
    def get(self, req: HttpRequest, token: uuid.UUID) -> HttpResponse:
        # retrieve the request
        request = CreateAccountRequest.objects.filter(token=token).first()

        # assert the request exists.
        if not request:
            error(req, "The link is invalid or has expired")
            return HttpResponseRedirect(reverse('accounts:sign_in'))

        # attempt to create an account 
        try:
            user = request.create_account()
        except ValueError as e:
            error(req, "The link is invalid or has expired.")
            logger.exception(e)
            return HttpResponseRedirect(reverse('accounts:sign_in'))
        
        # log the user in automatically
        success(req, 'Sign up was successful!')
        login(req, user)
        return HttpResponseRedirect(reverse('core:browse'))
