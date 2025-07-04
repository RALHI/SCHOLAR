from django.contrib import admin
from .models import *


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('servicename', 'content')
    search_fields = ('servicename',)

admin.site.register(Service, ServiceAdmin)
