from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class TestModels(TestCase):
    """models test"""
    def test_slug_unique_is_true(self):
        """
        this function creates a user and post instance
        and tests if their respective slugs are unique
        """
        newuser = User.objects.create(username='test', password='test')
        post = Post.objects.create(
            title='Banana',
            slug='banana',
            author=newuser,
            item_description='sweet banana',
            status=1,
            address='Berlin, 122345')
        unique = post.slug == post.id
        self.assertTrue(post.slug, unique)
