from django.contrib import admin
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView
from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="blog:home"), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('profile/<str:username>/', views.ProfileAnotherUser.as_view(), name='another_profile'),

    path('password_change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password_change_done', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),

]
