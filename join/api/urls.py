from django.urls import path
from .views import UserListCreateView, TaskListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user'),
    path('tasks', TaskListCreateView.as_view(), name='task'),
]