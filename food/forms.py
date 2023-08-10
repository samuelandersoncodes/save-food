from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    This class creates the body field
    for the comment section
    """
    class Meta:
        model = Comment
        fields = ('body',)
