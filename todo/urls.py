from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='index'),
     path('delete-todo/<id>', views.delete_todo, name='delete-todo'),
     path('edit-todo/<id>', views.edit_todo, name='edit-todo'),
]