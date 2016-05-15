# -*- coding: utf8 -*-
import json
import os
import sys
import uuid
import zipfile
import simplejson
from django.forms import widgets
import re
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.pagination import PaginationSerializer
from api import settings
from api.exceptions import APIError
from plugins.models import Plugin
import plugins.models
from django.utils.translation import ugettext  as _

class PluginValidator(object):

    def __init__(self,request):
        self.request = request

    def is_post(self):
        return self.request.method == "POST"

    def __is_image_extensions_valid(self, path):
        fileName, fileExtension = os.path.splitext(path)
        return fileExtension in settings.ALLOWED_IMAGE_EXTENSIONS

    def __validate_plugin_id(self, plugin_id):
        is_valid = re.match("^([0-9]|[A-Z]|[a-z]){32}$", plugin_id)
        if not is_valid:
            raise APIError(_("Invalid plugin id format."))
        if self.is_post():
            if Plugin.objects.filter(plugin_id=plugin_id).count() > 0:
                raise APIError(_("Plugin id already exist."))

    def __validate_version(self, version):
        if not version:
            raise APIError(
                _("Invalid plugin config. You must provide Version key in your plugin.json."))

        if not re.match("^(\d*)\.(\d*)\.(\d*)$", version):
            raise APIError(_("Invalid version format."))

    def __validate_icon(self, icon_path):
        if not icon_path:
            raise APIError(
                _("Invalid plugin config. You must provide IcoPath key in your plugin.json. "
                  'It should be a relateive path to your plugin directory, E.g. "IcoPath":"Image\\\\myicon.png"'))
        if not self.__is_image_extensions_valid(icon_path):
            raise APIError(_("Invalid plugin config. IcoPath extension is not allowed"))

    def __validate_execute_filename(self, executefilename):
        if not executefilename:
            raise APIError(
                _("Invalid plugin config. You must provide ExecuteFileName key in your plugin.json."))

    def __validate_name(self, name):
        if self.is_post():
            if Plugin.objects.filter(name=name).count() > 0:
                raise APIError(_("Plugin name already exist."))

    def __validate_language(self, language):
        if language.upper() not in [k.upper() for k, v in plugins.models.LANGUAGE_CHOICES]:
            raise APIError(_("Invalid plugin file. we didn't support {} language".format(language)))

    def validate_plugin(self,plugin_file,attrs):
        if not plugin_file.name.endswith(".wox"):
            raise APIError(_("Invalid plugin file. Wox plugin should ends with .wox"))

	try:
	    z = zipfile.ZipFile(plugin_file)
	except Exception,e:
            raise APIError(_("Invalid plugin file. {}".format(str(e))))

        if not "plugin.json" in z.namelist():
            raise APIError(_("Invalid plugin file. we didn't find plugin.json file in your plugin."))

        try:
            config = simplejson.loads(z.read("plugin.json"))
	except Exception,e:
            raise APIError(_("Invalid plugin file. {}".format(str(e))))

        self.__validate_execute_filename(config.get("ExecuteFileName"))

        self.__validate_version(config.get("Version"))
        attrs["version"] = config.get("Version")

        self.__validate_name(config.get("Name"))
        attrs["name"] = config.get("Name")

        self.__validate_icon(config.get("IcoPath"))

        self.__validate_plugin_id(config.get("ID"))
        attrs["plugin_id"] = config.get("ID")

        attrs["action_keyword"] = config.get("ActionKeyword")
        attrs["description"] = config.get("Description")

        self.__validate_language(config.get("Language"))
        attrs["language"] = config.get("Language").upper()

    def validate_preview(self,preview):
        if not self.__is_image_extensions_valid(preview.name):
            raise APIError(_("Invalid preview file. Preview image should be either a png or jpg"))

    def validate_icon(self,icon):
        if not self.__is_image_extensions_valid(icon.name):
            raise APIError(_("Invalid icon file. Preview image should be either a png or jpg"))

class CreatePluginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plugin
        fields = ("id","plugin_id","long_description", "private", "icon", "preview", "github", "plugin_file")
        read_only_fields = ("id","plugin_id")

    def validate_plugin_file(self, attrs, source):
        self.validator = PluginValidator(self.context["request"])
        plugin_file = attrs[source]
        self.validator.validate_plugin(plugin_file,attrs)
        return attrs

    def validate_preview(self, attrs, source):
        self.validator = PluginValidator(self.context["request"])
        if attrs.get(source,None):
            preview = attrs[source]
            self.validator.validate_preview(preview)
        return attrs

    def validate_icon(self, attrs, source):
        self.validator = PluginValidator(self.context["request"])
        icon = attrs[source]
        self.validator.validate_icon(icon)
        return attrs

class UpdatePluginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plugin
        fields = ("id","plugin_id","long_description", "private", "icon", "preview", "github", "plugin_file")
        read_only_fields = ("id","plugin_id")

    def validate_plugin_file(self, attrs, source):
        self.validator = PluginValidator(self.context["request"])
        if attrs.get(source,None):
            plugin_file = attrs[source]
            self.validator.validate_plugin(plugin_file,attrs)
        return attrs

    def validate_preview(self, attrs, source):
        self.validator = PluginValidator(self.context["request"])
        if attrs.get(source,None):
            preview = attrs[source]
            self.validator.validate_preview(preview)
        return attrs

    def validate_icon(self, attrs, source):
        self.validator = PluginValidator(self.context["request"])
        if attrs.get(source,None):
            icon = attrs[source]
            self.validator.validate_icon(icon)
        return attrs

class PluginSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField('get_created_by')
    liked_by_logined_user = serializers.SerializerMethodField('checkif_liked_by_logined_user')

    def get_created_by(self,plugin):
        return {"id":plugin.created_by.id,"username":plugin.created_by.username}

    def checkif_liked_by_logined_user(self,plugin):
        request = self.context.get("request")
        if request and request.user.is_authenticated():
            return plugin.liked_users.filter(pk = request.user.id).count() > 0
        return False

    class Meta:
        model = Plugin
        exclude = ("enabled","liked_users")

class PaginatedPluginSerializer(PaginationSerializer):

    class Meta:
        object_serializer_class = PluginSerializer
