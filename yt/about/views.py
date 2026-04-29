from django.shortcuts import render
from django.views.generic import TemplateView


class AboutAuthorView(TemplateView):
    """Статичная страница 'Об авторе'."""
    template_name = 'about/author.html'


class AboutTechView(TemplateView):
    """Статичная страница 'Технологии'."""
    template_name = 'about/tech.html'