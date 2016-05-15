# -*- coding: utf8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api import settings
from auths.views import AuthAPIViewSet
from dashboard.views import DashboardAPIViewSet
from woxerrors.views import ErrorAPIViewSet
from plugins.views import PluginAPIViewSet
from release.views import ReleaseAPIViewSet
from users.views import UserAPIViewSet

router = routers.SimpleRouter()
router.register(r'plugin', PluginAPIViewSet,base_name="plugin")
router.register(r'auth', AuthAPIViewSet,base_name="auth")
router.register(r'release', ReleaseAPIViewSet,base_name="release")
router.register(r'dashboard', DashboardAPIViewSet,base_name="dashboard")
router.register(r'user', UserAPIViewSet,base_name="user")
router.register(r'error', ErrorAPIViewSet,base_name="error")

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^plugin/',include('plugins.urls')),
    url(r'^release/',include('release.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^docs/', include('rest_framework_swagger.urls')),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
    )
