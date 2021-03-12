from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Form to create the User model"""
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'username', 'email', 'isLister',)


class CustomUserChangeForm(UserChangeForm):
    """Form to update a User Account"""
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email',)

