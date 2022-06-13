from re import template
from django.shortcuts import render
from datetime import datetime
from weatherapp.models import AppUser

from weatherapp.forms import LoginForm, RegistrationForm

# Create your views here.
def landing(request):
    return render(request, 'index.html')

def user_login(request):    
    # creating form object
    lf = LoginForm()
    template = 'users/login.html'
    if request.method == "POST":
        # creating use object
        user = AppUser.objects.get(email=request.POST.get('email'))
        if request.POST.get('password') == user.password:
            context = {
                'form': lf,
                'msg_success': 'Login Success'
            }
            return render(request, template, context)
        else:
            context = {
                'form': lf,
                'msg_error': 'Invalid email or password'
            }
            return render(request, template, context)
    else:
        context = {'form': lf}
        return render(request, template, context)

def user_register(request):
    template = 'users/create.html'
    rf = RegistrationForm()
    if request.method == "POST":
        # first_name = request.POST.get('first_name')
        # middle_name = request.POST.get('middle_name')
        # last_name = request.POST['last_name']
        # contact = request.POST.get('contact')
        # email = request.POST.get('email')
        # dob = request.POST.get('dob')
        # password = request.POST.get('password')
        # address = request.POST.get('address')
        
        # creating AppUser model object

        # parameterized constructor
        # user = AppUser(first_name=first_name,\
        #     middle_name=middle_name, last_name=last_name,\
        #         contact=contact, email=email, \
        #             dob=dob, password=password,address=address,\
        #                 created_at=datetime.now())
        # storing data to Model Attribute via object

        # non parameterized constructor
        user = AppUser()
        user.first_name = request.POST.get('first_name')
        user.middle_name = request.POST.get('middle_name')
        user.last_name = request.POST['last_name']
        user.contact = request.POST['contact']
        user.email = request.POST['email']
        user.dob = request.POST['dob']
        user.password = request.POST['password']
        user.address = request.POST['address']
        user.created_at = datetime.now()
        # to store data
        user.save()
        context = {
            'form': rf,
            'success': 'Registered Successfully'
        }
        return render(request, template, context)
    else:
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