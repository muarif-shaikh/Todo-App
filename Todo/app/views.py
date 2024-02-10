from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime

def todoapp(request):
    if request.method == "POST":
        data = request.POST

        todo_title = data.get('todo_title')
        todo_desc = data.get('todo_desc')
        date_created = datetime.utcnow()

        Todo.objects.create(
            todo_title = todo_title,
            todo_desc = todo_desc,
            date_created = date_created
        )

        return redirect('/')
    
    queryset = Todo.objects.all()

    if request.GET.get('search-todo'):
        queryset = queryset.filter(todo_title__icontains = request.GET.get('search-todo'))

    context = {'allTodos' : queryset}

    return render(request, 'index.html', context)

def delete_todo(request, id):
    queryset = Todo.objects.get(id = id)
    queryset.delete()
    return redirect('/')


def update_todo(request, id):
    queryset = Todo.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('todo_title')
        receipe_desc = data.get('todo_desc')

        queryset.todo_title = receipe_name
        queryset.todo_desc = receipe_desc

        queryset.save()

        return redirect('/')

    context = {'todo' : queryset}

    return render(request, 'update.html', context)


def about_page(request):
    return HttpResponse ("This is a simple todo app made using Django")
