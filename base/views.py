from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import Signup
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'Animation_lib/index.html')

def doc_page1(request):
    return render(request, 'Animation_lib/doc_page.html')

def doc_page2(request):
    return render(request, 'Animation_lib/doc_page2.html')

def doc_page3(request):
    return render(request, 'Animation_lib/doc_page3.html')

def doc_page4(request):
    return render(request, 'Animation_lib/doc_page4.html')


@login_required(login_url='signin')
def about(request):
    return render(request, 'Animation_lib/about.html')


# @login_required(login_url='signin')
# def documentation(request):
#     return HttpResponse('Documentation Page not ready yet')

@login_required(login_url='signin')
def animation(request):
    return HttpResponse('Animation Page not ready yet')

def faq(request):
    return render(request, 'Animation_lib/faq.html')

def signupform(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = Signup(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            password = form.cleaned_data.get('password2')

            if password != raw_password:
                messages.error(request, 'password do not match')
            
            else:
                form.save()
                new_user = authenticate(username = username, password = raw_password)
                if new_user is not None:
                    
                    login(request, new_user)
                    return redirect('home')
                else:
                    messages.error(request, 'Service TimedOut')
        else:
            messages.error(request, 'Check Your Details Carefully')
    else:
        form = Signup()
    context = {'form' : form}
    return render(request, 'Animation_lib/signup.html', context)


def signinform(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = User.objects.get(email = email.lower()).username

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'user is not recognised')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong Password')
    
    context = {} 
    return render(request, 'Animation_lib/signin.html', context)


def logoutUser(request):
    logout(request)
    return redirect('signin')
