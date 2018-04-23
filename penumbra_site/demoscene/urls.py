from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'demoscene'

urlpatterns = [
    url(r'^$', views.demoscene, name='demoscene'),
]