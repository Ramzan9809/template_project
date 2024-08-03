from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutUs
# Create your views here.

class HomeView(TemplateView):
    template_name = 'pages/index.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = AboutUs.objects.first()
        return context
