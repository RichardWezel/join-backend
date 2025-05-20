from rest_framework import serializers
from join.models import Subtask, Task, Contact, CurrentUser, User, TaskStatus

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = []

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        exclude = ['task']

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False)
    contacts = ContactSerializer(many=True, required=False)
    due_date = serializers.DateField(
        input_formats=['%d/%m/%y'],  # für Eingabe wie "11/07/24"
        format='%d/%m/%y'            # für Ausgabe wie "11/07/24"
    )


    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'due_date', 'priority', 'status', 'contacts', 'subtasks']

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        contacts_data = validated_data.pop('contacts', [])
        
        task = Task.objects.create(**validated_data)
        
        # Kontakte zuordnen
        task.contacts.set(contacts_data)
        
        # Subtasks erstellen
        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)
        
        return task

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentUser
        fields = ['currentUserIndex']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ['taskstatus']