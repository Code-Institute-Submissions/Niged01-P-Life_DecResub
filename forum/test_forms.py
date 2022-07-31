""" Unit Testing for forms """
from django.test import TestCase
from .forms import PostForm, CommentForm


class TestPostForm(TestCase):
    """ Unit test for posts form """
    def test_post_title_is_required(self):
        """ title function """
        form = PostForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_content_is_required(self):
        """ content function"""
        form = PostForm(({'content': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """ fields function """
        form = PostForm()
        self.assertEqual(
            form.Meta.fields, ("title", "content", "categories", "tags", "post_image")
        )


class TestCommentForm(TestCase):
    """  Unit test for comment form"""
    def test_post_body_is_required(self):
        """ title function """
        form = CommentForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """ fields function """
        form = CommentForm()
        self.assertEqual(
            form.Meta.fields, ('body',)
        )
