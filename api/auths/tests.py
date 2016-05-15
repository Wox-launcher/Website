# -*- coding: utf8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User


class AuthAPITest(TestCase):
    def setUp(self):
        self.c = Client()

    def login(self, username, password):
        data = {"username": username, "password": password}
        return self.c.post(reverse("auth-login"), data=data)

    def register(self, username, password, email):
        data = {"username": username, "password": password, "email": email}
        return self.c.post(reverse("auth-register"), data=data)

    def test_login(self):
        username = "scott"
        password = "scott"
        User.objects.create_user(username=username, password=password)
        response = self.login(username, password)
        self.assertEqual(response.status_code, 200, response.data)

    def test_register(self):
        username = "scott1"
        password = "pass"
        email = "1@1.com"
        response = self.register(username, password, email)
        self.assertEqual(response.status_code, 200, response.data)

    def test_register_duplicate(self):
        username = "scott2"
        password = "pass"
        email = "email@1.com"
        response = self.register(username, password, email)
        self.assertEqual(response.status_code, 200, response.data)

        response = self.register(username, password, email)
        self.assertEqual(response.status_code, 400, response.data)