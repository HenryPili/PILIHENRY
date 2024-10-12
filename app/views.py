from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class BasePageView(TemplateView):
    template_name = 'app/base.html'

class ProjectsPageView(TemplateView):
    template_name = 'app/Projects.html'