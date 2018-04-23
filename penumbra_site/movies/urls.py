from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'movies'

urlpatterns = [
    url(r'^$', views.movies, name='movies'),
]