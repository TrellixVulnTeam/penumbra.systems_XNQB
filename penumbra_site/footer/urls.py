from django.conf.urls import include, url
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'footer'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]