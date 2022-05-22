from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from account.forms import RegisterUserForm


class SignUpView(generic.CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


def logout_user(request):
    logout(request)
    return redirect('login')
