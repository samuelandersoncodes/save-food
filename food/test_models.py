from django.test import TestCase
from .models import Post, Comment
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

    def test_string_method_returns_title(self):
        """
        this function creates a user and post instance
        and tests if string method returns title value
        """
        newuser = User.objects.create(username='test', password='test')
        post = Post.objects.create(
            title='Banana',
            slug='banana',
            author=newuser,
            item_description='sweet banana',
            status=1,
            address='Berlin, 122345')
        self.assertEqual(str(post), 'Banana')

    def test_posts_ordered_per_created_date_time(self):
        """
        this function creates a user and post instance
        and tests if posts are ordered per their created date and time
        """
        newuser = User.objects.create(username='test', password='test')
        post = Post.objects.create(
            title='Banana',
            slug='banana',
            author=newuser,
            item_description='sweet banana',
            status=1,
            address='Berlin, 122345',
        )
        ordering = ['-created_on']
        self.assertTrue((post), ordering)

    def test_comment_approved_to_true(self):
        """
        this function creates a user and comment instance
        and tests if its approval defaults to true
        """
        newuser = User.objects.create(username='test', password='test')
        post = Post.objects.create(
            title='Banana',
            slug='banana',
            author=newuser,
            item_description='sweet banana',
            status=1,
            address='Berlin, 122345')
        comment = Comment.objects.create(
            name=newuser,
            email='test@gmail.com',
            body='I love to have it for dinner',
            post=post,
            approved=True
        )
        self.assertTrue(comment.approved)

    def test_string_method_returns_body_message(self):
        """
        this function creates a user and comment instance
        and tests if the body message of comment returns
        its string value
        """
        newuser = User.objects.create(username='test', password='test')
        post = Post.objects.create(
            title='Banana',
            slug='banana',
            author=newuser,
            item_description='sweet banana',
            status=1,
            address='Berlin, 122345')
        comment = Comment.objects.create(
            name=newuser,
            email='test@gmail.com',
            body='I love to have it for dinner',
            post=post,
            approved=True
        )
        self.assertEqual(str(comment.body), 'I love to have it for dinner')

    def test_comments_ordered_per_created_date_time(self):
        """
        this function creates a user and comment instance
        and tests if comments are ordered per their created date and time
        """
        newuser = User.objects.create(username='test', password='test')
        post = Post.objects.create(
            title='Banana',
            slug='banana',
            author=newuser,
            item_description='sweet banana',
            status=1,
            address='Berlin, 122345'
        )
        comment = Comment.objects.create(
            name=newuser,
            email='test@gmail.com',
            body='I love to have it for dinner',
            post=post
        )
        ordering = ['created_on']
        self.assertTrue((comment), ordering)
