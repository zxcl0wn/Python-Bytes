from django.http import HttpResponse
from django.shortcuts import render
from django.template.backends.django import reraise

posts = [
    {
        'author': "Администратор",
        'title': "Это первый пост",
        'content': "Содержание первого поста.",
        'date_posted': "12 мая, 2022",
    },
    {
        'author': "Пользователь",
        'title': "Это второй пост",
        'content': "Подробное содержание второго поста.",
        'date_posted': "13 мая, 2022",
    }
]


def home(request):
    data = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context=data)


def about(request):
    return render(request, 'blog/about.html')
