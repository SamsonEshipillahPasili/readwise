from django.urls import path
from .views import SignInTemplateView

app_name = 'accounts'

urlpatterns = [
    path('sign-in', SignInTemplateView.as_view(), name='sign_in')
]
