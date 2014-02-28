from django.conf.urls import patterns, url, include

from account import views


urlpatterns = patterns('',
    url(r'^login/$', views.login_view, name='account_login'),
    url(r'^logout/$', views.logout_view, name='account_logout'),
    url(r'^register/$', views.register, name='account_register'),
)