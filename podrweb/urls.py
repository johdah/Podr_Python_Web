from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('podr.urls', namespace="podr")),
    url(r'^account/', include('account.urls', namespace="account")),
    url(r'^episode/', include('episode.urls', namespace="episode")),
    url(r'^podcast/', include('podcast.urls', namespace="podcast")),
    url(r'^admin/', include(admin.site.urls)),
)