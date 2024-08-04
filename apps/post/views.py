from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class CategoryView(TemplateView):
    template_name = 'pages/post_list.html'

class PostView(TemplateView):
    template_name = 'pages/post_detail.html'

