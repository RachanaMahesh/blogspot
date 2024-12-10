from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PostListView.as_view(), name="blog-home"),# Best practice is to keep unique name bcoz anytime we reference that we will be directed to views.home
    path('post-detail/<int:pk>', views.PostDetailView.as_view(), name="post-detail"),
    path('post/new', views.PostCreateView.as_view(), name="post-created"),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name="post-delete"),
    path('about/', views.about, name="blog-about"),
]