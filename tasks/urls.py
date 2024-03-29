from django.urls import path
from tasks import views


app_name = "tasks" 

urlpatterns=[
    path("",views.task_list,name="task_list"),
    path("add-task/",views.add_task,name="add_task"),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/update/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('api/tasks/', views.TaskListCreate.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', views.TaskDetailUpdateDelete.as_view(), name='task-detail-update-delete'),
]