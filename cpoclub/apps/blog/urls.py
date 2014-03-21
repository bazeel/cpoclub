from django.conf.urls import patterns, url, include
from django.views.generic import ListView
from .models import Record
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.CustomRecordList.as_view(), name='record_list'),
    url(r'^(?P<pk>\d+)/$', views.record_detail, name='record_detail'),
)