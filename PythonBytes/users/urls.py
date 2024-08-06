from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="blog:home"), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.profile_user, name='profile'),
]
