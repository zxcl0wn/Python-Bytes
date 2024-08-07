from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, View
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('blog:home')


class RegisterUser(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return response


class ProfileUser(LoginRequiredMixin, View):
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    login_url = 'users:login'

    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        data = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, self.template_name, context=data)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен.')
            return redirect(self.success_url)

        data = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, self.template_name, context=data)
