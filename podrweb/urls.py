from django.conf.urls import patterns, include, url

from django.contrib import admin
import podr

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('podr.urls', namespace="podr")),
    # ex: /about/
    url(r'^about/$', podr.views.about_changelog, name='about'),
    # ex: /about/changelog/
    url(r'^about/changelog/$', podr.views.about_changelog, name='about_changelog'),
    # Other
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^account/', include('account.urls', namespace="account")),
    url(r'^episode/', include('episode.urls', namespace="episode")),
    url(r'^podcast/', include('podcast.urls', namespace="podcast")),
    url(r'^admin/', include(admin.site.urls)),
)
