from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from .models import CustomUser

# Our classes inherit from the UserCreationForms, but we are going to customize & add functionality.
# We are adding 'age'

class CustomUserCreationForm(UserCreationForm):
    """Form to create the User model"""
    class Meta(UserCreationForm):
        model = CustomUser
        # appending to a tuple with appending another tuple to create a new one. Tuples are immutable (unchangeable), so you must make a new one.
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'username', 'email', 'isLister',)


class CustomUserChangeForm(UserChangeForm):
    """Form to update a User Account"""
    class Meta(UserChangeForm):
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email',)

