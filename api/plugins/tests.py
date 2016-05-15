# -*- coding: utf8 -*-
import json
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
import os
import shutil
from api.setting import test
from plugins.models import Plugin


class PluginTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.u1 = {"username": "scott", "password": "scott"}
        User.objects.create_user(**self.u1)
        self.BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        self.plugin_file = os.path.join(self.BASE_DIR, "unittest", "plugin.wox")
        self.preview_file = os.path.join(self.BASE_DIR, "unittest", "preview.png")
        self.icon_file = os.path.join(self.BASE_DIR, "unittest", "preview.png")
        self.plugin_directory = os.path.join(test.MEDIA_ROOT, "plugin")

    def create_plugin(self, plugin=None, preview=None, icon=None):
        if not plugin:
            plugin = self.plugin_file
        if not preview:
            preview = self.preview_file
        if not icon:
            icon = self.icon_file

        if plugin:
            plugin = open(plugin, "rb")
        if preview:
            preview = open(preview, "rb")
        if icon:
            icon = open(icon, "rb")

        data = {
            "plugin_file": plugin,
            "preview": preview,
            "icon": icon
        }

        response = self.c.post(reverse("plugin-list"), data=data)

        if plugin:
            plugin.close()
        if preview:
            preview.close()
        if icon:
            icon.close()
        return response

    def update_plugin(self, id, plugin=None, preview=None, icon=None):
        if plugin:
            plugin = open(plugin, "rb")
        if preview:
            preview = open(preview, "rb")
        if icon:
            icon = open(icon, "rb")

        data = {}
        if plugin:
            data["plugin_file"] = plugin
        if preview:
            data["preview"] = preview,
        if icon:
            data["icon"] = icon

        response = self.c.patch(reverse("plugin-list") + "{}/".format(id), data=json.dumps(data), content_type="application/json",)

        if plugin:
            plugin.close()
        if preview:
            preview.close()
        if icon:
            icon.close()
        return response

    def empty_plugin_directory(self):
        if os.path.exists(self.plugin_directory):
            shutil.rmtree(self.plugin_directory, ignore_errors=True)

    def login(self):
        self.c.login(username=self.u1["username"], password=self.u1["password"])

    def get_test_file(self, name):
        return os.path.join(self.BASE_DIR, "unittest",name)

    def test_create_plugin(self):
        self.login()
        response = self.create_plugin()
        self.assertEqual(response.status_code, 201, response.data)

    def test_create_plugin_with_invalid_extension(self):
        self.login()
        response = self.create_plugin(self.get_test_file("plugin.invliadextension"))
        self.assertEqual(response.status_code, 400, response.data)

    def test_create_plugin_with_invalid_id(self):
        self.login()
        response = self.create_plugin(self.get_test_file("plugin_invalid_id.wox"))
        self.assertEqual(response.status_code, 400, response.data)

    def test_create_plugin_with_invalid_icon(self):
        self.login()
        response = self.create_plugin(icon=self.get_test_file("plugin.wox"))
        self.assertEqual(response.status_code, 400, response.data)

    def test_create_plugin_with_invalid_preview(self):
        self.login()
        response = self.create_plugin(preview=self.get_test_file("plugin.wox"))
        self.assertEqual(response.status_code, 400, response.data)

    def test_create_plugin_with_invalid_language(self):
        self.login()
        response = self.create_plugin(self.get_test_file("plugin_invalid_language.wox"))
        self.assertEqual(response.status_code, 400, response.data)

    def test_create_plugin_with_invalid_version(self):
        self.login()
        response = self.create_plugin(self.get_test_file("plugin_invalid_version.wox"))
        self.assertEqual(response.status_code, 400, response.data)

    def test_create_plugin_twice(self):
        self.login()
        response = self.create_plugin()
        self.assertEqual(response.status_code, 201, response.data)
        response = self.create_plugin()
        self.assertEqual(response.status_code, 400, response.data)

    def test_create_plugin_without_login(self):
        response = self.create_plugin()
        self.assertEqual(response.status_code, 401, response.data)

    def test_update_plugin(self):
        self.login()
        response = self.create_plugin()
        self.assertEqual(response.status_code, 201, response.data)

        # response = self.update_plugin(response.data["id"], plugin=self.get_test_file("plugin.wox"))
        # self.assertEqual(response.status_code, 200, response.data)

    def test_delete_plugin(self):
        self.empty_plugin_directory()
        self.login()
        response = self.create_plugin()
        plugin_dir = os.path.join(self.plugin_directory, response.data["plugin_id"])
        self.assertEqual(response.status_code, 201, response.data)
        self.assertTrue(os.path.exists(plugin_dir), response.data)

        response = self.c.delete(reverse("plugin-list") + "{}/".format(response.data["id"]))
        self.assertEqual(response.status_code, 204, response.data)
        self.assertFalse(os.path.exists(plugin_dir), response.data)
