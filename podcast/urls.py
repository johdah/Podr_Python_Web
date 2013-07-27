from django.conf.urls import patterns, url
from podcast import views

urlpatterns = patterns('',
    # ex: /podcast/
    url(r'^$', views.index, name='index'),
    # ex: /podcast/all/
    url(r'^all/$', views.all, name='all'),
    # ex: /podcast/category/5/
    url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
    # ex: /podcast/top/
    url(r'^top/$', views.top, name='top'),
    # ex: /podcast/5/
    url(r'^(?P<podcast_id>\d+)/$', views.details, name='details'),
    # ex: /podcast/5/follow
    url(r'^(?P<podcast_id>\d+)/follow/$', views.follow, name='follow'),
    # ex: /podcast/5/thumb_down
    url(r'^(?P<podcast_id>\d+)/thumb_down', views.thumb_down, name='thumb_down'),
    # ex: /podcast/5/thumb_up
    url(r'^(?P<podcast_id>\d+)/thumb_up', views.thumb_up, name='thumb_up'),
    # ex: /podcast/5/unfollow
    url(r'^(?P<podcast_id>\d+)/unfollow/$', views.unfollow, name='unfollow'),
    # ex: /podcast/5/update
    url(r'^(?P<podcast_id>\d+)/update/$', views.update, name='update'),
    # ex: /podcast/add/
    url(r'^add$', views.add, name='add'),
)