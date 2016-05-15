# -*- coding: utf8 -*-
from rest_framework import viewsets
from rest_framework.decorators import list_route
from api.permissions import IsSuperUserOrReadOnly
from rest_framework.response import Response
from release.models import Release, UpgradeRequest
from release.serializers import ReleaseSerializer


class ReleaseAPIViewSet(viewsets.ModelViewSet):
    model = Release
    serializer_class = ReleaseSerializer
    # trun off pagination
    paginate_by = None
    permission_classes = (IsSuperUserOrReadOnly,)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_latest_release(self):
        if Release.objects.count() > 0:
            latest_release = Release.objects.order_by("-created_date")[:1].get()
            serializer = ReleaseSerializer(latest_release)
            return serializer.data
        else:
            return {}

    @list_route()
    def newest(self, request):
        return Response(self.get_latest_release())

    @list_route()
    def latest(self, request):
        UpgradeRequest.objects.create(ip=self.get_client_ip(request))
        return Response(self.get_latest_release())

    #/release/x.x.x/
    def version(self, request, version):
        release = Release.objects.filter(version=version).first()
        serializer = self.get_serializer(release)
        return Response(serializer.data)