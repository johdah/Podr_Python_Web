import datetime
from django.utils import timezone
from django.db import models


class Subscription(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    copyright = models.CharField(max_length=100, null=True)
    description = models.TextField()
    language = models.CharField(max_length=100, null=True)
    last_updated = models.DateTimeField('Last updated')

    def __unicode__(self):
        return self.title


class Episode(models.Model):
    subscription = models.ForeignKey(Subscription)
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Date published')
    guid = models.CharField(max_length=255, unique=True)
    enclosureUrl = models.CharField(max_length=255, null=True)
    enclosureLength = models.IntegerField(default=-1)
    enclosureType = models.CharField(max_length=30, null=True)

    def __unicode__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)