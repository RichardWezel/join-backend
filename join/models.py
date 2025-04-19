from django.db import models

# Create your models here.

class CustomUser(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)  # Farbcodes wie #ff4646
    mail = models.EmailField()
    password = models.CharField(max_length=100)
    locked_in = models.BooleanField(default=False)

class Subtask(models.Model):
    name = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    task = models.ForeignKey('Task', related_name='subtasks', on_delete=models.CASCADE)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    due_date = models.DateField()
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    contacts = models.ManyToManyField('CustomUser', related_name='tasks')
