from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    class for posts
    inheriting from the python model
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="food_item_posts")
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    item_description = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


class Meta:
    """
    This class orders posts
    on the created on field
    """
    ordering = ['-created_on']


def __str__(self):
    """
    returns custom string object representation for posts
    instead of the default
    """
    return self.title


class Comment(models.Model):
    """
    class for comments
    that inherits from the python model
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


class Meta:
    """
    This class orders comments on the created on field
    in an ascending order
    """
    ordering = ['created_on']


def __str__(self):
    """
    returns custom string object representation for comments
    instead of the default
    """
    return f"Comment {self.body} by {self.name}"

