from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField

from . import models


class AddAdvertForm(forms.ModelForm):
    class Meta:
        model = models.Advert
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}, ),
        }


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['language'].empty_label = "Language is not chosen"
        self.fields['gender'].empty_label = "Gender is not chosen"

    class Meta:
        model = models.Users
        fields = ['username', 'email', 'information', 'language', 'gender', 'photo']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'information': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'password': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactServiceForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()


class ContactUserForm(forms.Form):
    message = forms.CharField(label='message')
