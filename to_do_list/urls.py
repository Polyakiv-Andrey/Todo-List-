from django.urls import path

from to_do_list.views import *

urlpatterns = [
    path("", ToDoListView.as_view(), name="ToDoList"),
    path("creat-task/", CreateTaskView.as_view(), name="create-task"),
    path("update-task/<int:pk>/", UpdateTaskView.as_view(), name="update-task"),
    path("delete-task/<int:pk>/", DeleteTaskView.as_view(), name="delete-task"),
    path("task-status/<int:pk>/", change_task_status, name="change-task-status"),
    path("tags/", TagListView.as_view(), name="Tags"),

]

app_name = "to_do_list"
