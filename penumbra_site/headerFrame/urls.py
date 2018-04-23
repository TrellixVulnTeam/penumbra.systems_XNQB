from django.conf.urls import include, url
from django.contrib import admin

from . import views


app_name = 'headerFrame'

urlpatterns = [
    url(r'^$', views.headerFrame, name='headerFrame'),
]