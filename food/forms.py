from .models import Comment
from .models import Post
from django import forms


class CommentForm(forms.ModelForm):
    """
    This class creates the body field
    for the comment section
    """
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """
    This class creates fields
    for the post section
    """
    class Meta:
        model = Post
        fields = [
            'title', 'featured_image', 'item_description', 'address',
        ]


class AddressFilterForm(forms.Form):
    address = forms.ModelChoiceField(
        queryset=Post.objects.all(), empty_label="search by address")
