# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission
from api.exceptions import APIError, APINotAuthenticateError


class IsAdminOrSelf(BasePermission):
    """
    Allow access to admin users or the user himself.
    """
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        elif (request.user and type(obj) == type(request.user) and
              obj == request.user):
            return True
        return False

class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
        if (request.method in SAFE_METHODS or (request.user and request.user.is_authenticated())):
            return True
        raise APINotAuthenticateError()

class IsSuperUserOrWriteOnly(BasePermission):
    """
    The request is authenticated as a user, or is a write-only request.
    """

    def has_permission(self, request, view):
        SAFE_METHODS = ['POST', 'HEAD', 'OPTIONS']
        if (request.method in SAFE_METHODS or (request.user and request.user.is_superuser)):
            return True
        return False

class IsSuperUserOrReadOnly(BasePermission):
    """
    The request is authenticated as admin, or is a read-only request.
    """

    def has_permission(self, request, view):
        SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
        if (request.method in SAFE_METHODS or (request.user and request.user.is_superuser)):
            return True
        return False

class IsSuperUser(BasePermission):
    """
    Allows access only to super users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
