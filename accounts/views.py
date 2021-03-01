from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm #CustomUserChangeForm
from django.views.generic import CreateView
from django.db import models

# Signup View
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

