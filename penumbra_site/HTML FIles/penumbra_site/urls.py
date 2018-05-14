"""penumbra_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import auth
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog.views import blog
from pictures.views import pictures
from movies.views import movies
from links.views import links
from contactme.views import contactme
from headerFrame.views import headerFrame
from demoscene.views import demoscene

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin', admin.site.urls),
	url(r'^$', include('headerFrame.urls', namespace="headerFrame")),
	url(r'^blog/', include('blog.urls', namespace="blog")),
	url(r'^pictures/', include('pictures.urls', namespace="pictures")),
	url(r'^movies/', include('movies.urls', namespace="movies")),
	url(r'^links/', include('links.urls', namespace="links")),
	url(r'^contactme', include('contactme.urls', namespace="contactme")),
	url(r'^menu/', include('headerFrame.urls', namespace="headerFrame")),
	url(r'^demoscene/', include('demoscene.urls', namespace="demoscene")),
	url(r'^menu/blog/', include('blog.urls', namespace="blog")),
	url(r'^menu/pictures/', include('pictures.urls', namespace="pictures")),
	url(r'^menu/movies/', include('movies.urls', namespace="movies")),
	url(r'^menu/links/',  include('links.urls', namespace="links")),
	url(r'^menu/contactme/', include('contactme.urls', namespace="contactme")),

]
urlpatterns += staticfiles_urlpatterns()

"""urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', blog),
	url(r'^blog/$', blog, name='blog'),
	url(r'^pics/$', pictures, name='pictures'),
	url(r'^movies/$', movies, name='movies'),
	url(r'^links/$', links, name='links'),
	url(r'^contactme/$', contactme, name='contactme'),
	url(r'^radius/$', radius, name='radius'),
	url(r'^menu/$', headerFrame, name='headerFrame'),
	url(r'^demoscene/$', demoscene, name='demoscene'),
]"""
