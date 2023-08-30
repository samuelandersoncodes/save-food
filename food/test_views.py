from django.test import TestCase
from .models import Post, Comment
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

    def test_posted_detail(self):
        """
        this function creates a user, post and comment instance
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
            address='Berlin, 122345'
        )
        comment = Comment.objects.create(
            name=newuser,
            email='test@gmail.com',
            body='I love to have it for dinner',
            post=post,
            approved=True
        )
        response = self.client.post('/post_detail/{post.slug}/')
        url = reverse('post_detail', kwargs={'slug': post.slug})
        self.response = self.client.post(url)
        self.assertEqual(self.response.status_code, 200)

    def test_add_post(self):
        """
        this function gets the addpost page url
        comfrims that its response status is good
        and also confirm the accurate template used
        """
        response = self.client.get('/addpost/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_post.html')

    def test_can_add_post(self):
        """
        this function test the addpost post method
        comfrims that its response status is good
        and also confirm the accurate template used
        """
        response = self.client.post('/addpost/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_post.html')

    def test_edit_post(self):
        """
        this function creates a user and post instance
        gets the editpost page url
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
        response = self.client.get('/editpost/{post.pk}/')
        url = reverse('edit_post', kwargs={'pk': post.pk})
        self.response = self.client.get(url)
        self.assertEqual(self.response.status_code, 200)

    def test_delete_post(self):
        """
        this function creates a user and post instance
        gets the deletepost page url
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
        response = self.client.get('/deletepost/{post.pk}/')
        url = reverse('delete_post', kwargs={'pk': post.pk})
        self.response = self.client.get(url)
        self.assertEqual(self.response.status_code, 200)

    def test_reserve_food_item_toggle(self):
        """
        this function creates a user and post instance
        gets the deletepost page url
        and comfrims that its response status is good
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
        response = self.client.get('/post_reserved/{post.slug}/')
        url = reverse('post_detail', kwargs={'slug': post.slug})
        self.response = self.client.get(url)
        self.assertEqual(self.response.status_code, 200)
