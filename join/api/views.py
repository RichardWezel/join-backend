from rest_framework import generics
from join.models import CustomUser, Task, Subtask
from .serializers import UserSerializer, TaskSerializer, SubtaskSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = TaskSerializer
