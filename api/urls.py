from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
import api
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
urlpatterns = format_suffix_patterns(patterns('api.views',
    url(r'^v1/$', api.views.APIRootView),
    url(r'^v1/episodes/$', episode_list, name="episode-list"),
    url(r'^v1/episodes/(?P<pk>[0-9]+)/$', episode_detail, name="episode-detail"),
    url(r'^v1/podcasts/$', podcast_list, name="podcast-list"),
    url(r'^v1/podcasts/(?P<pk>[0-9]+)/$', podcast_detail, name="podcast-detail"),
    url(r'^v1/userepisodes/$', user_episode_list, name="user-episode-list"),
    url(r'^v1/userepisodes/(?P<pk>[0-9]+)/$', user_episode_detail, name="user-episode-detail"),
    url(r'^v1/userpodcasts/$', user_podcast_list, name="user-podcast-list"),
    url(r'^v1/userpodcasts/(?P<pk>[0-9]+)/$', user_podcast_detail, name="user-podcast-detail")
))