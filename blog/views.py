from django.shortcuts import get_object_or_404, render
from .models import post
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class PostListView(ListView):
    model = post
    template_name='blog/home.html'
    context_object_name = 'posts'
    ordering = '-date_posted'
    paginate_by = 5

class PostDetailView(DetailView):
    model = post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    fields = ['title','content']
    success_url='/'
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

class UserPostListView(ListView):
    model = post
    template_name='blog/user_posts.html'
    context_object_name = 'posts'
    # ordering = '-date_posted'
    paginate_by = 5

    def get_queryset(self,):
        user = get_object_or_404(User, username= self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date_posted')