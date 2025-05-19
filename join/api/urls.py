from django.urls import path, include
from .views import TaskViewSet, ContactViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]