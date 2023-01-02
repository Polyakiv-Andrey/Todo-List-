from django.views import generic
from django.shortcuts import render

from to_do_list.models import Task, Tags


class ToDoList(generic.ListView):
    model = Task
    template_name = "to_do_list/home.html"
    paginate_by = 5


class Tag(generic.ListView):
    model = Tags
    template_name = "to_do_list/tags.html"
    paginate_by = 5
