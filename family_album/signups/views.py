from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic


class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login'
    template_name = 'registration/register.html'
