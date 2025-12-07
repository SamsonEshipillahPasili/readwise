from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign-in', views.SignInTemplateView.as_view(), name='sign_in'),
    path('sign-up', views.SignUpTemplateView.as_view(), name='sign-up'),
    path('forgot-password', views.ForgotPasswordTemplateView.as_view(), name='forgot-password'),
]
