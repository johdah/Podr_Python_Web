from django.conf.urls import patterns, url
from subscription import views

urlpatterns = patterns('',
    # ex: /subscription/
    url(r'^$', views.index, name='index'),
    # ex: /subscription/add/
    url(r'^add$', views.add, name='add'),
    # ex: /subscription/5/
    url(r'^(?P<subscription_id>\d+)/$', views.details, name='detail'),
    # ex: /subscription/5/
    url(r'^(?P<subscription_id>\d+)/update/$', views.details, name='update'),
)