# -*- coding: utf8 -*
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from api.decorators import serializer_validation
from api import apiresponse
from rest_framework.permissions import IsAuthenticated
from auths.serializers import UserLoginSerializer, UserRegisterSerializer, UserChangePasswordSerializer


class AuthAPIViewSet(GenericViewSet):
    permission_classes = ()
    model = User

    def get_serializer_class(self):
        action = self.action_map.get("post")
        if action == "login":
            return UserLoginSerializer
        elif action == "register":
            return UserRegisterSerializer

    @list_route(methods=["post"])
    @serializer_validation(UserLoginSerializer)
    def login(self, request):
        username = request.DATA.get("username")
        password = request.DATA.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth.login(request, user)
                return Response({"messsage": u"success", "data": {"id": user.pk,"name":user.username,"isSuperUser":user.is_superuser}})
            else:
                return apiresponse.error(u"user has been disabled")
        else:
            return apiresponse.error(u"login failed, username or password is not correct")

    @list_route()
    def islogined(self, request):
        if request.user.is_authenticated():
             return Response({"messsage": u"success", "data": {"id": request.user.pk,"name":request.user.username,"isSuperUser":request.user.is_superuser}})
        return Response({"messsage": u"failed"})

    @list_route(methods=["post"])
    def logout(self, request):
        auth.logout(request)
        return Response({"messsage": u"success"})

    @list_route(methods=["post"],permission_classes=[IsAuthenticated])
    @serializer_validation(UserChangePasswordSerializer)
    def changepwd(self, request):
        oldpwd = request.DATA.get("oldpwd")
        newpwd = request.DATA.get("newpwd")
        user = authenticate(username=request.user.username, password=oldpwd)
        if user:
            if user.is_active:
                user.set_password(newpwd)
                user.save()
                return Response({"messsage": u"success", "data": {"id": user.pk,"name":user.username,"isSuperUser":user.is_superuser}})
            else:
                return apiresponse.error(u"user has been disabled")
        else:
            return apiresponse.error(u"old password is not correct")

    @list_route(methods=["post"])
    @serializer_validation(UserRegisterSerializer)
    def register(self, request):
        username = request.DATA.get("username")
        password = request.DATA.get("password")
        email = request.DATA.get("email")
        if "inbound" in email:
            return apiresponse.error("register failed")
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            if user:
                return apiresponse.success({"userId": user.pk})
            else:
                return apiresponse.error("register failed")
