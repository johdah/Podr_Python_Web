from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class Podcast(models.Model):
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

    @property
    def sorted_episode_set(self):
        return self.episode_set.order_by('-pub_date')


class UserPodcast(models.Model):
    user = models.ForeignKey(User)
    podcast = models.ForeignKey(Podcast)
    following = models.BooleanField(default=False)
    last_updated = models.DateTimeField('Last Updated', default=datetime.now())


class Episode(models.Model):
    podcast = models.ForeignKey(Podcast)
    title = models.CharField(max_length=100)
    guid = models.CharField(max_length=255, unique=True)
    enclosureUrl = models.CharField(max_length=255, null=True)
    enclosureLength = models.IntegerField(default=-1)
    enclosureType = models.CharField(max_length=30, null=True)
    itunes_author = models.CharField(max_length=100, null=True)
    itunes_block = models.BooleanField(default=False)
    itunes_duration = models.IntegerField(default=-1)
    itunes_itunesIsClosedCaption = models.BooleanField(default=False)
    itunes_image = models.CharField(max_length=255, null=True)
    itunes_explicit = models.BooleanField(default=False)
    itunes_subtitle = models.TextField(null=True)
    itunes_summary = models.TextField(null=True)
    pub_date = models.DateTimeField('Date published')

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=7)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def itunes_duration_as_string(self):
        return str(timedelta(seconds=self.itunes_duration))


class UserEpisode(models.Model):
    PLAYING_UNPLAYED, PLAYING_PARTIALLY, PLAYING_FINISHED = range(0, 3)
    PlayingStatus = (
        (PLAYING_UNPLAYED, 'Unplayed'),
        (PLAYING_PARTIALLY, 'Partially played'),
        (PLAYING_FINISHED, 'Finished'),
    )

    user = models.ForeignKey(User)
    episode = models.ForeignKey(Episode)
    archived = models.BooleanField(default=False)
    playing_status = models.IntegerField(choices=PlayingStatus, default=PLAYING_UNPLAYED)
    playing_current_time = models.IntegerField(default=0)
    last_updated = models.DateTimeField('Last Updated', default=datetime.now())
