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
    path('user/<str:username>', views.UserPostListView.as_view(), name="user-posts"),
    path('about/', views.about, name="blog-about"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html') , name="password_reset"),
    path('password-reset/done', 
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html') , 
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
         name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name="password_reset_complete"),
]