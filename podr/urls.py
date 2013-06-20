from django.conf.urls import patterns, url

from podr import views

urlpatterns = patterns('',
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /subscription/
    url(r'^subscription/$', views.subscription, name='index'),
    # ex: /subscription/5/
    url(r'^subscription/(?P<subscription_id>\d+)/$', views.subscription_details, name='detail'),
    # ex: /subscription/5/add/
    url(r'^subscription/(?P<subscription_id>\d+)/add/$', views.subscription_add, name='add'),
)