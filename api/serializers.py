from rest_framework import serializers
from podr.models import Episode, Podcast


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ('title', 'podcast', 'guid', 'enclosureUrl', 'enclosureType', 'enclosureLength')


class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Podcast
        fields = ('title', 'link', 'copyright', 'description', 'last_updated')