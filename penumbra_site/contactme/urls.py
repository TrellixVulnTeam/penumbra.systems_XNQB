from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'contactme'

urlpatterns = [
    url(r'^$', views.contactme, name='contactme'),
]