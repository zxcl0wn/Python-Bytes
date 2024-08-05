from django.http import HttpResponse
from django.shortcuts import render
from django.template.backends.django import reraise
from django.views.generic import DetailView

from .models import Post


def home(request):
    posts = Post.objects.all()

    data = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context=data)


def about(request):
    return render(request, 'blog/about.html')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'



class PostCreateView():
    pass



class PostUpdateView():
    pass



class PostDeleteView():
    pass