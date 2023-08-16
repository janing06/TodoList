from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User  # Assuming you have imported User from django.contrib.auth.models
        fields = ['username', 'password1', 'password2']