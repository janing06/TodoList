from django.shortcuts import render, redirect,  get_object_or_404
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

def register(request):

     if not request.user.is_authenticated:
          
          if request.method == 'POST':
               form = RegistrationForm(request.POST)
               if form.is_valid():
                    form.save()
                    messages.success(request, 'Registered successfully.')
                    return redirect('login')  # Redirect to login page after successful registration
          else:
               form = RegistrationForm()
          return render(request, 'todo/register.html', {'form': form})
     else:
          return redirect('index')

def login(request):
     if not request.user.is_authenticated:
          if request.method == "POST":
               username = request.POST.get('username')
               password = request.POST.get('password')
               user = authenticate(username=username, password=password)
               if user is not None:
                    auth_login(request, user)  # Use auth_login instead of login
                    return redirect('index')
          return render(request, 'todo/login.html')
     else:
          return redirect('index')


@login_required(login_url='/login')
def index(request):
     if request.method == "POST":
          task = request.POST.get('task')
          if request.user.is_authenticated:
               user = request.user
          else:
               anonymous_user, _ = User.objects.get_or_create(username='Anonymous')
               user = anonymous_user
          Todo.objects.create(name=task, user=user)
          return redirect('index')
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