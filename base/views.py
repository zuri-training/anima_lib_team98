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

def reset(request):
    return render(request, 'Animation_lib/reset.html')

def resetdone(request):
    return render(request, 'Animation_lib/resetdone.html')

def resetconfirm(request):
    return render(request, 'Animation_lib/resetconfirm.html')

def resetcomplete(request):
    return render(request, 'Animation_lib/resetcomplete.html')


@login_required(login_url='signin')
def about(request):
    return render(request, 'Animation_lib/about.html')


# @login_required(login_url='signin')
# def documentation(request):
#     return HttpResponse('Documentation Page not ready yet')

@login_required(login_url='signin')
def animation(request):
    return render(request, 'Animation_lib/animation-blink.html')


@login_required(login_url='signin')
def animation_two(request):
    return render(request, 'Animation_lib/animation-blink-2.html')

@login_required(login_url='signin')
def animation_cloud(request):
    return render(request, 'Animation_lib/animation-cloud.html')

@login_required(login_url='signin')
def animation_fade(request):
    return render(request, 'Animation_lib/animation-fade.html')

@login_required(login_url='signin')
def animation_fade_two(request):
    return render(request, 'Animation_lib/animation-fade-2.html')

@login_required(login_url='signin')
def animation_fade3(request):
    return render(request, 'Animation_lib/animation-fade-3.html')

@login_required(login_url='signin')
def animation_fade4(request):
    return render(request, 'Animation_lib/animation-fade-4.html')

@login_required(login_url='signin')
def animation_rotate(request):
    return render(request, 'Animation_lib/animation-rotate.html')

@login_required(login_url='signin')
def animation_rotate_two(request):
    return render(request, 'Animation_lib/animation-rotate-2.html')

@login_required(login_url='signin')
def animation_rotate3(request):
    return render(request, 'Animation_lib/animation-rotate-3.html')

@login_required(login_url='signin')
def animation_rotate4(request):
    return render(request, 'Animation_lib/animation-rotate-4.html')

@login_required(login_url='signin')
def animation_stretch(request):
    return render(request, 'Animation_lib/animation-stretch.html')

@login_required(login_url='signin')
def animation_stretch_two(request):
    return render(request, 'Animation_lib/animation-stretch-2.html')

@login_required(login_url='signin')
def animation_stretch3(request):
    return render(request, 'Animation_lib/animation-stretch-3.html')


@login_required(login_url='signin')
def animation_pulse(request):
    return render(request, 'Animation_lib/animation-pulse.html')

@login_required(login_url='signin')
def animation_pulse_two(request):
    return render(request, 'Animation_lib/animation-pulse-2.html')

@login_required(login_url='signin')
def animation_bounce(request):
    return render(request, 'Animation_lib/animation-bounce.html')

@login_required(login_url='signin')
def animation_bounce_two(request):
    return render(request, 'Animation_lib/animation-bounce-2.html')

@login_required(login_url='signin')
def animation_move_two(request):
    return render(request, 'Animation_lib/animation-move-2.html')

@login_required(login_url='signin')
def animation_move(request):
    return render(request, 'Animation_lib/animation-move.html')

@login_required(login_url='signin')
def animation_move3(request):
    return render(request, 'Animation_lib/animation-move-3.html')

@login_required(login_url='signin')
def animation_move4(request):
    return render(request, 'Animation_lib/animation-move-4.html')

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
    return redirect('home')
