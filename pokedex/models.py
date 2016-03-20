from __future__ import unicode_literals

from django.db import models

class Type(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    name = models.CharField(max_length=255, blank=False)

    def __unicode__(self):
        return self.name


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    english_full_name = models.CharField(max_length=255, blank=False)
    japanese_full_name = models.CharField(max_length=255, blank=True)
    primary_type = models.ForeignKey(Type, blank=False, related_name='primary_type')
    secondary_type = models.ForeignKey(Type, blank=True, null=True, related_name='secondary_type')

    def __unicode__(self):
        return self.english_full_name
