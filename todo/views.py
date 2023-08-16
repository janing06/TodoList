from django.shortcuts import render, redirect
from .models import Todo
from django.shortcuts import redirect, get_object_or_404


def index(request):
     if request.method == "POST":
          task = request.POST.get('task')
          Todo.objects.create(name=task)
     todos = Todo.objects.all().order_by('-created_at')
     return render(request, 'todo/index.html',{'todos': todos,})

def delete_todo(request, id):
     task = get_object_or_404(Todo, pk=id)
     task.delete()
     return redirect('index')

def edit_todo(request, id):
     
     todo = Todo.objects.get(pk=id)
     todo.is_completed = not todo.is_completed
     todo.save()
     return redirect('index')