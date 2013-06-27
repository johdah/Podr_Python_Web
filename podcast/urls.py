from django.conf.urls import patterns, url
from podcast import views

urlpatterns = patterns('',
    # ex: /podcast/
    url(r'^$', views.index, name='index'),
    # ex: /podcast/add/
    url(r'^add$', views.add, name='add'),
    # ex: /podcast/5/
    url(r'^(?P<podcast_id>\d+)/$', views.details, name='detail'),
    # ex: /podcast/5/
    url(r'^(?P<podcast_id>\d+)/update/$', views.update, name='update'),
)