from django.test import TestCase

from forums.factories import TopicFactory


class CategoryModelTests(TestCase):
    def setUp(self):
        self.topic = TopicFactory()

    def test_string_method(self):
        self.assertEquals(str(self.topic), 'Topic')
