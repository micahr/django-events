
from south.db import db
from django.db import models
from events.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'EventTime'
        db.create_table('event_times', (
            ('id', orm['events.EventTime:id']),
            ('event', orm['events.EventTime:event']),
            ('start', orm['events.EventTime:start']),
            ('end', orm['events.EventTime:end']),
            ('is_all_day', orm['events.EventTime:is_all_day']),
        ))
        db.send_create_signal('events', ['EventTime'])
        
        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', orm['events.Event:id']),
            ('user', orm['events.Event:user']),
            ('title', orm['events.Event:title']),
            ('slug', orm['events.Event:slug']),
            ('description', orm['events.Event:description']),
            ('location', orm['events.Event:location']),
            ('created', orm['events.Event:created']),
            ('modified', orm['events.Event:modified']),
        ))
        db.send_create_signal('events', ['Event'])
        
        # Adding model 'Attendee'
        db.create_table('events_attendee', (
            ('id', orm['events.Attendee:id']),
            ('user', orm['events.Attendee:user']),
            ('name', orm['events.Attendee:name']),
            ('event_time', orm['events.Attendee:event_time']),
        ))
        db.send_create_signal('events', ['Attendee'])
        
        # Creating unique_together for [user, name, event_time] on Attendee.
        db.create_unique('events_attendee', ['user_id', 'name', 'event_time_id'])
        
    
    
    def backwards(self, orm):
        
        # Deleting unique_together for [user, name, event_time] on Attendee.
        db.delete_unique('events_attendee', ['user_id', 'name', 'event_time_id'])
        
        # Deleting model 'EventTime'
        db.delete_table('event_times')
        
        # Deleting model 'Event'
        db.delete_table('events_event')
        
        # Deleting model 'Attendee'
        db.delete_table('events_attendee')
        
    
    
    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'events.attendee': {
            'Meta': {'unique_together': "(('user', 'name', 'event_time'),)"},
            'event_time': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.EventTime']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'events.event': {
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'events.eventtime': {
            'Meta': {'db_table': "'event_times'"},
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event_times'", 'to': "orm['events.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_all_day': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {})
        }
    }
    
    complete_apps = ['events']
