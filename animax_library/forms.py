from django.contrib.auth.forms import UserCreationForm
from .models import User
# from django import forms
# from django.forms import ModelForm

class Signin(UserCreationForm):
    # username = forms.CharField(max_length= 22, min_length=8, required=True, widget= forms.TextInput(attrs ={
    #     'placeholder' : 'John Doe',
    #     'name':'username',
    #     'type' : 'text',
    #     'id' : 'username'
    # }))

    # email = forms.EmailField(required=True, widget= forms.TextInput(attrs ={
    #     'placeholder' : 'JohnDoe@email.com',
    #     'name':'username',
    #     'type' : 'email',
    #     'id' : 'email'
    # }))

    # password1 = forms.CharField( max_length= 22, min_length=8, required=True, widget= forms.PasswordInput(attrs ={
    #     'placeholder' : '********',
    #     'name':'username',
    #     'data-toggle' : 'password',
    #     'type' : 'password',
    #     'id' : 'password1'
    # }))


    # password2 = forms.CharField( max_length= 22, min_length=8, required=True, widget= forms.PasswordInput(attrs ={
    #     'placeholder' : '********',
    #     'name':'username',
    #     'data-toggle' : 'password',
    #     'type' : 'password',
    #     'id' : 'password2'
    # }))
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name':'username',
            'type' : 'text',
             'pattern' : "[A-Za-z]{1,30} [A-Za-z]{1,30}",
            'placeholder' : 'John Doe',
            'maxlength' : '22',
            'minlength' : '6' ,
            'id' : 'username'
        })
        self.fields['email'].widget.attrs.update({
            'required': '',
            'name':'email',
            'type' : 'email',
           
            'placeholder' : 'JohnDoe@email.com',
            'id' : 'email'
        })
        self.fields['password1'].widget.attrs.update({
            'required': '',
            'name':'password1',
            'id' : 'password1',
            'type' : 'password',
        
            'placeholder' : '********',
            'maxlength' : '22',
            'minlength' : '8' 
        })
        self.fields['password2'].widget.attrs.update({
            'required': '',
            'name':'password2',
            'id' : 'password2',
            'type' : 'password',
        
            'placeholder' : '********',
            'maxlength' : '22',
            'minlength' : '8' 
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class loginForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['email', 'password']
