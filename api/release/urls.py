# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from release.views import ReleaseAPIViewSet

release_version = ReleaseAPIViewSet.as_view({"get":"version"})

urlpatterns =  patterns('',
    url(r'^(?P<version>[0-9]+\.[0-9]+\.[0-9]+)/$', release_version, name='release-version'),
)