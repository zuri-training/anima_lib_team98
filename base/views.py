from django.shortcuts import render, redirect
from .forms import Signup
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# Create your views here.


def home(request):
    return render(request, 'Animation_lib/home.html')

def signupform(request):
    if request.method == 'POST':
        form = Signup(request.POST)


        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')

        elif form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            password = form.cleaned_data.get('password2')

            if password != raw_password:
                messages.error(request, 'password do not match')
            
            else:
                form.save()

                messages.success(request, 'Your account has been created, you can log in now')

                new_user = authenticate(username = username, password = raw_password)
                if new_user is not None:
                    
                    login(request, new_user)
                    return redirect('signup')
                else:
                    messages.error(request, 'Service TimedOut')
        else:
            messages.error(request, 'An error has occured during registeration')
    else:
        form = Signup()
    context = {'form' : form}
    return render(request, 'Animation_lib/signup.html', context)


def signinform(request):
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

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "Animation_lib/password/password_reset_email.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Animax',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="Animation_lib/password/password_reset.html", context={"password_reset_form":password_reset_form})
