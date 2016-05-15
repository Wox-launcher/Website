# -*- coding: utf8 -*-
from rest_framework import serializers
from api.exceptions import APIError
from woxerrors.models import Error
from django.utils.translation import ugettext  as _

class CreateErrorSerializer(serializers.ModelSerializer):
    step = serializers.CharField(max_length=2000,required=True)

    class Meta:
        model = Error
        fields = ("step",)
        read_only_fields = ("count",)

    def validate_step(self, attrs, source):
        step = attrs[source]
        if not step:
            raise APIError(_("step is requried"))
        return attrs