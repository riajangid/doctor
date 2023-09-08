from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "field input-field",
                "type": "text",
                "placeholder": "Enter your username",
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "field input-field",
                "type": "password",
                "placeholder": "Enter your password",
            }
        )
    )



class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "field input-field",
                "id": "inputUsername",
                "placeholder": "Enter username",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "field input-field",
                "id": "inputChoosePassword",
                "placeholder": "Enter Password",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "field input-field",
                "id": "inputConfirmPassword",
                "placeholder": "Confirm Password",
            }
        )
    )
    
    aadharnum = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "field input-field",
                "id":"aadharnumber",
                "placeholder": "Enter your aadhar number",
            }
        )
    )
    

    class Meta:
        model = User
        fields = ("username", "aadharnum", "password1", "password2")