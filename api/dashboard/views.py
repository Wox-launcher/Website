# -*- coding: utf8 -*-
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Count

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from api.permissions import IsSuperUser
from plugins.models import Plugin

from release.models import Release, UpgradeRequest
from release.serializers import ReleaseSerializer


class DashboardAPIViewSet(viewsets.GenericViewSet):
    model = UpgradeRequest
    permission_classes = (IsSuperUser,)

    def upgrade_request_day(self, f, to):
        return UpgradeRequest.objects.filter(created_date__lt=to, created_date__gt=f) \
            .extra({'hour': "extract(hour from created_date)"}) \
            .values("hour").annotate(count=Count("id")) \
            .order_by('hour')

    def upgrade_request_month(self, f, to):
        return UpgradeRequest.objects.filter(created_date__lt=to, created_date__gt=f) \
            .extra({'day': "extract(day from created_date)"}) \
            .values("day").annotate(count=Count("id")) \
            .order_by('day')

    @list_route()
    def summary(self,request):
        plugin_count = Plugin.objects.all().count()
        user_count = User.objects.all().count()
        return Response({
            "plugin_count":plugin_count,
            "user_count":user_count
        })

    @list_route()
    def upgrade_request_today(self, request):
        to = datetime.now()
        f = datetime(to.year, to.month, to.day)
        return Response(self.upgrade_request_day(f,to))

    @list_route()
    def upgrade_request_current_month(self, request):
        to = datetime.now()
        f = datetime(to.year, to.month, 1)
        return Response(self.upgrade_request_month(f,to))