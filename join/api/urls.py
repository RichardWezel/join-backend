from django.urls import path, include
from .views import TaskViewSet, ContactViewSet, CurrentUserViewSet, UserViewSet
from django.conf import settings
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'users', UserViewSet, basename='user')
router.register(r'current_user', CurrentUserViewSet, basename='current_user')

urlpatterns = [
    path('', include(router.urls)),
]