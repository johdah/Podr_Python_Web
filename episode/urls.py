from django.conf.urls import patterns, url
from episode import views

urlpatterns = patterns('',
   # ex: /
   url(r'^$', views.index, name='index'),
)