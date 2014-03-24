from django.conf.urls import patterns, url, include
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from members import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.MembersList.as_view()), name='member_list'),
    #url(r'^(?P<pk>\d+)/$', views.record_detail, name='profile'),
)