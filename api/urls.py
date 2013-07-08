from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    #url(r'^$', views.api_root),
    url(r'^episodes/$', views.EpisodeList.as_view()),
    url(r'^episodes/(?P<pk>[0-9]+)/$', views.EpisodeDetails.as_view()),
    url(r'^podcasts/$', views.PodcastList.as_view()),
    url(r'^podcasts/(?P<pk>[0-9]+)/$', views.PodcastDetails.as_view()),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns = format_suffix_patterns(urlpatterns)