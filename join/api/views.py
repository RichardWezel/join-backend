from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from join.models import Contact, Task, Subtask, CurrentUser, User, TaskStatus
from .serializers import ContactSerializer, TaskSerializer, SubtaskSerializer, CurrentUserSerializer, UserSerializer, TaskStatusSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CurrentUserViewSet(viewsets.ModelViewSet):
    queryset = CurrentUser.objects.all()
    serializer_class = CurrentUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskStatusViewSet(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer
