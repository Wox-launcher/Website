# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from plugins.views import PluginAPIViewSet

plugin_search = PluginAPIViewSet.as_view({"get":"search"})

urlpatterns =  patterns('',
    url(r'^search/(?P<search>[\w\W]+)/$', plugin_search, name='plugin-search'),
)