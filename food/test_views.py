from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse


class TestViews(TestCase):
    """ test for views """
    def test_post_list(self):
        """
        this function gets the home page url
        comfrims that its response status is good
        and also confirm the accurate template used
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_detail(self):
        """
        this function creates a user and post instance
        gets the post detail page url
        and comfrims that its response status is good
        """
        newuser = User.objects.create(username='test', password='test')
        post = Post.objects.create(
            title='Banana',
            slug='banana',
            author=newuser,
            item_description='sweet banana',
            status=1,
            address='Berlin, 122345')
        response = self.client.get('/post_detail/{post.slug}/')
        url = reverse('post_detail', kwargs={'slug': post.slug})
        self.response = self.client.get(url)
        self.assertEqual(self.response.status_code, 200)
