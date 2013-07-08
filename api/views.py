from rest_framework import viewsets, renderers
from rest_framework.decorators import link, api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from api.serializers import EpisodeSerializer, PodcastSerializer
from podr.models import Episode, Podcast


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'episodes': reverse('episode-list', request=request, format=format),
        'podcasts': reverse('podcast-list', request=request, format=format)
    })


class EpisodeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'details'
    """
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


class PodcastViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer