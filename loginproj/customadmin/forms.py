from django import forms
from authentication.models import User
from django.forms import ModelForm

class Usereditform(forms.ModelForm):
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
        }