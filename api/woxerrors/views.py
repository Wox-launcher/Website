# -*- coding: utf8 -*
import os
import shutil
from os import listdir
from os.path import isfile, join

from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from api import apiresponse
from api.exceptions import APINoPermissionError
from api.permissions import IsAuthenticatedOrReadOnly, IsSuperUserOrWriteOnly
from woxerrors.models import Error
from api import settings
from plugins.models import Plugin
from plugins.serializers import PluginSerializer, CreatePluginSerializer, UpdatePluginSerializer, \
    PaginatedPluginSerializer
from rest_framework import status

class ErrorAPIViewSet(viewsets.ModelViewSet):
    model = Error
    permission_classes = (IsSuperUserOrWriteOnly,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.DATA, files=request.FILES)

        if serializer.is_valid():
            error = Error.objects.filter(detail = serializer.object.detail).first()
            if error:
                error.count = error.count + 1
                error.save()
                return Response("ok", status=status.HTTP_201_CREATED)
            else:
                #create new error
                self.pre_save(serializer.object)
                self.object = serializer.save(force_insert=True)
                self.post_save(self.object, created=True)
                return Response("ok", status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)