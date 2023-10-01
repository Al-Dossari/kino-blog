from django.shortcuts import render

from django.views.generic import CreateView, DetailView, TemplateView, UpdateView
from django.urls import reverse_lazy

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class EditView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/signup.html'
    model = CustomUser
class ProfileView(TemplateView):
    template_name = 'registration/profile.html'
