from django.conf.urls import patterns, url
from pirate_site import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^help/$', views.help, name='help'),
    url(r'^(?P<category>\w+)/$', views.category, name='category'),
    url(r'^(?P<category>\w+)/(?P<id>\d+)/$', views.detail, name='detail'),
)
