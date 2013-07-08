from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from api.serializers import EpisodeSerializer, PodcastSerializer
from podr.models import Episode, Podcast


#@api_view(('GET',))
#def api_root(request, format=None):
    #return Response({
        #'episodes': reverse('episode-list', request=request, format=format),
        #'podcasts': reverse('podcast-list', request=request, format=format)
    #})


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