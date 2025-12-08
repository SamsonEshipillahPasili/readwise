from django.shortcuts import render
from django.views.generic import TemplateView

class BrowseTemplateView(TemplateView):
    template_name = 'core/browse.html'
