from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'links'

urlpatterns = [
    url(r'^$', views.links, name='links'),
]