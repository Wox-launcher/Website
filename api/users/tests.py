# -*- coding: utf8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User


class IAPITest(TestCase):
    def setUp(self):
        self.c = Client()

    def login(self, username, password):
        data = {"username": username, "password": password}
        return self.c.post(reverse("auth-login"), data=data)

    def register(self, username, password, email):
        data = {"username": username, "password": password, "email": email}
        return self.c.post(reverse("auth-register"), data=data)

    def test_get_user_info(self):
        username = "scott3"
        password = "pass"
        email = "1@1.com"
        response = self.register(username, password, email)
        userId = response.data.get("data").get("userId")
        self.assertIsNotNone(userId, response.data)

        response = self.c.get("/user/{}/".format(userId))
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data.get("id"), userId, response.data)

