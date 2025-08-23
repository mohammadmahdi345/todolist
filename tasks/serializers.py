from rest_framework import serializers
from .models import *

class TaskMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'user','date']

class TimeSerializer(serializers.ModelSerializer):
    task = TaskMiniSerializer(read_only=True)
    class Meta:
        fields = '__all__'
        model = Timeslot



class TimeMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeslot
        fields = ['id', 'start_time', 'end_time']

class TaskSerializer(serializers.ModelSerializer):
    time_slots = TimeMiniSerializer(many=True, read_only=True)
    class Meta:
        fields = '__all__'
        model = Task
        extra_kwargs = {
            'user': {'read_only': True},
        }


