from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    # Best practice is to keep unique name bcoz anytime we reference that we will be directed to views.home
    path('about/', views.about, name="blog-about"),
]