from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'MagicFighter'

urlpatterns = [
    url(r'^$', views.MagicFighter, name='MagicFighter'),
]