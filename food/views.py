from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Post
from django.contrib import messages
from .forms import CommentForm
from .forms import PostForm


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

    def get(self, request, slug, *args, **kwargs):
        """
        This function gets the food item posts by slug
        filters out the active ones
        post them and their associated comments on the
        postdetail page
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        this function gets data from the user form
        filters approved comments
        checks for user form validity
        asigns comment to its respective post
        and save the comment
        or return an empty field if invalid
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
            },
        )


class AddPost(ListView, FormView):
    """user post view """
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = '/post_detail.html/'

    def form_valid(self, form):
        """
        form for post submission
        the function checks if the form is valid
        if it is, it saves the input data
        and alerts a success message
        """
        for post in posts:
            form.instance.username = self.request.user
            if form.is_valid:
                form.save()
            else:
                form.clear()

        messages.success(
            self.request,
            f'Post submitted successfully'
        )

        return super(self, AddPost).form_valid(form)
