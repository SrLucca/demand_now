from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from register.models import CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    last_name = forms.CharField(label='Sobrenome')
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name' ,'password1', 'password2')