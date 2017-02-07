from core.models import GroupTask, Task
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'date_created', 'date_updated', 'group_task')


class GroupTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupTask
        fields = ('id', 'name')