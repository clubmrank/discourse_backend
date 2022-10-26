from django import forms
from . import models

class UserSignupForm(forms.Form):
    first_names = forms.CharField(max_length=128)
    surname = forms.CharField(max_length=64)
    student_number = forms.CharField(max_length=16)
    password = forms.CharField(max_length=16)


class UserLoginForm(forms.Form):
    student_number = forms.CharField(max_length=16)
    password = forms.CharField(max_length=16)