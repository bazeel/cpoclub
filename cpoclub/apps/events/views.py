from django.views.generic import ListView

from events.models import Event


class EventList(ListView):
    model = Event
    paginate_by = 8
    queryset = Event.objects.filter(active=True)
    template_name='events/event_list.html'