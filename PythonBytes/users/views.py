from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegisterForm


def login_user(request):
    return HttpResponse("<h1>Login_user</h1>")


def logout_user(request):
    return HttpResponse("<h1>Logout_user</h1>")


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
