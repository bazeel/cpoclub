from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from library import views


urlpatterns = patterns('',
    url(r'^$', login_required(views.DocList.as_view()), name='doc_list'),
)