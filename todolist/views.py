from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import Tasklist
from todolist.form import TaskForm
from django.contrib import messages
# this is new

def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('New Task Added'))
        return redirect('todolist')
    else:
        all_tasks = Tasklist.objects.all
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def delete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == 'POST':
        task = Tasklist.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance= task)
        if form.is_valid():
            form.save()
        
        messages.success(request, ('Task Edit'))
        return redirect('todolist')
    else:
        task_obj = Tasklist.objects.get(id=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

def index(request):
    context = {
        'index_text': 'Welcome to Index Page',
    }
    return render(request, 'index.html', context)

def contact(request):
    context = {
        'contact_text': 'Welcome to contact page',
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text': 'Welcome to about page',
    }
    return render(request, 'about.html', context)
