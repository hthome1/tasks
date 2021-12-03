from django.urls import path
from . import views
# from .views import TaskCreate, TaskList, TaskDelete, TaskUpdate
from .views import getTasks

urlpatterns = [
    path('list', views.getTasks),
    path('add', views.createTask),
    path('delete', views.deleteTasks)
]