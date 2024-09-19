from django.shortcuts import render
from .models import post
# Create your views here.
# posts = [
#     {
#         'author':'Rachana',
#         'title': 'Blog Post 1',
#         'content': 'First Content post',
#         'date_posted': 'January 1, 2023'
#     },
#     {
#         'author':'Poornima',
#         'title': 'Blog Post 2',
#         'content': 'Second Content post',
#         'date_posted': 'January 28, 2023'
#     }
# ]

def home(request):
    # inorder to pass dictionary values creating the dictionary and passing it as arguement
    context = {
        'posts': post.objects.all()
        # posts ---> Keys('posts') will be accessible n html page
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})