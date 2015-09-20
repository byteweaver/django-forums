from django.test import TestCase

from forums.factories import ForumFactory


class CategoryModelTests(TestCase):
    def setUp(self):
        self.forum = ForumFactory()

    def test_string_method(self):
        self.assertEquals(str(self.forum), 'Forum')
