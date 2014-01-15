from django.test import TestCase

from forums.models import Category


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(**{
            'name': 'Category',
        })

        self.assertEquals(category.name, 'Category')
