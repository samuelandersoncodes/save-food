from django.test import TestCase


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
