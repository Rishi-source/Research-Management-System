from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 255)
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not username and not password:
            raise forms.ValidationError('Add username and password')

