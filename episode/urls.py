from django.conf.urls import patterns, url
from episode import views

urlpatterns = patterns('',
   # ex: /episode/
   url(r'^$', views.index, name='index'),
   # ex: /subscription/5/
   url(r'^(?P<episode_id>\d+)/$', views.details, name='detail'),
)