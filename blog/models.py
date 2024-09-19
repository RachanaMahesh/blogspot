from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # auto_now==True ---> this will add the time when post is created/modified similar to last modified date & time
    # auto_now_add == True ---> this will add the time when the post is created but cannot be changed later
    # default=timezone.now() ---> now() is a function which we currently noo need in above code we just want to add current time hence fun() is not required
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 1(User): many(Post) relationship , on_delete means to delete post when respective User is deleted .

    def __str__(self):
        return self.title
