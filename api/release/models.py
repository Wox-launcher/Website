# -*- coding: utf8 -*
from __future__ import unicode_literals

from django.utils.translation import ugettext  as _
from django.db import models


class Release(models.Model):
    version = models.CharField(max_length=20, unique=True, verbose_name=_("Version"),
                               help_text=_("A version should be a MAJOR.MINOR.PATCH format. E.g. 1.0.0"))
    download_link = models.URLField()
    download_link1 = models.URLField(blank=True, verbose_name=_("Backup download link 1"))
    download_link2 = models.URLField(blank=True, verbose_name=_("Backup download link 2"))
    description = models.CharField(max_length=1000, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_date"]

    def __unicode__(self):
        return self.version


class UpgradeRequest(models.Model):
    ip = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_date"]