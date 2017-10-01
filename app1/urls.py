from django.conf.urls import url
from django.contrib import admin
from . import views
from .models import blogpost
from django.views.generic import ListView,DetailView
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = blogpost, template_name = 'detail.html')),
    url(r'^home', views.home),
]
