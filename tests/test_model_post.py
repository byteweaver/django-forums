from django.test import TestCase

from forums.factories import PostFactory


class CategoryModelTests(TestCase):
    def setUp(self):
        self.post = PostFactory()

    def test_string_method(self):
        self.assertEquals(str(self.post), 'Body text\nWith multiple lines!')
