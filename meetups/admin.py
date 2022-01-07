from django.contrib import admin
from meetups.models import Meetup, Location, Participant


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
