import json
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status
from api import exceptions
from api import apiresponse
from api.exceptions import APIError, APINotAuthenticateError, APINoPermissionError


class APIExceptionMiddleware(object):
    def process_exception(self, request, exception):
        error = json.dumps({"message": exception.message})
        response = HttpResponse(error, content_type="application/json")
        response.data = error  # for Django Rest framework Response compatibility
        if type(exception) == APIError:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return response
        elif type(exception) == APINotAuthenticateError:
            response.content = json.dumps({"message": "login required"})
            response.status_code = status.HTTP_401_UNAUTHORIZED
            return response
        elif type(exception) == APINoPermissionError:
            response.content = json.dumps({"message": "permission denied"})
            response.status_code = status.HTTP_403_FORBIDDEN
            return response
        return None


class DisableCSRFMiddleware(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
