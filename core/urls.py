from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('browse', views.BrowseTemplateView.as_view(), name='browse'),
]
