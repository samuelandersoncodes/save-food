from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .models import Post
from django.contrib.messages.views import SuccessMessageMixin
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
    paginate_by = 6


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
        reserved = True
        while post.reserve.filter(id=request.user.id).exists():
            reserved = False
            break

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "reserved": reserved,
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


class AddPost(CreateView):
    """user post view """
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = '/'

    def form_valid(self, form):
        """
        form for post submission
        the function checks if the form is valid
        if it is, it saves the input data
        and alerts a success message
        """
        form.instance.author = self.request.user
        messages.success(
            self.request,
            f'Post submitted successfully'
        )

        return super(AddPost, self).form_valid(form)


class EditPost(UpdateView):
    """user edit post view """
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'
    success_url = '/'

    def form_valid(self, form):
        """
        form for post update
        the function checks if the form is valid
        if it is, it saves the updated data
        and alerts a success message
        """
        form.instance.author = self.request.user
        messages.success(
            self.request,
            f'Post successfully updated'
        )

        return super(EditPost, self).form_valid(form)


class DeletePost(SuccessMessageMixin, DeleteView):
    """user delete post view """
    model = Post
    template_name = 'delete_post.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        """
        references the post to be deleted
        and alerts a success message upon deletion
        """
        post = self.get_object()
        messages.success(
            self.request,
            f'{post.title} successfully deleted'
        )
        return super(DeletePost, self).delete(request, *args, **kwargs)


class Reserve_Food_Item(View):
    """food item reservation view"""

    def post(self, request, slug):
        """
        this function first checks if the user is the
        author of the respective post
        then, checks if a post item is reserved
        if it is, the reserved status is removed
        if not, then reserved it added
        and returns back to postdetail page
        """
        post = get_object_or_404(Post, slug=slug)
        if request.user.id == post.author.id:
            if post.reserve.filter(id=request.user.id).exists():
                post.reserve.remove(request.user)
            else:
                post.reserve.add(request.user)
                post.save()

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
