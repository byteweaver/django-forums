from django.test import TestCase

from forums.models import Category
from forums.tests.factories import CategoryFactory


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = CategoryFactory.create()

        self.assertEquals(category.name, 'Category')
