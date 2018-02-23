from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'accounts/home.html'


class SignupView(TemplateView):
    template_name = 'accounts/signup.html'


"""class LoginView(TemplateView):
    template_name = 'accounts/login.html'"""


