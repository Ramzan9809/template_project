from django.urls import path
from .views import *


urlpatterns = [
    path('post_list/', CategoryView.as_view(), name='list'),
    path('post_delail/', PostView.as_view(), name='detail')
]

