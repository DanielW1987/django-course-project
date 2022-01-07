from django.contrib import admin
from meetups.models import Meetup, Location


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    list_filter = ('title', 'location',)
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
