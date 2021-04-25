from django.contrib import admin
from django.urls import path, include
from todolist import views 

urlpatterns = [
    path('', views.todolist, name = 'todolist'),
    path('delete/<task_id>', views.delete_task, name = 'delete_task'),
    path('edit/<task_id>', views.edit_task, name = 'edit_task'),
  
]


