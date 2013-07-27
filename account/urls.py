from django.conf.urls import patterns, url
from account import views

urlpatterns = patterns('',
    # ex: /account/
    url(r'^$', views.index, name='index'),
    # ex: /account/callback/oauth2
    #url(r'^callback/oauth2', views.callback_oauth2, name='callback_oauth2'),
    # ex: /account/login
    url(r'^login', views.login_view, name='login'),
    # ex: /account/logout
    url(r'^logout', views.logout_view, name='logout'),
    # ex: /account/5/
    url(r'^(?P<user_id>\d+)/$', views.user_profile, name='user_profile'),
)