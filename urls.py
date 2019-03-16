# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

urlpatterns = (
    url(r'^downloads/(?P<filter>(all|unstable))/$', views.show_downloads, name='show_downloads'),
    url(r'^downloads/$', views.show_downloads, name='show_downloads'),
)
