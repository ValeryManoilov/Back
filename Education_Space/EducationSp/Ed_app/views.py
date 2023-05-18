from django.shortcuts import render
from Ed_app.forms import UserForm, CourseForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'Ed_app/index.html')

@login_required
def special(request):
    return HttpResponse('You are logged!')

@login_required
def Logout(request):
    logout(request)
    return render(request, 'Ed_app/index.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse('Account not active')
        else:
            print('Someone tired to login and failed')
            print('Username: {} and password: {}'.format(username, password))
    else:
        return render(request, 'Ed_app/login.html', {})

def User_register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'Ed_app/user_registration.html', {'user_form':user_form, 'registered':registered})

def Course_register(request):

    registered = False

    if request.method == "POST":
        course_form = CourseForm(data=request.POST)
        if course_form.is_valid():
            course = course_form.save()
            course.save()
            registered = True
        else:
            print(course_form.errors)

    else:
        course_form = CourseForm()

    return render(request, 'Ed_app/course_registration.html', {'course_form':course_form, 'registered':registered})
