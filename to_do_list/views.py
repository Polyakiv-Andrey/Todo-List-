from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from to_do_list.models import Task, Tags


class ToDoListView(generic.ListView):
    model = Task
    template_name = "to_do_list/home.html"
    paginate_by = 5


class CreateTaskView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:ToDoList")
    template_name = "to_do_list/form_task.html"


class UpdateTaskView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:ToDoList")
    template_name = "to_do_list/form_task.html"


class DeleteTaskView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do_list:ToDoList")


def change_task_status(request, pk):
    task = Task.objects.get(id=pk)
    if task.completeness is False:
        task.completeness = True
    else:
        task.completeness = False
    task.save()
    return HttpResponseRedirect(reverse_lazy("to_do_list:ToDoList"))


class TagListView(generic.ListView):
    model = Tags
    template_name = "to_do_list/tags.html"
    paginate_by = 5


class CreateTagView(generic.CreateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:Tags")
    template_name = "to_do_list/form_tags.html"


class UpdateTagView(generic.UpdateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:Tags")
    template_name = "to_do_list/form_tags.html"


class DeleteTagView(generic.DeleteView):
    model = Tags
    success_url = reverse_lazy("to_do_list:Tags")

