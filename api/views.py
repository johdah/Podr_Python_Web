from django.contrib.auth.models import User
from django.core.context_processors import request
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import viewsets, renderers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import link, api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from api.serializers import EpisodeSerializer, PodcastSerializer
from podr.models import Episode, Podcast


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


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
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


class PodcastViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


# TODO: User specific
#class UserPodcast_view(request, format=None):
    #return Response(content)