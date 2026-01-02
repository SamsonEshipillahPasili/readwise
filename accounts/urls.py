from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('sign-in', views.SignInView.as_view(), name='sign_in'),
    path('sign-up', views.SignUpView.as_view(), name='sign_up'),
    path('sign-out', LogoutView.as_view(), name='sign_out'),
    path('reset-password', views.AccountsResetPasswordView.as_view(), name='reset_password'),
    path('reset-password-done', views.AccountsResetPasswordDoneView.as_view(), name='reset_password_done'),
    path('reset-password-confirm/<str:uidb64>/<str:token>/', views.AccountsResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
    path('reset-password-complete/', views.AccountsResetPasswordCompleteView.as_view(), name='reset_password_complete'),
    path('sign-up-started', views.SignUpStartedView.as_view(), name='sign_up_started'),
    path('complete-signup/<uuid:token>', views.CompleteSignUpView.as_view(), name='complete_signup'),

]
