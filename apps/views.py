from django.shortcuts import render
from django.views.generic import TemplateView


class UserTemplateView(TemplateView):
    template_name = 'main.html'

