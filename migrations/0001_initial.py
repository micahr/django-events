
from south.db import db
from django.db import models
from django_events.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'EventTime'
        db.create_table('event_times', (
            ('id', orm['django_events.EventTime:id']),
            ('event', orm['django_events.EventTime:event']),
            ('start', orm['django_events.EventTime:start']),
            ('end', orm['django_events.EventTime:end']),
            ('is_all_day', orm['django_events.EventTime:is_all_day']),
        ))
        db.send_create_signal('django_events', ['EventTime'])
        
        # Adding model 'Event'
        db.create_table('django_events_event', (
            ('id', orm['django_events.Event:id']),
            ('user', orm['django_events.Event:user']),
            ('title', orm['django_events.Event:title']),
            ('slug', orm['django_events.Event:slug']),
            ('description', orm['django_events.Event:description']),
            ('location', orm['django_events.Event:location']),
            ('created', orm['django_events.Event:created']),
            ('modified', orm['django_events.Event:modified']),
        ))
        db.send_create_signal('django_events', ['Event'])
        
        # Adding model 'Attendee'
        db.create_table('django_events_attendee', (
            ('id', orm['django_events.Attendee:id']),
            ('user', orm['django_events.Attendee:user']),
            ('name', orm['django_events.Attendee:name']),
            ('event_time', orm['django_events.Attendee:event_time']),
        ))
        db.send_create_signal('django_events', ['Attendee'])
        
        # Creating unique_together for [user, name, event_time] on Attendee.
        db.create_unique('django_events_attendee', ['user_id', 'name', 'event_time_id'])
        
    
    
    def backwards(self, orm):
        
        # Deleting unique_together for [user, name, event_time] on Attendee.
        db.delete_unique('django_events_attendee', ['user_id', 'name', 'event_time_id'])
        
        # Deleting model 'EventTime'
        db.delete_table('event_times')
        
        # Deleting model 'Event'
        db.delete_table('django_events_event')
        
        # Deleting model 'Attendee'
        db.delete_table('django_events_attendee')
        
    
    
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
        'django_events.attendee': {
            'Meta': {'unique_together': "(('user', 'name', 'event_time'),)"},
            'event_time': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['django_events.EventTime']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'django_events.event': {
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'django_events.eventtime': {
            'Meta': {'db_table': "'event_times'"},
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event_times'", 'to': "orm['django_events.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_all_day': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {})
        }
    }
    
    complete_apps = ['django_events']
