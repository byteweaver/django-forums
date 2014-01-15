from django.test import TestCase


class CategoryListViewTest(TestCase):
    def test_plain_get_request(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
