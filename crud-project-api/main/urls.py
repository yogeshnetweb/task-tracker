from django.urls import path, include
from .views import TaskViewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('tasks', TaskViewsets, basename="task")

urlpatterns = [
    path('', include(router.urls))
]
