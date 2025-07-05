from django.contrib import admin
from .models import *

class UpcomingEventsAdmin(admin.ModelAdmin):
    list_display = ('cateory', 'title', 'date', 'time', 'price')
    search_fields = ('title',)
    
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('servicename', 'content')
    search_fields = ('servicename',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(UpcomingEvents, UpcomingEventsAdmin)
