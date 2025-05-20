from rest_framework import serializers
from join.models import Subtask, Task, Contact, CurrentUser, User, TaskStatus

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = []

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'

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
    
    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', None)
        contacts_data = validated_data.pop('contacts', None)

        # Aktualisiere die Task-Instanz
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        # Aktualisiere Kontakte
        if contacts_data is not None:
            instance.contacts.set(contacts_data)

        # Aktualisiere Subtasks
        if subtasks_data is not None:
            for subtask in instance.subtasks.all():
                subtask.delete()
            for subtask_data in subtasks_data:
                Subtask.objects.create(task=instance, **subtask_data)

        return instance
    

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
        fields = ['status']