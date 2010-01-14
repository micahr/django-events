from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.views.generic import list_detail

from events.models import *
    
def event_detail(request, event_id, event_slug, template_name = 'event.html'):
    event = get_object_or_404(Event, id=event_id, slug=event_slug)
    name = request.session.get('name', None)
    return render_to_response(
        template_name,
        locals(),
        context_instance = RequestContext(request)
    )
    
def event_time_detail(request, event_time_id, event_slug,
                        template_name = 'event_time.html'):
    event_time = get_object_or_404(EventTime,
        id = event_time_id,
        event__slug = event_slug)
    attending = False
    past = False
    if event_time.end < datetime.datetime.now():
        past = True
    if request.user.is_authenticated() \
        and event_time in [x.event_time for x in request.user.attendee_set.all()] \
        or event_time in request.session.get('event_times',[]):
        attending = True
    if request.user.is_authenticated():
        request.session['name'] = ''
    return list_detail.object_detail(
            request,
            queryset = EventTime.objects.filter(id=event_time_id,
                event__slug = event_slug),
            template_name = template_name,
            object_id = event_time_id,
            extra_context = {'attending':attending, 
                             'name':request.session.get('name', None),
                             'past':past},
            template_object_name = 'event_time',
        )
    
@require_http_methods(['POST',])
def register_for_event(request, event_time_id, event_slug,
                        template_name = 'json/register.json'):
    ''' Register for Event '''
    message_type, message_body = 'ERROR', ''
    event_time = get_object_or_404(EventTime, id = event_time_id, event__slug = event_slug)
    attendee = Attendee(event_time=event_time)
    full_name = ''
    if request.user.is_authenticated():
        try:
            if request.user.id == int(request.POST.get('user_id', None)):
                attendee.user = User.objects.get(id=request.POST.get('user_id',None))
                full_name = attendee.user.get_full_name()
            else:
                User.DoesNotExist
        except User.DoesNotExist:
            attendee.user = None
    else:
        attendee.name = request.POST.get('name',None)
        request.session['name'] = attendee.name
        try:
            request.session['event_times'].append(event_time)
        except KeyError:
            request.session['event_times'] = [event_time] 
        full_name = attendee.name.title()
    try:
        attendee.save()
    except IntegrityError:
        message_body = 'You can only register once!'
    message_type = 'SUCCESS'
    message_body = 'You have been registered for %s' % event_time.event
    return render_to_response(
            template_name,
            locals(),
            context_instance = RequestContext(request)                  
        )