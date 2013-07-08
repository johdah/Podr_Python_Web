from django.conf.urls import patterns, url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'episodes', views.EpisodeViewSet)
router.register(r'podcasts', views.PodcastViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
)