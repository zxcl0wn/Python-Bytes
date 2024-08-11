from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug_post_update>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug_post_delete>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/my_posts', views.MyPosts.as_view(), name='my_posts'),
]
