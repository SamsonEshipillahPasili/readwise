from django.shortcuts import render
from django.views.generic import TemplateView

class BrowseTemplateView(TemplateView):
    template_name = 'core/browse.html'

class ShelvesTemplateView(TemplateView):
    template_name = 'core/shelves.html'

class WishlistTemplateView(TemplateView):
    template_name = 'core/wishlist.html'
