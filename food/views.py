from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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


class PostDetail(View):
    """
    This class gets the food item posts by slug
    filters out the active ones
    post them and their associated comments on the
    postdetail page
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
            },
        )
