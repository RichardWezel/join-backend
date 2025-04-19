from rest_framework import serializers
from join.models import CustomUser, Subtask, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = []

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = '__all__'
