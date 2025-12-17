from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView

from .forms import CreateAccountRequestForm
from .models import CreateAccountRequest

class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'

class SignUpView(FormView):
    template_name = 'accounts/sign_up.html'
    form_class = CreateAccountRequestForm
    success_url = '/accounts/sign-up'

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

class ForgotPasswordTemplateView(TemplateView):
    template_name = 'accounts/forgot_password.html'

class ResetPasswordTemplateView(TemplateView):
    template_name = 'accounts/reset_password.html'
