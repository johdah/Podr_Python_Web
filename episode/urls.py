from django.conf.urls import patterns, url
from episode import views

urlpatterns = patterns('',
   # ex: /episode/
   url(r'^$', views.index, name='index'),
   # ex: /episode/starred
   url(r'^starred/$', views.starred, name='starred'),
   # ex: /episode/5/
   url(r'^(?P<episode_id>\d+)/$', views.details, name='details'),
   # ex: /episode/5/archive
   url(r'^(?P<episode_id>\d+)/archive$', views.archive, name='archive'),
   # ex: /episode/5/star
   url(r'^(?P<episode_id>\d+)/star', views.star, name='star'),
   # ex: /episode/5/unarchive
   url(r'^(?P<episode_id>\d+)/unarchive$', views.unarchive, name='unarchive'),
   # ex: /episode/5/unstar
   url(r'^(?P<episode_id>\d+)/unstar', views.unstar, name='unstar'),
)