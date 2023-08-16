from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
     path('', views.index, name='index'),
     path('delete-todo/<id>', views.delete_todo, name='delete-todo'),
     path('edit-todo/<id>', views.edit_todo, name='edit-todo'),
     path('login/', views.login, name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('register/', views.register, name='register'),
]