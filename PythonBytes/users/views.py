from django.http import HttpResponse
from django.shortcuts import render
from django.template.backends.django import reraise


def login_user(request):
    return HttpResponse("<h1>Login_user</h1>")


def logout_user(request):
    return HttpResponse("<h1>Logout_user</h1>")


def register_user(request):
    return HttpResponse("<h1>Register user</h1>")
