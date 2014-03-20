from django.conf.urls import patterns, url, include
from django.views.generic import ListView
from .models import Record

from blog import views

urlpatterns = patterns('',
    url(r'^$', 
        ListView.as_view(
            model=Record, 
            paginate_by=10,
            queryset=Record.objects.filter(active=True)
        ),
        name='record_list'),
    #url(r'^$', views.blog_list, name='blog_list'),
    url(r'^(?P<pk>\d+)/$', views.record_detail, name='record_detail'),
)