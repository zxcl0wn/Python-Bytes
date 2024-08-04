from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegisterForm, UserLoginForm


def login_user(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('blog:home'))
    else:
        form = UserLoginForm()

    data = {
        'form': form,
    }

    return render(request, 'users/login.html', context=data)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('blog:home'))


def register_user(request):
    # return HttpResponse("<h1>Register_user</h1>")
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return reverse_lazy('users:login')
            # return render(request, 'users/register_done.html')  # TODO
    else:
        form = UserRegisterForm()

    data = {
        'form': form,
    }

    return render(request, 'users/register.html', context=data)


class RegisterUser(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


@login_required(login_url='users:login')
def profile_user(request):
    return render(request, 'users/profile.html')
