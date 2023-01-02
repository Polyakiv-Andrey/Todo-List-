from django.urls import path

from to_do_list.views import *

urlpatterns = [
    path("", ToDoList.as_view(), name="ToDoList"),
    path("tags/", Tag.as_view(), name="Tags")
]

app_name = "to_do_list"
