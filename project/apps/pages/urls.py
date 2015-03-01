from django.conf.urls import patterns, url

from .views import *


urlpatterns = patterns('',
               url(regex=r'^$', view=HomePageView.as_view(), name='home'),
               url(regex=r'^about/$', view=AboutPageView.as_view(), name='about'),
            )