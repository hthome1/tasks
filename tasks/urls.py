from django.urls import path
from . import views
from .views import getTasks

urlpatterns = [
    path('allTasks', views.getTasks),
    path('add', views.createTask),
    path('delete', views.deleteTasks)
]