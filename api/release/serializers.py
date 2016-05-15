# -*- coding: utf8 -*-
import re

from rest_framework import serializers
from django.utils.translation import ugettext  as _
from api.exceptions import APIError

from release.models import Release


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release

    def validate_version(self, attrs, source):
        version = attrs[source]
        if not re.match("^(\d*)\.(\d*)\.(\d*)$", version):
            raise APIError(_("Invalid version."))
        return attrs