from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm


# def login_user(request):  # TODO
#     form = UserLoginForm()
#     if request.method == "POST":
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse_lazy('blog:home'))
#     else:
#         form = UserLoginForm()
#
#     data = {
#         'form': form,
#     }
#
#     return render(request, 'users/login.html', context=data)


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('blog:home')


# def logout_user(request):  # TODO
#     logout(request)
#     return HttpResponseRedirect(reverse_lazy('blog:home'))


# class LogoutUser(LogoutView):
#     next_page = 'blog:home'


def register_user(request):  # TODO
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


@login_required(login_url='users:login')  # TODO
def profile_user(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('users:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    data = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context=data)