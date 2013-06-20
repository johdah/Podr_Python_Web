from django.conf.urls import patterns, url
from subscription import views

urlpatterns = patterns('',
    # ex: /subscription/
    url(r'^$', views.index, name='index'),
    # ex: /subscription/5/add/
    url(r'^(?P<subscription_id>\d+)/add/$', views.add, name='add'),
    # ex: /subscription/5/
    url(r'^(?P<subscription_id>\d+)/$', views.details, name='detail'),
)