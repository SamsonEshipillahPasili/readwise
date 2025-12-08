from django.shortcuts import render
from django.views.generic import TemplateView

class BrowseTemplateView(TemplateView):
    template_name = 'core/browse.html'

class ShelvesTemplateView(TemplateView):
    template_name = 'core/shelves.html'

class WishlistTemplateView(TemplateView):
    template_name = 'core/wishlist.html'

class FriendsTemplateView(TemplateView):
    template_name = 'core/friends.html'

class ChatTemplateView(TemplateView):
    template_name = 'core/chat.html'

class ProfileTemplateView(TemplateView):
    template_name = 'core/profile.html'

class SettingsTemplateView(TemplateView):
    template_name = 'core/settings.html'

