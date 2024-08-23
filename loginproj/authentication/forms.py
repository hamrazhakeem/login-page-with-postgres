from django import forms
from .models import User
from django.forms import ModelForm

class Signinform(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))

    username.label = ''
    password.label = ''

class Signupform(forms.ModelForm):
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    confirm_password.label = ''

    class Meta:
        model = User
        fields = "__all__"
        labels = {
            'firstname' : '',
            'lastname' : '',
            'email' : '',
            'username' : '',
            'password' : '',
        }
        widgets = {
            'firstname' : forms.TextInput(attrs={'placeholder':'First Name'}),
            'lastname' : forms.TextInput(attrs={'placeholder':'Last Name'}),
            'email' : forms.TextInput(attrs={'placeholder':'Email'}),
            'username' : forms.TextInput(attrs={'placeholder':'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Password'}),
            'confirm_password' : forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),
        }