from re import template
from django.shortcuts import render

from weatherapp.forms import LoginForm, RegistrationForm

# Create your views here.
def landing(request):
    return render(request, 'index.html')

def user_login(request):
    # creating form object
    lf = LoginForm()
    template = 'users/login.html'
    context = {'form': lf}
    return render(request, template, context)

def user_register(request):
    rf = RegistrationForm()
    template = 'users/create.html'
    context = {'form': rf}
    return render(request, template, context)

def user_index(request):
    # render() - this function is use to render pages in django
    # takes three parameter
    # 1. request
    # 2. template
    # 3. data (which can be null) - must be a dict - context
    context = {
        'page_content_title': 'This is a user dashboard.',
        'page_content_body': 'Hello! Welcome to our User Dashboard.'
        }
    template = 'users/index.html'
    return render(request, template, context)