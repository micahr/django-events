from django.conf.urls.defaults import *

from events.views import *
from events.models import Event, EventTime

urlpatterns = patterns('',
    url(r'^(?P<event_id>\d+)-(?P<event_slug>[\w\-]+)/$', event_detail,
        name="event"),
    url(r'^time/(?P<event_time_id>\d+)-(?P<event_slug>[\w\-]+)/$',
        event_time_detail, name="event_time"),
    url(r'^time/(?P<event_time_id>\d+)-(?P<event_slug>[\w\-]+)/register/$', 
        register_for_event, 
        name='event_time_register'),
)
