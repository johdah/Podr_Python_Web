from django.conf.urls import patterns, url, include
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from api.views import EpisodeViewSet, PodcastViewSet, UserEpisodeViewSet, UserPodcastViewSet

episode_list = EpisodeViewSet.as_view({
    'get': 'list',
})
episode_detail = EpisodeViewSet.as_view({
    'get': 'retrieve',
})
podcast_list = PodcastViewSet.as_view({
    'get': 'list'
})
podcast_detail = PodcastViewSet.as_view({
    'get': 'retrieve'
})
user_episode_list = UserEpisodeViewSet.as_view({
    'get': 'list',
    })
user_episode_detail = UserEpisodeViewSet.as_view({
    'get': 'retrieve',
    })
user_podcast_list = UserPodcastViewSet.as_view({
    'get': 'list'
})
user_podcast_detail = UserPodcastViewSet.as_view({
    'get': 'retrieve'
})



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^$', 'api_root'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^episodes/$', episode_list, name="episode-list"),
    url(r'^episodes/(?P<pk>[0-9]+)/$', episode_detail, name="episode-detail"),
    url(r'^podcasts/$', podcast_list, name="podcast-list"),
    url(r'^podcasts/(?P<pk>[0-9]+)/$', podcast_detail, name="podcast-detail"),
    url(r'^userepisodes/$', user_episode_list, name="user-episode-list"),
    url(r'^userepisodes/(?P<pk>[0-9]+)/$', user_episode_detail, name="user-episode-detail"),
    url(r'^userpodcasts/$', user_podcast_list, name="user-podcast-list"),
    url(r'^userpodcasts/(?P<pk>[0-9]+)/$', user_podcast_detail, name="user-podcast-detail")
)

urlpatterns = format_suffix_patterns(urlpatterns)