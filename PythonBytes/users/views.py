from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordContextMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, View, DetailView, TemplateView
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from .forms import UserPasswordChangeForm


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    extra_context = {
        'title_page': "Авторизация",
    }

    def get_success_url(self):
        return reverse_lazy('blog:home')


class RegisterUser(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    extra_context = {
        'title_page': "Регистрация",
    }

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
            'title_page': f"Мой профиль: {self.request.user}",
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
            'title_page': "Профиль",
        }
        return render(request, self.template_name, context=data)


class ProfileAnotherUser(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile_another_user.html'
    login_url = 'users:login'
    context_object_name = 'profile'
    extra_context = {
        'title_page': "Профиль другого пользователя",
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title_page'] = f'Профиль пользователя: {self.kwargs.get('username')}'

    def get_object(self, queryset=None):
        # Получаем пользователя по username из URL
        username = self.kwargs.get('username')
        # Получаем профиль по username связанного пользователя
        return Profile.objects.get(user__username=username)


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = "users/password_change_form.html"
