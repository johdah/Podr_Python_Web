from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import  api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from api.serializers import EpisodeSerializer, PodcastSerializer, UserEpisodeSerializer, UserPodcastSerializer
from podr.models import Episode, Podcast, UserPodcast, UserEpisode


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class APIRootView(APIView):
    def get(self, request):
        data = {
            'episodes': reverse('episode-list', request=request, format=format),
            'podcasts': reverse('podcast-list', request=request, format=format),
            'userepisodes': reverse('user-episode-list', request=request, format=format),
            'userpodcasts': reverse('user-podcast-list', request=request, format=format)
        }
        return Response(data)


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


class UserEpisodeViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    serializer_class = UserEpisodeSerializer

    def get_queryset(self):
        userObj = self.request.user
        return UserEpisode.objects.filter(user=userObj)


class UserPodcastViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    serializer_class = UserPodcastSerializer

    def get_queryset(self):
        userObj = self.request.user
        return UserPodcast.objects.filter(user=userObj)