import email
from re import template
from django.shortcuts import render
from datetime import date, datetime
from weatherapp.models import AppUser
import random
# package for sending email
from django.core.mail import send_mail

# forms
from weatherapp.forms import LoginForm, RegistrationForm, ProfileUploadForm

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
            # storing user data in session
            # request.session.setdefault("user_email", user.email)
            # request.session.update({'user_email': user.email})
            # method two
            request.session['user_email'] = user.email

            if request.session.has_key('user_email'):
                template = "users/index.html"
                context = {
                    'page_content_title': 'This is a user dashboard.',
                    'page_content_body': 'Hello! Welcome to our User Dashboard.',
                    'user_email': request.session.get('user_email')
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

def user_logout(request):
    # destroying session object
    del request.session['user_email']

    # using dict function
    # request.session.clear()
    # request.session.pop("user_email")
    template = "users/login.html"
    lf = LoginForm()
    context = {
        'form': lf,
        'msg_error': "Please login."
    }
    return render(request, template, context)

def user_register(request):
    template = 'users/create.html'
    rf = RegistrationForm()
    if request.method == "POST":
        # non parameterized constructor
        user = AppUser()
        user.first_name = request.POST.get('first_name')
        user.middle_name = request.POST.get('middle_name')
        user.last_name = request.POST['last_name']
        user.contact = request.POST['contact']
        user.email = request.POST['email']
        user.dob = request.POST['dob']
        user.verification_code = str(random.random())
        user.password = request.POST['password']
        user.address = request.POST['address']
        user.created_at = datetime.now()
        # to store data
        user.save()

        send_mail(
            'Weather App - Verification Code',
            'Your email verification code is: ' + user.verification_code,
            'c4crypt@gmail.com', # sender email
            [user.email], # receiver email
            fail_silently=False,
        )
        context = {
            'form': rf,
            'success': 'Registered Successfully'
        }
        return render(request, template, context)
    else:
        context = {'form': rf}
        return render(request, template, context)

def user_profile(request):
    if request.session.has_key('user_email'):
        profile_form = ProfileUploadForm()
        template = "users/show.html"
        user = AppUser.objects.get(email=request.session['user_email'])
        context = {
            'form': profile_form, 
            'user_data': user,
            'page_content_title': 'User Profile',
            'email': user.email
            }
        if request.method == "POST":
            user_post = ProfileUploadForm(request.POST, request.FILES)
            if user_post.is_valid():
                user_post.email = request.POST.get('email')
                user_post.created_at = datetime.now()
                user_post.save()
                return render(request, template, context)
            else:
                return render(request, template, context)
        else:
            return render(request, template, context)
    else:
        template = 'users/login.html'
        lf = LoginForm()
        context = {
                'form': lf,
                'msg_error': 'Please login first.'
            }
        return render(request, template, context)

def user_index(request):
    # render() - this function is use to render pages in django
    # takes three parameter
    # 1. request
    # 2. template
    # 3. data (which can be null) - must be a dict - context
    if request.session.has_key('user_email'):
        context = {
            'page_content_title': 'This is a user dashboard.',
            'page_content_body': 'Hello! Welcome to our User Dashboard.',
            'user_email': request.session['user_email']
            }
        template = 'users/index.html'
        return render(request, template, context)
    else:
        template = 'users/login.html'
        lf = LoginForm()
        context = {
                'form': lf,
                'msg_error': 'Please login first.'
            }
        return render(request, template, context)