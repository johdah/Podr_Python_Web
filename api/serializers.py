from rest_framework import serializers
from podr.models import Episode, Podcast, UserPodcast, UserEpisode, Category, PodcastCategories


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'level', 'parent')


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    podcast = serializers.Field(source='podcast.id')

    class Meta:
        model = Episode
        fields = ('id', 'title', 'podcast', 'guid', 'enclosureUrl', 'enclosureType', 'enclosureLength', 'itunes_author',
                  'itunes_block', 'itunes_duration', 'itunes_itunesIsClosedCaption', 'itunes_image', 'itunes_explicit',
                  'itunes_subtitle', 'itunes_summary', 'pub_date')


class PodcastCategoriesSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.Field(source='category.id')
    podcast = serializers.Field(source='podcast.id')

    class Meta:
        model = PodcastCategories
        fields = ('id', 'category', 'podcast')


class UserEpisodeSerializer(serializers.HyperlinkedModelSerializer):
    episode = serializers.Field(source='episode.id')

    class Meta:
        model = UserEpisode
        fields = ('episode', 'archived', 'starred', 'rating', 'playing_status', 'playing_current_time', 'last_updated')


class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Podcast
        fields = ('id', 'title', 'link', 'copyright', 'description', 'itunes_author', 'itunes_block', 'itunes_complete',
                  'itunes_explicit', 'itunes_image', 'itunes_owner_name', 'itunes_owner_email',
                  'itunes_subtitle', 'itunes_summary', 'last_updated')


class UserPodcastSerializer(serializers.HyperlinkedModelSerializer):
    podcast = serializers.Field(source='podcast.id')

    class Meta:
        model = UserPodcast
        fields = ('podcast', 'following', 'rating', 'last_updated')