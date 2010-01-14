from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink

import datetime

class EventManager(models.Manager):
    def future_events(self):
        return self.filter(event_times__start__gt = datetime.datetime.now()).distinct()
    def past_events(self):
        return self.filter(event_times__end__lte = datetime.datetime.now()).distinct()
    
class EventTimeManager(models.Manager):
    def future_event_times(self):
        return self.filter(start__gt = datetime.datetime.now()).order_by('start')
    def past_event_times(self):
        return self.filter(start__lte = datetime.datetime.now()).order_by('-start')

class Event(models.Model):
    '''
    Events class
    '''
    user = models.ForeignKey(User)
    title = models.CharField('Event Name', max_length = 50)
    slug = models.SlugField('Event Slug', max_length = 50)
    description = models.TextField(blank = True)
    location = models.CharField('Location', max_length = 200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    objects = EventManager()
    
    def save(self):
        self.slug = self.title.replace(' ','-')
        super(Event, self).save()
    
    def __unicode__(self):
        return u'%s' % self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('event',(),{'event_id':self.id,'event_slug':self.slug})
    
class EventTime(models.Model):
    """EventTime model"""
    event = models.ForeignKey(Event, related_name='event_times')
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    is_all_day = models.BooleanField(default=False)
    
    objects = EventTimeManager()
 
    class Meta:
        verbose_name = _('event time')
        verbose_name_plural = _('event times')
        db_table = 'event_times'
        ordering = ['start']
 
    @property
    def is_past(self):
        NOW = datetime.datetime.now()
        if self.start < NOW:
            return True
        return False
    
    @models.permalink
    def get_absolute_url(self):
        return ('event_time',(),{'event_time_id':self.id,
                                'event_slug':self.event.slug})
 
    def __unicode__(self):
        return u'%s' % self.event.title

class Attendee(models.Model):
    '''
    Attendee Class
    '''
    user = models.ForeignKey(User, blank = True, null = True)
    name = models.CharField('Attendee Name', max_length = 200, blank = True)
    event_time = models.ForeignKey(EventTime)
    
    class Meta:
        unique_together = (
            ('user','name','event_time'),
        )
    
    def is_attending(self, user=None):
        if self.user == user:
            return True
        else:
            return False
    
    def __unicode__(self):
        try:
            return u'%s' % self.user.get_full_name() or self.user.username
        except AttributeError:
            return u'%s' % self.name.title()
        