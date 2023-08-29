from django.test import TestCase
from .forms import CommentForm
from .forms import PostForm


class TestCommentForm(TestCase):
    """ comment form test """

    def test_body_message_is_required(self):
        """
        this function instatiates a form without a message in the body
        checks its validity which turns out to be not valid
        and finds the body key in the dictionary of form errors
        then checks for the associated error message
        """
        form = CommentForm({'body': ' '})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_field_explicit_in_form_metaclass(self):
        """
        this function ensures that no other fields outside
        the body field are not loaded accidentally
        """
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))

