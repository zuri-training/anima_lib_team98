from tokenize import Name
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class Signin(UserCreationForm):
    username = forms.CharField(max_length= 22, min_length=8, required=True, widget= forms.TextInput(attrs ={
        'placeholder' : 'John Doe',
        'pattern' : "[A-Za-z]{1,30} [A-Za-z]{1,30}",
        'name':'username',
        'title' : "Enter full name using alphabets only",
        'type' : 'text',
        'id' : 'username'
    }))

    email = forms.EmailField(required=True, widget= forms.TextInput(attrs ={
        'placeholder' : 'JohnDoe@email.com',
        
        'name':'email',
        'type' : 'email',
        'id' : 'email'
    }))

    password1 = forms.CharField( max_length= 22, min_length=8, required=True, widget= forms.PasswordInput(attrs ={
        'placeholder' : '********',
        'name':'password1',
        'data-toggle' : 'password',
        'pattern' : "(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}",
        'title' : "Password must be 8 or more characters, containing at least one number, one UPPERCASE and lowercase letter",
        'type' : 'password',
        'id' : 'password1'
    }))


    password2 = forms.CharField( max_length= 22, min_length=8, required=True, widget= forms.PasswordInput(attrs ={
        'placeholder' : '********',
        'name':'password2',
        'data-toggle' : 'password',
         'pattern' : "(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}",
        'title' : "Password must be 8 or more characters, containing at least one number, one UPPERCASE and lowercase letter",
        'type' : 'password',
        'id' : 'password2'
    }))
    

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({
    #         'required': '',
    #         'name':'username',
    #         'type' : 'text',
            
    #         'placeholder' : 'John Doe',
    #         'maxlength' : '24',
    #         'minlength' : '6' ,
    #         'id' : 'username'
    #     })
    #     self.fields['email'].widget.attrs.update({
    #         'required': '',
    #         'name':'email',
    #         'type' : 'email',
            
    #         'placeholder' : 'JohnDoe@email.com',
    #         'id' : 'email'
    #     })
    #     self.fields['password1'].widget.attrs.update({
    #         'required': '',
    #         'name':'password1',
    #         'id' : 'password1',
    #         'type' : 'password',
    #         'data-toggle' : 'password',
    #         'placeholder' : '********',
    #         'maxlength' : '22',
    #         'minlength' : '8' 
    #     })
    #     self.fields['password2'].widget.attrs.update({
    #         'required': '',
    #         'name':'password2',
    #         'id' : 'password2',
    #         'type' : 'password',
    #         'data-toggle' : 'password',
    #         'placeholder' : '********',
    #         'maxlength' : '22',
    #         'minlength' : '8' 
    #     })

    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
