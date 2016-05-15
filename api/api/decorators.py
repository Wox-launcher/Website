# -*- coding: utf8 -*-
from api import apiresponse

def serializer_validation(serializer_class = None):
    """validate POST data using giving serializer class"""
    def wrapper(func):
        def decorated(instance,request, *args, **kwargs):
            serializer = serializer_class(data = request.DATA)
            if serializer.is_valid():
                return func(instance,request,*args,**kwargs)
            return apiresponse.serializer_error(serializer.errors)
        return decorated
    return wrapper