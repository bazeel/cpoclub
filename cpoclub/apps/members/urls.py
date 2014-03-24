from django.conf.urls import patterns, url, include
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from members import views


urlpatterns = patterns('',
    url(r'^$', login_required(views.MembersList.as_view()), name='user_list'),
    url(r'^(?P<pk>\d+)/$', 
        login_required(DetailView.as_view(model=User, template_name='members/user_detail.html')), 
        name='user_detail'),
    url(r'^(?P<pk>\d+)/rec/$', login_required(views.UserRecList.as_view()), name='user_rec_list'),
)