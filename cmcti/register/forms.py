from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from register.models import CustomUser, Profile

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':"form-control"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    last_name = forms.CharField(label='Sobrenome', widget=forms.TextInput(attrs={'class':"form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control", 'aria-describedby':"passwordHelpBlock"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name' ,'password1', 'password2')
