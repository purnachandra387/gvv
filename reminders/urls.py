from django.urls import path
from .views import add_task, view_tasks,update_task_status

urlpatterns = [
    path('add/', add_task, name='add_task'),  # Ensure this name matches
    path('view/', view_tasks, name='view_tasks'),
    path('update_status/<int:task_id>/', update_task_status, name='update_task_status'),
]
