from django.test import TestCase

from .models import Post


class PostModelTest(TestCase):

  def setUp(self):
    self.post = Post.objects.create(title='Django',author='Aayush',slug='django')


  def test_post_model(self):
    d = self.post
    self.assertTrue(isinstance(d, Post))
    self.assertEqual(str(d), 'Django')
