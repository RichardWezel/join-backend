from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)  # Farbcodes wie #ff4646
    mail = models.EmailField()
    phone = models.CharField(max_length=30)
    locked_in = models.BooleanField(default=False)

class Subtask(models.Model):
    name = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    task = models.ForeignKey('Task', related_name='subtasks', on_delete=models.CASCADE)

class Task(models.Model):
    STATUS_CHOICES = [
        ('toDo', 'To Do'),
        ('inProgress', 'In Progress'),
        ('awaitFeedback', 'Await Feedback'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    due_date = models.DateField()
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    contacts = models.ManyToManyField('Contact', related_name='tasks')

class CurrentUser(models.Model):
    currentUserIndex = models.IntegerField(default=999)

class User(models.Model):
    first_name = models.CharField(max_length=100, default="Guest")
    second_name = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=7, default="#ff4646")
    mail = models.EmailField(blank=True)
    password = models.CharField(max_length=100, blank=True)
    locked_in = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.second_name}".strip()