from django.contrib import admin
from meetups.models import Meetup


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Meetup, MeetupAdmin)
