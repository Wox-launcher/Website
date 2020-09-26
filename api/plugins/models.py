# -*- coding: utf8 -*
from __future__ import unicode_literals
import os
import uuid
from django.contrib.auth.models import User

from django.utils.translation import ugettext  as _
from django.db import models


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    name = ".".join(filename.split(".")[:-1])
    filename = "{}-{}.{}".format(name, uuid.uuid4(), ext)
    return 'plugin/{}/{}'.format(instance.plugin_id, filename)


LANGUAGE_CHOICES = (
    ("CSharp", "CSharp"),
    ("Python", "Python"),
    ("Executable", "Executable"),
    ("Other", "Other"),
)

class Plugin(models.Model):
    plugin_id = models.CharField(max_length=50, unique=True, verbose_name=_("Id"),
                                 help_text=_("Plugin Id should be a 32 bit string with only A-Z or 0-9."))
    name = models.CharField(max_length=200, unique=True, verbose_name=_('Name'))
    action_keyword = models.CharField(max_length=50, verbose_name=_("Default Action Keyword"))
    description = models.CharField(max_length=100, verbose_name=_("Description"))
    long_description = models.CharField(max_length=2000, blank=True, verbose_name=_("Long Description"))
    version = models.CharField(max_length=20, verbose_name=_("Version"),
                               help_text=_("A version should be a MAJOR.MINOR.PATCH format. E.g. 1.0.0"))
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, verbose_name=_("Plugin language"))
    website = models.URLField(verbose_name=_("Plugin Website"), blank=True, null=True)
    enabled = models.BooleanField(default=True, verbose_name=_("Enabled"))
    private = models.BooleanField(default=False, verbose_name=_("Private"),
                                  help_text=_("User can only access pluign via plugin id"))
    icon = models.ImageField(upload_to=get_file_path, verbose_name=_("Plugin Icon"), max_length=500,
                             help_text=_("Only support .jpg and .png image"))
    preview = models.ImageField(upload_to=get_file_path,max_length=500, null=True,blank=True, verbose_name=_("Preview"))
    github = models.URLField(verbose_name=_("github link"), blank=True, null=True)
    plugin_file = models.FileField(max_length=500,upload_to=get_file_path, verbose_name=_("Plugin file"))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Create datetime"))
    modified_date = models.DateTimeField(auto_now=True, verbose_name=_("Last modified datetime"))
    liked_users = models.ManyToManyField(User, verbose_name=_("Liked Users"), related_name="liked_plugins")
    liked_count = models.IntegerField(verbose_name=_("Liked count"),default=0)
    created_by = models.ForeignKey(User, verbose_name=_("user"), related_name="created_plugins")

    def __unicode__(self):
        return self.name