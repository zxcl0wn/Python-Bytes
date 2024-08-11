from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template.backends.django import reraise
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView, ListView
from .models import Post


class Home(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 3
    # extra_context = {
    #     'menu': menu,
    # }
    #

class About(TemplateView):
    template_name = 'blog/about.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:home')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:home')
    login_url = reverse_lazy('users:login')

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


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')
    login_url = reverse_lazy('users:login')

    def test_func(self):
        post = self.get_object()
        print(f'self.request.user: {self.request.user}')
        print(f'post.author: {post.author}')
        if self.request.user == post.author:
            return True
        return False

