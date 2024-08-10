from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # 3 обязательных поля для UserCreationForm
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
        labels = {
            'email': "E-mail",
        }


class ProfileUpdateForm(forms.ModelForm):
    # image = forms.ImageField(label="Изображение!")

    class Meta:
        model = Profile
        fields = ['image']
        labels = {
            'image': "Изображение",
        }
