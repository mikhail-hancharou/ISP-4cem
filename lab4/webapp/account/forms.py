from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# from account.models import Publisher


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


'''class RegisterPublisherForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    pseudonym = forms.CharField(label='Pseudonym', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password conf.', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Publisher
        fields = ('username', 'pseudonym', 'password1', 'password2')
'''