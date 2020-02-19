from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.TextField()
    image1 = models.ImageField(null = True)
    image2 = models.ImageField(null = True)
    image3 = models.ImageField(null = True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)