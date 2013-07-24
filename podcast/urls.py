from django.conf.urls import patterns, url
from podcast import views

urlpatterns = patterns('',
    # ex: /podcast/
    url(r'^$', views.index, name='index'),
    # ex: /podcast/all/
    url(r'^all/$', views.all, name='all'),
    # ex: /podcast/5/
    url(r'^(?P<podcast_id>\d+)/$', views.details, name='details'),
    # ex: /podcast/5/follow
    url(r'^(?P<podcast_id>\d+)/follow/$', views.follow, name='follow'),
    # ex: /podcast/5/unfollow
    url(r'^(?P<podcast_id>\d+)/unfollow/$', views.unfollow, name='unfollow'),
    # ex: /podcast/5/update
    url(r'^(?P<podcast_id>\d+)/update/$', views.update, name='update'),
    # ex: /podcast/add/
    url(r'^add$', views.add, name='add'),
)