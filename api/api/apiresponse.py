# -*- coding: utf8 -*-
from rest_framework import status
from rest_framework.response import Response

'''Wox API Response Policy
For error response:
    {"message":"reason why this request failed","data":"addtional data passed to client"}
For success response:
    {"message":"success","data":"data passed to client"}
'''

def msg(message, data = None, status=status.HTTP_200_OK):
    if not data:
        data = {}
    return Response({"message": message, "data": data}, status=status)

def error(message):
    return msg(message, status = status.HTTP_400_BAD_REQUEST)

def success(data):
    return msg("success",data)

def not_authenticate():
    return msg("authentication required", status.HTTP_401_UNAUTHORIZED)

def no_permission():
    return msg("you have no permission to do this action", status.HTTP_403_FORBIDDEN)

def serializer_error(serializer_error):
    return error(format_serializer_error(serializer_error))

def format_serializer_error(serializer_error):
    """format a django rest framework serializer errors"""
    if serializer_error:
        for key,value in serializer_error.iteritems():
            return "{}: {}".format(key,value[0])
    return ""