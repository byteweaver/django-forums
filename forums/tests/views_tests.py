from django.test import TestCase

from forums.tests.factories import ForumFactory, TopicFactory


class CategoryListViewTest(TestCase):
    def test_plain_get_request(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


class ForumListViewTest(TestCase):
    def setUp(self):
        self.forum = ForumFactory.create()

    def test_plain_get_request(self):
        response = self.client.get('/%d/' % self.forum.pk)
        self.assertEquals(response.status_code, 200)


class TopicListViewTest(TestCase):
    def setUp(self):
        self.topic = TopicFactory.create()

    def test_plain_get_request(self):
        response = self.client.get('/topic/%d/' % self.topic.pk)
        self.assertEquals(response.status_code, 200)
