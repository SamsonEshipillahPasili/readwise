from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

class BrowseTemplateView(TemplateView):
    template_name = 'core/browse.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'browse'
        return ctx


class ShelvesTemplateView(TemplateView):
    template_name = 'core/shelves.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'shelves'
        return ctx

class WishlistTemplateView(TemplateView):
    template_name = 'core/wishlist.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'wishlist'
        return ctx

class FriendsTemplateView(TemplateView):
    template_name = 'core/friends.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'friends'
        return ctx

class ChatTemplateView(TemplateView):
    template_name = 'core/chat.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'chat'
        return ctx

class ProfileTemplateView(TemplateView):
    template_name = 'core/profile.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'profile'
        return ctx

class SettingsTemplateView(TemplateView):
    template_name = 'core/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'settings'
        return ctx

