from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    title = models.CharField(max_length=30)
    content = models.TextField()
    image_url = models.TextField(blank=True, null=True)
    image_file = models.ImageField(blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.edited} {self.author} commented on {self.post}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} liked {self.post}"


# class Profile(models.Model):
#     image = models.ImageField(blank=True, null=True)
#     username = models.CharField(max_length=20)
