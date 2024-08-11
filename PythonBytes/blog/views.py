from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template.backends.django import reraise
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView, ListView
from .models import Post
from .utils import DataMixin


class Home(DataMixin, ListView):
    model = Post
    title_page = "Главная страница"
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class About(DataMixin, TemplateView):
    template_name = 'blog/about.html'
    title_page = "О клубе"


class PostDetailView(DataMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'
    title_page = "Просмотр записи"
    context_object_name = 'post'


class PostCreateView(DataMixin, LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:home')
    login_url = reverse_lazy('users:login')
    title_page = "Создание записи"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(DataMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:home')
    login_url = reverse_lazy('users:login')
    title_page = "Изменение записи"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        print(f'self.request.user: {self.request.user}')
        print(f'post.author: {post.author}')
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DataMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')
    login_url = reverse_lazy('users:login')
    title_page = "Удаление записи"

    def test_func(self):
        post = self.get_object()
        print(f'self.request.user: {self.request.user}')
        print(f'post.author: {post.author}')
        if self.request.user == post.author:
            return True
        return False


class MyPosts(DataMixin, LoginRequiredMixin, ListView):
    template_name = 'blog/home.html'
    title_page = "Мои записи"
    context_object_name = 'posts'
    login_url = 'users:login'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
