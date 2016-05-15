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
from api.permissions import IsAuthenticatedOrReadOnly
from api import settings
from plugins.models import Plugin
from plugins.serializers import PluginSerializer, CreatePluginSerializer, UpdatePluginSerializer, \
    PaginatedPluginSerializer


class PluginAPIViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Plugin.objects.filter(private=False, enabled=True).order_by('-liked_count')

    def get_serializer_class(self):
        SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
        if self.request.method in SAFE_METHODS:
            return PluginSerializer
        if self.request.method == "PATCH":
            return UpdatePluginSerializer
        else:
            return CreatePluginSerializer

    def is_plugin_owner(self,plugin):
        return self.request.user == plugin.created_by

    def pre_delete(self,obj):
        if not self.is_plugin_owner(obj):
            raise APINoPermissionError()

    def post_delete(self, obj):
        plugin_id = obj.plugin_id
        # delete plugin directory
        plugin_directory = os.path.join(settings.MEDIA_ROOT, "plugin/{}".format(plugin_id))
        if os.path.exists(plugin_directory):
            shutil.rmtree(plugin_directory, ignore_errors=True)

    def post_save(self, obj, created=False):
        if not created:
            #clean plugin directory
            plugin_id = obj.plugin_id
            plugin_directory = os.path.join(settings.MEDIA_ROOT, "plugin/{}".format(plugin_id))
            files = [ f for f in listdir(plugin_directory)]
            existing_files = [os.path.basename(obj.icon.name),os.path.basename(obj.plugin_file.name)]
            if obj.preview:
                existing_files.append(os.path.basename(obj.preview.name))
            need_delete = set(files) - set(existing_files)
            for f in need_delete:
                try:
                    os.remove(os.path.join(plugin_directory,f))
                except:
                    pass

    def pre_save(self, obj):
        obj.created_by = self.request.user

    @detail_route(methods=["post"])
    def like(self, request, pk=None):
        try:
            p = Plugin.objects.get(id=pk)
            if request.user.liked_plugins.filter(id=p.id).count() == 0:
                p.liked_users.add(request.user)
            else:
                p.liked_users.remove(request.user)
            p.liked_count = p.liked_users.count()
            p.save()

            return apiresponse.success({"latest_like_count": p.liked_count})
        except Plugin.DoesNotExist:
            return apiresponse.error("plugin doesn't exist")

    @list_route()
    def count(self, request):
        all_plugins = Plugin.objects.all().count()
        return apiresponse.success({"count": all_plugins})

    #/plugin/search/xxx/
    def search(self, request, search):
        plugins = self.queryset.filter(name__icontains=search)
        serializer = self.get_serializer(plugins, many=True)
        return Response(serializer.data)
