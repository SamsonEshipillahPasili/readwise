from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign-in', views.SignInView.as_view(), name='sign_in'),
    path('sign-up', views.SignUpTemplateView.as_view(), name='sign_up'),
    path('sign-out', views.SignOutView.as_view(), name='sign_out'),
    path('forgot-password', views.ForgotPasswordTemplateView.as_view(), name='forgot_password'),
    path('reset-password', views.ResetPasswordTemplateView.as_view(), name='reset_password'),
]
