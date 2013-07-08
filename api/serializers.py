from rest_framework import serializers
from podr.models import Episode, Podcast


# TODO: Not working
class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ('title', 'podcasts', 'guid', 'enclosureUrl', 'enclosureType', 'enclosureLength')


class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Podcast
        fields = ('title', 'link', 'copyright', 'description', 'itunes_author', 'itunes_block', 'itunes_complete',
                  'itunes_explicit', 'itunes_image', 'itunes_owner_name', 'itunes_owner_email',
                  'itunes_subtitle', 'itunes_summary', 'last_updated')