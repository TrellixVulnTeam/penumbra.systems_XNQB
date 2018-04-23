from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'pictures'

urlpatterns = [
    url(r'^$', views.pictures, name='pictures'),
]