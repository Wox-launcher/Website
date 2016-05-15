# -*- coding: utf8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
import os
import shutil
import time
from api import settings
from plugins.models import Plugin
from release.models import Release, UpgradeRequest


class ReleaseTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.u1 = {"username": "scott", "password": "scott"}
        u = User.objects.create_user(**self.u1)
        u.is_superuser = True
        u.save()

    def login(self):
        self.c.login(username=self.u1["username"], password=self.u1["password"])

    def test_create_release(self):
        self.login()
        response = self.c.post(reverse("release-list"), data={
            "version": "1.0.0",
            "download_link": "http://www.baidu.com"
        })
        self.assertEqual(response.status_code, 201, response.data)

    def test_create_release_without_login(self):
        response = self.c.post(reverse("release-list"), data={
            "version": "1.0.0",
            "download_link": "http://www.baidu.com"
        })
        self.assertEqual(response.status_code, 403, response.data)

    def test_get_release(self):
        Release.objects.create(version=u"1.0.0", download_link=u"http://www.baidu.com")
        time.sleep(0.1)
        Release.objects.create(version=u"1.0.1", download_link=u"http://www.baidu.com")
        time.sleep(0.1)
        r2 = Release.objects.create(version=u"1.1.1", download_link=u"http://www.baidu.com")

        response = self.c.get(reverse("release-list"))
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(len(response.data), 3, response.data)
        self.assertEqual(str(response.data[0].get("version")), str(r2.version), response.data)

    def test_update_release(self):
        r = Release.objects.create(version=u"1.0.0", download_link=u"http://www.baidu.com")
        self.login()
        response = self.c.patch(reverse("release-list") + "{}/".format(r.id), content_type="application/json", data = '{\
            "version" : "1.1.0"\
        }')
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data.get("version"), "1.1.0", response.data)

    def test_get_latest_release(self):
        Release.objects.create(version=u"1.0.0", download_link=u"http://www.baidu.com")
        time.sleep(0.1)
        Release.objects.create(version=u"1.0.1", download_link=u"http://www.baidu.com")
        time.sleep(0.1)
        Release.objects.create(version=u"1.1.1", download_link=u"http://www.baidu.com")

        response = self.c.get(reverse("release-latest"))
        self.assertEqual(response.data.get("version"),"1.1.1",response.data)

    def test_log_release_request(self):
        Release.objects.create(version=u"1.0.0", download_link=u"http://www.baidu.com")
        self.c.get(reverse("release-latest"))

        self.assertEqual(UpgradeRequest.objects.count(),1)
        self.assertEqual(UpgradeRequest.objects.all()[0].ip,"127.0.0.1")
