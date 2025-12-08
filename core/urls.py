from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('browse', views.BrowseTemplateView.as_view(), name='browse'),
    path('shelves', views.ShelvesTemplateView.as_view(), name='shelves'),
    path('wishlist', views.WishlistTemplateView.as_view(), name='wishlist'),
    path('friends', views.FriendsTemplateView.as_view(), name='friends'),
    path('chat', views.ChatTemplateView.as_view(), name='chat'),
    path('profile', views.ProfileTemplateView.as_view(), name='profile'),
    path('settings', views.SettingsTemplateView.as_view(), name='settings'),
]
