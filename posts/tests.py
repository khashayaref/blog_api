from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create(
            username='tester',
            email='test@test.com',
            password='secret',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title='Test post',
            body='just for test',
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'tester')
        self.assertEqual(self.post.title, 'Test post')
        self.assertEqual(str(self.post), 'Test post')
        self.assertEqual(self.post.body, 'just for test')

