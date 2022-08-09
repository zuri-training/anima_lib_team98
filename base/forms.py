import email
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Signup(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name':'username',
            'type' : 'text',
            
            'placeholder' : 'JohnDoe',
            'maxlength' : '16',
            'minlength' : '4' ,
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

    def save(self, commit=True):
        user = super(Signup, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

