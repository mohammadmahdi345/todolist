from django.contrib import admin

from .models import Task,Timeslot

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'completed', 'title')


@admin.register(Timeslot)
class TimeslotAdmin(admin.ModelAdmin):
    list_display = ('task', 'start_time', 'end_time')




