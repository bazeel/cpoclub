from django.conf.urls import patterns, url, include
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from events import views
from events.models import Event


urlpatterns = patterns('',
    url(r'^ymap/$', TemplateView.as_view(template_name='events/ymap.html'), name='event_ymap'),
    url(r'^$', login_required(views.EventList.as_view()), name='event_list'),
    url(r'^(?P<pk>\d+)/$', 
        login_required(DetailView.as_view(model=Event, template_name='events/event_detail.html')), 
        name='event_detail'),
)