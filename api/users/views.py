# -*- coding: utf8 -*
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.viewsets import GenericViewSet

from users.serializers import UserSerializer


class UserAPIViewSet(GenericViewSet, RetrieveModelMixin):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = User
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserSerializer(user, context={"request": request})
        return Response(serializer.data)
