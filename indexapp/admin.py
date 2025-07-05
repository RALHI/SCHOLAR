from django.contrib import admin
from .models import *

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('servicename', 'content')
    search_fields = ('servicename',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Team, TeamAdmin)
