from django.test import TestCase

from forums.factories import CategoryFactory


class CategoryModelTests(TestCase):
    def setUp(self):
        self.category = CategoryFactory()

    def test_string_method(self):
        self.assertEquals(str(self.category), 'Category')
