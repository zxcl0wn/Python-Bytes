from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # 3 обязательных поля для UserCreationForm
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput())
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


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={'class': "form-input"}))
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': "form-input"}))
    new_password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': "form-input"}))
