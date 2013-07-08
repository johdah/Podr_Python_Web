from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.serializers import EpisodeSerializer, PodcastSerializer
from podr.models import Episode, Podcast


class EpisodeList(ListAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


class EpisodeDetails(RetrieveAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


class PodcastList(ListAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


class PodcastDetails(RetrieveAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer