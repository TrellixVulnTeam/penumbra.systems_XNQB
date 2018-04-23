from django.conf.urls import url

from . import views

app_name = 'reactTest'

urlpatterns = [
    url(r'^$', views.reactTest, name='reactTest'),
]