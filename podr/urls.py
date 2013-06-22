from django.conf.urls import patterns, url
from podr import templates

urlpatterns = patterns('',
    # ex: /
    url(r'^$', templates.index, name='index'),
)