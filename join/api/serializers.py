from rest_framework import serializers
from join.models import Subtask, Task, Contact, CurrentUser, User, TaskStatus

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class SubtaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Subtask
        fields = ['id', 'name', 'done']

    def create(self, validated_data):
        # `task` wird manuell hinzugefügt
        task = self.context.get('task')
        return Subtask.objects.create(task=task, **validated_data)


class TaskSerializer(serializers.ModelSerializer):
    contact_ids = serializers.PrimaryKeyRelatedField(
        source='contacts',       # <-- wichtig! Verbindung zu M2M-Feld
        queryset=Contact.objects.all(),
        many=True,
        write_only=True          # <-- nur für POST/PUT sichtbar
    )
    contacts = ContactSerializer(
        many=True,
        read_only=True           # <-- nur für GET sichtbar
    )

    subtasks = SubtaskSerializer(many=True, required=False)

    due_date = serializers.DateField(
        input_formats=['%d/%m/%y'],
        format='%d/%m/%y'
    )

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'category',
            'due_date',
            'priority',
            'status',
            'contact_ids',  # <-- für Schreiben (POST/PUT)
            'contacts',     # <-- für Lesen (GET)
            'subtasks'
        ]

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        contacts_data = validated_data.pop('contacts', [])
        
        task = Task.objects.create(**validated_data)
        task.contacts.set(contacts_data)

        # Subtasks erstellen und `task` mitgeben
        for subtask_data in subtasks_data:
            SubtaskSerializer(context={'task': task}).create(subtask_data)
        return task

    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', None)
        contacts_data = validated_data.pop('contacts', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if contacts_data is not None:
            instance.contacts.set(contacts_data)

        if subtasks_data is not None:
            existing_subtasks = {subtask.id: subtask for subtask in instance.subtasks.all()}

            for subtask_data in subtasks_data:
                subtask_id = subtask_data.get('id', None)
                if subtask_id and subtask_id in existing_subtasks:
                    # Update vorhandener Subtask
                    subtask = existing_subtasks.pop(subtask_id)
                    for attr, value in subtask_data.items():
                        setattr(subtask, attr, value)
                    subtask.save()
                else:
                    # Neuer Subtask
                    Subtask.objects.create(task=instance, **subtask_data)

            # Übrig gebliebene löschen
            for subtask in existing_subtasks.values():
                subtask.delete()

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