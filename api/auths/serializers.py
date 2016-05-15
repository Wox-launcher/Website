# -*- coding: utf8 -*-
from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User
from api.exceptions import APIError


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True, max_length=50)
    password = serializers.CharField(required = True, max_length=50)

class UserChangePasswordSerializer(serializers.Serializer):
    oldpwd = serializers.CharField(required = True, max_length=50)
    newpwd = serializers.CharField(required = True, max_length=50)

class UserRegisterSerializer(UserLoginSerializer):
    email = serializers.EmailField()

    def validate_username(self, attrs, source):
        username = attrs[source]
        if User.objects.filter(username = username).count() > 0:
            raise APIError(u"username already exist")
        return attrs

    def validate_email(self, attrs, source):
        email = attrs[source]
        if User.objects.filter(email = email).count() > 0:
            raise APIError(u"email already exist")
        return attrs
