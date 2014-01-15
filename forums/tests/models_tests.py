from django.test import TestCase

from forums.models import Category, Forum, Topic
from forums.tests.factories import CategoryFactory, ForumFactory, TopicFactory


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = CategoryFactory.create()

        self.assertEquals(Category.objects.count(), 1)
        self.assertEquals(category.name, 'Category')

    def test_forum_creation(self):
        forum = ForumFactory.create()

        self.assertEquals(Forum.objects.count(), 1)
        self.assertEquals(forum.name, 'Forum')
        self.assertEquals(forum.position, 0)
        self.assertEquals(forum.description , '')
        self.assertEquals(forum.is_closed, False)

    def test_topic_creation(self):
        topic = TopicFactory.create()

        self.assertEquals(Topic.objects.count(), 1)
        self.assertEquals(topic.name, 'Topic')
        self.assertEquals(topic.last_post, None)
