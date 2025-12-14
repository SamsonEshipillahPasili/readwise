from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class BrowseTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'core/browse.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'browse'
        return ctx


class ShelvesTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'core/shelves.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'shelves'
        return ctx

class WishlistTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'core/wishlist.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'wishlist'
        return ctx

class FriendsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'core/friends.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'friends'
        return ctx

class ChatTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'core/chat.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'chat'
        return ctx

class ProfileTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'core/profile.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'profile'
        return ctx

class SettingsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'core/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['menu'] = 'settings'
        return ctx

