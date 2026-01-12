from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('browse', views.BrowseTemplateView.as_view(), name='browse'),
    path('shelves', views.ShelvesTemplateView.as_view(), name='shelves'),
    path('add-shelf', views.AddShelfView.as_view(), name='add_shelf'),
    path('wishlist', views.WishlistTemplateView.as_view(), name='wishlist'),
    path('profile', views.ProfileTemplateView.as_view(), name='profile'),
    path('settings', views.SettingsTemplateView.as_view(), name='settings'),
]
