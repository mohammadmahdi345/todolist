from django.db import models
from user.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} - ({self.date})'
    

class Timeslot(models.Model):

    task = models.ForeignKey(Task, related_name='time_slots', on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    notified_10min = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'




