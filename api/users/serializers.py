# -*- coding: utf8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from plugins.serializers import PluginSerializer

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username")

class UserSerializer(serializers.ModelSerializer):
    plugins = PluginSerializer(source="created_plugins",many=True)
    is_owner = serializers.SerializerMethodField('checkif_owned_by_logined_user',help_text="check if current login user is this user")

    def checkif_owned_by_logined_user(self,user):
        request = self.context.get("request")
        if request and request.user.is_authenticated():
            return user == request.user
        return False

    class Meta:
        model = User
        fields = ("id","username","plugins","is_owner")
