from django.contrib import admin
from models import EventTime, Event, Attendee

class EventTimeInline(admin.TabularInline):
    model = EventTime
    fk = 'event'
 
 
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'created')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [EventTimeInline,]

admin.site.register(Event, EventAdmin)
admin.site.register(EventTime)
admin.site.register(Attendee)