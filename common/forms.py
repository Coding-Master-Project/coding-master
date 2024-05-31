from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')
    pw_valid = forms.CharField(max_length=1, label="비밀번호 유효")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'pw_valid')