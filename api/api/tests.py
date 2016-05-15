# -*- coding: utf8 -*-
from django.test import TestCase, Client
from django.contrib.auth.models import User
from api import apiresponse

class ErrorTest(TestCase):
    def test_error_format(self):
        error = {
            "username": [
                "error msg"
            ],
            "password":[
                "error1 msg",
                "error2 msg"
            ]
        }

        err = apiresponse.format_serializer_error(error)
        self.assertEqual(err, "username: error msg", err)

