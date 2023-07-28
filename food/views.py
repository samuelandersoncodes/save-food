from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    This class inherits from generic view
    filter posts by status
    order them by creation time and date
    and paginates the post page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8
