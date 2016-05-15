# -*- coding: utf8 -*
from __future__ import unicode_literals
import os
import uuid
from django.contrib.auth.models import User

from django.utils.translation import ugettext  as _
from django.db import models

class Error(models.Model):
    detail = models.CharField(max_length=3000,verbose_name=_("Error detail"))
    is_solved = models.BooleanField(default=False,verbose_name=_("Is s olved"))
    count = models.IntegerField(verbose_name=_("Count"),default=0)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Create datetime"))
    modified_date = models.DateTimeField(auto_now=True, verbose_name=_("Last modified datetime"))

    def __unicode__(self):
        return self.detail

class ErrorReproduceStep(models.Model):
    error = models.ForeignKey(Error,verbose_name=_("error"))
    step_detail = models.CharField(max_length=3000,verbose_name=_("step detail"))
