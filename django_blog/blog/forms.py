from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# user update form to update username and email fields
class UpdateForm(forms.ModelForm):
        password = ReadOnlyPasswordHashField()
        class Meta:
            model = User
            fields = ["username", "email", 'password' ]