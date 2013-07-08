from django.conf.urls import patterns, url, include
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from api.views import EpisodeViewSet, PodcastViewSet

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



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^$', views.api_root),
    url(r'^episodes/$', episode_list, name="episode-list"),
    url(r'^episodes/(?P<pk>[0-9]+)/$', episode_detail, name="episode-detail"),
    url(r'^podcasts/$', podcast_list, name="podcast-list"),
    url(r'^podcasts/(?P<pk>[0-9]+)/$', podcast_detail, name="podcast-detail"),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns = format_suffix_patterns(urlpatterns)