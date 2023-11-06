from django.urls import path
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
