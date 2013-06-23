from datetime import datetime
from django.utils import timezone
from django.db import models


class Subscription(models.Model):
    title = models.CharField(max_length=100, default="Unknown")
    link = models.CharField(max_length=255)
    copyright = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    language = models.CharField(max_length=100, null=True)
    itunes_author = models.CharField(max_length=100, null=True)
    itunes_block = models.BooleanField(default=False)
    itunes_complete = models.BooleanField(default=False)
    itunes_explicit = models.BooleanField(default=False)
    itunes_image = models.CharField(max_length=255, null=True)
    itunes_owner_name = models.CharField(max_length=100, null=True)
    itunes_owner_email = models.CharField(max_length=100, null=True)
    itunes_subtitle = models.TextField(null=True)
    itunes_summary = models.TextField(null=True)
    last_updated = models.DateTimeField('Last updated', default=datetime.now())

    def __unicode__(self):
        return self.title


class Episode(models.Model):
    subscription = models.ForeignKey(Subscription)
    title = models.CharField(max_length=100)
    guid = models.CharField(max_length=255, unique=True)
    enclosureUrl = models.CharField(max_length=255, null=True)
    enclosureLength = models.IntegerField(default=-1)
    enclosureType = models.CharField(max_length=30, null=True)
    itunes_author = models.CharField(max_length=100, null=True)
    itunes_block = models.BooleanField(default=False)
    itunes_duration = models.IntegerField(default=-1)
    itunes_explicit = models.BooleanField(default=False)
    itunes_image = models.CharField(max_length=255, null=True)
    itunes_explicit = models.BooleanField(default=False)
    itunes_subtitle = models.TextField(null=True)
    itunes_summary = models.TextField(null=True)
    pub_date = models.DateTimeField('Date published')

    def __unicode__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
