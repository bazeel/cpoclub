from django.contrib import admin
from events.models import Image, Event


class ImagesInline(admin.StackedInline):
    model = Image


class EventAdmin(admin.ModelAdmin):
    list_display = ['date', 'city', 'address', 'preview', 'active']
    list_editable = ['active']
    search_fields = ['city', 'date', 'address']
    inlines = [ImagesInline]


admin.site.register(Event, EventAdmin)