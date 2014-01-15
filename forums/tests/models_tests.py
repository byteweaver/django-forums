from django.test import TestCase

from forums.models import Category, Forum
from forums.tests.factories import CategoryFactory, ForumFactory


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = CategoryFactory.create()

        self.assertEquals(category.name, 'Category')

    def test_forum_creation(self):
        forum = ForumFactory.create()

        self.assertEquals(Forum.objects.count(), 1)
        self.assertEquals(forum.name, 'Forum')
        self.assertEquals(forum.position, 0)
        self.assertEquals(forum.description , '')
        self.assertEquals(forum.is_closed, False)
