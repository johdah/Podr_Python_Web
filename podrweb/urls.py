from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'podrweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('podr.urls', namespace="podr")),
    url(r'^episode/', include('episode.urls', namespace="episode")),
    url(r'^subscription/', include('subscription.urls', namespace="subscription")),
    url(r'^admin/', include(admin.site.urls)),
)
