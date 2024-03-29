from rest_framework import generics
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .serializers import TaskSerializer
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})


def task_detail(request, pk):

    task = get_object_or_404(Task, pk=pk)

    return render(request, 'tasks/task_detail.html', {'task': task})


@require_POST
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks:task_list')


def task_update(request, pk):
    task = get_object_or_404(
        Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()

            return redirect('tasks:task_list')

    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_update.html', {

        'form': form

    })




# Api DRF

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer