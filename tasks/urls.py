from django.urls import path
import views

from . import views

urlpatterns = [
    path('list', views.getTask),
    path('delete', views.deleteTask),
    path('create', views.createTask)
]
