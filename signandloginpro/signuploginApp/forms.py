from django import forms
from .models import SignUpData


class SignUpDataForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'place-holder':'enter name'
            }
        )
    )
    age=forms.IntegerField(
        label="Enter your age",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'place-holder':'enter age'
            }
        )
    )
    email_id=forms.EmailField(
        label="Enter your Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'place-holder':'enter email'
            }
        )
    )
    username=forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'place-holder':'enter username'
            }
        )
    )
    password=forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'place-holder':'enter password'
            }
        )
    )

class LoginDataForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'place-holder': 'enter username'
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'place-holder': 'enter password'
            }
        )
    )






















