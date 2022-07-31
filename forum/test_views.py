""" Unit testing for Views """

from django.test import TestCase


class TestPostList(TestCase):
    """ Unit test home page view """
    def test_get_index(self):
        """ function """
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestPostDetail(TestCase):
    """ unit test for post detail page """
    def test_can_post_detail(self):
        """ function """
        response = self.client.get('/post_detail')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')